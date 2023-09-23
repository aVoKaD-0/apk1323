from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from math import sqrt

class MainApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_numbers(self, instance):
        if (str(instance.text) == "√"):
            self.formula += "#"
        else:
            self.formula += str(instance.text)
        self.update_label()

    def add_result(self, instance):
        self.lbl.text = self.osnova()
        self.formula = ""

    def add_del(self, instance):
        a = len(self.lbl.text)
        self.lbl.text = self.lbl.text[:a-1]
        self.formula = self.lbl.text

    def add_ac(self, instance):
        self.formula = ""
        self.lbl.text = self.formula

    def build(self):
        self.formula = ""
        bl = BoxLayout(orientation = "vertical", padding = 25)
        gl = GridLayout(cols = 4, spacing = 3, size_hint = (1, .6))

        self.lbl = Label(text="0", font_size = 40, size_hint = (1, .4))

        bl.add_widget( self.lbl )

        gl.add_widget(Button(text="Ac", on_press = self.add_ac))
        gl.add_widget(Button(text="DEL", on_press = self.add_del))
        gl.add_widget(Button(text="√", on_press = self.add_numbers))
        gl.add_widget(Button(text="/", on_press = self.add_numbers))

        gl.add_widget(Button(text="7", on_press = self.add_numbers))
        gl.add_widget(Button(text="8", on_press = self.add_numbers))
        gl.add_widget(Button(text="9", on_press = self.add_numbers))
        gl.add_widget(Button(text="*", on_press = self.add_numbers))

        gl.add_widget(Button(text="4", on_press = self.add_numbers))
        gl.add_widget(Button(text="5", on_press = self.add_numbers))
        gl.add_widget(Button(text="6", on_press = self.add_numbers))
        gl.add_widget(Button(text="-", on_press = self.add_numbers))

        gl.add_widget(Button(text="1", on_press = self.add_numbers))
        gl.add_widget(Button(text="2", on_press = self.add_numbers))
        gl.add_widget(Button(text="3", on_press = self.add_numbers))
        gl.add_widget(Button(text="+", on_press = self.add_numbers))

        gl.add_widget(Widget())
        gl.add_widget(Button(text = "0", on_press = self.add_numbers))
        gl.add_widget(Button(text = ".", on_press = self.add_numbers))
        gl.add_widget(Button(text = "=", on_press = self.add_result))

        bl.add_widget(gl)

        return bl




    def osnova(self):
        def kdlT(h):
            c = 0
            for i in range(1, h):
                for k in range(1, h+1):
                    if i*i == h:
                        c += 1
                        return i
                    elif i*k == h:
                        for t in range(1, k):
                            if t*t == k:
                                c += 1
                                return t
            if c == 0:
                return 0
        def kdlTr(h):
            for i in range(1, h):
                for k in range(1, h+1):
                    if i*i == h:
                        return i
                    elif i*k == h:
                        for t in range(1, k):
                            if t*t == k:
                                return i
        def kdlF(b, w, s):
            p = int(s/2)
            i = str("0.")
            k = str("0.")
            if w == "0":
                for l in range(1, p+1):
                    i += "0"
                    if l != p:
                        k += "0"
                    else:
                        k += "1"
            else:
                k = "0.1"
                i = "0.0"
                p = 1
            k = float(k)
            i = float(i)
            i += k
            c = i*i
            c = round(c, s)
            while c < b:
                i += k
                i = round(i, p)
                c = i*i
                c = round(c, s+1)
            if c == b:
                return i
            else:
                cout = 0
                for i in range(s):
                    cout += 1
                cout2 = cout
                while cout != 0:
                    b *= 10
                    cout -= 1
                b = int(b)
                for i in range(1, b+1):
                    for k in range(1, b+1):
                        if i*k == b:
                            if i == k:
                                return k
                            else:
                                for l in range(1, k):
                                    if l*l == k:
                                        return l
        def kdlFl(b, w, s):
            p = int(s/2)
            i = str("0.")
            k = str("0.")
            if w == "0":
                for l in range(1, p+1):
                    i += "0"
                    if l != p:
                        k += "0"
                    else:
                        k += "1"
            else:
                k = "0.1"
                i = "0.0"
                p = 1
            k = float(k)
            i = float(i)
            i += k
            c = i*i
            c = round(c, s)
            while c < b:
                i += k
                i = round(i, p)
                c = i*i
                c = round(c, s+1)
            if c == b:
                return i
            else:
                cout = 0
                for i in range(s):
                    cout += 1
                cout2 = cout
                while cout != 0:
                    b *= 10
                    cout -= 1
                b = int(b)
                for i in range(1, b+1):
                    for k in range(1, b+1):
                        if i*k == b:
                            if i == k:
                                return k
                            else:
                                for l in range(1, k):
                                    if l*l == k:
                                        i = Dpl(i, s)
                                        return i
        def Dpl(i, h):
            cout3 = 0
            while cout3 != h:
                i *= 0.1
                cout3 += 1
                i = round(i, cout3)
            return i
        def Dp(k, cout3):
            n = 1
            while cout3 != 0:
                k *= 0.1
                k = round(k, n)
                n += 1
                cout3 -= 1
            return k
        flag = True
        fla = True
        fl = True
        f = True
        NeKPL = True
        KPL = True
        KDR = True
        NeKDR = True
        query = 1
        koren = self.lbl.text
        a = koren.find("#")
        for i in koren[a+1:]:
            if i == ".":
                KPL = False    
        for i in koren[:a]:
            if i ==".":
                NeKPL = False
        for i in koren[a+1:]:
            if i == "/":
                KDR = False
        for i in koren[:a]:
            if i == "/":
                NeKDR = False
        if query == 1:
            if KPL == True and NeKPL == True and KDR == True and NeKDR == True:
                b = int(koren[a+1:])
                for i in range(1, b+1):
                    if i*i == b:
                        if koren[:a] == "":
                            flag = False
                            return f"{i}"
                        elif flag == True:
                            i *= int(koren[:a])
                            flag = False
                            return f"{i}"
                if flag == True:
                    for i in range(1, b+1):
                        for k in range(1, b+1):
                            if i*k == b:
                                for l in range(1, k):
                                    if koren[:a] == "":
                                        if l*l == k:
                                            flag = False
                                            return f"{l}#{i}"
                                    else:
                                        if l*l == k:
                                            l *= int(koren[:a])
                                            flag = False
                                            return f"{l}#{i}"
            if KPL == True and NeKPL == False and KDR == True and NeKDR == True and flag == True:
                b = int(koren[a+1:])
                for i in range(1, b+1):
                    if i*i == b:
                        if koren[:a] == "":
                            flag = False
                            return "число будет", i
                        elif flag == True:
                            i = float(i)
                            i *= float(koren[:a])
                            flag = False
                            return "число будет", i
                if flag == True:
                    for i in range(1, b+1):
                        for k in range(1, b+1):
                            if i*k == b:
                                for l in range(1, k):
                                    if koren[:a] == "":
                                        if l*l == k:
                                            flag = False
                                            return f"{l}#{i}"
                                    else:
                                        if l*l == k:
                                            l = float(l)
                                            l *= float(koren[:a])
                                            flag = False
                                            return f"{l}#{i}"
            if KPL == False and NeKPL == True and NeKDR == True and KDR == True and flag == True:
                for i in range(a, len(koren)):
                    if koren[i] == ".":
                        h = i #координата точки внутри корня
                s = h
                h = len(koren)-1 - h
                b = float(koren[a+1:])
                i = str("0.")
                k = str("0.")
                p = int(h/2)
                if koren[a+1:s] == "0":
                    for l in range(1, p+1):
                        i += "0"
                        if l != p:
                            k += "0"
                        else:
                            k += "1"
                else:
                    k = "0.1"
                    i = "0.0"
                    p = 1
                k = float(k)
                i = float(i)
                i += k
                c = i*i
                c = round(c, h)
                while c < b:
                    i += k
                    i = round(i, p)
                    c = i*i
                    c = round(c, h+1)
                if c == b:
                    if koren[:a] == "":
                        flag = False
                        fl = False
                        return "число будет", i
                    elif flag == True:
                        flag = False
                        fl = False
                        i *= float(koren[:a])
                        return "число будет", i
                else:
                    cout = 0
                    for i in range(h):
                        cout += 1
                    cout2 = cout
                    while cout != 0:
                        b *= 10
                        cout -= 1
                    b = int(b)
                    for i in range(1, b+1):
                        for k in range(1, b+1):
                            if i*k == b:
                                if i == k:
                                    cout3 = int(cout2/2)
                                    k = Dp(k, cout3)
                                    if koren[:a] == "":
                                        flag = False
                                        fl = False
                                        return f"{k}#0.1"
                                    else:
                                        k *= int(koren[:a])
                                        flag = False
                                        fl = False
                                        return f"{k}#0.1"
                                else:
                                    for l in range(1, k):
                                        if l*l == k:
                                            i = Dpl(i, h)
                                            if koren[:a] == "":
                                                    flag = False
                                                    fl = False
                                                    return f"{l}#{i}"
                                            else:
                                                    l = int(l)
                                                    l *= int(koren[:a])
                                                    flag = False
                                                    fl = False
                                                    return f"{l}#{i}"
            if KPL == False and NeKPL == False and NeKDR == True and KDR == True and flag == True:
                for i in range(a, len(koren)):
                    if koren[i] == ".":
                        h = i #координата точки внутри корня
                s = h
                h = len(koren)-1 - h
                b = float(koren[a+1:])
                i = str("0.")
                k = str("0.")
                p = int(h/2)
                if koren[a+1:s] == "0":
                    for l in range(1, p+1):
                        i += "0"
                        if l != p:
                            k += "0"
                        else:
                            k += "1"
                else:
                    k = "0.1"
                    i = "0.0"
                    p = 1
                k = float(k)
                i = float(i)
                i += k
                c = i*i
                c = round(c, h)
                while c < b:
                    i += 0.1
                    i = round(i, p)
                    c = i*i
                    c = round(c, h+1)
                if c == b:
                    if koren[:a] == "":
                        flag = False
                        return "число будет", i
                    elif flag == True:
                        i *= float(koren[:a])
                        flag = False
                        return "число будет", i
                else:
                    cout = 0
                    for i in range(h):
                        cout += 1
                    cout2 = cout
                    while cout != 0:
                        b *= 10
                        cout -= 1
                    b = int(b)
                    for i in range(1, b+1):
                        for k in range(1, b+1):
                            if i*k == b:
                                if i == k:
                                    cout3 = int(cout2/2)
                                    k = Dp(k, cout3)
                                    if koren[:a] == "":
                                        flag = False
                                        return f"{k}#0.1"
                                    else:
                                        k *= float(koren[:a])
                                        flag = False
                                        return f"{k}#0.1"
                                else:
                                    for l in range(1, k):
                                        if l*l == k:
                                            i = Dpl(i, h)
                                            if koren[:a] == "":
                                                flag = False
                                                return f"{l}#{i}"
                                            else:
                                                l = int(l)
                                                l *= float(koren[:a])
                                                flag = False
                                                return f"{l}#{i}"
            if NeKDR == False and KDR == False and KPL == True and flag == True:
                for i in range(0, a):
                    if koren[i] == "/":
                        u = i #координата дроби снаружи корня
                for i in range(a, len(koren)-1):
                    if koren[i] == "/":
                        d = i #координата дроби внутри корня
                b = int(koren[a+1:d]) #числитель дроби внутри корня
                h = int(koren[d+1:len(koren)]) #знаменатель дроби внутри корня
                u = 0
                j = 1
                g = 1
                for i in range(0, a):
                    if koren[i] == "/":
                        u = i #координата дроби снаружи корня
                for i in range(0, u):
                    if koren[i] == ".":
                        g = 0
                for i in range(u, a):
                    if koren[i] == ".":
                        j = 0
                if g != 0 :
                    g = int(koren[0:u]) #числитель дроби снаружи корня
                else:
                    g = float(koren[0:u]) #числитель дроби снаружи корня
                if j != 0:
                    j = int(koren[u+1:a]) #знаменатель дроби снаружи корня
                else:
                    j = float(koren[u+1:a]) #знаменатель дроби снаружи корня
                if b*b * 0.1 == b:
                    if h*h * 0.1 == h:
                        flag = False
                        return f"{b*g}#0.1/{h*j}#0.1"
                    else:
                        for i in range(1, h+1):
                            if i*i == h:
                                fl = False
                                return f"{b*g}#0.1/{i*j}"
                        if fl == True:
                            for i in range(1, h+1):
                                for k in range(1, h+1):
                                    if i*k == h:
                                        for t in range(1, k):
                                            if t*t == k:
                                                fl = False
                                                return f"{b*g}/{t*j}#{i}"
                elif h*h * 0.1 == h:
                    for i in range(1, b+1):
                            if i*i == b:
                                fl = False
                                return f"{i*g}/{h*j}#0.1"
                    if fl == True:
                        for i in range(1, b+1):
                            for k in range(1, b+1):
                                if i*k == b:
                                    for t in range(1, k):
                                        if t*t == k:
                                            fl = False
                                            return f"{k*g}#{i}/{h*j}#0.1"
                else:
                    for i in range(1, b+1):
                        if i*i == b:
                            fl = False
                            for k in range(1, h+1):
                                if k*k == h:
                                    flag = False
                                    return f"{g*i}/{j*k}"
                        elif i == b:
                            for k in range(1, h+1):
                                if k*k == h:
                                    flag = False
                    if fl == False and flag == True:
                        for i in range(1, h+1):
                            for k in range(1, h+1):
                                if i*k == h:
                                    for t in range(1, k):
                                        if t*t == k:
                                            for n in range(1, b+1):
                                                if n*n == b:
                                                    flag = False
                                                    return f"{n*g}/{t*j}#{i}"
                    if fl == True and flag == False:
                        for i in range(1, b+1):
                            for k in range(1, b+1):
                                if i*k == b:
                                    for t in range(1, k):
                                        if t*t == k:
                                            for n in range(1, h+1):
                                                if n*n == h:
                                                    fl = False
                                                    return f"{t*g}#{i}/{n*j}"
                    if fl == True and flag == True:
                        for i in range(1, b+1):
                            for k in range(1, b+1):
                                if i*k == b:
                                    for t in range(1, k):
                                        if t*t == k:
                                            fl = False
                                            for n in range(1, h+1):
                                                for s in range(1, h+1):
                                                    if n*s == h:
                                                        for y in range(1, s):
                                                            if y*y == s:
                                                                flag = False
                                                                if fl == False:
                                                                    return f"{t*g}#{i}/{y*j}#{n}"
                        if flag == True:
                            for n in range(1, h+1):
                                for s in range(1, h+1):
                                    if n*s == h:
                                        for y in range(1, s):
                                            if y*y == s:
                                                flag = False
                                                return f"{g*b}/{h*j}"
                    if fl == True and flag == True:
                        fl = False
                        flag = False
                        return f"{g}#{b}/{j}#{h}"
                    if fl == True and flag == False:
                        for i in range(1, h+1):
                            if i*i == h:
                                f = False
                                return f"{g}#{b}/{i*j}"
                        if f == True:
                            for i in range(1, h+1):
                                for k in range(1, h+1):
                                    if i*k == h:
                                        for t in range(1, k):
                                            if t*t == k:
                                                flag = False
                                                return f"{g}#{b}/{t*j}#{i}"
                    if fl == False and flag == True:
                        for i in range(1, b+1):
                            if i*i == b:
                                f = False
                                return f"{i*g}/{j}#{h}"
                        if f == True:
                            for i in range(1, b+1):
                                for k in range(1, b+1):
                                    if i*k == b:
                                        for t in range(1, k):
                                            if t*t == k:
                                                flag = False
                                                return f"{g*t}#{i}/{j}#{h}"
            if NeKDR == False and KDR == True and KPL == True and flag == True:
                u = 0
                j = 1
                g = 1
                for i in range(0, a):
                    if koren[i] == "/":
                        u = i #координата дроби снаружи корня
                for i in range(0, u):
                    if koren[i] == ".":
                        g = 0
                for i in range(u, a):
                    if koren[i] == ".":
                        j = 0
                if g != 0 :
                    g = int(koren[0:u]) #числитель дроби снаружи корня
                else:
                    g = float(koren[0:u]) #числитель дроби снаружи корня
                if j != 0:
                    j = int(koren[u+1:a]) #знаменатель дроби снаружи корня
                else:
                    j = float(koren[u+1:a]) #знаменатель дроби снаружи корня
                b = int(koren[a+1:]) # число в корне
                if b*b * 0.1 == b:
                    fl = False
                    return f"{b*g}#0.1/{j}"
                else:
                    for i in range(1, b+1):
                        if i*i == b:
                            fl = False
                            return f"{g*i}/{j} 1"
                    if fl == True:
                        for i in range(1, b+1):
                            for k in range(1, b+1):
                                if i*k == b:
                                    for t in range(1, k):
                                        if t*t == k:
                                            fl = False
                                            return f"{t*g}#{i}/{j}"
                    if fl == True:
                        fl = False
                        return f"{g}#{b}/{j}"
            if NeKDR == False and KPL == False and KDR == True and flag == True:
                u = 0
                j = 1
                g = 1
                for i in range(0, a):
                    if koren[i] == "/":
                        u = i #координата дроби снаружи корня
                for i in range(0, u):
                    if koren[i] == ".":
                        g = 0
                for i in range(u, a):
                    if koren[i] == ".":
                        j = 0
                for i in range(a, len(koren)):
                    if koren[i] == ".":
                        q = i #координата точки внутри корня
                h = len(koren)-1 - q
                if g != 0 :
                    g = int(koren[0:u]) #числитель дроби снаружи корня
                else:
                    g = float(koren[0:u]) #числитель дроби снаружи корня
                if j != 0:
                    j = int(koren[u+1:a]) #знаменатель дроби снаружи корня
                else:
                    j = float(koren[u+1:a]) #знаменатель дроби снаружи корня
                b = float(koren[a+1:]) # число в корне
                i = str("0.")
                k = str("0.")
                p = int(h/2)
                if koren[a+1:q] == "0":
                    for l in range(1, p+1):
                        i += "0"
                        if l != p:
                            k += "0"
                        else:
                            k += "1"
                else:
                    k = "0.1"
                    i = "0.0"
                    p = 1
                k = float(k)
                i = float(i)
                i += k
                c = i*i
                c = round(c, h)
                while c < b:
                    i += k
                    i = round(i, p)
                    c = i*i
                    c = round(c, h+1)
                if c == b:
                    flag = False
                    fl = False
                    return f"{i*g}/{j}"
                else:
                    cout = 0
                    for i in range(h):
                        cout += 1
                    cout2 = cout
                    while cout != 0:
                        b *= 10
                        cout -= 1
                    b = int(b)
                    for i in range(1, b+1):
                        for k in range(1, b+1):
                            if i*k == b:
                                if i == k:
                                    cout3 = int(cout2/2)
                                    k = Dp(k, cout3)
                                    flag = False
                                    fl = False
                                    return f"{g*k}#0.1/{j}"
                                else:
                                    for l in range(1, k):
                                        if l*l == k:
                                            i = Dpl(i, h)
                                            if koren[:a] == "":
                                                    cout3 = cout2
                                                    flag = False
                                                    fl = False
                                                    return f"{l*g}#{i}/{j}"
                                            else:
                                                    l = int(l)
                                                    flag = False
                                                    fl = False
                                                    return f"{l*g}#{i}/{j}"
            if KDR == False and flag == True: # 1#1.0/1 или 1.0#1.0/1 или 1/1#1.0/1 или 1.0/1#1.0/1
                d = 0
                for i in range(a, len(koren)-1):
                    if koren[i] == "/":
                        d = i #координата дроби внутри корня
                u = 0
                j = 1
                g = 1
                y = 0
                q = 0
                w = 0
                cout4 = 0
                for i in range(0, a):
                    if koren[i] == "/":
                        u = i #координата дроби снаружи корня
                for i in range(0, u):
                    if koren[i] == ".":
                        g = 0
                for i in range(u, a):
                    if koren[i] == ".":
                        j = 0
                if u == 0:
                    u = a
                if d != 0:
                    if koren[0:a] != "":
                        if g != 0 :
                            g = int(koren[0:u]) #числитель дроби снаружи корня
                            y = 0
                        else:
                            g = float(koren[0:u]) #числитель дроби снаружи корня
                            y = 1
                        if u != a:
                            if j != 0:
                                j = int(koren[u+1:a]) #знаменатель дроби снаружи корня
                            else:
                                j = float(koren[u+1:a]) #знаменатель дроби снаружи корня
                else:
                    if j != 0 :
                        g = int(koren[0:u]) #числитель дроби снаружи корня
                        y = 0
                    else:
                        g = float(koren[0:u]) #числитель дроби снаружи корня
                        y = 1
                for i in koren[a+1:d]:
                    if i == ".":
                        fla = False
                for i in koren[d+1:]:
                    if i == ".":
                        f = False
                if fla == False:
                    b = float(koren[a+1:d]) #числитель дроби внутри корня
                else:
                    b = int(koren[a+1:d]) #числитель дроби внутри корня
                if f == False:
                    h = float(koren[d+1:len(koren)]) #знаменатель дроби внутри корня
                else:
                    h = int(koren[d+1:len(koren)]) #знаменатель дроби внутри корня
                for i in range(a, d):
                    if koren[i] == ".":
                        q = i #координата точки внутри корня
                for i in range(d+1, len(koren)):
                    if koren[i] == ".":
                        w = i #координата точки внутри корня
                i = str("0.")
                k = str("0.")
                s = len(koren[q+1:d])
                p = int(s/2)
                x = 1
                n2 = 0
                e = b
                if fla == False and f == True:
                    s = len(koren[q+1:d])
                    x = 0
                    n = kdlT(h)
                    if n != 0 and n*n != h:
                        x = kdlTr(h)
                    if koren[a+1:q] == "0":
                        for l in range(1, p+1):
                            i += "0"
                            if l != p:
                                k += "0"
                            else:
                                k += "1"
                    else:
                        k = "0.1"
                        i = "0.0"
                        p = 1
                    k = float(k)
                    i = float(i)
                    i += k
                    c = i*i
                    c = round(c, s)
                    while c < b:
                        i += k
                        i = round(i, p)
                        c = i*i
                        c = round(c, s+1)
                        return i, c
                    if c == b:
                        if koren[:a] == "":
                            if n*n == h:
                                return f"{i}/{n}"
                            elif n**2*x == h:
                                return f"{i}/{n}#{x}"
                            elif n == 0:
                                return f"{i}/#{h}"
                            flag = False
                            fl = False
                        else:
                            if u == a:
                                if n*n == h:
                                    return f"{i*g}/{n}"
                                elif n**2*x == h:
                                    return f"{i*g}/{n}#{x}"
                                elif n == 0:
                                    return f"{i*g}/#{h}"
                            else:
                                if n*n == h:
                                    return f"{i*g}/{n*j}"
                                elif n**2*x == h:
                                    return f"{i*g}/{n*j}#{x}"
                                elif n == 0:
                                    return f"{i*g}/{j}#{h}"
                            flag = False
                            fl = False
                    else:
                        cout = 0
                        for i in range(s):
                            cout += 1
                        cout2 = cout
                        while cout != 0:
                            b *= 10
                            cout -= 1
                        b = int(b)
                        if cout2 != 1:
                            cout4 = int(cout2/2)
                        else:
                            cout4 = 1
                        for i in range(1, b+1):
                            for k in range(1, b+1):
                                if i*k == b:
                                    if i == k:
                                        cout3 = int(cout2/2)
                                        while cout3 != 0:
                                            k *= 0.1
                                            cout3 -= 1
                                        if koren[:a] == "":
                                            if n*n == h:
                                                return f"{k}#0.1/{n}"
                                            elif n**2*x == h:
                                                return f"{k}#0.1/{n}#{x}"
                                            elif n == 0:
                                                return f"{k}#0.1/#{h}"
                                            flag = False
                                            fl = False
                                        else:
                                            if u == a:
                                                if n*n == h:
                                                    return f"{g*k}#0.1/{n}"
                                                elif n**2*x == h:
                                                    return f"{g*k}#0.1/{n}#{x}"
                                                elif n == 0:
                                                    return f"{g*k}#0.1/#{h}"
                                            else:
                                                if n*n == h:
                                                    return f"{g*k}#0.1/{n*j}"
                                                elif n**2*x == h:
                                                    return f"{g*k}#0.1/{n*j}#{x}"
                                                elif n == 0:
                                                    return f"{g*k}#0.1/{j}#{h}"
                                            flag = False
                                            fl = False
                                    else:
                                        for l in range(1, k):
                                            if koren[:a] == "":
                                                if l*l == k:
                                                    cout3 = cout2
                                                    while cout3 != 0:
                                                        i /= 10
                                                        cout3 -= 1
                                                    if n*n == h:
                                                        return f"{l}#{i}/{n}"
                                                    elif n**2*x == h:
                                                        return f"{l}#{i}/{n}#{x}"
                                                    elif n == 0:
                                                        return f"{l}#{i}/#{h}"
                                                    flag = False
                                                    fl = False
                                            else:
                                                if l*l == k:
                                                    l = int(l)
                                                    cout3 = cout2
                                                    while cout3 != 0:
                                                        i /= 10
                                                        cout3 -= 1
                                                    if u == a:
                                                        if n*n == h:
                                                            return f"{g*l}#{i}/{n}"
                                                        elif n**2*x == h:
                                                            return f"{g*l}#{i}/{n}#{x}"
                                                        elif n == 0:
                                                            return f"{g*l}#{i}/#{h}"
                                                    else:
                                                        if n*n == h:
                                                            return f"{g*l}#{i}/{n*j}"
                                                        elif n**2*x == h:
                                                            return f"{g*l}#{i}/{n*j}#{x}"
                                                        elif n == 0:
                                                            return f"{g*l}#{i}/{j}#{h}"
                                                    flag = False
                                                    fl = False
                    if flag == True and fl == True:
                        while cout4 != 0:
                            b /= 10
                            cout4 -= 1
                        if u == a:
                            if n*n == h:
                                return f"#{b}/{n}"
                            elif n**2*x == h:
                                return f"#{b}/{n}#{x}"
                            elif n == 0:
                                return f"#{b}/#{h}"
                        else:
                            if n*n == h:
                                return f"{g}#{b}/{n*j}"
                            elif n**2*x == h:
                                return f"{g}#{b}/{n*j}#{x}"
                            elif n == 0:
                                return f"{g}#{b}/{j}#{h}"
                        flag = False
                        fl = False
                if fla == False and f == False:
                    s = len(koren[q+1:d])
                    x = 0
                    n = kdlF(h, koren[d+1:w], s)
                    if n != 0 and n*n != h:
                        x = kdlFl(h, koren[d+1:w], s)
                    n2 = float(n**2)
                    for z in range(1, s+1):
                        n2 *= 0.1
                        n2 = round(n2, z)
                    if koren[a+1:q] == "0":
                        for l in range(1, p+1):
                            i += "0"
                            if l != p:
                                k += "0"
                            else:
                                k += "1"
                    else:
                        k = "0.1"
                        i = "0.0"
                        p = 1
                    k = float(k)
                    i = float(i)
                    i += k
                    c = i*i
                    c = round(c, s)
                    while c < b:
                        i += k
                        i = round(i, p)
                        c = i*i
                        c = round(c, s+1)
                    if c == b:
                        if koren[:a] == "":
                            if n*n == h:
                                return f"{i}/{n}"
                            elif n**2*x == h:
                                return f"{i}/{n}#{x}"
                            elif n2 == h:
                                return f"{i}/{n}#{x}"
                            elif n == 0:
                                return f"{i}/#{h}"
                            flag = False
                            fl = False
                        elif flag == True:
                            if u == a:
                                if n*n == h:
                                    return f"{i*g}/{n}"
                                elif n**2*x == h:
                                    return f"{i*g}/{n}#{x}"
                                elif n2 == h:
                                    return f"{i*g}/{n}#{x}"
                                elif n == 0:
                                    return f"{i*g}/#{h}"
                            else:
                                if n*n == h:
                                    return f"{i*g}/{n*j}"
                                elif n**2*x == h:
                                    return f"{i*g}/{n*j}#{x}"
                                elif n2 == h:
                                    return f"{i*g}/{n*j}#{x}"
                                elif n == 0:
                                    return f"{i*g}/{j}#{h}"
                            flag = False
                            fl = False
                    else:
                        s = len(koren[q+1:d])
                        cout = 0
                        for i in range(s):
                            cout += 1
                        cout2 = cout
                        while cout != 0:
                            b *= 10
                            cout -= 1
                        b = int(b)
                        if cout2 != 1:
                            cout4 = int(cout2/2)
                        else:
                            cout4 = 1
                        for i in range(1, b+1):
                            for k in range(1, b+1):
                                if i*k == b:
                                    if i == k:
                                        cout3 = int(cout2/2)
                                        k = Dp(k, cout3)
                                        if koren[:a] == "":
                                            if n*n == h:
                                                return f"{k}#0.1/{n}"
                                            elif n**2*x == h:
                                                return f"{k}#0.1/{n}#{x}"
                                            elif n2 == h:
                                                return f"{k}#0.1/{n}#{x}"
                                            elif n == 0:
                                                return f"{k}#0.1/#{h}"
                                            flag = False
                                            fl = False
                                        else:
                                            if u == a:
                                                if n*n == h:
                                                    return f"{g*k}#0.1/{n}"
                                                elif n**2*x == h:
                                                    return f"{g*k}#0.1/{n}#{x}"
                                                elif n2 == h:
                                                    return f"{g*k}#0.1/{n}#{x}"
                                                elif n == 0:
                                                    return f"{g*k}#0.1/#{h}"
                                            else:
                                                if n*n == h:
                                                    return f"{g*k}#0.1/{n*j}"
                                                elif n**2*x == h:
                                                    return f"{g*k}#0.1/{n*j}#{x}"
                                                elif n2 == h:
                                                    return f"{g*k}#0.1/{n*j}#{x}"
                                                elif n == 0:
                                                    return f"{g*k}#0.1/{j}#{h}"
                                            flag = False
                                            fl = False
                                    else:
                                        for l in range(1, k):
                                            if koren[:a] == "":
                                                if l*l == k:
                                                    cout3 = cout2
                                                    i = Dpl(i, len(koren[q+1:d]))
                                                    if u == a:
                                                        if n*n == h:
                                                            return f"{l*g}#{i}/{n}"
                                                        elif n**2*x == h:
                                                            return f"{l*g}#{i}/{n}#{x}"
                                                        elif n2 == h:
                                                            return f"{l*g}#{i}/{n}#{x}"
                                                        elif n == 0:
                                                            return f"{l*g}#{i}/#{h}"
                                                    else:
                                                        if n*n == h:
                                                            return f"{l*g}#{i}/{n*j}"
                                                        elif n**2*x == h:
                                                            return f"{l*g}#{i}/{n*j}#{x}"
                                                        elif n2 == h:
                                                            return f"{l*g}#{i}/{n*j}#{x}"
                                                        elif n == 0:
                                                            return f"{l*g}#{i}/{j}#{h}"
                                                    flag = False
                                                    fl = False
                                            else:
                                                if l*l == k:
                                                    l = int(l)
                                                    cout3 = cout2
                                                    i = Dpl(i, len(koren[q+1:d]))
                                                    if u == a:
                                                        if n*n == h:
                                                            return f"{g*l}#{i}/{n}"
                                                        elif n**2*x == h:
                                                            return f"{g*l}#{i}/{n}#{x}"
                                                        elif n2 == h:
                                                            return f"{g*l}#{i}/{n}#{x}"
                                                        elif n == 0:
                                                            return f"{g*l}#{i}/#{h}"
                                                    else:
                                                        if n*n == h:
                                                            return f"{l*g}#{i}/{n*j}"
                                                        elif n**2*x == h:
                                                            return f"{l*g}#{i}/{n*j}#{x}"
                                                        elif n2 == h:
                                                            return f"{l*g}#{i}/{n*j}#{x}"
                                                        elif n == 0:
                                                            return f"{l*g}#{i}/{j}#{h}"
                                                    flag = False
                                                    fl = False
                if fla == True and f == False:
                    s = len(koren)-1 - w
                    x = 0
                    n = kdlF(h, koren[d+1:w], s)
                    if n != 0 and n*n != h:
                        x = kdlFl(h, koren[d+1:w], s)
                    n2 = float(n**2)
                    for i in range(1, s+1):
                        n2 *= 0.1
                        n2 = round(n2, i)
                    for i in range(1, b+1):
                        if i*i == b:
                            if koren[:a] == "":
                                if n*n == h:
                                    return f"{i}/{n}"
                                elif n**2*x == h:
                                    return f"{i}/{n}#{x}"
                                elif n2 == h:
                                    return f"{i}/{n}#{x}"
                                elif n == 0:
                                    return f"{i}/#{h}"
                                flag = False
                            elif flag == True:
                                if u != a:
                                    if n*n == h:
                                        return f"{g*i}/{n*j}"
                                    elif n**2*x == h:
                                        return f"{g*i}/{n*j}#{x}"
                                    elif n2 == h:
                                        return f"{g*i}/{n*j}#{x}"
                                    elif n == 0:
                                        return f"{g*i}/{j}#{h}"
                                else:
                                    if n*n == h:
                                        return f"{g*i}/{n}"
                                    elif n**2*x == h:
                                        return f"{g*i}/{n}#{x}"
                                    elif n2 == h:
                                        return f"{g*i}/{n}#{x}"
                                    elif n == 0:
                                        return f"{g*i}/#{h}"
                                flag = False
                    if flag == True:
                        for i in range(1, b+1):
                            for k in range(1, b+1):
                                if i*k == b:
                                    for l in range(1, k):
                                        if koren[:a] == "":
                                            if l*l == k:
                                                if u != a:
                                                    if n*n == h:
                                                        return f"{l}#{i}/{n*j}"
                                                    elif n**2*x == h:
                                                        return f"{l}#{i}/{n*j}#{x}"
                                                    elif n2 == h:
                                                        return f"{l}#{i}/{n*j}#{x}"
                                                    elif n == 0:
                                                        return f"{l}#{i}/{j}#{h}"
                                                else:
                                                    if n*n == h:
                                                        return f"{l}#{i}/{n}"
                                                    elif n**2*x == h:
                                                        return f"{l}#{i}/{n}#{x}"
                                                    elif n2 == h:
                                                        return f"{l}#{i}/{n}#{x}"
                                                    elif n == 0:
                                                        return f"{l}#{i}/#{h}"
                                                flag = False
                                        else:
                                            if l*l == k:
                                                if u != a:
                                                    if n*n == h:
                                                        return f"{g*l}#{i}/{n*j}"
                                                    elif n**2*x == h:
                                                        return f"{g*l}#{i}/{n*j}#{x}"
                                                    elif n2 == h:
                                                        return f"{g*l}#{i}/{n*j}#{x}"
                                                    elif n == 0:
                                                        return f"{g*l}#{i}/{j}#{h}"
                                                else:
                                                    if n*n == h:
                                                        return f"{g*l}#{i}/{n}"
                                                    elif n**2*x == h:
                                                        return f"{g*l}#{i}/{n}#{x}"
                                                    elif n2 == h:
                                                        return f"{g*l}#{i}/{n}#{x}"
                                                    elif n == 0:
                                                        return f"{g*l}#{i}/#{h}"
                                                flag = False
                if fla == True and f == True:
                    n = kdlT(h)
                    if n != 0 and n*n != h:
                        x = kdlTr(h)
                    for i in range(1, b+1):
                        if i*i == b:
                            if koren[:a] == "":
                                if n*n == h:
                                    return f"{i}/{n}"
                                elif n**2*x == h:
                                    return f"{i}/{n}#{x}"
                                elif n2 == h:
                                    return f"{i}/{n}#{x}"
                                elif n == 0:
                                    return f"{i}/#{h}"
                                flag = False
                            elif flag == True:
                                if u != a:
                                    if n*n == h:
                                        return f"{g*i}/{n*j}"
                                    elif n**2*x == h:
                                        return f"{g*i}/{n*j}#{x}"
                                    elif n2 == h:
                                        return f"{g*i}/{n*j}#{x}"
                                    elif n == 0:
                                        return f"{g*i}/{j}#{h}"
                                else:
                                    if n*n == h:
                                        return f"{g*i}/{n}"
                                    elif n**2*x == h:
                                        return f"{g*i}/{n}#{x}"
                                    elif n2 == h:
                                        return f"{g*i}/{n}#{x}"
                                    elif n == 0:
                                        return f"{g*i}/#{h}"
                                flag = False
                    if flag == True:
                        for i in range(1, b+1):
                            for k in range(1, b+1):
                                if i*k == b:
                                    for l in range(1, k):
                                        if koren[:a] == "":
                                            if l*l == k:
                                                if u != a:
                                                    if n*n == h:
                                                        return f"{l}#{i}/{n*j}"
                                                    elif n**2*x == h:
                                                        return f"{l}#{i}/{n*j}#{x}"
                                                    elif n2 == h:
                                                        return f"{l}#{i}/{n*j}#{x}"
                                                    elif n == 0:
                                                        return f"{l}#{i}/{j}#{h}"
                                                else:
                                                    if n*n == h:
                                                        return f"{l}#{i}/{n}"
                                                    elif n**2*x == h:
                                                        return f"{l}#{i}/{n}#{x}"
                                                    elif n2 == h:
                                                        return f"{l}#{i}/{n}#{x}"
                                                    elif n == 0:
                                                        return f"{l}#{i}/#{h}"
                                                flag = False
                                        else:
                                            if l*l == k:
                                                if u != a:
                                                    if n*n == h:
                                                        return f"{g*l}#{i}/{n*j}"
                                                    elif n**2*x == h:
                                                        return f"{g*l}#{i}/{n*j}#{x}"
                                                    elif n2 == h:
                                                        return f"{g*l}#{i}/{n*j}#{x}"
                                                    elif n == 0:
                                                        return f"{g*l}#{i}/{j}#{h}"
                                                else:
                                                    if n*n == h:
                                                        return f"{g*l}#{i}/{n}"
                                                    elif n**2*x == h:
                                                        return f"{g*l}#{i}/{n}#{x}"
                                                    elif n2 == h:
                                                        return f"{g*l}#{i}/{n}#{x}"
                                                    elif n == 0:
                                                        return f"{g*l}#{i}/#{h}"
                                                flag = False
                if flag == True and fl == True:
                        b = e
                        while cout4 != 0:
                            b /= 10
                            cout4 -= 1
                        if u == a:
                            if n*n == h:
                                return f"#{b}/{n}"
                            elif n**2*x == h:
                                return f"#{b}/{n}#{x}"
                            elif n == 0:
                                return f"#{b}/#{h}"
                        else:
                            if n*n == h:
                                return f"{g}#{b}/{n*j}"
                            elif n**2*x == h:
                                return f"{g}#{b}/{n*j}#{x}"
                            elif n == 0:
                                return f"{g}#{b}/{j}#{h}"
                        flag = False
                        fl = False

            if flag == True and fl == True:
                    return f"Число {koren} нельзя вынести!"
            



if __name__ == "__main__":
    MainApp().run()
