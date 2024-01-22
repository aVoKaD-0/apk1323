from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
import math

ch = 1 # Если число с плавающей надо проверить снова, переменная меняется на 2 и число не проверяется на sqrt, используется в f вынос целого и не целого числа

def vynos_celogo_chisla(number): # выносит целое число
    global ch
    number2 = math.sqrt(number)
    if str(number2).find(".") == len(str(number2))-2 and ch == 1:
        ch = 1
        return int(str(number2)[:-2]), 0
    for i in range(1, number+1):
        for k in range(1, number):
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

class MainApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_numbers(self, instance):
        if (str(instance.text) == "√"):
            self.formula += "√"
        else:
            self.formula += str(instance.text)
        self.update_label()

    def add_result(self, instance):
        self.lbl.text = self.VynosIzPodKoren()
        self.formula = ""

    def add_res(self, instance):
        self.lbl.text = self.VnosPodKoren()
        self.formula = ""

    def add_del(self, instance):
        a = len(self.lbl.text)
        self.lbl.text = self.lbl.text[:a-1]
        self.formula = self.lbl.text

    def add_ac(self, instance):
        self.formula = ""
        self.lbl.text = self.formula

    def add_znak(self, instance):
        self.lbl.text = "Скоро всё будет;)"

    def build(self):
        self.formula = ""
        bl = BoxLayout(orientation = "vertical", padding = 25)
        gl = GridLayout(cols = 4, spacing = 3, size_hint = (1, .6))

        self.lbl = Label(text="Что сделаем на этот раз?", font_size = 40, size_hint = (1, .4))

        bl.add_widget( self.lbl )

        gl.add_widget(Button(text="Ac", on_press = self.add_ac))
        gl.add_widget(Button(text="DEL", on_press = self.add_del))
        gl.add_widget(Button(text="√", on_press = self.add_numbers))
        gl.add_widget(Button(text="/", on_press = self.add_numbers))

        gl.add_widget(Button(text="7", on_press = self.add_numbers))
        gl.add_widget(Button(text="8", on_press = self.add_numbers))
        gl.add_widget(Button(text="9", on_press = self.add_numbers))
        gl.add_widget(Button(text="*", on_press = self.add_znak))

        gl.add_widget(Button(text="4", on_press = self.add_numbers))
        gl.add_widget(Button(text="5", on_press = self.add_numbers))
        gl.add_widget(Button(text="6", on_press = self.add_numbers))
        gl.add_widget(Button(text="-", on_press = self.add_znak))

        gl.add_widget(Button(text="1", on_press = self.add_numbers))
        gl.add_widget(Button(text="2", on_press = self.add_numbers))
        gl.add_widget(Button(text="3", on_press = self.add_numbers))
        gl.add_widget(Button(text="+", on_press = self.add_znak))

        gl.add_widget(Button(text = "внести под корень", on_press = self.add_res))
        gl.add_widget(Button(text = "0", on_press = self.add_numbers))
        gl.add_widget(Button(text = ".", on_press = self.add_numbers))
        gl.add_widget(Button(text = "вынести из под корня", on_press = self.add_result))

        bl.add_widget(gl)

        return bl

    def VynosIzPodKoren(self): #внос их под корня
        koren = self.lbl.text
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
                if NeKDR == True and (NeKPL == True and NeKPL == False): # если вне корня либо целое число, либо числа нету
                    if number == 0 and number2 == 0: 
                        return f"Число {koren} иррациональное"
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
                        return f"Число {koren} иррациональное"
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
                        return f"Число {koren} иррациональное"
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
                        return f"Число {koren} иррациональное"
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
        c = 0
        f = 0
        g = 0
        f2 = 0
        g2 = 0
        c2 = 0
        koren = self.lbl.text
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

if __name__ == "__main__":
    MainApp().run()
