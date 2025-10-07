from tkinter import *


"""---------------------------------Creating the Window-----------------------------------"""
# Let's create the Tkinter window
window = Tk()
# Then, you will define the size of the window in width(312) and height(324) using the 'geometry' method
window.geometry("550x550")
# In order to prevent the window from getting resized you will call 'resizable' method on the window
window.resizable(0, 0)
#Finally, define the title of the window
window.title("Calculator")
window.configure(bg="#2C3E50")

"""---------------------------------The Main Fuctions ----------------------------------"""

expression = ""
# 1.continuously update the input field whenever a number is entered or any button is pressed.
def clicked_button(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 2.clears the input field or previous calculations using the button "C"
def clear_button():
    global expression
    expression = ""
    input_text.set("")

# 3.calculate the expression present in input field.
def equal_button():
    global expression
    result = str(eval(expression)) # 'eval' function is used for evaluating the string expressions directly
    input_text.set(f"{expression} = {result}")
    expression = ""

"""---------------------------------Input,Output Display Frame -------------------------------------"""

# creates a variable that automatically updates the input field And set the GUI for The input and output display 
input_text = StringVar()
input_frame = Frame(window, width = 312, height = 80, bd = 0, highlightbackground = "#34495E",\
                     highlightcolor = "#34495E", highlightthickness = 2, bg="#2C3E50")
input_frame.pack(side = TOP, padx=15, pady=15)
#creates the text box at the top where input and output appear. 
input_field = Entry(input_frame, font = ('Arial', 20, 'bold'), textvariable = input_text, width = 50,\
                     bg = "#ECF0F1", fg="#2C3E50", bd = 0, justify = RIGHT, relief="flat")
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 18) # 'ipady' increase the height of input field


"""---------------------------------buttons Frame -------------------------------------"""
#a separate frame which will incorporate all the buttons inside it below the 'input field'
btns_frame = Frame(window, width = 312, height = 272.5, bg = "#2C3E50")
btns_frame.pack(padx=10, pady=10)

"""---------------------------------'Clear (C)' and 'Divide (/) buttons -------------------------------------"""
clear = Button(btns_frame, text = "C", fg = "white", width = 36, height = 3, bd = 0, bg = "#E74C3C", cursor = "hand2",\
                command = lambda: clear_button(), font=('Arial', 14, 'bold'), relief="flat", activebackground="#C0392B")
clear.grid(row = 0, column = 0, columnspan = 3, padx = 2, pady = 2)

divide = Button(btns_frame, text = "/", fg = "white", width = 10, height = 3, bd = 0, bg = "#3498DB", cursor = "hand2",\
                 command = lambda: clicked_button("/"), font=('Arial', 14, 'bold'), relief="flat", activebackground="#2980B9")
divide.grid(row = 0, column = 3, padx = 2, pady = 2)


"""---------------------------------'7', '8', '9' and 'Multiply (*) buttons -------------------------------------"""
seven = Button(btns_frame, text = "7", fg = "#2C3E50", width = 10, height = 3, bd = 0, bg = "#ECF0F1", cursor = "hand2",\
                command = lambda: clicked_button(7), font=('Arial', 14, 'bold'),\
                      relief="flat", activebackground="#BDC3C7").grid(row = 1, column = 0, padx = 2, pady = 2)

eight = Button(btns_frame, text = "8", fg = "#2C3E50", width = 10, height = 3, bd = 0, bg = "#ECF0F1", cursor = "hand2",\
                command = lambda: clicked_button(8), font=('Arial', 14, 'bold'),\
                  relief="flat", activebackground="#BDC3C7").grid(row = 1, column = 1, padx = 2, pady = 2)

nine = Button(btns_frame, text = "9", fg = "#2C3E50", width = 10, height = 3, bd = 0, bg = "#ECF0F1", cursor = "hand2",\
               command = lambda: clicked_button(9), font=('Arial', 14, 'bold'),\
                 relief="flat", activebackground="#BDC3C7").grid(row = 1, column = 2, padx = 2, pady = 2)

multiply = Button(btns_frame, text = "*", fg = "white", width = 10, height = 3, bd = 0, bg = "#3498DB", cursor = "hand2",\
                   command = lambda: clicked_button("*"), font=('Arial', 14, 'bold'),\
                     relief="flat", activebackground="#2980B9").grid(row = 1, column = 3, padx = 2, pady = 2)

"""---------------------------------'4', '5', '6' and 'Subtract (-) buttons -------------------------------------"""

four = Button(btns_frame, text = "4", fg = "#2C3E50", width = 10, height = 3, bd = 0, bg = "#ECF0F1", cursor = "hand2",\
               command = lambda: clicked_button(4), font=('Arial', 14, 'bold'),\
                  relief="flat", activebackground="#BDC3C7").grid(row = 2, column = 0, padx = 2, pady = 2)

