# -*- coding: utf-8 -*-

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import yaml
import os
import keyboard as kb


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(qtg.QIcon("./textures/calculator.png"))
        self.setWindowTitle(lg["root_window"]["title"])

        self.setings = qtw.QPushButton()
        self.setings.setStyleSheet("image: url(./textures/configuracion2.png)")
        self.panel = qtw.QLineEdit()
        self.panel.setReadOnly(True)
        self.boton0 = qtw.QPushButton("0")
        self.boton1 = qtw.QPushButton("1")
        self.boton2 = qtw.QPushButton("2")
        self.boton3 = qtw.QPushButton("3")
        self.boton4 = qtw.QPushButton("4")
        self.boton5 = qtw.QPushButton("5")
        self.boton6 = qtw.QPushButton("6")
        self.boton7 = qtw.QPushButton("7")
        self.boton8 = qtw.QPushButton("8")
        self.boton9 = qtw.QPushButton("9")
        self.botoncoma = qtw.QPushButton(".")
        self.botonmas = qtw.QPushButton("+")
        self.botonmenos = qtw.QPushButton("-")
        self.botonmultiplicar = qtw.QPushButton("x")
        self.botondividir = qtw.QPushButton(u"\u00f7")
        self.botonclear = qtw.QPushButton(lg["root_window"]["boton_clear"])
        self.botonigual = qtw.QPushButton("=")

        self.layout = qtw.QGridLayout()
        self.widget = qtw.QWidget(self)
        self.setCentralWidget(self.widget)
        self.widget.setLayout(self.layout)

        self.layout.addWidget(self.panel, 0, 0, 1, 4)
        self.layout.addWidget(self.botonclear, 1, 0, 1, 3)
        self.layout.addWidget(self.setings, 1, 3)
        self.layout.addWidget(self.boton7, 2, 0)
        self.layout.addWidget(self.boton8, 2, 1)
        self.layout.addWidget(self.boton9, 2, 2)
        self.layout.addWidget(self.botondividir, 2, 3)
        self.layout.addWidget(self.boton4, 3, 0)
        self.layout.addWidget(self.boton5, 3, 1)
        self.layout.addWidget(self.boton6, 3, 2)
        self.layout.addWidget(self.botonmultiplicar, 3, 3)
        self.layout.addWidget(self.boton1, 4, 0)
        self.layout.addWidget(self.boton2, 4, 1)
        self.layout.addWidget(self.boton3, 4, 2)
        self.layout.addWidget(self.botonmenos, 4, 3)
        self.layout.addWidget(self.botoncoma, 5, 0)
        self.layout.addWidget(self.boton0, 5, 1)
        self.layout.addWidget(self.botonigual, 5, 2)
        self.layout.addWidget(self.botonmas, 5, 3)

        self.setings.clicked.connect(self.showdialog)
        self.boton0.clicked.connect(lambda: self.printnumber("0"))
        self.boton1.clicked.connect(lambda: self.printnumber("1"))
        self.boton2.clicked.connect(lambda: self.printnumber("2"))
        self.boton3.clicked.connect(lambda: self.printnumber("3"))
        self.boton4.clicked.connect(lambda: self.printnumber("4"))
        self.boton5.clicked.connect(lambda: self.printnumber("5"))
        self.boton6.clicked.connect(lambda: self.printnumber("6"))
        self.boton7.clicked.connect(lambda: self.printnumber("7"))
        self.boton8.clicked.connect(lambda: self.printnumber("8"))
        self.boton9.clicked.connect(lambda: self.printnumber("9"))
        self.botoncoma.clicked.connect(lambda: self.printnumber("."))
        self.botonmas.clicked.connect(lambda: self.printnumber("+"))
        self.botonmenos.clicked.connect(lambda: self.printnumber("-"))
        self.botonmultiplicar.clicked.connect(lambda: self.printnumber("*"))
        self.botondividir.clicked.connect(lambda: self.printnumber("/"))
        self.botonclear.clicked.connect(self.clearnumber)
        self.botonigual.clicked.connect(self.resultado)

        kb.add_hotkey("zero", lambda: self.printnumber("0"))
        kb.add_hotkey("one", lambda: self.printnumber("1"))
        kb.add_hotkey("two", lambda: self.printnumber("2"))
        kb.add_hotkey("three", lambda: self.printnumber("3"))
        kb.add_hotkey("four", lambda: self.printnumber("4"))
        kb.add_hotkey("five", lambda: self.printnumber("5"))
        kb.add_hotkey("six", lambda: self.printnumber("6"))
        kb.add_hotkey("seven", lambda: self.printnumber("7"))
        kb.add_hotkey("eight", lambda: self.printnumber("8"))
        kb.add_hotkey("nine", lambda: self.printnumber("9"))
        kb.add_hotkey(".", lambda: self.printnumber("."))
        kb.add_hotkey("shift+*", lambda: self.printnumber("*"))
        kb.add_hotkey("+", lambda: self.printnumber("+"))
        kb.add_hotkey("-", lambda: self.printnumber("-"))
        kb.add_hotkey("shift+seven", lambda: self.printnumber("/"))
        kb.add_hotkey("backspace", self.clearnumber)
        kb.add_hotkey("supr", self.clearnumber)
        kb.add_hotkey("enter", self.resultado)

        kb.add_hotkey("up, down, right, left", lambda: self.printnumber(""))

        self.list = []

        self.layout_menu = qtw.QVBoxLayout()
        self.menu = qtw.QWidget(self)
        self.menu.setLayout(self.layout_menu)
        self.menu.setGeometry(0, 0, 0, 0)

        self.title = qtw.QLabel("Menu")
        self.style_bn = qtw.QPushButton("Estilo")
        self.lenguage_bn = qtw.QPushButton("Idioma")

        for i in [self.title, self.style_bn, self.lenguage_bn]:
            self.layout_menu.addWidget(i)

    def printnumber(self, number):
        endlist = ""
        self.list.append(number)
        for i in self.list:
            if i == "*":
                endlist += "x"
            elif i == "/":
                endlist += u"\u00f7"
            else:
                endlist += i
        self.panel.setText(endlist)

    def clearnumber(self):
        self.list = []
        self.panel.clear()

    def resultado(self):
        try:
            cuenta = ""
            for i in self.list:
                cuenta += i
            resultado = eval(cuenta)
            self.clearnumber
            self.list = []
            self.printnumber(str(resultado))
        except ZeroDivisionError:
            self.list = []
            self.printnumber(
                lg["root_window"]["errors"]["zero_divicion_error"]
                )
            self.list = []

    def showdialog(self):
        dialog = Dialog(self)
        dialog.show()

    def show_menu(self):
        self.menu.setGeometry(0, 0, 100, 300)


