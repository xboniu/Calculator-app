import tkinter as tk
class Calculator:

    def key_press(self, event):
        # print(event.keysym)
        # print(event.state)
        if event.state == 8:
            if event.keysym in '0123456789':
                self.write_number(event.keysym)
            elif event.keysum == 'asterisk':
                self.operation()
            elif event.keysym == 'minus':
                self.operation()
            elif event.keysym == 'equal':
                self.equal()
        elif event.state == 9 and event.keysym == 'plus':
            self.operation()
                
        
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Calculator')
        self.root.bind('<KeyPress>', self.key_press)
        self.display = tk.Entry(self.root, width=25, borderwidth=5, font = ('Courier', 18))
        self.display.grid(row=0, column=0, columnspan=4, padx = 10, pady = 10)
        self.display.insert(tk.END, f'{0:>25}')
        self.number1 = ''
        self.number2 = ''
        self.operator = ' '
        self.last_equal = False
        self.MAX_NUM_LENGTH = 23
        self.DISPLAY_LENGTH = 25
        self.last_not_num = False
            # creating self.buttons
        self.button_1 = tk.Button(self.root, text = '1', padx = 40, pady = 20, command=lambda: self.write_number('1'))
        self.button_2 = tk.Button(self.root, text = '2', padx = 40, pady = 20, command=lambda: self.write_number('2'))
        self.button_3 = tk.Button(self.root, text = '3', padx = 40, pady = 20, command=lambda: self.write_number('3'))
        self.button_4 = tk.Button(self.root, text = '4', padx = 40, pady = 20, command=lambda: self.write_number('4'))
        self.button_5 = tk.Button(self.root, text = '5', padx = 40, pady = 20, command=lambda: self.write_number('5'))
        self.button_6 = tk.Button(self.root, text = '6', padx = 40, pady = 20, command=lambda: self.write_number('6'))
        self.button_7 = tk.Button(self.root, text = '7', padx = 40, pady = 20, command=lambda: self.write_number('7'))
        self.button_8 = tk.Button(self.root, text = '8', padx = 40, pady = 20, command=lambda: self.write_number('8'))
        self.button_9 = tk.Button(self.root, text = '9', padx = 40, pady = 20, command=lambda: self.write_number('9'))
        self.button_0 = tk.Button(self.root, text = '0', padx = 40, pady = 20, command=lambda: self.write_number('0'))
        self.button_add = tk.Button(self.root, text = '+', padx = 39, pady = 52, command=lambda: self.operation('+'))
        self.button_equal = tk.Button(self.root, text = '=', padx = 39, pady = 20, command=self.equal)
        self.button_minus = tk.Button(self.root, text = '-', padx = 40, pady = 20, command=lambda: self.operation('-'))
        self.button_multiply = tk.Button(self.root, text = 'x', padx = 40, pady = 20, command=lambda: self.operation('x'))
        self.button_clear = tk.Button(self.root, text = 'CLEAR', padx = 26, pady = 20, command=self.clear)
        # placing self.buttons
        self.button_1.grid(row=1, column=0)
        self.button_2.grid(row=1, column=1)
        self.button_3.grid(row=1, column=2)
        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)
        self.button_7.grid(row=3, column=0)
        self.button_8.grid(row=3, column=1)
        self.button_9.grid(row=3, column=2)
        self.button_0.grid(row=4, column=1)
        self.button_add.grid(row=3, column=3, rowspan=2)
        self.button_equal.grid(row=4, column=2)
        self.button_minus.grid(row = 2, column=3)
        self.button_multiply.grid(row = 1, column=3)
        self.button_clear.grid(row=4, column=0)

        self.root.mainloop()

    def solve(self, num1, operator, num2):
        if operator == '+':
            output = str(int(num1)+int(num2))
        elif operator == '-':
            output = str(int(num1)-int(num2))
        elif operator == 'x':
            output = str(int(num1)*int(num2))
        if len(output)>23:
            self.clear()
            return False
        return output


    def display_function(self, operator, number):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, f'{operator} {number:>23}')
        

    def write_number(self, num):
        if self.display.get() == f'{0:>25}':
            self.display.delete(0, tk.END)
        # checks if the prev input was an operator
        if self.last_not_num:
            self.display_function(self.operator, '')
            self.last_not_num = False
        if self.last_equal:
            self.display_function(' ', '')
            self.number1 = ''
            self.number2 = ''
            self.operator = ' '
            self.last_equal = False
        number = self.display.get()[1:].strip()
        if len(number)==23:
            return
        number = number + num
        self.display_function(self.operator, number)

        

    def operation(self, o):
        self.last_equal = False
        #
        # what if the display is empty
        if self.display.get() == f'{0:>25}':
            return
        # sets the number to what is in the display (besides the operator)
        number = self.display.get()[1:].strip()
        if self.number1 == '':
            self.number1 = number
            self.operator = o
            self.display_function(self.operator, number)
            self.last_not_num = True
        else:
            if not self.solve(self.number1, self.operator, number):
                return
            self.number1 = self.solve(self.number1, self.operator, number)
            self.operator = o
            self.display_function(self.operator, self.number1)
            self.last_not_num = True



            
        

    def equal(self):
        if self.display.get() == f'{0:>25}':
            return
        number = self.display.get()[1:].strip()
        if self.number1 == '':
            return
        else:
            if not self.solve(self.number1, self.operator, number):
                return
            number = self.solve(self.number1, self.operator, number)
            self.display_function(' ', number)
            self.operator = ' '
            self.number1 = ''
            self.last_equal = True

            

    def clear(self):
        self.number1 = ''
        self.number2 = ''
        self.operator = ' '
        self.last_not_num = False
        self.last_equal = False
        self.display_function(self.operator, '0')

if __name__ == '__main__':
    Calculator()
