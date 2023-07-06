from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
                    QApplication, 
                    QWidget,
                    QPushButton,
                    QLabel,
                    QVBoxLayout,
                    QHBoxLayout )
app = QApplication([])
window = QWidget()                    
window.setFixedSize(360, 500)
window.setWindowTitle("Калькулятор")
window.setStyleSheet('''
*{
    font-size: 24px;
}
QWidget{
    background-color: rgba(0,0,0,0.5);
}
QPushButton{
    height: 70px;
    color: white;
    }''')

main_layout = QVBoxLayout()
main_layout.setSpacing(0)
h1_layout = QHBoxLayout()
h1_layout.setSpacing(12)
h2_layout = QHBoxLayout()
h2_layout.setSpacing(12)
h3_layout = QHBoxLayout()
h3_layout.setSpacing(12)
h4_layout = QHBoxLayout()
h4_layout.setSpacing(12)
h5_layout = QHBoxLayout()
h5_layout.setSpacing(12)
h6_layout = QHBoxLayout()
h6_layout.setSpacing(12)

total = QLabel('')
total_str = ''
h1_layout.addWidget(total, alignment= Qt.AlignRight)
total.setStyleSheet('''background-color: transparent;
font-size: 28px;
color: white;
''')
button_C = QPushButton('C')
button_AC = QPushButton('AC')
button_percent = QPushButton('%')
button_devision = QPushButton('/')
button_multi = QPushButton('*') # 2
button_minus = QPushButton('-') # 3
button_plus = QPushButton('+') # 4
button_dot = QPushButton('.') # 6
button_equals = QPushButton('=') # 6
button_devision.setStyleSheet('''background-color: #EBAD1C;''')
button_multi.setStyleSheet('''background-color: #EBAD1C;''')
button_minus.setStyleSheet('''background-color: #EBAD1C;''')
button_plus.setStyleSheet('''background-color: #EBAD1C;''')
button_equals.setStyleSheet('''background-color: #EBAD1C;''')
button_dot.setStyleSheet('''background-color: #7D7D7D;''')


h2_layout.addWidget(button_C)
h2_layout.addWidget(button_AC)
h2_layout.addWidget(button_percent)
h2_layout.addWidget(button_devision)
numbers = []
for number in range(10):
    numbers.append(QPushButton(str(number)))
    numbers[-1].setStyleSheet('''
    background-color: #7D7D7D; ''')
numbers[0].setStyleSheet('''width: 152px;
background-color: #7D7D7D;''')
k = 1
h6_layout.addWidget(numbers[0])
for  i in range(3):
    h5_layout.addWidget(numbers[k])
    k += 1
for i in range(3):
    h4_layout.addWidget(numbers[k])
    k += 1  
for i in range(3):
    h3_layout.addWidget(numbers[k])
    k += 1

h3_layout.addWidget(button_multi)
h4_layout.addWidget(button_minus)
h5_layout.addWidget(button_plus)
h6_layout.addWidget(button_dot)
h6_layout.addWidget(button_equals)

main_layout.addLayout(h1_layout)
main_layout.addLayout(h2_layout)
main_layout.addLayout(h3_layout)
main_layout.addLayout(h4_layout)
main_layout.addLayout(h5_layout)
main_layout.addLayout(h6_layout)



def a1():
    global total_str
    total_str += '1'
    total.setText(total_str)
def a2():
    global total_str
    total_str += '2'
    total.setText(total_str)
def a3():
    global total_str
    total_str += '3'
    total.setText(total_str)
def a4():
    global total_str
    total_str += '4'
    total.setText(total_str)
def a5():
    global total_str
    total_str += '5'
    total.setText(total_str)
def a6():
    global total_str
    total_str += '6'
    total.setText(total_str)
def a7():
    global total_str
    total_str += '7'
    total.setText(total_str)
def a8():
    global total_str
    total_str += '8'
    total.setText(total_str)
def a9():
    global total_str
    total_str += '9'
    total.setText(total_str)
def a0():
    global total_str
    total_str += '0'
    total.setText(total_str)
blocked = ['-', '+', '.', '*', '/']

def a_plus():
    global total_str
    if total_str != "":
        if total_str[-1] not in blocked:
            total_str += '+'
            total.setText(total_str)