class Dialog(qtw.QMainWindow):
    def __init__(self, *args):
        super(Dialog, self).__init__(*args)

        self.setWindowTitle(lg["styles_window"]["title"])
        self.setWindowIcon(qtg.QIcon("./textures/edit-alt.png"))
        self.setFixedSize(400, 250)

        self.widget = qtw.QWidget(self)
        self.setCentralWidget(self.widget)

        self.theme_widget = qtw.QWidget()
        self.layout = qtw.QGridLayout()
        self.theme_widget.setLayout(self.layout)

        self.items = []
        files = os.listdir(r"./skins")
        for i in files:
            self.items.append(i.replace(".stylesheet", ""))

        self.combobox = qtw.QComboBox()
        self.combobox.addItems(self.items)
        self.select = qtw.QPushButton(lg["styles_window"]["boton_select"])
        self.select.clicked.connect(
            lambda: self.updatevalue(self.combobox.currentText())
            )
        self.brows = qtw.QPushButton(lg["styles_window"]["boton_brows"])
        self.brows.clicked.connect(self.showfile)
        self.delet = qtw.QPushButton(lg["styles_window"]["boton_delet"])
        self.delet.clicked.connect(self.show_delet)

        self.layout.addWidget(self.combobox, 0, 0)
        self.layout.addWidget(self.select, 0, 1)
        self.layout.addWidget(self.brows, 1, 0)
        self.layout.addWidget(self.delet, 2, 0)

        self.lenguge_widget = qtw.QWidget()
        self.layout_lenguage = qtw.QVBoxLayout()
        self.lenguge_widget.setLayout(self.layout_lenguage)

        self.spanish = qtw.QRadioButton("Español")
        self.english = qtw.QRadioButton("English")
        self.select_lenguage = qtw.QPushButton(
            lg["styles_window"]["boton_select"],
            clicked=lambda: self.updatelenguage()
        )

        for i in [self.spanish, self.english, self.select_lenguage]:
            self.layout_lenguage.addWidget(i)

        self.tab_widget = qtw.QTabWidget(self)
        self.tab_widget.setMinimumSize(400, 250)
        self.tab_widget.addTab(
            self.theme_widget,
            lg["styles_window"]["tab"]["tab1"]
            )
        self.tab_widget.addTab(
            self.lenguge_widget,
            lg["styles_window"]["tab"]["tab2"]
            )

    def updatevalue(self, name):
        with open("savestyle.yaml", "r") as file:
            newconf = yaml.safe_load(file)
            file.close()

        with open("savestyle.yaml", "w") as file:
            newconf["status"] = name
            yaml.safe_dump(newconf, file)
            file.close()
        try:
            setstyle(self)
        except FileNotFoundError:
            qtw.QMessageBox.about(
                self,
                lg["styles_window"]["errors"]["file_not_found_error"]["title"],
                lg["styles_window"]["errors"]["file_not_found_error"]["message"]
                )

    def updatelenguage(self):
        if self.spanish.isChecked():
            var = "spanish"
        if self.english.isChecked():
            var = "english"

        with open("savestyle.yaml", "r") as file:
            newconf = yaml.safe_load(file)
            file.close

        with open("savestyle.yaml", "w") as file:
            newconf["lenguage"] = var
            yaml.safe_dump(newconf, file)
            file.close()

        qtw.QMessageBox.about(
            self,
            lg["styles_window"]["tab"]["tab2"],
            lg["styles_window"]["tab"]["message"]
        )
        self.destroy()

    def showfile(self):
        openfile = qtw.QFileDialog.getOpenFileName(
            self,
            lg["styles_window"]["show_file"]["title"],
            "",
            "StyleSheet (*.stylesheet)"
            )

        try:
            url = openfile[0]
            list = openfile[0].split("/")
            list.reverse()
            name = list[0]
            with open(f"./skins/{name}", "w") as file:
                file.write(open(f"{url}", "r").read())
                file.close()

            qtw.QMessageBox.about(
                self,
                lg["styles_window"]["show_file"]["messagebox"]["title"],
                lg["styles_window"]["show_file"]["messagebox"]["message"]
                )
        except PermissionError:
            pass

    def show_delet(self):
        Delet = DeletList(self)
        Delet.show()


