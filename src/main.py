from tkinter import *
from tkinter import ttk
import os
from math import sqrt
from color import COLORS


# -------------------------------------------------------------
# clear console
# -------------------------------------------------------------
def clear():
    os.system('CLS')


# -------------------------------------------------------------
# start menu
# -------------------------------------------------------------
def menu(ref_a: float, ref_b: float, ref_c: float, ref_color: int):
    while True:
        clear()
        # print menu & wait for input
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

        # mach option if correctly typed
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
                        # modulo to not get out of range
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
                    # return values
                    return ref_a, ref_b, ref_c, ref_color
                case 0:
                    # return None to quit
                    return None, None, None, None


# -------------------------------------------------------------
# set some defaults on top to save for next runs'
# -------------------------------------------------------------
a = 1
b = 0
c = -1
color = 100
x_zero_name = "Inf. number of zero points"

# -------------------------------------------------------------
# start the loop
# -------------------------------------------------------------
while True:
# -------------------------------------------------------------
    # get info from user
# -------------------------------------------------------------
    a, b, c, color = menu(a, b, c, color)
    if a is None:
        break

# -------------------------------------------------------------
    # set window
# -------------------------------------------------------------
    root = Tk()
    root.title('Quadratic Function')
    root.geometry("1200x800")
    root.resizable(False, False)

# -------------------------------------------------------------
    # set default values
# -------------------------------------------------------------
    # set default for zero places
    x_zero = None
    x1, x2 = None, None
    # set deafult half of Cartesian coordinate system
    half_size = 350

# -------------------------------------------------------------
    # calculate needed on top
# -------------------------------------------------------------
    # calculate delta
    delta = b ** 2 - 4 * a * c

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

# -------------------------------------------------------------
    # set info
# -------------------------------------------------------------
    # seperate info from graph
    sep = ttk.Separator(orient=VERTICAL)
    sep.place(x=195, y=0, relheight=1)

    # Canvas init
    canvas = Canvas(root, width=1000, height=800)
    canvas.pack(side=RIGHT)

    # set info
    enter_text = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    a_input_label = Label(root, text=enter_text)
    a_input_label.pack(side=LEFT and TOP)

    d_input_text = "Δ = {:.2f}\n".format(delta)
    d_input_label = Label(root, text=d_input_text)
    d_input_label.pack(side=LEFT and TOP)

    # set Canonical form info
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

    # set a, b, c info
    a_input_text = f"a = {a}"
    a_input_label = Label(root, text=a_input_text)
    a_input_label.pack(side=LEFT and TOP)

    b_input_text = f"b = {b}"
    b_input_label = Label(root, text=b_input_text)
    b_input_label.pack(side=LEFT and TOP)

    c_input_text = f"c = {c}\n"
    c_input_label = Label(root, text=c_input_text)
    c_input_label.pack(side=LEFT and TOP)

    # set general form info
    if a != 0:
        if b >= 0:
            if c > 0:
                f_input_text = 'y = {:.2f}x^2 + {:.2f}x + {:.2f}\n\n'.format(a, b, c)
            elif c == 0:
                f_input_text = 'y = {:.2f}x^2 + {:.2f}x\n\n'.format(a, b)
            else:
                f_input_text = 'y = {:.2f}x^2 + {:.2f}x - {:.2f}\n\n'.format(a, b, -c)
        elif b == 0:
            if c > 0:
                f_input_text = 'y = {:.2f}x^2 + {:.2f}\n\n'.format(a, c)
            elif c == 0:
                f_input_text = 'y = {:.2f}x^2\n\n'.format(a)
            else:
                f_input_text = 'y = {:.2f}x^2 - {:.2f}\n\n'.format(a, -c)
        else:
            if c > 0:
                f_input_text = 'y = {:.2f}x^2 - {:.2f}x + {:.2f}\n\n'.format(a, -b, c)
            elif c == 0:
                f_input_text = 'y = {:.2f}x^2 - {:.2f}x\n\n'.format(a, -b)
            else:
                f_input_text = 'y = {:.2f}x^2 - {:.2f}x - {:.2f}\n\n'.format(a, -b, -c)
    else:
        if b == 0:
            f_input_text = 'y = {:.2f}\n\n'.format(c)
        else:
            if c > 0:
                f_input_text = 'y = {:.2f}x + {:.2f}\n\n'.format(b, c)
            elif c == 0:
                f_input_text = 'y = {:.2f}x\n\n'.format(b)
            else:
                f_input_text = 'y = {:.2f}x - {:.2f}\n\n'.format(b, -c)

    f_input_label = Label(root, text=f_input_text)
    f_input_label.pack(side=LEFT and TOP)

    # set zero place info
    zero_place_text = f"f(x)=0 for:\n{x_zero_name}"
    zero_place_label = Label(root, text=zero_place_text)
    zero_place_label.pack(side=LEFT and TOP)

