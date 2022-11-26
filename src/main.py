from tkinter import *
from tkinter import ttk
import os
from math import sqrt
from color import COLORS


def clear():
    os.system('CLS')


def menu(ref_a: float, ref_b: float, ref_c: float, ref_color: int):
    while True:
        clear()
        choice = input(f'a = {ref_a}\n'
                       f'b = {ref_b}\n'
                       f'c = {ref_c}\n'
                       f'color: {COLORS[ref_color]}'
                       '\n'
                       'y = ax^2 + bx + c\n'
                       f'y = {ref_a}x^2 + {ref_b}x + {ref_c}\n'
                       '\n'
                       'Choose viable option:\n'
                       '1: change a\n'
                       '2: change b\n'
                       '3: change c\n'
                       '4: change color\n'
                       '5: calculate\n'
                       '0: exit\n> ')
        if choice.isnumeric():
            match int(choice):
                case 1:
                    temp = input("a: ")
                    if temp.isnumeric() or temp[0] == '-' or '.' in temp:
                        ref_a = float(temp)
                case 2:
                    temp = input("b: ")
                    if temp.isnumeric() or temp[0] == '-' or '.' in temp:
                        ref_b = float(temp)
                case 3:
                    temp = input("c: ")
                    if temp.isnumeric() or temp[0] == '-' or '.' in temp:
                        ref_c = float(temp)
                case 4:
                    temp = input("type number to choose, anything else to see viable colors\n"
                                 "color: ")
                    if temp.isnumeric():
                        ref_color = int(temp) % len(COLORS)
                    else:
                        inc = 0
                        for color_i in COLORS:
                            print(inc, ': ', color_i, end="\t")
                            inc += 1
                            if inc % 3 == 0:
                                print()
                        print()
                        os.system('pause')
                case 5:
                    return ref_a, ref_b, ref_c, ref_color
                case 0:
                    return None, None, None, None


a = 1
b = 0
c = -1
color = 100
while True:
    options = {1, 2, 0}
    x_zero_name = "Inf. number of zero points"

    a, b, c, color = menu(a, b, c, color)
    if a is None:
        break

    root = Tk()
    root.title('Quadratic Function')
    root.geometry("1200x800")
    root.resizable(False, False)

    sep = ttk.Separator(orient=VERTICAL)
    sep.place(x=195, y=0, relheight=1)

    half_size = 350
    canvas = Canvas(root, width=1000, height=800)
    canvas.create_line(100, 400, 800, 400)  # x
    canvas.create_line(450, 50, 450, 750)  # y

    delta = b ** 2 - 4 * a * c

    x_zero = None

    x1, x2 = None, None

    # calculate zero places
    if delta < 0:
        x_zero_name = "No points"
    elif a == 0 and b == 0 and c == 0:
        x_zero_name = "Inf. number of x"
    elif a == 0 and b != 0:
        x_zero = -c / b
        x_zero_name = f"x = {x_zero}"
    elif delta == 0 and a != 0:
        x_zero = -b / (2 * a)
        x_zero_name = f"x ={-b / (2 * a)}"
    elif a != 0:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)

        if x1 > x2:
            x_zero_name = "x1 = {:.2f}   x2 = {:.2f}".format(x2, x1)
        else:
            x_zero_name = "x1 = {:.2f}   x2 = {:.2f}".format(x1, x2)  # reverse for sad function
    else:
        x_zero_name = "No points"

    canvas.pack(side=RIGHT)

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

        can_input_text = "Canonical form:\nNo for linear function\n"
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

    zero_place_text = f"f(x)=0 for:\n{x_zero_name}"
    zero_place_label = Label(root, text=zero_place_text)
    zero_place_label.pack(side=LEFT and TOP)

    if x_zero is not None or x1 is not None:
        if x1 is not None:
            x_min = int(x1) - 2 + int(abs(q))
            x_max = -x_min
            if x_max < x2:
                x_max = int(x2) + 2 + int(abs(q))
                x_min = -x_max
            if x_min > x1:
                x_min = int(x1) - 2 + int(abs(q))
                x_max = -x_min
        else:
            if c > 0:
                x_min = int(x_zero) - 3
                x_max = -x_min
            if c < 0:
                x_max = int(x_zero) + 3
                x_min = -x_max
    else:
        x_min = int(-c) - 3
        x_max = -x_min

    mark_text_min = str(x_min)
    mark_text_max = str(x_max)
    top_label = Label(root, text=mark_text_max)
    top_label.place(x=620, y=40, relheight=0.01, height=10)

    bottom_label = Label(root, text=mark_text_min)
    bottom_label.place(x=615, y=740, relheight=0.01, height=10)

    left_label = Label(root, text=mark_text_min)
    left_label.place(x=280, y=405, relheight=0.01, height=10)

    left_label = Label(root, text=mark_text_max)
    left_label.place(x=980, y=405, relheight=0.01, height=10)

    zero_point_label = Label(root, text='0')
    zero_point_label.place(x=630, y=405, relheight=0.001, height=10)

    # reverse for reversed yaxis on tkinter
    zoom = half_size / abs(x_max)
    a = -a / zoom
    b = -b
    c = -c * zoom

    # function
    for i in range(x_min, x_max, 1):
        x = i * zoom
        xP1 = x + (0.1 * zoom)

        while x < i * zoom + 1 * zoom:
            first_y = (a * (x ** 2)) + (b * x) + c
            second_y = (a * (xP1 ** 2)) + (b * xP1) + c

            first_x_shift = x + 450
            second_x_shift = xP1 + 450

            first_y += 400
            second_y += 400

            canvas.create_line(first_x_shift,
                               first_y,
                               second_x_shift,
                               second_y,
                               fill=COLORS[color], width=2)
            x += 0.1 * zoom
            xP1 += 0.1 * zoom

    a = -a * zoom
    b = -b
    c = -c / zoom

    root.mainloop()
