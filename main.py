from tkinter import *

m = Tk()
#m.attributes('-fullscreen', True)

#equation = Text(m, width = 10, height = 2)

t = Label(m, height=2, width=25, bg='snow', highlightthickness=2, highlightbackground='black', padx = 10, pady = 10)
t.grid(row=0, column=0, columnspan=4)

def one():
    t['text'] += '1'
def two(): 
    t['text'] += '2'
def three():
    t['text'] += '3'
def four():
    t['text'] += '4'
def five():
    t['text'] += '5'
def six():
    t['text'] += '6'
def seven():
    t['text'] += '7'
def eight():
    t['text'] += '8'
def nine():
    t['text'] += '9'
def zero():
    t['text'] += '0'
def plus():
    t['text'] += '+'
def minus():
    t['text'] += '-'
def X():
    t['text'] += 'x'
def divide():
    t['text'] += '/'
def exponent():
    t['text'] += '^'
def decimal():
    t['text'] += '.'
def backspace():
    a = t['text']
    a = a[:-1]
    t['text'] = a
def destroy():
    m.destroy()
def reset():
    t['text'] = ''
def addition(x):
    a = t['text']
    a = a[0:x]
    b = t['text']
    b = b[x+1:len(b)]
    exp = int(a) + int(b)
    t['text'] = str(exp)
def subtraction(x):
    a = t['text']
    a = a[0:x]
    b = t['text']
    b = b[x+1:len(b)]
    exp = int(a) - int(b)
    t['text'] = str(exp)
def multiply(x):
    a = t['text']
    a = a[0:x]
    b = t['text']
    b = b[x+1:len(b)]
    exp = int(a) * int(b)
    t['text'] = str(exp)
def division(x):
    a = t['text']
    a = a[0:x]
    b = t['text']
    b = b[x+1:len(b)]
    exp = int(a) / int(b)
    t['text'] = str(exp)
def expo(x):
    a = t['text']
    a = a[0:x]
    b = t['text']
    b = b[x+1:len(b)]
    exp = int(a) ** int(b)
    t['text'] = str(exp)

def equals():
    i = 0
    for x in t['text']:
        if(x == '+' and i != 0):
            addition(i)
        if(x == '-' and i != 0):
            subtraction(i)
        if(x == 'x' and i != 0):
            multiply(i)
        if(x == '/' and i != 0):
            division(i)
        if(x == '^' and i != 0):
            expo(i)
        i += 1
    

Button(m , text = 'AC', height = 2, width = 3, bg = 'magenta3', command = reset).grid(row = 1, column = 0)
Button(m, text = '☠️', height = 2, width = 3 , bg = 'ORANGE', command = destroy).grid(row = 1, column = 1)
Button(m, text = ' ^ ', height = 2, width = 3, bg = 'ORANGE', command = exponent).grid(row = 1, column = 2)
Button(m, text = " + ", height = 2, width = 3, bg = 'ORANGE', command = plus).grid(row = 1, column = 3)

Button(m, text='1', height = 2, width = 3, bg = 'RED', command = one).grid(row=2, column = 0)
Button(m, text = '2', height = 2, width = 3, bg = 'RED', command = two).grid(row =2, column = 1)
Button(m, text='3', height = 2, width = 3, bg = 'RED', command = three).grid(row=2, column = 2)
Button(m, text = ' - ', height = 2, width = 3, bg = 'ORANGE', command = minus).grid(row = 2, column = 3)

Button(m, text = '4', height = 2, width = 3, bg = 'RED', command = four).grid(row = 3, column = 0)
Button(m, text = '5', height = 2, width = 3, bg = 'RED', command = five).grid(row = 3, column = 1)
Button(m, text = '6', height = 2, width = 3, bg = 'RED', command = six).grid(row = 3, column = 2)
Button(m, text  = ' X ', height = 2, width = 3, bg = 'ORANGE', command = X).grid(row = 3, column = 3)

Button(m, text = '7', height = 2, width = 3, bg = 'RED', command = seven).grid(row = 4, column = 0)
Button(m, text = '8', height = 2, width = 3, bg = 'RED', command = eight).grid(row =4, column = 1)
Button(m, text = '9', height = 2, width = 3, bg = 'RED', command = nine).grid(row = 4, column = 2)
Button(m, text =' / ', height = 2, width = 3, bg = 'ORANGE', command = divide).grid(row = 4, column = 3)


Button(m, text = '.', height = 2, width = 3, bg = 'sandy brown', command = decimal).grid(row = 5, column = 0)
Button(m, text = '0', height = 2, width = 3, bg = 'RED', command = zero).grid(row = 5, column = 1)
Button(m, text = '⌫', height = 2, width = 3, bg = "sandy brown", command = backspace).grid(row = 5, column = 2)
Button(m, text = ' = ', height = 2, width = 3, bg = 'royal blue', command = equals).grid(row = 5, column = 3)

m.mainloop()
