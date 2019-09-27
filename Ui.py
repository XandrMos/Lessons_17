import sys
import ClassFond
from PyQt5 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.win = QtWidgets.QWidget()
        self.win.resize(800, 600)
        self.win.setWindowTitle("InstFond")
        self.head = QtWidgets.QLabel(self.win)
        self.head.setText("<b>Задати період моделювання роботи інвестеційного фонда</b>")
        self.head.move(10,10)
        self.text_hd = QtWidgets.QLabel(self.win)
        self.text_hd.setText("Вкажіть термін тривалістю від 12 до 30 місяців")
        self.text_hd.setWordWrap(True)
        self.text_hd.setAlignment(QtCore.Qt.AlignRight)
        self.ed_mounth = QtWidgets.QLineEdit(self.win)
        self.ed_mounth.setText("12")
        self.ed_mounth.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_mounth = QtWidgets.QPushButton(self.win)
        self.btn_mounth.setText("Задати період")
        self.btn_mounth.setStyleSheet("QPushButton {font-weight: bold;}")
        self.group = QtWidgets.QGroupBox(self.win)
        self.head_group = QtWidgets.QHBoxLayout(self.win)
        self.head_group.addWidget(self.text_hd)
        self.head_group.addWidget(self.ed_mounth)
        self.head_group.addWidget(self.btn_mounth)
        self.group.setLayout(self.head_group)
        self.group.move(10, 36)
        self.group.resize(380, 60)
        self.InfoAboutFond()
        self.InfoAboutIvestPorfel()
        self.win.show()
    def InfoAboutFond(self):
        self.inf_lbl_1 = QtWidgets.QLabel(self.win)
        self.inf_lbl_1.setText("Капітал фонда:")
        self.inf_lbl_1.setAlignment(QtCore.Qt.AlignRight)
        self.inf_lbl_2 = QtWidgets.QLabel(self.win)
        self.inf_lbl_2.setText(str(fond.capital) + " у. о.")
        self.inf_lbl_3 = QtWidgets.QLabel(self.win)
        self.inf_lbl_3.setText("Загальна кількість паїв:")
        self.inf_lbl_3.setAlignment(QtCore.Qt.AlignRight)
        self.inf_lbl_4 = QtWidgets.QLabel(self.win)
        self.inf_lbl_4.setText(str(fond.all_pai))
        self.inf_lbl_5 = QtWidgets.QLabel(self.win)
        self.inf_lbl_5.setText("Кількість паїв у населення:")
        self.inf_lbl_5.setAlignment(QtCore.Qt.AlignRight)
        self.inf_lbl_6 = QtWidgets.QLabel(self.win)
        self.inf_lbl_6.setText(str(fond.hum_pai))
        self.inf_lbl_7 = QtWidgets.QLabel(self.win)
        self.inf_lbl_7.setText("Вартість одного паю:")
        self.inf_lbl_7.setAlignment(QtCore.Qt.AlignRight)
        self.inf_lbl_8 = QtWidgets.QLabel(self.win)
        self.inf_lbl_8.setText(str(fond.pai) + " у. о.")
        self.i_group = QtWidgets.QGroupBox(self.win)
        self.inf_group = QtWidgets.QGridLayout(self.win)
        self.inf_group.addWidget(self.inf_lbl_1, 0, 0)
        self.inf_group.addWidget(self.inf_lbl_2, 0, 1)
        self.inf_group.addWidget(self.inf_lbl_3, 1, 0)
        self.inf_group.addWidget(self.inf_lbl_4, 1, 1)
        self.inf_group.addWidget(self.inf_lbl_5, 2, 0)
        self.inf_group.addWidget(self.inf_lbl_6, 2, 1)
        self.inf_group.addWidget(self.inf_lbl_7, 3, 0)
        self.inf_group.addWidget(self.inf_lbl_8, 3, 1)
        self.i_group.setLayout(self.inf_group)
        self.i_group.move(10, 106)
        self.i_group.setTitle("Інформація про фонд")
        self.i_group.setStyleSheet("QGroupBox {font-weight: bold;}")
    def InfoAboutIvestPorfel(self):
        if fond.portfel == {}:
            self.box_port = QtWidgets.QGroupBox(self.win)
            self.port_group = QtWidgets.QHBoxLayout(self.win)
            self.massege = QtWidgets.QLabel(self.win)
            self.massege.setText("Інформація про портфель відсутня")
            self.port_group.addWidget(self.massege)
            self.box_port.setLayout(self.port_group)
            self.box_port.move(10, 246)
            self.box_port.setTitle("Інформація про портфель фонду")
            self.box_port.resize(265, 56)
            self.box_port.setStyleSheet("QGroupBox {font-weight: bold;}")
        else:
            self.box_port = QtWidgets.QGroupBox(self.win)
            self.port_group = QtWidgets.QGridLayout()
            self.box_port.setLayout(self.port_group)
            self.box_port.move(10, 246)
            self.box_port.setTitle("Інформація про портфель фонду")
            self.box_port.resize(265, 100)
            self.widgets = []
            self.build_widgets()
    def build_widgets(self):
        names = ('плюшки', 'баранки', 'бублики')

        for row, i in enumerate(names):
            self.label = QtWidgets.QLabel("Введите {}: ".format(i))
            self.port_group.addWidget(self.label, row, 0)

            self.line_edit = QtWidgets.QLineEdit()
            self.port_group.addWidget(self.line_edit, row, 1)

            self.widgets.append((self.label, self.line_edit))

        # show = QtGui.QPushButton('Вывести содердимое полей')
        # show.clicked.connect(self.show_content)
        # self.main_layout.addWidget(show, len(names) + 1, 0)




if __name__ == "__main__":
    fond = ClassFond.Infond()
    fond.add_bank('pb', 10000, 3, 3, 0.12)
    # fond.add_bank('pb', 10000, 3, 3, 0.12)
    # fond.add_bank_metal('gold', 5, 1536)
    # fond.add_bank_metal('plt', 5, 2536)
    # fond.add_actions('metivest', 100, 12.5)
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()

    sys.exit(app.exec_())