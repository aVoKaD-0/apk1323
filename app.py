import sys
from typing import Optional

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase

from design import Ui_MainWindow
import config
import math
ch = 1

def vynos_celogo_chisla(number): # выносит целое число
    global ch
    number2 = math.sqrt(number)
    if str(number2).find(".") == len(str(number2))-2 and ch == 1:
        ch = 1
        return int(str(number2)[:-2]), 0
    number2 = 10
    while number2**2 < number:
        number2 += 10
    for i in range(number2-10, number2+1):
        for k in range(number2-10, number2+1):
            if i*k == number:
                for l in range(1, k):
                    if l*l == k:
                        ch = 1
                        return l, i
    ch = 1
    return 0, 0

def vynos_NeCelogo_chisla(number): # выносит не целое число
    number2 = number
    decrease = "1"
    global ch
    for i in range(len(str(number2))-1, 0, -1):
        if str(number2)[i] == "e":
            decrease += "0"*int(str(number2)[i+2:])
            break
    number2 *= float(decrease)
    decrease = 1/int(decrease)
    dlina = len(str(number2)[(str(number2).find("."))+1:])
    while str(number2)[-1] != "0" or str(number2)[-2] != ".":
        number2 *= 10
        decrease /= 10
        dlina -= 1
        number2 = round(number2, dlina)
    number3, number4 = vynos_celogo_chisla(int(number2))
    if number4 == 0 and number3 != 0:
        if len(str(number)[str(number).find(".")+1:])%2 == 0:
            number3 /= int("1"+("0"*((len(str(decrease))-1)//2)))
        else:
            ch = 2
            number3, number4 = vynos_celogo_chisla(int(number2))
    if number4 != 0 and number3 != 0:
        flag = True
        for t in range(0, len(str(decrease))): # Смотрим длину после точки у первого числа
            for i in range(0, len(str(decrease))): # Смотрим длину после точки у второго числа
                if round(round(((number3/int("1"+"0"*t))**2), t*2)*round((number4/int("1"+"0"*i)), i*2), i*2+t*2) == number:
                    number3 = number3/int("1"+"0"*t)
                    number4 = number4/int("1"+"0"*i)
                    if i == 0:
                        number4 = int(number4)
                    if t == 0:
                        number3 = int(number3)
                    flag = False
                    break
            if flag == False:
                break
        if flag == True:
            number3, number4 = 0, 0
    return number3, number4

def proverka_dlin_chisla(number):
    flag = True
    number = str(number)
    tochka = str(number).find(".")
    for t in range(tochka+2, len(str(number[tochka+1:]))): # Смотрим длину после точки у первого числа
        if t != len(number)-2:
            if  number[t+1] == number[t]:
                for i in range(t+2, len(str(number[tochka+1:]))):
                    if number[i] == number[t+2]:
                        if i-t >= 3:
                            if int(number[t+2]) > 5:
                                number = number[:t-1]+str(int(number[t-1])+1)
                                flag = False
                            else:
                                number = number[:t]
                                flag = False
                            break
                    else:
                        break
        if flag == False:
            break
    if number[-1] == "0" and number[-2] == ".":
        number = number[:-2]
    return number

class Calculator(QMainWindow):
    def VynosIzPodKoren(self): #вынос из под корня
            koren = self.entry.text().replace(" ", "")
            c = 0 # проверка правильно ли стоит знак корня в строке
            f = 0 # проверка правильно ли стоит знак деления
            g = 0 # проверка правильно ли стоят числа с плавающей запятой
            f2 = 0 # проверка не стоит ли знак деления в конце или в начале
            g2 = 0 # проверка не стоит ли точка в конце или в начале  
            c2 = 0 # проверка не стоит ли знак корня в конце 
            for i in range(0, len(koren)-1):
                if koren[i] == "√":
                    c += 1
                if koren[i] == "/":
                    f += 1
                if koren[i] == ".":
                    g += 1
                if koren[i] == "√" and i == len(koren):
                    c2 += 1
                if koren[i] == "." and (i != 0 and i != len(koren)-1) and koren[i-1].isdigit() and koren[i+1].isdigit():
                    g2 += 1
                if koren[i] == "/" and (i != 0 and i != len(koren)-1) and koren[i-1].isdigit() and koren[i+1].isdigit():
                    f2 += 1
            if g > 4 or c != 1 or f > 2 or f != f2 or g != g2 or c2 != 0:
                return "Некорректный ввод"
            elif len(koren) == 1:
                return "Некорректный ввод"
            else:
                a = str(koren).find("√")
                NeKPL = True # проверяет есть ли число с плавающей запятой вне корня
                KPL = True # проверяет есть ли число с плавающей запятой под корнем
                KDR = True # проверяет есть ли дробь под корняем
                NeKDR = True # проверяет есть ли дробь вне корня
                Drob_Ne = 0
                Drob_V = 0
                for i in range(a+1, len(koren)):
                    if koren[i] == ".":
                        KPL = False  
                for i in range(a):
                    if koren[i] ==".":
                        NeKPL = False
                for i in range(a+1, len(koren)):
                    if koren[i] == "/":
                        KDR = False
                        Drob_V = i
                for i in range(a):
                    if koren[i] == "/":
                        NeKDR = False
                        Drob_Ne = i
                if KDR == True and (KPL == True or KPL == False):
                    if str(koren[a+1:]).find(".") == -1:
                        number, number2 = vynos_celogo_chisla(int(koren[a+1:]))
                    else:
                        number, number2 = vynos_NeCelogo_chisla(float(koren[a+1:]))
                    if NeKDR == True and (NeKPL == True or NeKPL == False): # если вне корня либо целое число, либо числа нету
                        if number == 0 and number2 == 0: 
                            return f"Число иррациональное"
                        else:
                            if a != 0:
                                if str(koren[:a]).isdigit() == True: # если число вне корня целое
                                    numerator = proverka_dlin_chisla(float(number*int(koren[:a])))
                                else: # если число вне корня не целое
                                    if str(number*float(koren[:a]))[-1] == "0" and str(number*float(koren[:a]))[-2] == ".":
                                        numerator = str(number*float(koren[:a]))[:-2]
                                    else:
                                        numerator = proverka_dlin_chisla(float(number*float(koren[:a])))
                            else:
                                numerator = number
                            if number2 == 0: # если вне дроби есть число и число расскладывается нацело
                                return f"{numerator}"
                            elif number2 != 0: # если вне дроби есть число и число расскладывается нацело
                                return f"{numerator}√{number2}"
                            else:
                                if number2 == 0:
                                    return f"{number}"
                                else:
                                    return f"{number}√{number2}"
                    elif NeKDR == False and (NeKPL == True or NeKPL == False): # если вне корня дробь
                        if number == 0 and number2 == 0:
                            return f"Число иррациональное"
                        else:
                            if str(koren[:Drob_Ne]).isdigit() == True: # если число вне корня целое
                                numerator = proverka_dlin_chisla(float(number*int(koren[:Drob_Ne])))
                            else: # если число вне корня не целое
                                if str(number*float(koren[:Drob_Ne]))[-1] == "0" and str(number*float(koren[:Drob_Ne]))[-2] == ".":
                                    numerator = str(number*float(koren[:Drob_Ne]))[:-2]
                                else:
                                    numerator = proverka_dlin_chisla(float(number*float(koren[:Drob_Ne])))
                            if koren[:a] != "" and number2 == 0: # если вне дроби нету числа и число расскладывается нацело
                                return f"{numerator}/{koren[Drob_Ne+1:a]}"
                            elif koren[:a] != "" and number2 != 0 : # если вне дроби есть число и число расскладывается нацело
                                return f"{numerator}√{number2}/{koren[Drob_Ne+1:a]}"
                elif KDR == False and (KPL == False or KPL == True):
                    if koren[a+1:Drob_V].find(".") == -1:
                        number, number2 = vynos_celogo_chisla(int(koren[a+1:Drob_V]))
                    else:
                        number, number2 = vynos_NeCelogo_chisla(float(koren[a+1:Drob_V]))
                    if koren[Drob_V+1:].find(".") == -1:
                        number3, number4 = vynos_celogo_chisla(int(koren[Drob_V+1:]))
                    else:
                        number3, number4 = vynos_NeCelogo_chisla(float(koren[Drob_V+1:]))
                    if NeKDR == True and (NeKPL == True or NeKPL == False):  # если вне корня либо целое число, либо числа нету
                        if (number == 0 and number2 == 0) or (number3 == 0 and number4 == 0):
                            return f"Число иррациональное"
                        else:
                            if a != 0:
                                if str(koren[:a]).isdigit() == True: # если число вне корня целое
                                    numerator = proverka_dlin_chisla(float(number*int(koren[:a])))
                                else: # если число вне корня не целое
                                    if str(number*float(koren[:a]))[-1] == "0" and str(number*float(koren[:a]))[-2] == ".":
                                        numerator = str(number*float(koren[:a]))[:-2]
                                    else:
                                        numerator = proverka_dlin_chisla(float(number*float(koren[:a])))
                            else:
                                numerator = number
                            if number2 == 0 and number4 == 0: # если исло расскладывается нацело и знаменатель расскадывается нацело
                                return f"{numerator}/{number3}" 
                            elif number2 == 0 and number4 != 0: # если число расскладывается нацело, но знаменатель расскадывается не нацело
                                return f"{numerator}/{number3}√{number4}" 
                            elif number2 != 0 and number4 == 0: # если число расскладывается нацело, но знаменатель расскадывается нацело
                                return f"{numerator}√{number2}/{number3}"
                            elif number2 != 0 and number4 != 0: # если число расскладывается нацело и знаменатель расскадывается не нацело
                                return f"{numerator}√{number2}/{number3}√{number4}"
                    elif NeKDR == False and (NeKPL == False or NeKPL == True): # если вне корня либо дробь с целыми числами, либо дробь с числа с плавающей запятой, либо смешаная дробь
                        if (number == 0 and number2 == 0) or (number3 == 0 and number4 == 0):
                            return f"Число иррациональное"
                        else:
                            if str(koren[:Drob_Ne]).isdigit() == True: # если число вне корня целое
                                numerator = proverka_dlin_chisla(float(number*int(koren[:Drob_Ne])))
                            else: # если число вне корня не целое
                                if str(number*float(koren[:Drob_Ne]))[-1] == "0" and str(number*float(koren[:Drob_Ne]))[-2] == ".":
                                    numerator = str(number*float(koren[:Drob_Ne]))[:-2]
                                else:
                                    numerator = proverka_dlin_chisla(float(number*float(koren[:Drob_Ne])))
                            if str(koren[Drob_Ne+1:a]).isdigit() == True: # если число в корне целое
                                denominator = proverka_dlin_chisla(float(number3*int(koren[Drob_Ne+1:a])))
                            else: # если число в корне не целое
                                if str(number3*float(koren[Drob_Ne+1:a]))[-1] == "0" and str(number3*float(koren[Drob_Ne+1:a]))[-2] == ".":
                                    denominator = str(number3*float(koren[Drob_Ne+1:a]))[:-2]
                                else:
                                    denominator = proverka_dlin_chisla(float(number3*float(koren[Drob_Ne+1:a])))
                            if number2 == 0 and number4 == 0: # если число расскладывается нацело и знаменатель расскадывается нацело
                                return f"{numerator}/{denominator}" 
                            elif number2 == 0 and number4 != 0: # если число расскладывается нацело, но знаменатель расскадывается не нацело
                                return f"{numerator}/{denominator}√{number4}" 
                            elif number2 != 0 and number4 == 0: # если число расскладывается нацело, но знаменатель расскадывается нацело
                                return f"{numerator}√{number2}/{denominator}"
                            elif number2 != 0 and number4 != 0: # если число расскладывается нацело и знаменатель расскадывается не нацело
                                return f"{numerator}√{number2}/{denominator}√{number4}"
        
    def VnosPodKoren(self):
        koren = self.entry.text().replace(" ", "")
        c = 0
        f = 0
        g = 0
        f2 = 0
        g2 = 0
        c2 = 0
        for i in range(0, len(koren)-1):
            if koren[i] == "√":
                c += 1
            if koren[i] == "/":
                f += 1
            if koren[i] == ".":
                g += 1
            if koren[i] == "√" and i == 0:
                c2 += 1
            if koren[i] == "." and (i != 0 and i != len(koren)-1) and koren[i-1].isdigit() and koren[i+1].isdigit():
                g2 += 1
            if koren[i] == "/" and (i != 0 and i != len(koren)-1) and koren[i-1].isdigit() and koren[i+1].isdigit():
                f2 += 1
        if koren[len(koren)-1] == "√":
            c += 1
        if g > 4 or c != 1 or f > 2 or f != f2 or g != g2 or c2 != 0:
            return "Некорректный ввод"
        elif len(koren) == 1:
            return "Некорректный ввод"
        else:
            a = str(koren).find("√")
            Drob_Ne = a
            Drob_V = len(koren)
            number2 = 0
            for i in range(a+1, len(koren)):
                if koren[i] == "/":
                    Drob_V = i
            for i in range(a):
                if koren[i] == "/":
                    Drob_Ne = i
            if str(koren[:Drob_Ne]).isdigit() == True:
                number = int(koren[:Drob_Ne])**2
            else:
                number = float(koren[:Drob_Ne])**2
            if Drob_Ne != a:
                if str(koren[Drob_Ne+1:a]).isdigit() == True:
                    number2 = int(koren[Drob_Ne+1:a])**2
                else:
                    number2 = float(koren[Drob_Ne+1:a])**2
            if str(koren[a+1:Drob_V]).isdigit() == True and len(koren[a+1:Drob_V]) != 0:
                number *= int(koren[a+1:Drob_V])
            elif str(koren[a+1:Drob_V]).isdigit() != True and len(koren[a+1:Drob_V]) != 0:
                number *= float(koren[a+1:Drob_V])
            if Drob_V != len(koren):
                if number2 == 0:
                    number2 = 1
                if str(koren[Drob_V+1:]).isdigit() == True and len(koren[Drob_V+1:]) != 0:
                    number2 *= int(koren[Drob_V+1:])
                elif str(koren[Drob_V+1:]).isdigit() != True and len(koren[Drob_V+1:]) != 0:
                    number2 *= float(koren[Drob_V+1:])
            if type(number) == float:
                if str(number)[-1] == "0" and str(number)[-2] == ".":
                    number = int(str(number)[:-2])
            if type(number2) == float:
                if str(number2)[-1] == "0" and str(number2)[-2] == ".":
                    number2 = int(str(number2)[:-2])
            if number2 == 0:
                return f"√{number}"
            else:
                return f"√{number}/{number2}"

    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.entry = self.ui.le_entry
        self.temp = self.ui.lbl_temp
        self.entry_max_len = self.entry.maxLength()

        QFontDatabase.addApplicationFont("ui/fonts/Rubik-Regular.ttf")

        self.connect_digit_buttons()
        self.connect_math_operations()
        self.connect_other_buttons()

        self.entry.textChanged.connect(self.adjust_entry_font_size)
        self.temp.textChanged.connect(self.adjust_temp_font_size)

    def connect_digit_buttons(self) -> None:
        for btn in config.DIGIT_BUTTONS:
            getattr(self.ui, btn).clicked.connect(self.add_digit)

    def connect_math_operations(self) -> None:
        self.ui.btn_calc.clicked.connect(self.calculate)
        for btn in config.MATH_OPERATIONS:
            getattr(self.ui, btn).clicked.connect(self.math_operation)

    def connect_other_buttons(self) -> None: 
        self.ui.btn_clear.clicked.connect(self.clear_all)
        self.ui.btn_ce.clicked.connect(self.clear_entry)
        self.ui.btn_point.clicked.connect(self.add_point)
        self.ui.btn_neg.clicked.connect(self.negate)
        self.ui.btn_backspace.clicked.connect(self.backspace)

    def add_digit(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        btn = self.sender()

        if btn.objectName() in config.DIGIT_BUTTONS:
            self.temp.setText("")
            if self.entry.text() == '0' or self.entry.text() == "Некорректный ввод" or self.entry.text() == "Число иррациональное":
                self.entry.setText(btn.text())
                self.temp.setText("") 
            else:
                self.entry.setText(self.entry.text() + btn.text())

    def add_point(self) -> None:
        self.clear_temp_if_equality()
        self.entry.setText(self.entry.text() + '.')

    def negate(self) -> None:
        self.temp.setText("")
        self.temp.setText(self.entry.text() + ' =')
        self.entry.setText(self.VnosPodKoren())

    def backspace(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        entry = self.entry.text()

        if len(entry) != 1:
            self.entry.setText(entry[:-1])
        else:
            self.entry.setText('0')

    def clear_all(self) -> None:
        self.remove_error()
        self.entry.setText('0')
        self.temp.clear()

    def clear_entry(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        self.entry.setText('0')

    def clear_temp_if_equality(self) -> None:
        if self.get_math_sign() == '=':
            self.entry.clear()

    @staticmethod
    def remove_trailing_zeros(number) -> str:
        return number

    def add_temp(self) -> None:
        btn = self.sender()
        if self.entry.text() == '0':
             self.entry.setText(btn.text())
        elif self.entry.text() == "Некорректный ввод" or self.entry.text() == "Число иррациональное":
            self.entry.setText(btn.text())
            self.temp.setText("")
        else:
            self.entry.setText(self.entry.text() + btn.text())

    def get_math_sign(self) -> Optional[str]:
        if self.temp.text():
            return self.temp.text().strip('.').split()[-1]

    def get_entry_text_width(self) -> int:
        return self.entry.fontMetrics().boundingRect(self.entry.text()).width()

    def get_temp_text_width(self) -> int:
        return self.temp.fontMetrics().boundingRect(self.temp.text()).width()

    def calculate(self) -> Optional[str]:
        try:
            result = self.remove_trailing_zeros(self.VynosIzPodKoren())
            self.temp.setText("")

            self.temp.setText(self.temp.text() +
                              self.remove_trailing_zeros(self.entry.text()) + ' =')

            self.entry.setText(result)

            return result

        except KeyError:
            pass
        except ZeroDivisionError:
            self.show_zero_division_error()

    def show_zero_division_error(self) -> None:
        if self.get_temp_num() == 0:
            self.show_error(config.ERROR_UNDEFINED)
        else:
            self.show_error(config.ERROR_ZERO_DIV)

    def math_operation(self) -> None:
        btn = self.sender()
        if btn.text() == "+" or btn.text() == "\u2212":
            self.temp.setText("Скоро будте;)")
        elif not self.temp.text():
            self.add_temp()
        elif btn.text() == "√":
            self.temp.setText("")
            self.entry.setText("√")

    def replace_temp_sign(self) -> None:
        btn = self.sender()
        self.temp.setText(self.temp.text()[:-2] + f'{btn.text()} ')

    def show_error(self, text: str) -> None:
        self.entry.setMaxLength(len(text))
        self.entry.setText(text)
        self.disable_buttons(True)

    def remove_error(self) -> None:
        if self.entry.text() in (config.ERROR_UNDEFINED, config.ERROR_ZERO_DIV):
            self.entry.setMaxLength(self.entry_max_len)
            self.entry.setText('0')
            self.disable_buttons(False)

    def disable_buttons(self, disable: bool) -> None:
        for btn in config.BUTTONS_TO_DISABLE:
            getattr(self.ui, btn).setDisabled(disable)

        color = 'color: #888;' if disable else 'color: white;'
        self.change_buttons_color(color)

    def change_buttons_color(self, css_color: str) -> None:
        for btn in config.BUTTONS_TO_DISABLE:
            getattr(self.ui, btn).setStyleSheet(css_color)

    def adjust_entry_font_size(self) -> None:
        font_size = config.DEFAULT_ENTRY_FONT_SIZE
        while self.get_entry_text_width() > self.entry.width() - 15:
            font_size -= 1
            self.entry.setStyleSheet(f'font-size: {font_size}pt; border: none;')

        font_size = 1
        while self.get_entry_text_width() < self.entry.width() - 60:
            font_size += 1

            if font_size > config.DEFAULT_ENTRY_FONT_SIZE:
                break

            self.entry.setStyleSheet(f'font-size: {font_size}pt; border: none;')

    def adjust_temp_font_size(self) -> None:
        font_size = config.DEFAULT_FONT_SIZE
        while self.get_temp_text_width() > self.temp.width() - 10:
            font_size -= 1
            self.temp.setStyleSheet(f'font-size: {font_size}pt; color: #888;')

        font_size = 1
        while self.get_temp_text_width() < self.temp.width() - 60:
            font_size += 1

            if font_size > config.DEFAULT_FONT_SIZE:
                break

            self.temp.setStyleSheet(f'font-size: {font_size}pt; color: #888;')

    def resizeEvent(self, event) -> None:
        self.adjust_entry_font_size()
        self.adjust_temp_font_size()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
