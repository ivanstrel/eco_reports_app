import sys
from docxtpl import DocxTemplate
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from darktheme.widget_template import DarkPalette
# Import UI
from reports_app.ui.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.report_pushButton.clicked.connect(self.generate_report)

    def generate_report(self):
        context = {
            "report_date": self.report_dat_dateEdit.date().toPyDate().strftime("%Y.%m.%d"),
            "start_time": self.measure_start_timeEdit.time().toString("hh.mm"),
            "end_time": self.measure_start_timeEdit.time().toString("hh.mm"),
            "obj_name": self.object_name_lineEdit.text(),
            "report_n": self.report_name_spinBox.text(),
        }

        name = QFileDialog.getSaveFileName(self, 'Сохранить файл', filter='Word 2007-365 (.docx)')
        doc = DocxTemplate("templates/appendix_1.docx")
        print(doc)
        print(name)
        doc.render(context)
        doc.save(name[0])


app = QApplication(sys.argv)
app.setPalette(DarkPalette())

# All code goes here

mainGui = MainWindow()
mainGui.show()
sys.exit(app.exec_())
