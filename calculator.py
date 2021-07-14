import tkinter as tk

y_axis = 175
x_axis = 20


app = tk.Tk()
app.title('Basic Arithmetic Calculator')
app.geometry('420x600')

tk.Label(app, text='Calculator').place(x=20, y=20)


input_str = tk.Variable(app)
Inpp = tk.Entry(app, textvariable=input_str).place(x=20, y=50, width=380, height=100)




tk.Button(app, text= '7', command = lambda : operate('7') ).place(x=(x_axis),     y=(y_axis),     height= 75, width=75)
tk.Button(app, text= '8', command = lambda : operate('8') ).place(x=(x_axis+100), y=(y_axis),     height= 75, width=75)
tk.Button(app, text= '9', command = lambda : operate('9') ).place(x=(x_axis+200), y=(y_axis),     height= 75, width=75)
tk.Button(app, text= '+', command = lambda : operate('+') ).place(x=(x_axis+300), y=(y_axis),     height= 75, width=75)

tk.Button(app, text= '4', command = lambda : operate('4') ).place(x=(x_axis),     y=(y_axis+85),  height= 75, width=75)
tk.Button(app, text= '5', command = lambda : operate('5') ).place(x=(x_axis+100), y=(y_axis+85),  height= 75, width=75)
tk.Button(app, text= '6', command = lambda : operate('6') ).place(x=(x_axis+200), y=(y_axis+85),  height= 75, width=75)
tk.Button(app, text= '-', command = lambda : operate('-') ).place(x=(x_axis+300), y=(y_axis+85),  height= 75, width=75)

tk.Button(app, text= '1', command = lambda : operate('1') ).place(x=(x_axis),     y=(y_axis+170), height= 75, width=75)
tk.Button(app, text= '2', command = lambda : operate('2') ).place(x=(x_axis+100), y=(y_axis+170), height= 75, width=75)
tk.Button(app, text= '3', command = lambda : operate('3') ).place(x=(x_axis+200), y=(y_axis+170), height= 75, width=75)
tk.Button(app, text= '*', command = lambda : operate('*') ).place(x=(x_axis+300), y=(y_axis+170), height= 75, width=75)

tk.Button(app, text= '.', command = lambda : operate('.') ).place(x=(x_axis),     y=(y_axis+255), height= 75, width=75)
tk.Button(app, text= 'C', command = lambda : delete()     ).place(x=(x_axis+100), y=(y_axis+255), height= 75, width=75)
tk.Button(app, text= '0', command = lambda : operate('0') ).place(x=(x_axis+200), y=(y_axis+255), height= 75, width=75)
tk.Button(app, text= '/', command = lambda : operate('/') ).place(x=(x_axis+300), y=(y_axis+255), height= 75, width=75)


tk.Button(app, text= '(', command = lambda : operate('(') ).place(x=(x_axis),     y=(y_axis+340), height= 75, width=75)
tk.Button(app, text= ')', command = lambda : operate(')') ).place(x=(x_axis+100), y=(y_axis+340), height= 75, width=75)
tk.Button(app, text= 'AC',command = lambda : clear()      ).place(x=(x_axis+200), y=(y_axis+340), height= 75, width=75)
tk.Button(app, text= '=', command = lambda : calc()       ).place(x=(x_axis+300), y=(y_axis+340), height= 75, width=75)




def operate(e):
    inp_str = input_str.get()
    print(type(inp_str))
    inp_str = inp_str + e
    input_str.set(inp_str)

def clear():
    print('All cleared')
    input_str.set('')

def delete():
    inp = input_str.get()
    inp = inp[:-1]
    input_str.set(inp)
    print('Deleted')
    
def calc():
    c = input_str.get()
    try:
        input_str.set(str(eval(c)))
    except:
        input_str.set('')


app.mainloop()
