import tkinter as tk
import math

# Set up the main window
root = tk.Tk()
root.title('Scientific Calculator')
root.configure(bg='#0000FF')
root.resizable(width=False, height=False)

# Entry field to display the input/output
ent_field = tk.Entry(root, bg='#ADD8E6', fg='#000080', font=('Arial', 25),
                     borderwidth=10, justify="right")
ent_field.grid(row=0, columnspan=8, padx=10, pady=10, sticky='nsew')
ent_field.insert(0, '0')

FONT = ('Arial', 10, 'bold')


class SC_Calculator:
    def __init__(self):
        self.current = ''
        self.inp_value = True

    def Entry(self, value):
        ent_field.delete(0, 'end')
        ent_field.insert(0, value)

    def Enter_Num(self, num):
        firstnum = ent_field.get()
        if self.inp_value:
            self.current = str(num)
            self.inp_value = False
        else:
            self.current = firstnum + str(num)
        self.Entry(self.current)

    def Standard_Ops(self, val):
        temp_str = ent_field.get()
        try:
            if val == '=':
                ans = str(eval(temp_str))
                self.Entry(ans)
                self.inp_value = True
            else:
                self.Entry(temp_str + val)
        except:
            self.Entry('Error')

    def Clear_Entry(self):
        self.current = "0"
        self.Entry(0)
        self.inp_value = True

    def Scientific_Ops(self, func):
        try:
            current_value = float(ent_field.get())
            if func == 'sqrt':
                result = math.sqrt(current_value)
            elif func == 'pi':
                result = math.pi
            elif func == 'e':
                result = math.e
            elif func == 'exp':
                result = math.exp(current_value)
            elif func == 'fact':
                result = math.factorial(int(current_value))
            elif func == 'sin':
                result = math.sin(math.radians(current_value))
            elif func == 'cos':
                result = math.cos(math.radians(current_value))
            elif func == 'tan':
                result = math.tan(math.radians(current_value))
            elif func == 'ln':
                result = math.log(current_value)
            elif func == 'log10':
                result = math.log10(current_value)
            elif func == 'log2':
                result = math.log2(current_value)
            elif func == 'pow2':
                result = current_value ** 2
            elif func == 'pow3':
                result = current_value ** 3
            elif func == '10pow':
                result = 10 ** int(current_value)
            elif func == '1divx':
                result = 1 / current_value
            elif func == 'abs':
                result = abs(current_value)
            elif func == 'deg':
                result = math.degrees(current_value)
            elif func == 'rad':
                result = math.radians(current_value)
            else:
                result = 'Error'

            self.Entry(result)
        except:
            self.Entry('Error')
            self.inp_value = True

# Creating the buttons
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('0', 5, 0),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('.', 5, 2), ('=', 5, 3), ('CE', 1, 0, 2), ('\u221A', 1, 2),
    ('\u03C0', 1, 4), ('e', 1, 5), ('Exp', 2, 4), ('x!', 2, 5),
    ('sin', 3, 4), ('cos', 3, 5), ('tan', 3, 6),
    ('ln', 4, 4), ('log10', 4, 5), ('log2', 5, 5),
    ('x\u00B2', 1, 6), ('x\u00B3', 2, 6), ('10\u207F', 3, 7),
    ('1/x', 4, 7), ('Abs', 5, 7), ('Deg', 2, 7), ('Rad', 1, 7)
]

sc_app = SC_Calculator()

for (text, row, col, *args) in buttons:
    command = None
    if text.isdigit() or text == '.':
        command = lambda x=text: sc_app.Enter_Num(x)
    elif text in ['+', '-', '*', '/']:
        command = lambda x=text: sc_app.Standard_Ops(x)
    elif text == '=':
        command = lambda x=text: sc_app.Standard_Ops('=')
    elif text == 'CE':
        command = sc_app.Clear_Entry
    else:
        command = lambda x=text: sc_app.Scientific_Ops({
            '\u221A': 'sqrt', '\u03C0': 'pi', 'e': 'e', 'Exp': 'exp', 'x!': 'fact',
            'sin': 'sin', 'cos': 'cos', 'tan': 'tan', 'ln': 'ln', 'log10': 'log10',
            'log2': 'log2', 'x\u00B2': 'pow2', 'x\u00B3': 'pow3', '10\u207F': '10pow',
            '1/x': '1divx', 'Abs': 'abs', 'Deg': 'deg', 'Rad': 'rad'
        }[x])

    btn = tk.Button(root, text=text, command=command, font=FONT, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2, width=6, height=2)
    btn.grid(row=row, column=col, columnspan=args[0] if args else 1, sticky='nsew', padx=10, pady=10)

root.mainloop()