# -------------------------------------------------------------
    # set zoom range
# -------------------------------------------------------------
    if x_zero is not None or x1 is not None:
        if x1 is not None:
            # set zoom so that you can see vertex and zero places
            min_zoom = -abs(int(x1) + int(q)) - 2
            max_zoom = -min_zoom
            if max_zoom < x2:
                max_zoom = -abs(int(x1) + int(q)) - 2
                min_zoom = -max_zoom
            if min_zoom > x1:
                min_zoom = -abs(int(x1) + int(q)) - 2
                max_zoom = -min_zoom
        else:
            # set zoom so that you can see zero place
            if c > 0:
                min_zoom = int(x_zero) - 4
                max_zoom = -min_zoom
            elif c < 0:
                max_zoom = int(x_zero) + 4
                min_zoom = -max_zoom
            else:
                min_zoom = -4
                max_zoom = 4
    else:
        if a != 0:
            # if is quadric without zero set so that you can see vertex
            min_zoom = -abs(int(-p) + int(q)) - 2
            max_zoom = -min_zoom
        else:
            # if only c in not 0 set so that you can see function
            min_zoom = int(-c) - 4
            max_zoom = -min_zoom
    
    # set zoom at atleast 4
    if max_zoom < 4:
        max_zoom = 4
        min_zoom = -max_zoom

    # set zoom
    zoom = half_size / abs(max_zoom)

# -------------------------------------------------------------
    # set ticks and labels for graph
