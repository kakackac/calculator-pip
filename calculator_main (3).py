import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QPushButton, QLineEdit

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QGridLayout()


        button_division = QPushButton("/")
        button_product = QPushButton("x")
        button_minus = QPushButton("-")
        button_plus = QPushButton("+")



        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################

    def number_button_clicked(self, num):
        equation = self.equation_solution_line.text()
        equation += str(num)
        self.equation_solution_line.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation_solution_line.text()
        equation += operation
        self.equation_solution_line.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation_solution_line.text()


    def button_backspace_clicked(self):
        equation = self.equation_solution_line.text()
        equation = equation[:-1]
        self.equation_solution_line.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