class DeletList(qtw.QMainWindow):
    def __init__(self, *args):
        super(DeletList, self).__init__(*args)

        self.setMinimumWidth(400)
        self.setWindowTitle(lg["delet_list"]["title"])

        self.widget = qtw.QWidget(self)
        self.setCentralWidget(self.widget)

        self.layout = qtw.QVBoxLayout()
        self.widget.setLayout(self.layout)

        archivo = os.listdir(r"./skins")
        self.list = []
        for i in archivo:
            self.list.append(i.replace(".stylesheet", ""))

        for i in self.list:
            exec(f"self.{i} = qtw.QCheckBox('{i}')")
            exec(f"self.layout.addWidget(self.{i})")

        self.delet = qtw.QPushButton(lg["delet_list"]["boton_delet"])
        self.layout.addWidget(self.delet)
        self.delet.clicked.connect(self.delet_style)

    def delet_style(self):
        self.message = qtw.QMessageBox.question(
            self,
            lg["delet_list"]["delet_style"]["title"],
            lg["delet_list"]["delet_style"]["message"]
            )

        if self.message == qtw.QMessageBox.Yes:
            self.check_list = []
            for i in self.list:
                exec(f"self.check_list.append(self.{i})")

            print(self.check_list)
            for i in self.check_list:
                if i.isChecked() is True:
                    os.remove(f"skins/{i.text()}.stylesheet")

            qtw.QMessageBox.about(
                self,
                lg["delet_list"]["delet_style"]["messagebox"]["title"],
                lg["delet_list"]["delet_style"]["messagebox"]["message"]
                )
            self.destroy()


if __name__ == "__main__":
    def setstyle(self):
        with open("savestyle.yaml", "r") as file:
            config = yaml.safe_load(file)
            name = config["status"]
            file.close()
        app.setStyleSheet(open(f"./skins/{name}.stylesheet", "r").read())

    with open("savestyle.yaml", "r") as file:
        config = yaml.safe_load(file)
        name = config["status"]
        lenguage = config["lenguage"]
        file.close()

    with open(f"./lenguages/{lenguage}.yaml", "r", encoding="utf8") as file:
        lg = yaml.safe_load(file)

    app = qtw.QApplication([])
    try:
        app.setStyleSheet(open(f"./skins/{name}.stylesheet", "r").read())
    except FileNotFoundError:
        pass
    window = MainWindow()
    window.show()
    app.exec_()
