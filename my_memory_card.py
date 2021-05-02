from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QMessageBox, QGroupBox, QHBoxLayout, QButtonGroup
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('2+2', '4', '5', '6', '7'))
question_list.append(Question('25+25', '50', '70', '45', '32'))
question_list.append(Question('43+32', '75', '123', '76', '81'))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')

RadioGroupBox = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton('a')
rbtn_2 = QRadioButton('b')
rbtn_3 = QRadioButton('c')
rbtn_4 = QRadioButton('d')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

answer  = QPushButton('Ответить')
lb_question = QLabel('?')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2, stretch = 10)
layout_ans1.addLayout(layout_ans3, stretch = 10)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox =QGroupBox('Результат теста')
label_res = QLabel('Верно!')
label_cor = QLabel('правильный ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(label_res, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(label_cor, alignment =  Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(answer, stretch = 1)
layout_line3.addStretch(1)

layout_main = QVBoxLayout()
layout_main.addLayout(layout_line1, stretch = 2)
layout_main.addLayout(layout_line2, stretch = 8)
layout_main.addStretch(1)
layout_main.addLayout(layout_line3, stretch = 1)
layout_main.addStretch(1)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

# def test():
#     if 'Ответить' == answer.text():
#         show_result()
#     else:
#         show_question()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    label_cor.setText(q.right_answer)
    show_question()

def show_correct(res):
    label_res.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked or answers[3].isChecked:
            show_correct('Неверно!')

def next_question():
    main_win.cur_question = main_win.cur_question + 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0
    q = question_list[main_win.cur_question]
    ask(q)

def click_ok():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()

main_win.setLayout(layout_main)
main_win.cur_question = -1
q = Question('?', '1', '2', '3', '4')
ask(q)
answer.clicked.connect(click_ok)

main_win.score = 0
main_win.show()

next_question()
main_win.show()
app.exec_()