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

        layout_number = QGridLayout()
        number_button_dict = {}

        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num=number: self.number_button_clicked(num))

            if number > 0:
                x, y = divmod(number - 1, 3)
                layout_number.addWidget(number_button_dict[number], x, y)
            elif number == 0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num=".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num="00": self.number_button_clicked(num))
        layout_number.addWidget(button_double_zero, 3, 0)

        button_division = QPushButton("/")
        button_product = QPushButton("x")
        button_minus = QPushButton("-")
        button_plus = QPushButton("+")

        button_division.clicked.connect(lambda state, operation="/": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation="*": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation="-": self.button_operation_clicked(operation))
        button_plus.clicked.connect(lambda state, operation="+": self.button_operation_clicked(operation))

        layout_buttons = QGridLayout()
        layout_buttons.addLayout(layout_number, 0, 0, 4, 4)
        layout_buttons.addWidget(button_plus, 0, 4)
        layout_buttons.addWidget(button_minus, 1, 4)
        layout_buttons.addWidget(button_product, 2, 4)
        layout_buttons.addWidget(button_division, 3, 4)

        button_equal = QPushButton("=")
        button_clear = QPushButton("Clear")
        button_backspace = QPushButton("Backspace")

        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        layout_clear_equal = QGridLayout()
        layout_clear_equal.addWidget(button_clear, 0, 0)
        layout_clear_equal.addWidget(button_backspace, 0, 1)
        layout_clear_equal.addWidget(button_equal, 0, 2)

        main_layout.addLayout(layout_buttons, 1, 0, 1, 4)
        main_layout.addLayout(layout_clear_equal, 2, 0, 1, 4)

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
