import sys
from docxtpl import DocxTemplate
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from darktheme.widget_template import DarkPalette
# Import UI
from reports_app.ui.main_window_ui import Ui_MainWindow
from datetime import datetime


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.report_pushButton.clicked.connect(self.generate_report)
        # Set current date
        self.report_dat_dateEdit.setDate(QDate(datetime.now()))
        # Hide/unhide rect/circle input widget
        self.circle_radioButton.toggled.connect(self.rect_circle_change)
        self.rect_groupBox.hide()

    def generate_report(self):
        context = {
            "report_date": self.report_dat_dateEdit.date().toPyDate().strftime("%Y.%m.%d"),
            "start_time": self.measure_start_timeEdit.time().toString("hh.mm"),
            "end_time": self.measure_start_timeEdit.time().toString("hh.mm"),
            "obj_name": self.object_name_textEdit.toPlainText(),
            "report_n": self.report_name_spinBox.text(),
            "obj_place": self.obj_place_textEdit.toPlainText(),
            "obj_place_det": self.obj_place_det_textEdit.toPlainText(),
            "straight_l": self.circle_straight_l_spinBox.text() if
            self.circle_radioButton.isChecked() else self.rect_straight_l_spinBox.text(),
            "circle_D": self.circle_D_spinBox.text(),
            "rect_A": self.rect_A_spinBox.text(),
            "rect_B": self.rect_B_spinBox.text()

        }
        name = QFileDialog.getSaveFileName(self, 'Сохранить файл', filter='Word 2007-365 (.docx)')
        doc = DocxTemplate("templates/appendix_1.docx")
        print(doc)
        print(name)
        doc.render(context)
        doc.save(name[0])

    def rect_circle_change(self):
        if self.circle_radioButton.isChecked():
            self.rect_groupBox.hide()
            self.circle_groupBox.show()
        else:
            self.circle_groupBox.hide()
            self.rect_groupBox.show()


app = QApplication(sys.argv)
app.setPalette(DarkPalette())

# All code goes here

mainGui = MainWindow()
mainGui.show()
sys.exit(app.exec_())
