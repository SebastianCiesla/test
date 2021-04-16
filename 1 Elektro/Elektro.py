from tkinter import *
import turtle
import math

#-------------
#Create positive charge
def positive(x, y, q=1):
    radius = 10
    positive = turtle.Turtle()
    positive.color('black', 'red')
    positive.speed(0)
    positive.penup()
    positive.setposition(x, y - radius)
    positive.pendown()
    positive.begin_fill()
    positive.circle(radius)
    positive.end_fill()

    positive.penup()
    positive.width(5)
    positive.setposition(x, y)
    positive.pendown()
    positive.forward(3)
    positive.back(6)
    positive.forward(3)
    positive.setheading(90)
    positive.forward(3)
    positive.back(6)

    positive.penup()
    positive.setposition(500, 500)

    return list_of_pos.append((x, y, q))

#-------------
#Create negative charge
def negative(x, y, q=1):
    radius = 10
    negative = turtle.Turtle()
    negative.color('black', 'blue')
    negative.speed(0)
    negative.penup()
    negative.setposition(x, y - radius)
    negative.pendown()
    negative.begin_fill()
    negative.circle(radius)
    negative.end_fill()

    negative.penup()
    negative.width(5)
    negative.setposition(x, y)
    negative.pendown()
    negative.forward(3)
    negative.back(6)

    negative.penup()
    negative.setposition(500, 500)

    return list_of_neg.append((x, y, q))

#-------------
#Create probe charge
def probe_charge(x, y):
    radius = 3
    prob = turtle.Turtle()
    prob.color('black', 'black')
    prob.speed(0)
    prob.penup()
    prob.setposition(x, y - radius)
    prob.pendown()
    prob.begin_fill()
    prob.circle(radius)
    prob.end_fill()  # Malowanie samego kółka

    prob.penup()
    prob.setposition(500, 500)

    return probe_charge_list.append(x), probe_charge_list.append(y)  # Zwróć do listy pozycje ładunku

#-------------
#Compute Intensity E
def calc(x2, x1, y2, y1, q):
    k = 500000  # 8.9875*(10**9)
    r = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if r==0:
        print('R=0, please choose another point!')
        Ex,Ey=0,0
        return Ex,Ey
    else:
        E = (k * q) / (r ** 2)

        dx = math.sqrt((x2 - x1) ** 2)
        dy = math.sqrt((y2 - y1) ** 2)

        sin = dx / r
        cos = dy / r

        if x2 - x1 < 0:
            Ex = sin * E * (-1)
        else:
            Ex = sin * E

        if y2 - y1 < 0:
            Ey = cos * E * (-1)
        else:
            Ey = cos * E

        return Ex, Ey

#-------------
# Drawing vector
def vector_printer():

    global list_of_results
    list_of_results = []  # List of results vectors

    lis_of_r_pos = []
    for (x, y, z) in list_of_pos:
        res = calc(x, probe_charge_list[0], y, probe_charge_list[1], z * (-1))
        lis_of_r_pos.append(res)
        list_of_results.append(res)

    lis_of_r_neg = []  # List of vectors
    for (x, y, z) in list_of_neg:
        res = calc(x, probe_charge_list[0], y, probe_charge_list[1], z)
        lis_of_r_neg.append(res)
        list_of_results.append(res)


    vecX = 0
    vecY = 0

    for x, y in list_of_results:  # Summing
        vecX += x
        vecY += y


    # Drawing vector
    draw_vector = turtle.Turtle()
    draw_vector.speed(0)
    draw_vector.penup()
    draw_vector.color('yellow', 'yellow')
    draw_vector.setposition(probe_charge_list[0], probe_charge_list[1])
    draw_vector.pendown()
    draw_vector.width(3)
    draw_vector.setheading(0)
    pitagoras = math.sqrt(vecX ** 2 + vecY ** 2)

    if pitagoras == 0:
        draw_vector.penup()
        draw_vector.setposition(500, 500)
    else:
        if vecX > 0 and vecY > 0:
            radian = math.asin(math.sin(vecY / pitagoras))
            kat = math.degrees(radian)
            draw_vector.left(kat)

        elif vecX < 0 and vecY > 0:
            radian = math.asin(math.sin(vecY / pitagoras))
            kat = math.degrees(radian)
            draw_vector.left(180 - kat)


        elif vecX < 0 and vecY < 0:
            radian = math.asin(math.sin(abs(vecX) / pitagoras))
            kat = math.degrees(radian)
            draw_vector.left(270 - kat)

        elif vecX > 0 and vecY < 0:
            radian = math.asin(math.sin(vecX / pitagoras))
            kat = math.degrees(radian)
            draw_vector.left(270 + kat)

        elif vecX>0 and vecY==0:
            draw_vector.setheading(0)

        elif vecX ==0 and vecY >0:
            draw_vector.setheading(90)

        elif vecX<0 and vecY==0:
            draw_vector.setheading(180)

        elif vecX==0 and vecY<0:
            draw_vector.setheading(270)

        draw_vector.forward(pitagoras)


