import tkinter as tk
import math

class Calculator:

    def __init__(self, root):
        #root.geometry("306x163")
        root.resizable(width=False, height=False)
        root.title("PyCalc")
        self.widgets()


    def widgets(self):
        self.calcdisplay = tk.Entry(root, font=("Ubuntu", 20))
        self.calcdisplay.insert(0, "0")
        self.calcdisplay.grid(row=0, column=0, columnspan=6)

        self.seven = tk.Button(root, text="7", command=lambda: self.append_to_display("7"))
        self.seven.grid(row=1, column=0, sticky="NWNESWSE")
        self.eight = tk.Button(root, text="8", command=lambda: self.append_to_display("8"))
        self.eight.grid(row=1, column=1, sticky="NWNESWSE")
        self.nine = tk.Button(root, text="9", command=lambda: self.append_to_display("9"))
        self.nine.grid(row=1, column=2, sticky="NWNESWSE")
        self.div = tk.Button(root, text="/", command=lambda: self.append_to_display("/"))
        self.div.grid(row=1, column=3, sticky="NWNESWSE")
        self.clear = tk.Button(root, text="Del", command=lambda: self.delete())
        self.clear.grid(row=1, column=4, sticky="NWNESWSE")
        self.clear = tk.Button(root, text="C", command=self.clear_display)
        self.clear.grid(row=1, column=5, rowspan=3, sticky="NWNESWSE")

        self.four = tk.Button(root, text="4", command=lambda: self.append_to_display("4"))
        self.four.grid(row=2, column=0, sticky="NWNESWSE")
        self.five = tk.Button(root, text="5", command=lambda: self.append_to_display("5"))
        self.five.grid(row=2, column=1, sticky="NWNESWSE")
        self.six = tk.Button(root, text="6", command=lambda: self.append_to_display("6"))
        self.six.grid(row=2, column=2, sticky="NWNESWSE")
        self.multiply = tk.Button(root, text="*", command=lambda: self.append_to_display("*"))
        self.multiply.grid(row=2, column=3, sticky="NWNESWSE")
        self.root = tk.Button(root, text="x^2", command=lambda : self.append_to_display("**2"))
        self.root.grid(row=2, column=4, sticky="NWNESWSE")

        self.one = tk.Button(root, text="1", command=lambda: self.append_to_display("1"))
        self.one.grid(row=3, column=0, sticky="NWNESWSE")
        self.two = tk.Button(root, text="2", command=lambda: self.append_to_display("2"))
        self.two.grid(row=3, column=1, sticky="NWNESWSE")
        self.three = tk.Button(root, text="3", command=lambda: self.append_to_display("3"))
        self.three.grid(row=3, column=2, sticky="NWNESWSE")
        self.sub = tk.Button(root, text="-", command=lambda: self.append_to_display("-"))
        self.sub.grid(row=3, column=3, sticky="NWNESWSE")
        self.root = tk.Button(root, text="sqrt()", command=self.sqrt)
        self.root.grid(row=3, column=4, sticky="NWNESWSE")

        self.one = tk.Button(root, text="0", command=lambda: self.append_to_display("0"))
        self.one.grid(row=4, column=0, sticky="NWNESWSE")
        self.two = tk.Button(root, text=".", command=lambda: self.append_to_display("."))
        self.two.grid(row=4, column=1, sticky="NWNESWSE")
        self.three = tk.Button(root, text="%", command=lambda: self.append_to_display("%"))
        self.three.grid(row=4, column=2, sticky="NWNESWSE")
        self.sub = tk.Button(root, text="+", command=lambda: self.append_to_display("+"))
        self.sub.grid(row=4, column=3, sticky="NWNESWSE")
        self.root = tk.Button(root, text="=", command=self.equal)
        self.root.grid(row=4, column=4, columnspan=2, sticky="NWNESWSE")

    def append_to_display(self, txt):
        if self.calcdisplay.get() == "0" or self.calcdisplay.get() == "MATH ERROR":
            self.calcdisplay.delete(0, tk.END)
            self.calcdisplay.insert(0, txt)

        else:
            self.calcdisplay.insert(len(self.calcdisplay.get()), txt)
            #print(self.calcdisplay.get())

    def clear_display(self):
        self.calcdisplay.delete(0, tk.END)
        self.calcdisplay.insert(0, "0")

    def equal(self):
        try:
            self.result = eval(self.calcdisplay.get())
            self.calcdisplay.delete(0, tk.END)
            self.calcdisplay.insert(0, str(self.result)[:7])
        except:
            self.matherror()

    def sqrt(self):
        self.digit = float(self.calcdisplay.get())
        try:
            self.calcdisplay.delete(0, tk.END)
            self.calcdisplay.insert(0, math.sqrt(self.digit))
        except:
            self.matherror()

    def delete(self):
        if self.calcdisplay.get() == "0" or self.calcdisplay.get() == "MATH ERROR":
            pass
        else:
            self.calcdisplay.delete(len(self.calcdisplay.get()) - 1)
            if self.calcdisplay.get() == "":
                self.calcdisplay.insert(0, "0")
            else:
                pass

    def matherror(self):
        self.calcdisplay.delete(0, tk.END)
        self.calcdisplay.insert(0, "MATH ERROR")


if __name__ == "__main__":

    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()