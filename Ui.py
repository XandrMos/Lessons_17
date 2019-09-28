import sys
import ClassFond
from PyQt5 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.win = QtWidgets.QWidget()
        self.win.resize(800, 800)
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
        self.push_btn_mounth = 0
        self.btn_mounth.clicked.connect(self.on_clicked)

        self.group = QtWidgets.QGroupBox(self.win)
        self.head_group = QtWidgets.QHBoxLayout(self.win)
        self.head_group.addWidget(self.text_hd)
        self.head_group.addWidget(self.ed_mounth)
        self.head_group.addWidget(self.btn_mounth)
        self.group.setLayout(self.head_group)
        self.group.move(10, 36)
        self.group.resize(380, 60)
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
        self.i_group.show()
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
            return 56
        else:
            self.box_port = QtWidgets.QGroupBox(self.win)
            self.port_group = QtWidgets.QGridLayout()
            self.box_port.setLayout(self.port_group)
            self.box_port.move(10, 246)
            self.box_port.setTitle("Інформація про портфель фонду")
            self.box_port.setStyleSheet("QGroupBox {font-weight: bold;}")
            self.widgets = []
            self.build_widgets_port_fond()
            self.box_port.resize(265, len(self.widgets) * 32)
            self.box_port.show()
            return len(self.widgets) * 32
    def build_widgets_port_fond(self):
        row = 0
        for samp in fond.portfel.keys():
            if samp[0:8] == 'bank_of_':
                for note in fond.portfel[samp]:
                    self.label = QtWidgets.QLabel(samp)
                    self.label.setAlignment(QtCore.Qt.AlignRight)
                    self.port_group.addWidget(self.label, row, 0)
                    self.inf_label = QtWidgets.QLabel(str(note[0]) + "$, " + str(note[2]) + " months, " + str(note[3]) + "%")
                    self.port_group.addWidget(self.inf_label, row, 1)
                    self.widgets.append((self.label, self.inf_label))
                    row += 1
            else:
                self.label = QtWidgets.QLabel(samp)
                self.label.setAlignment(QtCore.Qt.AlignRight)
                self.port_group.addWidget(self.label, row, 0)
                self.inf_label = QtWidgets.QLabel(str(fond.portfel[samp]) + " units")
                self.port_group.addWidget(self.inf_label, row, 1)
                self.widgets.append((self.label, self.inf_label))
                row += 1

    def info_profit(self, height_inf_port):
        self.box_profit = QtWidgets.QGroupBox(self.win)
        self.profit_group = QtWidgets.QGridLayout()
        self.profit_lbl_1 = QtWidgets.QLabel(self.win)
        self.profit_lbl_1.setText("Загалом:")
        self.profit_lbl_1.setAlignment(QtCore.Qt.AlignRight)
        self.profit_lbl_2 = QtWidgets.QLabel(self.win)
        self.profit_lbl_2.setText(str(fond.profit) + " у. о.")
        self.profit_lbl_3 = QtWidgets.QLabel(self.win)
        self.profit_lbl_3.setText("Податки:")
        self.profit_lbl_3.setAlignment(QtCore.Qt.AlignRight)
        self.profit_lbl_4 = QtWidgets.QLabel(self.win)
        self.profit_lbl_4.setText(str(fond.setTax()) + " у. о.")
        self.profit_lbl_5 = QtWidgets.QLabel(self.win)
        self.profit_lbl_5.setText("Чистий прибуток:")
        self.profit_lbl_5.setAlignment(QtCore.Qt.AlignRight)
        self.profit_lbl_6 = QtWidgets.QLabel(self.win)
        self.profit_lbl_6.setText(str(fond.profit - fond.setTax()) + " у. о.")
        self.profit_group.addWidget(self.profit_lbl_1, 0, 0)
        self.profit_group.addWidget(self.profit_lbl_2, 0, 1)
        self.profit_group.addWidget(self.profit_lbl_3, 1, 0)
        self.profit_group.addWidget(self.profit_lbl_4, 1, 1)
        self.profit_group.addWidget(self.profit_lbl_5, 2, 0)
        self.profit_group.addWidget(self.profit_lbl_6, 2, 1)
        self.box_profit.setLayout(self.profit_group)
        self.box_profit.move(10, height_inf_port + 256)
        self.box_profit.resize(265, 106)
        self.box_profit.setTitle("Прибуток інвестеціного фонда")
        self.box_profit.setStyleSheet("QGroupBox {font-weight: bold;}")
        self.box_profit.show()
    def GeneretTernds(self):
        self.banks = []
        self.metals = []
        self.actions = []
        for i in range(2):
            bnk = ClassFond.Bank()
            self.banks.append(bnk)
            mtls = ClassFond.BankMetal()
            self.metals.append(mtls)
            act = ClassFond.Actions()
            self.actions.append(act)
        self.box_trends = QtWidgets.QGroupBox(self.win)
        self.trends_group = QtWidgets.QGridLayout()
        self.box_trends.setLayout(self.trends_group)
        self.box_trends.move(400, 106)
        self.box_trends.setTitle("Інформація про тренди")
        self.box_trends.setStyleSheet("QGroupBox {font-weight: bold;}")
        self.widgets_trends = []
        self.build_widgets_trends()
        self.box_trends.resize(256,len(self.widgets_trends) * 31)
        self.box_trends.show()
    def build_widgets_trends(self):
        row = 0
        for i in range(2):
            self.label_t = QtWidgets.QLabel(self.banks[i].bank_name)
            self.label_t.setAlignment(QtCore.Qt.AlignRight)
            self.trends_group.addWidget(self.label_t, row, 0)
            self.inf_label_t = QtWidgets.QLabel(str(self.banks[i].bank_period) \
                                                + " months " \
                                                + str(int(self.banks[i].bank_percent * 100)) \
                                                + "%")
            self.trends_group.addWidget(self.inf_label_t, row, 1)
            self.widgets_trends.append((self.label_t, self.inf_label_t))
            row += 1
            self.label_t = QtWidgets.QLabel(self.metals[i].BankMetal_name)
            self.label_t.setAlignment(QtCore.Qt.AlignRight)
            self.trends_group.addWidget(self.label_t, row, 0)
            self.inf_label_t = QtWidgets.QLabel(str(self.metals[i].BankMetal_price) + " y.o. ")
            self.trends_group.addWidget(self.inf_label_t, row, 1)
            self.widgets_trends.append((self.label_t, self.inf_label_t))
            row += 1
            self.label_t = QtWidgets.QLabel(self.actions[i].Actions_name)
            self.label_t.setAlignment(QtCore.Qt.AlignRight)
            self.trends_group.addWidget(self.label_t, row, 0)
            self.inf_label_t = QtWidgets.QLabel(str(self.actions[i].Actions_price) + " y.o. ")
            self.trends_group.addWidget(self.inf_label_t, row, 1)
            self.widgets_trends.append((self.label_t, self.inf_label_t))
            row +=1
    def Banks_widget(self):
        self.box_Banks_widget = QtWidgets.QGroupBox(self.win)
        self.Banks_widget_group = QtWidgets.QGridLayout()
        self.box_Banks_widget.setLayout(self.Banks_widget_group)
        self.box_Banks_widget.move(400, 122 + len(self.widgets_trends) * 31)
        self.box_Banks_widget.setTitle("Депозити")
        self.box_Banks_widget.setStyleSheet("QGroupBox {font-weight: bold;}")
        self.widgets_Banks_widget = []
        self.build_widgets_Banks_widget()
        self.box_Banks_widget.resize(256, 106)
        self.box_Banks_widget.show()
    def build_widgets_Banks_widget(self):
        row = 0
        for i in range(2):
            self.label = QtWidgets.QLabel(self.banks[i].bank_name)
            self.label.setAlignment(QtCore.Qt.AlignRight)
            self.Banks_widget_group.addWidget(self.label, row, 0)
            self.edit = QtWidgets.QLineEdit("0")
            self.Banks_widget_group.addWidget(self.edit, row, 1)
            self.widgets_Banks_widget.append((self.label, self.edit))
            row += 1
    def Metals_widget(self):
        self.box_Metals_widget = QtWidgets.QGroupBox(self.win)
        self.Metals_widget_group = QtWidgets.QGridLayout()
        self.box_Metals_widget.setLayout(self.Metals_widget_group)
        self.box_Metals_widget.move(400, 2 * 122 +len(self.widgets_trends) * 31)
        self.box_Metals_widget.setTitle("Банківські метали")
        self.box_Metals_widget.setStyleSheet("QGroupBox {font-weight: bold;}")
        self.widgets_Metals_widget = []
        self.build_widgets_Metals_widget()
        self.box_Metals_widget.resize(256, 106)
        self.box_Metals_widget.show()
    def build_widgets_Metals_widget(self):
        row = 0
        for i in range(2):
            self.label = QtWidgets.QLabel(self.metals[i].BankMetal_name)
            self.label.setAlignment(QtCore.Qt.AlignRight)
            self.Metals_widget_group.addWidget(self.label, row, 0)
            self.edit = QtWidgets.QLineEdit("0")
            self.Metals_widget_group.addWidget(self.edit, row, 1)
            self.widgets_Metals_widget.append((self.label, self.edit))
            row += 1
    def Actions_widget(self):
        self.box_Actions_widget = QtWidgets.QGroupBox(self.win)
        self.Actions_widget_group = QtWidgets.QGridLayout()
        self.box_Actions_widget.setLayout(self.Actions_widget_group)
        self.box_Actions_widget.move(400, 3 * 122 + len(self.widgets_trends) * 31)
        self.box_Actions_widget.setTitle("Банківські метали")
        self.box_Actions_widget.setStyleSheet("QGroupBox {font-weight: bold;}")
        self.widgets_Actions_widget = []
        self.build_widgets_Actions_widget()
        self.box_Actions_widget.resize(256, 106)
        self.box_Actions_widget.show()
    def build_widgets_Actions_widget(self):
        row = 0
        for i in range(2):
            self.label = QtWidgets.QLabel(self.actions[i].Actions_name)
            self.label.setAlignment(QtCore.Qt.AlignRight)
            self.Actions_widget_group.addWidget(self.label, row, 0)
            self.edit = QtWidgets.QLineEdit("0")
            self.Actions_widget_group.addWidget(self.edit, row, 1)
            self.widgets_Actions_widget.append((self.label, self.edit))
            row += 1

    def on_clicked(self):
        if self.push_btn_mounth == 0:
            self.InfoAboutFond()
            h = self.InfoAboutIvestPorfel()
            self.info_profit(h)
            self.GeneretTernds()
            self.Banks_widget()
            self.Metals_widget()
            self.Actions_widget()
            self.push_btn_mounth = 1



if __name__ == "__main__":
    fond = ClassFond.Infond()
    fond.add_bank('pb', 10000, 3, 3, 0.12)
    fond.add_bank('pb', 10000, 6, 6, 0.12)
    fond.add_bank('aval', 10000, 6, 6, 0.12)
    fond.add_bank_metal('gold', 5, 1536)
    fond.add_bank_metal('plt', 5, 2536)
    fond.add_actions('metivest', 100, 12.5)
    fond.setProfit_bank(6)
    fond.sellMetal('gold', 3, 1245)
    fond.sellMetal('plt', 2, 1245)
    fond.sellAction('metivest', 20, 11.5)
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()

    sys.exit(app.exec_())