#-------------
#Compute point with Intensity E = 0
def zero_finder():

    zero_points=[]
    probe_charge2_list=[]

    def probe_charge2(x, y):
        return probe_charge2_list.append((x,y))

    def vector_printer2(p,t):
        list_of_results = []

        lis_of_r_pos = []
        for (x, y, z) in list_of_pos:
            res = calc(x, p, y, t, z * (-1))
            lis_of_r_pos.append(res)
            list_of_results.append(res)

        lis_of_r_neg = []
        for (x, y, z) in list_of_neg:
            res = calc(x, p, y, t, z)
            lis_of_r_neg.append(res)
            list_of_results.append(res)

        vecX = 0
        vecY = 0

        # Summing

        for x, y in list_of_results:
            vecX += x
            vecY += y


        if vecX==0 and vecY==0:
            print(list_of_results)
            print(p,t)
            print(list_of_neg)
            print(list_of_pos)
            # Draw vector
            draw_vector = turtle.Turtle()
            draw_vector.speed(0)
            draw_vector.penup()
            draw_vector.color('yellow', 'yellow')
            draw_vector.setposition(p, t-6)
            draw_vector.pendown()
            draw_vector.begin_fill()
            draw_vector.circle(6)
            draw_vector.width(1)
            draw_vector.end_fill()
            pitagoras = math.sqrt(vecX ** 2 + vecY ** 2)

            if pitagoras == 0 and vecY==0 and vecX==0:
                draw_vector.penup()
                draw_vector.setposition(500, 500)

    for x_p in range(500):
        for y_p in range(500):
            probe_charge2_list.append((x_p,y_p))

    god_list=[] #Create list with posision of charges
    for numbs in list_of_pos:
        x=numbs[0]
        y=numbs[1]
        god_list.append((x,y))
    for numb in list_of_neg:
        x = numb[0]
        y = numb[1]
        god_list.append((x, y))


    for ele in probe_charge2_list:
        if ele in god_list:
            probe_charge2_list.remove(ele)

    for (p,t) in probe_charge2_list:
        vector_printer2(p,t)

global list_of_pos
list_of_pos=[]

global list_of_neg
list_of_neg = []

global probe_charge_list
probe_charge_list = []



root=Tk()

xentry=Scale(root,from_=300,to=-300)
yentry=Scale(root,from_=300,to=-300)
qentry=Entry(root)
xentry.grid(row=0,column=0)
yentry.grid(row=1,column=0)
qentry.grid(row=2,column=0)

qentry.insert(0,int(1))

def positive_button():
    xpos=xentry.get()
    ypos=yentry.get()
    qpos=qentry.get()
    positive(int(xpos),int(ypos),int(qpos))

def negative_button():
    xpos = xentry.get()
    ypos = yentry.get()
    qpos = qentry.get()
    negative(int(xpos), int(ypos), int(qpos))

def probe_button():
    xpos = xentry.get()
    ypos = yentry.get()
    probe_charge(int(xpos), int(ypos))

def reset():
    xentry.set(0)
    yentry.set(0)
    global list_of_pos
    list_of_pos = []
    global list_of_neg
    list_of_neg = []
    global probe_charge_list
    probe_charge_list = []
    global list_of_results
    list_of_results=[]
    turtle.clearscreen()

def zero_pos():
    xentry.set(0)
    yentry.set(0)



#Creating buttons
positive_button=Button(root,text='Add positive charge',command=positive_button)
negative_button=Button(root,text='Add negative charge',command=negative_button)
probe_button=Button(root,text='Add probe charge',command=probe_button)
printer_vec=Button(root,text='Print Vector',command=vector_printer)
zero_button=Button(root,text='Zero potential finder',command=zero_finder)
reset_button=Button(root,text='RESET',command=reset)
position_zero=Button(root,text='Position 0, 0',command=zero_pos)
close=Button(root,text='EXIT',command=root.quit)
tex = Label(root, text='<-- Choose value of charge')

#Positioning
positive_button.grid(row=0,column=1)
negative_button.grid(row=1,column=1)
probe_button.grid(row=2,column=2)
printer_vec.grid(row=0,column=2)
zero_button.grid(row=1,column=2)
reset_button.grid(row=2,column=3)
position_zero.grid(row=0,column=3)
close.grid(row=1,column=3)
tex.grid(row= 2, column=1)


mainloop()

