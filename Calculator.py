import tkinter

from tkinter import *

from tkinter import messagebox

root = tkinter.Tk()

root.geometry('400x500')

root.resizable(800,800)

root.title('calculator by smit')

val=""

A=0

operator=""





#wORKING





def bt_1_isclicked():

    global val

    val=val+"1"

    data.set(val)



def bt_2_isclicked():

    global val

    val= val+"2"

    data.set(val)

def bt_3_isclicked():

    global val

    val= val+"3"

    data.set(val)

def bt_4_isclicked():

    global val

    val= val+"4"

    data.set(val)

def bt_5_isclicked():

    global val

    val= val+"5"

    data.set(val)

def bt_6_isclicked():

    global val

    val= val+"6"

    data.set(val)

def bt_7_isclicked():

    global val

    val= val+"7"

    data.set(val)

def bt_8_isclicked():

    global val

    val= val+"8"

    data.set(val)

def bt_9_isclicked():

    global val

    val= val+"9"

    data.set(val)

def bt_0_isclicked():

    global val

    val= val+"0"

    data.set(val)



def but_plus_isclicked():

    global A

    global operator,val



    A=int(val)

    operator="+"

    val=val + "+"

    data.set(val)

def but_minus_isclicked():

    global A

    global operator,val



    A=int(val)

    operator="-"

    val=val + "-"

    data.set(val)



def but_mult_isclicked():

    global A

    global operator,val

    A=int(val)

    operator="*"

    val=val + "*"

    data.set(val)

def but_div_isclicked():

    global A

    global operator,val

    A=int(val)

    operator="/"

    val=val + "/"

    data.set(val)



def c_pressed():

    global A

    global val,operator

    val=""

    A=0

    operator=""

    data.set(val)



def result():

    global A,operator,val

    val2=val

    if operator=="+":

        x=int(val2.split('+')[1])

        c=A+x

        data.set(c)

        val=str(c)

    elif operator=="-":

        x=int(val2.split('-')[1])

        c=A-x

        data.set(c)

        val=str(c)

    elif operator=="*":

        x=int(val2.split('*')[1])

        c=A*x

        data.set(c)

        val=str(c)

    elif operator=="/":

        x=int(val2.split('/')[1])

        if x==0:

            messagebox.showerror('erorr','devision by HIT')

        else:

            c =int(A / x)

            data.set(c)

            val = str(c)





#display

data=StringVar()

lbl=Label(

    root,

    text="Lable",

    anchor= SE,

    font=('verdana',22),

    textvariable=data,

    background='#FFB6C1',





)

lbl.pack(expand=True,fill='both')



#bUTTONS



btnrow1= Frame(root)

btnrow1.pack(expand=True,fill='both')



btnrow2= Frame(root)

btnrow2.pack(expand=True,fill='both')



btnrow3= Frame(root)

btnrow3.pack(expand=True,fill='both')



btnrow4= Frame(root)

btnrow4.pack(expand=True,fill='both')



btn1=Button(

    btnrow1,

    text="1",

    font=('verdana',22),

    relief=GROOVE,

    border=0,

    bg='#FFC0CB',

    command=bt_1_isclicked,

)

btn1.pack(side=LEFT,expand=True,fill='both')



btn2=Button(

    btnrow1,

    text="2",

    font=('verdana',22),

    relief=GROOVE,

    border=0,

    bg='#FFC0CB',

    command=bt_2_isclicked



)

btn2.pack(side=LEFT,expand=True,fill='both')



btn3=Button(

    btnrow1,

    text="3",

    font=('verdana',22),

    relief=GROOVE,

    command=bt_3_isclicked,

    border=0,

    bg='#FFC0CB',

)

btn3.pack(side=LEFT,expand=True,fill='both')



btn4=Button(

    btnrow1,

    text="+",

    font=('verdana',22),

    relief=GROOVE,

    border=0,

    bg='#FFC0CB',

    command=but_plus_isclicked,

)

btn4.pack(side=LEFT,expand=True,fill='both')













btn1=Button(

    btnrow2,

    text="4",

    font=('verdana',22),

    relief=GROOVE,

    border=0,

    bg='#FFC0CB',

    command=bt_4_isclicked

)

btn1.pack(side=LEFT,expand=True,fill='both')



btn2=Button(

    btnrow2,

    text="5",

    font=('verdana',22),

    relief=GROOVE,

    border=0,

    bg='#FFC0CB',

    command=bt_5_isclicked

)

btn2.pack(side=LEFT,expand=True,fill='both')



btn3=Button(

    btnrow2,

    text="6",

    font=('verdana',22),

    relief=GROOVE,

    border=0,

    bg='#FFC0CB',

    command=bt_6_isclicked,

)

btn3.pack(side=LEFT,expand=True,fill='both')



btn4=Button(

    btnrow2,

    text="-",

    font=('verdana',22),

    relief=GROOVE,

    border=0,

    bg='#FFC0CB',

    command=but_minus_isclicked

)

btn4.pack(side=LEFT,expand=True,fill='both')















btn1=Button(

    btnrow3,

    text="7",

    font=('verdana',22),

    relief=GROOVE,

    border=0,

    bg='#FFC0CB',

    command=bt_7_isclicked

)

btn1.pack(side=LEFT,expand=True,fill='both')



btn2=Button(

    btnrow3,

    text="8",

    font=('verdana',22),

    relief=GROOVE,

    border=0,

    bg='#FFC0CB',

    command=bt_8_isclicked

)

btn2.pack(side=LEFT,expand=True,fill='both')



btn3=Button(

    btnrow3,

    text="9",

    font=('verdana',22),

    relief=GROOVE,

    border=0,

    bg='#FFC0CB',

    command=bt_9_isclicked

)

btn3.pack(side=LEFT,expand=True,fill='both')



btn4=Button(

    btnrow3,

    text="*",

    font=('verdana',22),

    relief=GROOVE,

    border=0,

    bg='#FFC0CB',

    command=but_mult_isclicked

)

btn4.pack(side=LEFT,expand=True,fill='both')









btn1=Button(

    btnrow4,

    text="c",

    font=('verdana',22),

    relief=GROOVE,

    border=0,

    bg='#FFC0CB',

    command=c_pressed

)

btn1.pack(side=LEFT,expand=True,fill='both')



btn2=Button(

    btnrow4,

    text="0",

    font=('verdana',22),

    relief=GROOVE,

    border=0,

    bg='#FFC0CB',

    command=bt_0_isclicked



)

btn2.pack(side=LEFT,expand=True,fill='both')



btn3=Button(

    btnrow4,

    text="=",

    font=('verdana',22),

    relief=GROOVE,

    border=0,

    bg='#FF1493',

    command=result

)

btn3.pack(side=LEFT,expand=True,fill='both')



btn4=Button(

    btnrow4,

    text="/",

    font=('verdana',22),

relief=GROOVE,

    border=0,

    bg='#FFC0CB',

    command=but_div_isclicked

)

btn4.pack(side=LEFT,expand=True,fill='both')









root.mainloop()
