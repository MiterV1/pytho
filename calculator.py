import sys
import tkinter

equation = ""
label_text = ""


def btnNormal(num):
    global equation
    global label_text

    equation += num
    label_text.set(equation)


def btnEqual():
    global equation

    try:
        total = str(eval(equation))
    except ZeroDivisionError:
        label_text.set("error!!!")
    else:
        label_text.set(total)

    equation = ""


def main(argv):
    global label_text

    window = tkinter.Tk()
    window.title("Calculator")
    window.resizable(0, 0)

    label_text = tkinter.StringVar()
    label_wgt = tkinter.Label(window, height='3', width='40', textvariable=label_text, anchor='e',
                              font=('Consolas', 12))
    label_wgt.grid(row=0, column=0, columnspan=4)
    label_text.set("0")

    tkinter.Button(window, text="7", command=lambda: btnNormal("7"), height='4', width='10',
                   font=('Consolas', 12)).grid(row=1, column=0, sticky='E' + 'W')
    tkinter.Button(window, text="8", command=lambda: btnNormal("8"), height='4', width='10',
                   font=('Consolas', 12)).grid(row=1, column=1, sticky='E' + 'W')
    tkinter.Button(window, text="9", command=lambda: btnNormal("9"), height='4', width='10',
                   font=('Consolas', 12)).grid(row=1, column=2, sticky='E' + 'W')
    tkinter.Button(window, text="+", command=lambda: btnNormal("+"), height='4', width='10',
                   font=('Consolas', 12)).grid(row=1, column=3, sticky='E' + 'W')

    tkinter.Button(window, text="4", command=lambda: btnNormal("4"), height='4', width='10',
                   font=('Consolas', 12)).grid(row=2, column=0, sticky='E' + 'W')
    tkinter.Button(window, text="5", command=lambda: btnNormal("5"), height='4', width='10',
                   font=('Consolas', 12)).grid(row=2, column=1, sticky='E' + 'W')
    tkinter.Button(window, text="6", command=lambda: btnNormal("6"), height='4', width='10',
                   font=('Consolas', 12)).grid(row=2, column=2, sticky='E' + 'W')
    tkinter.Button(window, text="-", command=lambda: btnNormal("-"), height='4', width='10',
                   font=('Consolas', 12)).grid(row=2, column=3, sticky='E' + 'W')

    tkinter.Button(window, text="1", command=lambda: btnNormal("1"), height='4', width='10',
                   font=('Consolas', 12)).grid(row=3, column=0, sticky='E' + 'W')
    tkinter.Button(window, text="2", command=lambda: btnNormal("2"), height='4', width='10',
                   font=('Consolas', 12)).grid(row=3, column=1, sticky='E' + 'W')
    tkinter.Button(window, text="3", command=lambda: btnNormal("3"), height='4', width='10',
                   font=('Consolas', 12)).grid(row=3, column=2, sticky='E' + 'W')
    tkinter.Button(window, text="*", command=lambda: btnNormal("*"), height='4', width='10',
                   font=('Consolas', 12)).grid(row=3, column=3, sticky='E' + 'W')

    tkinter.Button(window, text="0", command=lambda: btnNormal("0"), height='4', width='10',
                   font=('Consolas', 12)).grid(row=4, column=0, sticky='E' + 'W')
    tkinter.Button(window, text=".", command=lambda: btnNormal("."), height='4', width='10',
                   font=('Consolas', 12)).grid(row=4, column=1, sticky='E' + 'W')
    tkinter.Button(window, text="=", command=lambda: btnEqual(), height='4', width='10',
                   font=('Consolas', 12)).grid(row=4, column=2, sticky='E' + 'W')
    tkinter.Button(window, text="/", command=lambda: btnNormal("/"), height='4', width='10',
                   font=('Consolas', 12)).grid(row=4, column=3, sticky='E' + 'W')

    window.mainloop()


if __name__ == '__main__':
    main(sys.argv)
