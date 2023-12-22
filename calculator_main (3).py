import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QPushButton, QLineEdit


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QGridLayout()


        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################


        self.equation_solution_line.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation_solution_line.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
