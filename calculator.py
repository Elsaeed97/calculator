import tkinter as tk
from subprocess import call

'''
Run: pip install tkinter  & pip install requests
'''

class Calculator:
    def click_button(self, value):
        self.operator = self.operator + str(value)
        self.var.set(self.operator)

    def clear(self):
        self.entry.delete(0, tk.END)
        self.operator = ""

    def evaluate(self):
        try:
            expression = self.entry.get()
            expression = expression.replace('sin(', 'math.sin(math.radians(')
            expression = expression.replace('cos(', 'math.cos(math.radians(')
            expression = expression.replace('tan(', 'math.tan(math.radians(')

            expression += ')'
            result = eval(expression)
            print(result)
            self.var.set(result)
            self.operator = str(result)
        except Exception as e:
            self.var.set("Error")

    def __init__(self, master):
        self.operator = ""
        self.var = tk.StringVar()
        frame_s = tk.Frame(master, height=600, width=200, bg="cornflowerblue")
        frame_s.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entry = tk.Entry(
            frame_s,
            textvariable=self.var,
            bg="lightgray",
            fg="black",
            width=45,
            bd=20,
            insertwidth=4,
            justify="right",
            font=("Arial", 10, "bold"),
        )
        self.entry.pack()

        label_key = tk.Label(root, height=15, width=30, bd=10, bg="cyan2")
        label_key.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        label_fkey = tk.Label(root, height=15, width=15, bg="cyan3")
        label_fkey.pack(fill=tk.BOTH, expand=True)

        buttons_frame = tk.Frame(label_key, bg="black")
        buttons_frame.grid(row=0, column=0, columnspan=3)

        button_style = {
            "font": ("Arial", "16", "italic"),
            "height": 1,
            "width": 3,
            "bg": "grey",
            "fg": "brown4",
        }

        button_7 = tk.Button(buttons_frame, text="7", command=lambda: self.click_button(7), **button_style)
        button_7.grid(row=0, column=0)

        button_8 = tk.Button(buttons_frame, text="8", command=lambda: self.click_button(8), **button_style)
        button_8.grid(row=0, column=1, padx=20)

        button_9 = tk.Button(buttons_frame, text="9", command=lambda: self.click_button(9), **button_style)
        button_9.grid(row=0, column=2, padx=10)

        button_4 = tk.Button(buttons_frame, text="4", command=lambda: self.click_button(4), **button_style)
        button_4.grid(row=1, column=0, padx=10, pady=10)

        button_5 = tk.Button(buttons_frame, text="5", command=lambda: self.click_button(5), **button_style)
        button_5.grid(row=1, column=1, padx=10, pady=10)

        button_6 = tk.Button(buttons_frame, text="6", command=lambda: self.click_button(6), **button_style)
        button_6.grid(row=1, column=2, padx=10, pady=10)

        button_1 = tk.Button(buttons_frame, text="1", command=lambda: self.click_button(1), **button_style)
        button_1.grid(row=2, column=0, padx=10)

        button_2 = tk.Button(buttons_frame, text="2", command=lambda: self.click_button(2), **button_style)
        button_2.grid(row=2, column=1, padx=10)

        button_3 = tk.Button(buttons_frame, text="3", command=lambda: self.click_button(3), **button_style)
        button_3.grid(row=2, column=2, padx=10)

        button_0 = tk.Button(buttons_frame, text="0", command=lambda: self.click_button(0), **button_style)
        button_0.grid(row=3, column=0, padx=10, pady=10)

        button_deci = tk.Button(buttons_frame, text=".", command=lambda: self.click_button("."), **button_style)
        button_deci.grid(row=3, column=1, padx=10, pady=10)

        button_equal = tk.Button(buttons_frame, text="=", command=self.evaluate, **button_style)
        button_equal.grid(row=3, column=2, padx=10, pady=10)

        label_C = tk.Label(label_fkey, bg="black")
        label_C.grid(row=0, column=0, columnspan=3)
        button_C = tk.Button(
            label_C,
            text="C",
            command=self.clear,
            font=("Arial", "16", "italic"),
            height=1,
            width=15,
            bg="grey",
            fg="brown4",
        )
        button_C.pack(side=tk.LEFT)

        label_sub = tk.Label(label_fkey, bg="black")
        label_sub.grid(row=1, column=0, sticky=tk.W, pady=10)
        button_sub = tk.Button(
            label_sub,
            text="-",
            command=lambda: self.click_button("-"),
            font=("Arial", "16", "italic"),
            height=1,
            width=3,
            bg="grey",
            fg="brown4",
        )
        button_sub.pack(side=tk.LEFT)

        label_mul = tk.Label(label_fkey, bg="black")
        label_mul.grid(row=1, column=1, sticky=tk.E)
        button_mul = tk.Button(
            label_mul,
            text="x",
            command=lambda: self.click_button("*"),
            font=("Arial", "16", "italic"),
            height=1,
            width=3,
            bg="grey",
            fg="brown4",
        )
        button_mul.pack()

        label_div = tk.Label(label_fkey, bg="black")
        label_div.grid(row=2, column=0, sticky=tk.W)
        button_div = tk.Button(
            label_div,
            text="/",
            command=lambda: self.click_button("/"),
            font=("Arial", "16", "italic"),
            height=1,
            width=3,
            bg="grey",
            fg="brown4",
        )
        button_div.pack()

        label_add = tk.Label(label_fkey, bg="black")
        label_add.grid(row=2, column=1, sticky=tk.E)
        button_add = tk.Button(
            label_add,
            text="+",
            command=lambda: self.click_button("+"),
            font=("Arial", "16", "italic"),
            height=1,
            width=3,
            bg="grey",
            fg="brown4",
        )
        button_add.pack()

        label_lbrace = tk.Label(label_fkey, bg="black")
        label_lbrace.grid(row=3, column=0, sticky=tk.W, pady=10)
        button_lbrace = tk.Button(
            label_lbrace,
            text="(",
            command=lambda: self.click_button("("),
            font=("Arial", "16", "italic"),
            height=1,
            width=3,
            bg="grey",
            fg="brown4",
        )
        button_lbrace.pack()

        label_rbrace = tk.Label(label_fkey, bg="black")
        label_rbrace.grid(row=3, column=1, sticky=tk.E, pady=10)
        button_rbrace = tk.Button(
            label_rbrace,
            text=")",
            command=lambda: self.click_button(")"),
            font=("Arial", "16", "italic"),
            height=1,
            width=3,
            bg="grey",
            fg="brown4",
        )
        button_rbrace.pack()

        # For sin operation
        label_sin = tk.Label(label_fkey, bg="black")
        label_sin.grid(row=1, column=2, sticky=tk.E, pady=10)
        button_sin = tk.Button(
            label_sin,
            text="sin",
            command=lambda: self.click_button("sin("),
            font=("Arial", "16", "italic"),
            height=1,
            width=3,
            bg="grey",
            fg="brown4",
        )
        button_sin.pack()

        # For cos operation
        label_cos = tk.Label(label_fkey, bg="black")
        label_cos.grid(row=2, column=2, sticky=tk.E, pady=10)

        button_cos = tk.Button(
            label_cos,
            text="cos",
            command=lambda: self.click_button("cos("),
            font=("Arial", "16", "italic"),
            height=1,
            width=3,
            bg="grey",
            fg="brown4",
        )
        button_cos.pack()

        # For tan operation
        label_tan = tk.Label(label_fkey, bg="black")
        label_tan.grid(row=3, column=2, sticky=tk.W, pady=10)

        button_tan = tk.Button(
            label_tan,
            text="tan",
            command=lambda: self.click_button("tan("),
            font=("Arial", "16", "italic"),
            height=1,
            width=3,
            bg="grey",
            fg="brown4",
        )
        button_tan.pack()


root = tk.Tk()
c = Calculator(root)
root.title("Python Calculator Challenge")
root.mainloop()