five = Button(btns_frame, text = "5", fg = "#2C3E50", width = 10, height = 3, bd = 0, bg = "#ECF0F1", cursor = "hand2",\
               command = lambda: clicked_button(5), font=('Arial', 14, 'bold'),\
                  relief="flat", activebackground="#BDC3C7").grid(row = 2, column = 1, padx = 2, pady = 2)

six = Button(btns_frame, text = "6", fg = "#2C3E50", width = 10, height = 3, bd = 0, bg = "#ECF0F1", cursor = "hand2",\
              command = lambda: clicked_button(6), font=('Arial', 14, 'bold'),\
                relief="flat", activebackground="#BDC3C7").grid(row = 2, column = 2, padx = 2, pady = 2)

minus = Button(btns_frame, text = "-", fg = "white", width = 10, height = 3, bd = 0, bg = "#3498DB", cursor = "hand2",\
                command = lambda: clicked_button("-"), font=('Arial', 14, 'bold'),\
                      relief="flat", activebackground="#2980B9").grid(row = 2, column = 3, padx = 2, pady = 2)

"""---------------------------------'1', '2', '3' and 'Addition (+) buttons -------------------------------------"""

one = Button(btns_frame, text = "1", fg = "#2C3E50", width = 10, height = 3, bd = 0, bg = "#ECF0F1", cursor = "hand2",\
              command = lambda: clicked_button(1), font=('Arial', 14, 'bold'),\
                  relief="flat", activebackground="#BDC3C7").grid(row = 3, column = 0, padx = 2, pady = 2)

two = Button(btns_frame, text = "2", fg = "#2C3E50", width = 10, height = 3, bd = 0, bg = "#ECF0F1", cursor = "hand2",\
              command = lambda: clicked_button(2), font=('Arial', 14, 'bold'),\
                  relief="flat", activebackground="#BDC3C7").grid(row = 3, column = 1, padx = 2, pady = 2)

three = Button(btns_frame, text = "3", fg = "#2C3E50", width = 10, height = 3, bd = 0, bg = "#ECF0F1", cursor = "hand2",\
                command = lambda: clicked_button(3), font=('Arial', 14, 'bold'),\
                      relief="flat", activebackground="#BDC3C7").grid(row = 3, column = 2, padx = 2, pady = 2)

plus = Button(btns_frame, text = "+", fg = "white", width = 10, height = 3, bd = 0, bg = "#3498DB", cursor = "hand2",\
               command = lambda: clicked_button("+"), font=('Arial', 14, 'bold'),\
                  relief="flat", activebackground="#2980B9").grid(row = 3, column = 3, padx = 2, pady = 2)

"""---------------------------------'0', 'Decimal (.)', and 'Equal To (=) buttons ------------------------------------"""
zero = Button(btns_frame, text = "0", fg = "#2C3E50", width = 23, height = 3, bd = 0, bg = "#ECF0F1", cursor = "hand2",\
               command = lambda: clicked_button(0), font=('Arial', 14, 'bold'),\
                  relief="flat", activebackground="#BDC3C7").grid(row = 4, column = 0, columnspan = 2, padx = 2, pady = 2)

point = Button(btns_frame, text = ".", fg = "white", width = 10, height = 3, bd = 0, bg = "#95A5A6", cursor = "hand2",\
                command = lambda: clicked_button("."), font=('Arial', 14, 'bold'),\
                      relief="flat", activebackground="#7F8C8D").grid(row = 4, column = 2, padx = 2, pady = 2)

equals = Button(btns_frame, text = "=", fg = "white", width = 10, height = 3, bd = 0, bg = "#27AE60", cursor = "hand2",\
                 command = lambda: equal_button(), font=('Arial', 14, 'bold'),\
                      relief="flat", activebackground="#229954").grid(row = 4, column = 3, padx = 2, pady = 2)


#Tkinter event loop — the GUI keeps running and waiting for user interaction
window.mainloop()


"""
| Concept                      | Explanation                                   |
| ---------------------------- | --------------------------------------------- |
| **Tkinter**                  | Python GUI toolkit                            |
| **Frame**                    | Container for grouping widgets                |
| **Entry**                    | Text box for input/output                     |
| **Button**                   | Clickable widget with command                 |
| **StringVar**                | Special variable that updates widgets         |
| **Grid**                     | Layout system for positioning widgets         |
| **Event-driven programming** | Functions respond to user actions like clicks |
| **eval()**                   | Evaluates string expressions as Python code   |
| **lambda**                   | Creates small anonymous functions             |
| **relief**                   | Button border style                           |
| **ipady**                    | Increases internal padding of widgets         |
| **cursor**                   | Changes mouse cursor appearance               |
--------------------------------------------------------------------------------\
"""