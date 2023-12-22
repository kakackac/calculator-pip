import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QPushButton, QLineEdit

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QGridLayout()

        self.equation_solution_line = QLineEdit("")
        main_layout.addWidget(self.equation_solution_line, 0, 0, 1, 4)


        
        self.equation_solution_line = QLineEdit("")
        main_layout.addWidget(self.equation_solution_line)

        
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")

        button_division = QPushButton("/")
        button_product = QPushButton("x")
        button_minus = QPushButton("-")
        button_plus = QPushButton("+")


        button_equal = QPushButton("=")
        button_clear = QPushButton("Clear")
        button_backspace = QPushButton("Backspace")

        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)



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
        solution = eval(equation)
        self.equation_solution_line.setText(str(solution))  # 숫자를 문자열로 변환하여 설정


    def button_clear_clicked(self):
        self.equation_solution_line.setText("")

    def button_backspace_clicked(self):
        equation = self.equation_solution_line.text()
        equation = equation[:-1]
        self.equation_solution_line.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
