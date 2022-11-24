from tkinter import *
from tkinter import ttk
import os
from math import sqrt


def clear():
    os.system('CLS')


def menu(ref_a: float, ref_b: float, ref_c: float):
    while True:
        clear()
        choice = input(f'a = {ref_a}\n'
                       f'b = {ref_b}\n'
                       f'c = {ref_c}\n'
                       '\n'
                       'y = ax^2 + bx + c\n'
                       f'y = {ref_a}x^2 + {ref_b}x + {ref_c}\n'
                       '\n'
                       'Choose viable option:\n'
                       '1: change a\n'
                       '2: change b\n'
                       '3: change c\n'
                       '4: calculate\n'
                       '0: exit\n> ')
        if choice.isnumeric():
            match int(choice):
                case 1:
                    temp = input("a: ")
                    if temp.isnumeric() or temp[0] == '-' or '.' in temp:
                        ref_a = float(temp)
                    if ref_a == 0 and ref_b == 0:
                        ref_b = 1.0
                case 2:
                    temp = input("b: ")
                    if temp.isnumeric() or temp[0] == '-' or '.' in temp:
                        ref_b = float(temp)
                    if ref_a == 0 and ref_b == 0:
                        ref_b = 1.0
                case 3:
                    temp = input("c: ")
                    if temp.isnumeric() or temp[0] == '-' or '.' in temp:
                        ref_c = float(temp)
                case 4:
                    return ref_a, ref_b, ref_c
                case 0:
                    return None, None, None


a = 0.4
b = 5.0
c = 10.0
while True:
    options = {1, 2, 0}
    x_zero = "Inf. number of zero points"

    x_min = -450
    x_max = 450

    a, b, c = menu(a, b, c)
    if a is None:
        break

    root = Tk()
    root.title('Quadratic Function')
    root.geometry("1200x800")
    root.resizable(False, False)

    sep = ttk.Separator(orient=VERTICAL)
    sep.place(x=195, y=0, relheight=1)

    canvas = Canvas(root, width=1000, height=800)
    canvas.create_line(100, 400, 800, 400)  # x
    canvas.create_line(450, 50, 450, 750)  # y

    # reverse for reversed yaxis on tkinter
    a = -a
    b = -b
    c = -c
    # function
    for x in range(x_min, x_max, 1):

        # less than or equal becouse i reversed everything
        if a <= 0:
            first = 400 + ((a * (x ** 2)) + (b * x) + c)
            second = 400 + ((a * ((x + 1) ** 2)) + (b * (x + 1)) + c)
        else:
            first = 400 + ((a * (x ** 2)) + (b * x) + c)
            second = 400 + ((a * ((x + 1) ** 2)) + (b * (x + 1)) + c)

        if a == 0 and b == 0:
            second += 1  # set to straight line by adding 1 to x value

        x_shift = x + 450

        canvas.create_line(x_shift,
                           first,
                           x_shift,
                           second,
                           fill='red', width=3)

    # reverse for delta
    a = -a
    b = -b
    c = -c

    delta = b ** 2 - 4 * a * c

    # calculate zero places
    if delta < 0:
        x_zero = "No points"
    elif a == 0 and b == 0 and c == 0:
        x_zero = "Inf. number of x"
    elif a == 0:
        x_zero = f"x = {-c / b}"
    elif delta == 0:
        x_zero = f"x ={-b / (2 * a)}"
    else:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        if x1 > x2:
            x_zero = "x1 = {:.2f}   x2 = {:.2f}".format(x2, x1)
        else:
            x_zero = "x1 = {:.2f}   x2 = {:.2f}".format(x1, x2)     # reverse for sad function

    canvas.pack(side=RIGHT)

    mark_text = "350"
    top_label = Label(root, text=mark_text)
    top_label.place(x=620, y=40, relheight=0.01, height=10)

    bottom_label = Label(root, text='-' + mark_text)
    bottom_label.place(x=615, y=740, relheight=0.01, height=10)

    left_label = Label(root, text='-' + mark_text)
    left_label.place(x=280, y=405, relheight=0.01, height=10)

    left_label = Label(root, text=mark_text)
    left_label.place(x=980, y=405, relheight=0.01, height=10)

    enter_text = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    a_input_label = Label(root, text=enter_text)
    a_input_label.pack(side=LEFT and TOP)

    d_input_text = "Δ = {:.2f}\n".format(delta)
    d_input_label = Label(root, text=d_input_text)
    d_input_label.pack(side=LEFT and TOP)

    if a != 0:
        p, q = -b / (2 * a), -delta / (4 * a)
        p_input_text = "p = {:.2f}".format(p)
        p_input_label = Label(root, text=p_input_text)
        p_input_label.pack(side=LEFT and TOP)

        q_input_text = "q = {:.2f}".format(q)
        q_input_label = Label(root, text=q_input_text)
        q_input_label.pack(side=LEFT and TOP)

        if p >= 0:
            if q >= 0:
                can_input_text = "Canonical form:\n{:.2f}(x - {:.2f})^2 + {:.2f}\n".format(a, p, q)
            else:
                can_input_text = "Canonical form:\n{:.2f}(x - {:.2f})^2 - {:.2f}\n".format(a, p, -q)
        else:
            if q >= 0:
                can_input_text = "Canonical form:\n{:.2f}(x - {:.2f})^2 + {:.2f}\n".format(a, -p, q)
            else:
                can_input_text = "Canonical form:\n{:.2f}(x - {:.2f})^2 - {:.2f}\n".format(a, -p, -q)

        can_input_label = Label(root, text=can_input_text)
        can_input_label.pack(side=LEFT and TOP)
    else:
        p, q = None, None
        p_input_text = "p = No p".format(p)
        p_input_label = Label(root, text=p_input_text)
        p_input_label.pack(side=LEFT and TOP)

        q_input_text = "q = No q".format(q)
        q_input_label = Label(root, text=q_input_text)
        q_input_label.pack(side=LEFT and TOP)

        can_input_text = "Canonical form:\nNo for linear function"
        can_input_label = Label(root, text=can_input_text)
        can_input_label.pack(side=LEFT and TOP)

    a_input_text = f"a = {a}"
    a_input_label = Label(root, text=a_input_text)
    a_input_label.pack(side=LEFT and TOP)

    b_input_text = f"b = {b}"
    b_input_label = Label(root, text=b_input_text)
    b_input_label.pack(side=LEFT and TOP)

    c_input_text = f"c = {c}\n"
    c_input_label = Label(root, text=c_input_text)
    c_input_label.pack(side=LEFT and TOP)

    f_input_text = f'y = {a}x^2 + {b}x + {c}\n\n'
    f_input_label = Label(root, text=f_input_text)
    f_input_label.pack(side=LEFT and TOP)

    zero_place_text = f"f(x)=0 for:\n{x_zero}"
    zero_place_label = Label(root, text=zero_place_text)
    zero_place_label.pack(side=LEFT and TOP)

    root.mainloop()