# -------------------------------------------------------------
    # set main lines
    canvas.create_line(95, 400, 805, 400)  # x
    canvas.create_line(450, 45, 450, 755)  # y

    # calculate step
    step = 1

    if c <= -1 or c >= 0:
        while step < (abs(min_zoom) + abs(max_zoom)):
            step *= 2
        step //= 8

    getLeftX = []
    getLeftY = []

    # set x tick_labels and ticks
    # left
    for i in range(min_zoom, max_zoom // 2, step):
        offset = 0
        if i > 0:
            break
        elif i == 0:
            offset = -5
            new_tick = canvas.create_line(450 + i * zoom, 45, 450 + i * zoom, 755)  # add black tick if 0
        else:
            getLeftX.append(-i)     # add to the list if not 0
            new_tick = canvas.create_line(450 + i * zoom, 45, 450 + i * zoom, 755, fill="grey50")   # add grey tick if not 0

        new_tick_label = Label(root, text=str(i))
        new_tick_label.place(x=635 + i * zoom + offset, y=410, relheight=0.001, height=10)

    # right
    itr = len(getLeftX) - 1
    for i in range(max_zoom, min_zoom + min_zoom // 2, -step):
        offset = 5
        if i <= 0:
            continue

        new_tick_label = Label(root, text=str(getLeftX[itr]))
        new_tick_label.place(x=635 + getLeftX[itr] * zoom + offset, y=410, relheight=0.001, height=10)
        new_tick = canvas.create_line(450 + getLeftX[itr] * zoom, 45, 450 + getLeftX[itr] * zoom, 755, fill="grey50")
        itr -= 1

    # set y tick_labels and ticks
    # top
    for i in range(min_zoom, max_zoom // 2 - 2, step):
        if i >= 0:
            continue
        else:
            getLeftY.append(-i)     # add to the list if not 0

        new_tick_label = Label(root, text=str(-i))
        new_tick_label.place(x=625, y=395 + i * zoom, relheight=0.001, height=10)
        new_tick = canvas.create_line(95, 400 + i * zoom, 805, 400 + i * zoom, fill="grey50")

    # bottom
    itr = len(getLeftY) - 1
    for i in range(max_zoom, min_zoom + min_zoom // 2 - 1, -step):
        if i <= 0:
            continue
        new_tick_label = Label(root, text=str(-getLeftY[itr]))
        new_tick_label.place(x=625, y=395 + getLeftY[itr] * zoom, relheight=0.001, height=10)
        new_tick = canvas.create_line(95, 400 + getLeftY[itr] * zoom, 805, 400 + getLeftY[itr] * zoom, fill="grey32")
        itr -= 1

    # draw (0, 0) coordinate label
    new_tick_label = Label(root, text=str(0))
    new_tick_label.place(x=630, y=410, relheight=0.001, height=10)

    # draw zero-points
    if x1 is not None:
        x1_label = Label(root, text="{:.1f}".format(x1))
        x1_label.place(x=630 + x1 * zoom, y=380, relheight=0.001, height=10)

        x2_label = Label(root, text="{:.1f}".format(x2))
        x2_label.place(x=635 + x2 * zoom, y=380, relheight=0.001, height=10)
    elif x_zero is not None and -x_zero not in getLeftX and x_zero != 0:
        x1_label = Label(root, text="{:.1f}".format(x_zero))
        x1_label.place(x=630 + x_zero * zoom, y=380, relheight=0.001, height=10)

    # draw x and y for vertex if needed
    if a != 0:
        if -p not in getLeftX and p not in getLeftX and p != 0:
            p_vertex_label = Label(root, text="{:.1f}".format(p))
            p_vertex_label.place(x=635 + p * zoom, y=380, relheight=0.001, height=10)
            new_tick = canvas.create_line(450 + p * zoom, 0, 450 + p * zoom, 800, fill=COLORS[color], dash=(2, 2))

        if -q not in getLeftY and q not in getLeftY and q != 0:
            q_vertex_label = Label(root, text="{:.1f}".format(q))
            q_vertex_label.place(x=650, y=395 + -q * zoom, relheight=0.001, height=10)
            new_tick = canvas.create_line(0, 400 + -q * zoom, 900, 400 + -q * zoom, fill=COLORS[color], dash=(2, 2))

# -------------------------------------------------------------
    # calculate function
# -------------------------------------------------------------
    # reverse for reversed yaxis on tkinter
    a = -a / zoom
    b = -b
    c = -c * zoom

    # iterate through every point
    for i in range(min_zoom, max_zoom):
        # set x to fit to the zoom
        x = i * zoom
        xP1 = x + (0.1 * zoom)

        # iterate through every 0.05 in range to get more precise graph
        while x < i * zoom + 1 * zoom:
            # get first and second y NOTE: no need for changing them for zoom becouse x is already changed
            first_y = (a * (x ** 2)) + (b * x) + c
            second_y = (a * (xP1 ** 2)) + (b * xP1) + c

            # add shift to get x and y correctly to the (0, 0) point that is set on window's coordinates on (450, 400)
            first_x_shift = x + 450
            second_x_shift = xP1 + 450
            first_y_shift = first_y + 400
            second_y_shift = second_y + 400

            # draw line
            canvas.create_line(first_x_shift,
                               first_y_shift,
                               second_x_shift,
                               second_y_shift,
                               fill=COLORS[color], width=2)

            # increment
            x += 0.05 * zoom
            xP1 += 0.05 * zoom

    # set back to normal state for next runs of the same function
    a = -a * zoom
    b = -b
    c = -c / zoom

    # start graph's loop
    root.mainloop()