def a_minus():
    global total_str
    if len(total_str) >= 2:
        if total_str[-1] != '.':
            if total_str[-1] in blocked and total_str[-2] in blocked:
                pass
            else:
                total_str += '-'
                total.setText(total_str)
    else:
        if total_str != '-':
            total_str += '-'
            total.setText(total_str)

def a_devision():
    global total_str
    if total_str != "":
        if total_str[-1] not in blocked:
            total_str += '/'
            total.setText(total_str)
def a_multi():
    global total_str
    if total_str != "":
        if total_str[-1] not in blocked:
            total_str += '*'
            total.setText(total_str)
def a_dot():
    global total_str
    if total_str != "":
        if total_str[-1] not in blocked and total_str[-1] != "%":
            total_str += '.'
            total.setText(total_str) 
def a_percent():
    global total_str
    if total_str != "":
        if total_str[-1] not in blocked and total_str[-1] != "%":
            total_str += '%'
            total.setText(total_str)
 
def a_AC():
    global total_str
    total.clear()
    total_str = ''
def a_C():
    global total_str
    if total_str:
        tmp_list = list(total_str)
        tmp_str = ''
        del tmp_list[-1]
        for i in tmp_list:
            tmp_str += i
        total_str = tmp_str
        total.setText(total_str)
defs_numbers = {}
defs_numbers['1'] = a1
defs_numbers['2'] = a2
defs_numbers['3'] = a3
defs_numbers['4'] = a4
defs_numbers['5'] = a5
defs_numbers['6'] = a6
defs_numbers['7'] = a7
defs_numbers['8'] = a8
defs_numbers['9'] = a9
defs_numbers['0'] = a0

for i in range(0, 10):
    numbers[i].clicked.connect(defs_numbers[str(i)])

button_plus.clicked.connect(a_plus)
button_minus.clicked.connect(a_minus)
button_devision.clicked.connect(a_devision)
button_multi.clicked.connect(a_multi)
button_dot.clicked.connect(a_dot)
button_percent.clicked.connect(a_percent)
button_C.clicked.connect(a_C)
button_AC.clicked.connect(a_AC)

def a_equals():
    global total_str
    if total_str[-1] in blocked:
        a_C()
    total_int = 0
    total_list = []


    # 100+200*10
    count_symbols = 0
    for i in range(0,len(total_str)):
        if (total_str[i] == '+' or 
            total_str[i] == '-' or 
            total_str[i] == '*' or 
            total_str[i] == '/' or 
            total_str[i] == '%'):
            if count_symbols != 0:
                tmp = total_str[i-count_symbols:i]
                try:
                    total_list.append(int(tmp))
                except:
                    total_list.append(float(tmp))
                total_list.append(total_str[i])
                count_symbols = 0
            elif total_str[i-1] == '%':
                total_list.append(total_str[i])
                count_symbols = 0
            else:
                count_symbols += 1
        elif i == len(total_str) - 1:
            tmp = total_str[i-count_symbols:i+1]
            try:
                total_list.append(int(tmp))
            except:
                total_list.append(float(tmp))
        else:
            count_symbols += 1
    print(total_list)
    while len(total_list) != 1:
        for i in range(0, len(total_list)):
            if total_list[i] == "%":
                # 81% - 100 + 200
                # 100  -   50    %
                # i-3 i-2  i-1   i
                if i == 1:
                    total_list[0]= total_list[0]/100
                    del total_list[1]
                    break
                else:
                    total_list[i-1] = total_list[i-3]/100*total_list[i-1]
                    print(total_list[i-1])
                    del total_list[i]
                    break
            elif total_list[i] == "*":
                total_list[i] = total_list[i-1] * total_list[i+1]
                del total_list[i+1]
                del total_list[i-1]
                break
            elif total_list[i] == "/":
                total_list[i] = total_list[i-1] / total_list[i+1]
                del total_list[i+1]
                del total_list[i-1]
                break
            elif ('*' not in total_list and 
                    "/" not in total_list and 
                    '%' not in total_list):
                if total_list[i] == "+":
                    total_list[i] = total_list[i-1] + total_list[i+1]
                    del total_list[i+1]
                    del total_list[i-1]
                    break
                elif total_list[i] == "-":
                    total_list[i] = total_list[i-1] - total_list[i+1]
                    del total_list[i+1]
                    del total_list[i-1]
                    break
    total.setText(str(total_list[0]))
    total_str = str(total_list[0])
button_equals.clicked.connect(a_equals)


window.setLayout(main_layout)
window.show()
app.exec_()
