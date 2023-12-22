import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QPushButton, QLineEdit
from functools import partial

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QGridLayout()

        self.equation_solution_line = QLineEdit("")
        main_layout.addWidget(self.equation_solution_line, 0, 0, 1, 5)

        layout_number = QGridLayout()
        number_button_dict = {}

        button_percent = QPushButton("%")
        button_ce = QPushButton("CE")
        button_clear = QPushButton("C")
        button_backspace = QPushButton("\u2190") 
        button_percent.clicked.connect(lambda state, operation="%": self.button_operation_clicked(operation))
        button_ce.clicked.connect(self.button_clear_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        main_layout.addWidget(button_percent, 1, 0)
        main_layout.addWidget(button_ce, 1, 1)
        main_layout.addWidget(button_clear, 1, 2)
        main_layout.addWidget(button_backspace, 1, 3)

        button_reciprocal = QPushButton("1/x")
        button_square = QPushButton("x^2")
        button_square_root = QPushButton("√x")
        button_division = QPushButton("÷")

        button_reciprocal.clicked.connect(self.reciprocal_clicked)
        button_square.clicked.connect(lambda state, operation="**2": self.button_operation_clicked(operation))
        button_square_root.clicked.connect(lambda state, operation="**0.5": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation="/": self.button_operation_clicked(operation))

        main_layout.addWidget(button_reciprocal, 2, 0)
        main_layout.addWidget(button_square, 2, 1)
        main_layout.addWidget(button_square_root, 2, 2)
        main_layout.addWidget(button_division, 2, 3)

        button_7 = QPushButton("7")
        button_8 = QPushButton("8")
        button_9 = QPushButton("9")
        button_product = QPushButton("x")

        button_7.clicked.connect(lambda state, num="7": self.number_button_clicked(num))
        button_8.clicked.connect(lambda state, num="8": self.number_button_clicked(num))
        button_9.clicked.connect(lambda state, num="9": self.number_button_clicked(num))
        button_product.clicked.connect(lambda state, operation="*": self.button_operation_clicked(operation))

        main_layout.addWidget(button_7, 3, 0)
        main_layout.addWidget(button_8, 3, 1)
        main_layout.addWidget(button_9, 3, 2)
        main_layout.addWidget(button_product, 3, 3)

        ### 4, 5, 6, - 버튼 생성
        button_4 = QPushButton("4")
        button_5 = QPushButton("5")
        button_6 = QPushButton("6")
        button_minus = QPushButton("-")

        button_4.clicked.connect(lambda state, num="4": self.number_button_clicked(num))
        button_5.clicked.connect(lambda state, num="5": self.number_button_clicked(num))
        button_6.clicked.connect(lambda state, num="6": self.number_button_clicked(num))
        button_minus.clicked.connect(lambda state, operation="-": self.button_operation_clicked(operation))

        main_layout.addWidget(button_4, 4, 0)
        main_layout.addWidget(button_5, 4, 1)
        main_layout.addWidget(button_6, 4, 2)
        main_layout.addWidget(button_minus, 4, 3)

        button_1 = QPushButton("1")
        button_2 = QPushButton("2")
        button_3 = QPushButton("3")
        button_plus = QPushButton("+")

        button_1.clicked.connect(lambda state, num="1": self.number_button_clicked(num))
        button_2.clicked.connect(lambda state, num="2": self.number_button_clicked(num))
        button_3.clicked.connect(lambda state, num="3": self.number_button_clicked(num))
        button_plus.clicked.connect(lambda state, operation="+": self.button_operation_clicked(operation))

        main_layout.addWidget(button_1, 5, 0)
        main_layout.addWidget(button_2, 5, 1)
        main_layout.addWidget(button_3, 5, 2)
        main_layout.addWidget(button_plus, 5, 3)

        button_change_sign = QPushButton("+/-")
        button_0 = QPushButton("0")
        button_dot = QPushButton(".")
        button_equal = QPushButton("=")

        button_change_sign.clicked.connect(self.change_sign_clicked)
        button_0.clicked.connect(lambda state, num="0": self.number_button_clicked(num))
        button_dot.clicked.connect(lambda state, num=".": self.number_button_clicked(num))
        button_equal.clicked.connect(self.button_equal_clicked)

        main_layout.addWidget(button_change_sign, 6, 0)
        main_layout.addWidget(button_0, 6, 1)
        main_layout.addWidget(button_dot, 6, 2)
        main_layout.addWidget(button_equal, 6, 3)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################

    def reciprocal_clicked(self):
        current_text = self.equation_solution_line.text()
        try:
            value = float(current_text)
            if value != 0:
                reciprocal_value = 1 / value
                self.equation_solution_line.setText(str(reciprocal_value))
            else:
                self.equation_solution_line.setText("Error")
        except Exception as e:
            self.equation_solution_line.setText("Error")

    def number_button_clicked(self, num):
        equation = self.equation_solution_line.text()
        if equation == "0" or equation == "-0":
            equation = num
        else:
            equation += str(num)
        self.equation_solution_line.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation_solution_line.text()
        if equation == "0" or equation == "-0":
            equation = ""
        equation += operation
        self.equation_solution_line.setText(equation)

        if operation in {"%", "1/x", "**2", "**0.5"}:
            self.button_equal_clicked()

    def button_equal_clicked(self):
        equation = self.equation_solution_line.text()
        if "%" in equation:
            equation = equation.replace("%", "/100")
        try:
            solution = eval(equation)
            self.equation_solution_line.setText(str(solution))  
        except Exception as e:
            self.equation_solution_line.setText("Error")

    def button_clear_clicked(self):
        self.equation_solution_line.setText("0")

    def button_backspace_clicked(self):
        equation = self.equation_solution_line.text()
        if len(equation) == 1 or (len(equation) == 2 and equation[0] == '-'):
            self.equation_solution_line.setText("0")
        else:
            equation = equation[:-1]
            self.equation_solution_line.setText(equation)

    def change_sign_clicked(self):
        equation = self.equation_solution_line.text()
        if equation and equation[0] == '-':
            equation = equation[1:]
        else:
            equation = '-' + equation
        self.equation_solution_line.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

