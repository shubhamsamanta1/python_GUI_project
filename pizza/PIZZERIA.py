# IMPORT MODULES REQUIRED goal

from tkinter import *
import datetime
# import pymysql
root = Tk()

# DATDABASE CONNECTIVITY
#
# conn = pymysql.connect(host="localhost",user="root",password="",database="db_pizza")
# cursor= conn.cursor()


# CREATED WINDOW FOR TKINTER

root.geometry("1000x1000")
root.title("Pizza hub")
root.configure(background="maroon")


# CREATED TIME & DATE FUNCTIONS

def dateotime():
    dt = datetime.datetime.now()
    string = dt.strftime('%d-%m-%y || %H:%M:%S%p')
    DT.config(text = string)
    DT.after(1000,dateotime)

# CREATED DATE & TIME LABEL

DT=Label(root,font=('calibri',20,'bold'),bg="maroon")
DT.place(x=535,y=60,anchor='nw')


# CREATED FUNCTION DEFINATIONS

# CREATED DEFINATIONS FOR ONCLICK PICTURE ITEMS (COUNTER FUNCTION)

# WHERE c0 TO c9 ARE SET OF GLOBAL VAR. & i0 TO i9 ARE SET OF EACH IMAGE ITEM DEFINATIONS & e0 TO e9 ARE ENTRY POINTS

global c0
c0 = 0
def i0():
    global c0
    e0.delete(0,END)
    c0+=1
    e0.insert(0,c0)

global c1
c1 = 0
def i1():
    global c1
    e1.delete(0,END)
    c1+=1
    e1.insert(0,c1)

global c2
c2 = 0
def i2():
    global c2
    e2.delete(0,END)
    c2+=1
    e2.insert(0,c2)

global c3
c3 = 0
def i3():
    global c3
    e3.delete(0,END)
    c3+=1
    e3.insert(0,c3)

global c4
c4 = 0
def i4():
    global c4
    e4.delete(0,END)
    c4+=1
    e4.insert(0,c4)

global c5
c5 = 0
def i5():
    global c5
    e5.delete(0,END)
    c5+=1
    e5.insert(0,c5)

global c6
c6 = 0
def i6():
    global c6
    e6.delete(0,END)
    c6+=1
    e6.insert(0,c6)

global c7
c7 = 0
def i7():
    global c7
    e7.delete(0,END)
    c7+=1
    e7.insert(0,c7)

global c8
c8 = 0
def i8():
    global c8
    e8.delete(0,END)
    c8+=1
    e8.insert(0,c8)


global c9
c9 = 0
def i9():
    global c9
    e9.delete(0,END)
    c9+=1
    e9.insert(0,c9)

# ADD-ONS MENUE DEFINATIONS

global ccola
ccola = 0
def icola():
    global ccola
    ecola.delete(0,END)
    ccola+=1
    ecola.insert(0,ccola)

global ctup
ctup = 0
def itup():
    global ctup
    etup.delete(0,END)
    ctup+=1
    etup.insert(0,ctup)

global cpep
cpep = 0
def ipep():
    global cpep
    epep.delete(0,END)
    cpep+=1
    epep.insert(0,cpep)

# CREATED FUNCTION FOR TOTAL GLOBAL VARIABLE COUNTS

def tpr():
    global c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,ccola,ctup,cpep
    sum=c0*500+c1*300+c2*250+c3*550+c4*350+c5*600+c6*650+c7*150+c8*450+c9*200+ccola*40+ctup*40+cpep*40
    print(sum)
    total.delete(0,END)
    total.insert(0,sum)

# CREATED CLEAR TOTAL ENTRY FUNCTION

def clearl():
    global c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,ccola,ctup,cpep
    c0=0
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    c7=0
    c8=0
    c9=0
    ccola=0
    ctup=0
    cpep=0
    total.delete(0,END)
    e0.delete(0,END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    ecola.delete(0,END)
    etup.delete(0,END)
    epep.delete(0,END)
    enem.delete(0,END)
    enum.delete(0,END)

# CREATED SPECIAL DEFINED & DEDICATED DEFINATION GUI FOR BILLING SECTION
global enem
global enum
global total
def bill():

    # BILL PAGE WINDOW CONFIGURATION

    toor = Tk()
    toor.geometry("600x600")
    toor.title("BILL")
    toor.configure(background="maroon")

    # TOTAL SUMMING FORMULA

    sum = c0*500+ c1*300 + c2*250 + c3*550 + c4*350 + c5*600 + c6*650 + c7*150 + c8*450 + c9*200 + ccola*40 + ctup*40 + cpep*40

    # TOTAL OF QUANTITIES

    sum1= c0+c1+c2+c3+c4+c5+c6+c7+c8+c9+ccola+ctup+cpep

    # TIME & DATE DEFINATION FOR DILL PAGE

    def dateotime():
        dt = datetime.datetime.now()
        string = dt.strftime('%d-%m-%y || %H:%M:%S%p')
        DT.config(text=string)
        DT.after(1000, dateotime)

    # DATE & TIME LABEL

    DT = Label(toor, font=(10), bg="maroon")
    DT.place(x=425, y=28, anchor='nw')

    # TITTLE LABEL FOR BILL

    tittle1 = Label(toor, text="FINAL BILL", font=("Helvetica", 20, "bold italic"), fg="blue", bg="maroon")
    tittle1.place(x=235, y=10)

    # DESIGN LABEL

    itii = Label(toor, font=('aria', 15, 'bold'),text="------------------------------------------------------------------------------------",fg="black", bg="maroon", bd=5)
    itii.place(x=0, y=50)

    # LABELS FOR  ITEMS , QUANTITIES & PRICE IN BILL PAGE

    iti = Label(toor,font=('aria', 15, 'bold'), text="ITEMS",bg="maroon", fg="black", bd=5)
    iti.place(x=120, y=80)
    iti = Label(toor, font=('aria', 15, 'bold'), text=" QUANTITIES",bg="maroon", fg="black", anchor=W)
    iti.place(x=280, y=80)
    iti = Label(toor, font=('aria', 15, 'bold'), text="PRICE",bg="maroon", fg="black", anchor=W)
    iti.place(x=490, y=80)

    # DESIGN LABEL

    itii = Label(toor, font=('aria', 15, 'bold'), text="------------------------------------------------------------------------------------",fg="black", bg="maroon", bd=5)
    itii.place(x=0, y=105)

    # ALL DATA LABELS ACCORDING TO HEDDINGS MENTIONED & SELECTED BY USER FROM MAIN PAGE

    it0 = Label(toor, font=('aria', 15, 'bold'), text="Pepperoni Pizza",bg="maroon", fg="royalblue3", anchor=W)
    it0.place(x=80,y=130)
    it0 = Label(toor, font=('aria', 15, 'bold'), text=c0,bg="maroon", fg="royalblue3", anchor=W)
    it0.place(x=340,y=130)
    it0 = Label(toor, font=('aria', 15, 'bold'), text=c0*500,bg="maroon", fg="royalblue3", anchor=W)
    it0.place(x=515,y=130)


    it1 = Label(toor, font=('aria', 15, 'bold'), text="Mushroom Pizza",bg="maroon", fg="royalblue3", anchor=W)
    it1.place(x=80,y=160)
    it1 = Label(toor, font=('aria', 15, 'bold'), text=c1,bg="maroon", fg="royalblue3", anchor=W)
    it1.place(x=340,y=160)
    it1 = Label(toor, font=('aria', 15, 'bold'), text=c1*300,bg="maroon", fg="royalblue3", anchor=W)
    it1.place(x=515,y=160)


    it2 = Label(toor, font=('aria', 15, 'bold'), text="Onions Pizza",bg="maroon", fg="royalblue3", anchor=W)
    it2.place(x=80,y=190)
    it2 = Label(toor, font=('aria', 15, 'bold'), text=c2,bg="maroon", fg="royalblue3", anchor=W)
    it2.place(x=340,y=190)
    it2 = Label(toor, font=('aria', 15, 'bold'), text=c2*250,bg="maroon", fg="royalblue3", anchor=W)
    it2.place(x=515,y=190)


    it3 = Label(toor, font=('aria', 15, 'bold'), text="Sausage Pizza",bg="maroon", fg="royalblue3", anchor=W)
    it3.place(x=80,y=220)
    it3 = Label(toor, font=('aria', 15, 'bold'), text=c3,bg="maroon", fg="royalblue3", anchor=W)
    it3.place(x=340,y=220)
    it3 = Label(toor, font=('aria', 15, 'bold'), text=c3*550,bg="maroon", fg="royalblue3", anchor=W)
    it3.place(x=515,y=220)


    it4 = Label(toor, font=('aria', 15, 'bold'), text="Classic Italian Pizza",bg="maroon", fg="royalblue3", anchor=W)
    it4.place(x=80,y=250)
    it4 = Label(toor, font=('aria', 15, 'bold'), text=c4,bg="maroon", fg="royalblue3", anchor=W)
    it4.place(x=340,y=250)
    it4 = Label(toor, font=('aria', 15, 'bold'), text=c4*350,bg="maroon", fg="royalblue3", anchor=W)
    it4.place(x=515,y=250)


    it5 = Label(toor, font=('aria', 15, 'bold'), text="Extra Cheese Pizza",bg="maroon", fg="royalblue3", anchor=W)
    it5.place(x=80,y=280)
    it5 = Label(toor, font=('aria', 15, 'bold'), text=c5, fg="royalblue3",bg="maroon", anchor=W)
    it5.place(x=340,y=280)
    it5 = Label(toor, font=('aria', 15, 'bold'), text=c5*600,bg="maroon", fg="royalblue3", anchor=W)
    it5.place(x=515,y=280)


    it6 = Label(toor, font=('aria', 15, 'bold'), text="Black Olives Pizza",bg="maroon", fg="royalblue3", anchor=W)
    it6.place(x=80,y=310)
    it6 = Label(toor, font=('aria', 15, 'bold'), text=c6,bg="maroon", fg="royalblue3", anchor=W)
    it6.place(x=340,y=310)
    it6 = Label(toor, font=('aria', 15, 'bold'), text=c6*650,bg="maroon", fg="royalblue3", anchor=W)
    it6.place(x=515,y=310)


    it7 = Label(toor, font=('aria', 15, 'bold'), text="Green Peppers Pizza",bg="maroon", fg="royalblue3", anchor=W)
    it7.place(x=80,y=340)
    it7 = Label(toor, font=('aria', 15, 'bold'), text=c7, fg="royalblue3",bg="maroon", anchor=W)
    it7.place(x=340,y=340)
    it7 = Label(toor, font=('aria', 15, 'bold'), text=c7*150,bg="maroon", fg="royalblue3", anchor=W)
    it7.place(x=515,y=340)


    it8 = Label(toor, font=('aria', 15, 'bold'), text="Pineapple Pizza", fg="royalblue3",bg="maroon", anchor=W)
    it8.place(x=80,y=370)
    it8= Label(toor, font=('aria', 15, 'bold'), text=c8, fg="royalblue3",bg="maroon", anchor=W)
    it8.place(x=340,y=370)
    it8 = Label(toor, font=('aria', 15, 'bold'), text=c8*450, fg="royalblue3",bg="maroon", anchor=W)
    it8.place(x=515,y=370)

    it9 = Label(toor, font=('aria', 15, 'bold'), text="Spinach Pizza",bg="maroon", fg="royalblue3", anchor=W)
    it9.place(x=80,y=400)
    it9 = Label(toor, font=('aria', 15, 'bold'), text=c9,bg="maroon", fg="royalblue3", anchor=W)
    it9.place(x=340,y=400)
    it9 = Label(toor, font=('aria', 15, 'bold'), text=c9*200,bg="maroon", fg="royalblue3", anchor=W)
    it9.place(x=515,y=400)

    itcoke = Label(toor,font=('aria', 15, 'bold'), text="Coke",bg="maroon", fg="royalblue3", anchor=W)
    itcoke.place(x=80,y=430)
    itcoke = Label(toor, font=('aria', 15, 'bold'), text=ccola,bg="maroon", fg="royalblue3", anchor=W)
    itcoke.place(x=340, y=430)
    itcoke = Label(toor, font=('aria', 15, 'bold'), text=ccola*40,bg="maroon", fg="royalblue3", anchor=W)
    itcoke.place(x=515, y=430)

    ittup = Label(toor, font=('aria', 15, 'bold'), text="Thums Up",bg="maroon", fg="royalblue3", anchor=W)
    ittup.place(x=80, y=460)
    ittup = Label(toor, font=('aria', 15, 'bold'), text=ctup,bg="maroon", fg="royalblue3", anchor=W)
    ittup.place(x=340, y=460)
    ittup = Label(toor, font=('aria', 15, 'bold'), text=ctup*40,bg="maroon", fg="royalblue3", anchor=W)
    ittup.place(x=515, y=460)

    itpep = Label(toor, font=('aria', 15, 'bold'), text="Pepsi", fg="royalblue3",bg="maroon", anchor=W)
    itpep.place(x=80, y=490)
    itpep = Label(toor, font=('aria', 15, 'bold'), text=cpep, fg="royalblue3",bg="maroon", anchor=W)
    itpep.place(x=340, y=490)
    itpep = Label(toor, font=('aria', 15, 'bold'), text=cpep*40, fg="royalblue3",bg="maroon", anchor=W)
    itpep.place(x=515, y=490)

    # DESIGN LABEL

    itii = Label(toor, font=('aria', 15, 'bold'), text="------------------------------------------------------------------------------------", fg="black",bg="maroon", bd=5)
    itii.place(x=0,y=520)

    # DISPLAY OF TOTAL PRICE LABEL

    itt = Label(toor, font=('aria', 15, 'bold'), text=" Total Price:", fg="black",bg="maroon", anchor=W)
    itt.place(x=380,y=550)
    itt = Label(toor, font=('aria', 15, 'bold'), text=sum, fg="black",bg="maroon", anchor=W)
    itt.place(x=515,y=550)

    # DISPLAY OF TOTAL QUANTITY

    itti = Label(toor, font=('aria', 15, 'bold'), text=" Total Qty.:", fg="black", bg="maroon", anchor=W)
    itti.place(x=210, y=550)
    itti = Label(toor, font=('aria', 15, 'bold'), text=sum1, fg="black", bg="maroon", anchor=W)
    itti.place(x=340, y=550)

    # DATA BASE ELEMENTS

    global enem
    global enum
    global total
    data1 = enem.get()
    data2 = enum.get()
    data3 = total.get()
    sql = "INSERT INTO db_pizza(customer_name,customer_contact,total_items,total_price)VALUES(%s,%s,%s,%s)"
    d = (data1, data2,sum1, data3)
    cursor.execute(sql, d)
    conn.commit()

    # CUSTOMER DETAIL LABELS

    dot = Label(toor, text="DATE || TIME", font=(10), bg="maroon")
    dot.place(x=445, y=10, anchor='nw')

    det = Label(toor, text="NAME:", font=(5), bg="maroon")
    det.place(x=0, y=10, anchor='nw')

    det1 = Label(toor, text="CONTACT:", font=(5), bg="maroon")
    det1.place(x=0, y=40, anchor='nw')

    na = Label(toor, text=data1, font=(5), bg="maroon")
    na.place(x=55, y=8, anchor='nw')

    nu = Label(toor, text=data2, font=(5), bg="maroon")
    nu.place(x=85, y=40, anchor='nw')

    dateotime()
    toor.mainloop()



# CREATED DESIGN LABELS

# LABEL FOR  PAGE TITLE HEADING

tittle =Label(root, text="PIZZA HUB", font=("Helvetica",20, "bold italic"),fg="red",bg="maroon")
tittle.place(x=600, y=20)

# LABEL FOR MENUE

MENUE1 =Label(root, text="OUR AUTHENTIC PIZZA MENU", font=("bold",15),fg="yellow",bg="maroon")
MENUE1.place(x=400, y=100)

MENUE2 =Label(root, text="EXTRA ADD-ONS (BREVRAGES)", font=("bold",10),fg="YELLOW",bg="maroon")
MENUE2.place(x=1110, y=100)

# LABEL FOR NAME & NUMBER

nam =Label(root, text="CUSTOMER NAME:", font=("Helvetica",15, "bold italic"),fg="BLACK",bg="maroon")
nam.place(x=50, y=20)

num =Label(root, text="CUSTOMER NUMBER:", font=("Helvetica",15, "bold italic"),fg="BLACK",bg="maroon")
num.place(x=50, y=60)

# LABEL FOR ITEMS & QUANTITY HEADINGS

ITEM =Label(root, text="ITEMS", font=("bold",15),fg="blue",bg="maroon")
ITEM.place(x=114, y=150)

QUANTITY =Label(root, text="QUANTITIES", font=("bold",15),fg="blue",bg="maroon")
QUANTITY.place(x=373, y=150)

ITEM1 =Label(root, text="ITEMS", font=("bold",15),fg="blue",bg="maroon")
ITEM1.place(x=614, y=150)

QUANTITY1 =Label(root, text="QUANTITIES", font=("bold",15),fg="blue",bg="maroon")
QUANTITY1.place(x=873, y=150)

# LABEL FOR ITEM & QUANTITY HEADINGS FOR ADD-ONS MENUE

ITEM2 =Label(root, text="ITEMS", font=("bold",12),fg="blue",bg="maroon")
ITEM2.place(x=1070, y=150)

QUANTITY2 =Label(root, text="QUANTITIES", font=("bold",12),fg="blue",bg="maroon")
QUANTITY2.place(x=1260, y=150)

# LABLES FOR ITEMS IM FOOD MENU

M0 =Label(root, text=("Pepperoni Pizza\n price:500per"),font=("bold",10),bg="maroon")
M0.place(x=200, y=214)

M1 =Label(root, text="Mushroom Pizza\n price:300per",font=("bold",10),bg="maroon")
M1.place(x=200, y=314)

M2 =Label(root, text="Onions Pizza\n price:250per",font=("bold",10),bg="maroon")
M2.place(x=200, y=414)

M3 =Label(root, text="Sausage Pizza\n price:550per",font=("bold",10),bg="maroon")
M3.place(x=200, y=514)

M4 =Label(root, text="Classic Italian Pizza\n price:350per",font=("bold",10),bg="maroon")
M4.place(x=200, y=614)

M5 =Label(root, text="Extra Cheese Pizza\n price:600per",font=("bold",10),bg="maroon")
M5.place(x=700, y=214)

M6 =Label(root, text="Black Olives Pizza\n price:650per",font=("bold",10),bg="maroon")
M6.place(x=700, y=314)

M7 =Label(root, text="Green Peppers Pizza\n price:150per",font=("bold",10),bg="maroon")
M7.place(x=700, y=414)

M8 =Label(root, text="Pineapple Pizza\n price:450per",font=("bold",10),bg="maroon")
M8.place(x=700, y=514)

M9 =Label(root, text="Spinach Pizza\n price:200per",font=("bold",10),bg="maroon")
M9.place(x=700, y=614)

# ADD-ONS MENUE LABLES

Mcola =Label(root, text="Coke\t\tx\n price:40rs/500ml",font=("bold",10),bg="maroon")
Mcola.place(x=1150, y=220)

Mtup =Label(root, text="Thums Up\tx\n price:40rs/500ml",font=("bold",10),bg="maroon")
Mtup.place(x=1150, y=320)

Mpep =Label(root, text="Pepsi\t\tx\n price:40rs/500ml",font=("bold",10),bg="maroon")
Mpep.place(x=1150, y=420)

# EXTRA DESIGN LABLES

D0 =Label(root, text="X",font=("bold",20),bg="maroon")
D0.place(x=330, y=214)

D1 =Label(root, text="X",font=("bold",20),bg="maroon")
D1.place(x=330, y=314)

D2 =Label(root, text="X",font=("bold",20),bg="maroon")
D2.place(x=330, y=414)

D3 =Label(root, text="X",font=("bold",20),bg="maroon")
D3.place(x=330, y=514)

D4 =Label(root, text="X",font=("bold",20),bg="maroon")
D4.place(x=330, y=614)

D5 =Label(root, text="X",font=("bold",20),bg="maroon")
D5.place(x=830, y=214)

D6 =Label(root, text="X",font=("bold",20),bg="maroon")
D6.place(x=830, y=314)

D7 =Label(root, text="X",font=("bold",20),bg="maroon")
D7.place(x=830, y=414)

D8 =Label(root, text="X",font=("bold",20),bg="maroon")
D8.place(x=830, y=514)

D9 =Label(root, text="X",font=("bold",20),bg="maroon")
D9.place(x=830, y=614)

T1 =Label(root, text="Total Price",fg="blue",font=("bold",20),bg="maroon")
T1.place(x=1020, y=530)


# CREATED BUTTONS

# IMAGE CLICK BUTTONS (item0 TO item9 FOR EACH ITEM RESPECTIVELY)

item0=PhotoImage(file=r"C:\Users\shubham\PycharmProjects\pizza\pizza\pr.png")
Button(root,image=item0,bd=4,command=i0).place(x=100,y=200)

item1=PhotoImage(file=r"C:\Users\shubham\PycharmProjects\pizza\pizza\mr.png")
Button(root,text="1",image=item1,bd=4,command=i1).place(x=100,y=300)

item2=PhotoImage(file=r"C:\Users\shubham\PycharmProjects\pizza\pizza\or.png")
Button(root,text="1",image=item2,bd=4,command=i2).place(x=100,y=400)

item3=PhotoImage(file=r"C:\Users\shubham\PycharmProjects\pizza\pizza\sr.png")
Button(root,text="1",image=item3,bd=4,command=i3).place(x=100,y=500)

item4=PhotoImage(file=r"C:\Users\shubham\PycharmProjects\pizza\pizza\ir.png")
Button(root,text="1",image=item4,bd=4,command=i4).place(x=100,y=600)

item5=PhotoImage(file=r"C:\Users\shubham\PycharmProjects\pizza\pizza\cr.png")
Button(root,text="1",image=item5,bd=4,command=i5).place(x=600,y=200)

item6=PhotoImage(file=r"C:\Users\shubham\PycharmProjects\pizza\pizza\br.png")
Button(root,text="1",image=item6,bd=4,command=i6).place(x=600,y=300)

item7=PhotoImage(file=r"C:\Users\shubham\PycharmProjects\pizza\pizza\gr.png")
Button(root,text="1",image=item7,bd=4,command=i7).place(x=600,y=400)

item8=PhotoImage(file=r"C:\Users\shubham\PycharmProjects\pizza\pizza\par.png")
Button(root,text="1",image=item8,bd=4,command=i8).place(x=600,y=500)

item9=PhotoImage(file=r"C:\Users\shubham\PycharmProjects\pizza\pizza\spr.png")
Button(root,text="1",image=item9,bd=4,command=i9).place(x=600,y=600)

# IMAGE BUTTON FOR ADD-ONS MENUE

itemcola=PhotoImage(file=r"C:\Users\shubham\PycharmProjects\pizza\pizza\cola.png")
Button(root,text="1",image=itemcola,bd=4,command=icola).place(x=1050,y=200)

itemtup=PhotoImage(file=r"C:\Users\shubham\PycharmProjects\pizza\pizza\tup.png")
Button(root,text="1",image=itemtup,bd=4,command=itup).place(x=1050,y=300)

itempep=PhotoImage(file=r"C:\Users\shubham\PycharmProjects\pizza\pizza\pep.png")
Button(root,text="1",image=itempep,bd=4,command=ipep).place(x=1050,y=400)

# TOTAL BUTTON

TOTAL=Button(root,text="TOTAL",width=17,bg="red",bd=5,command=tpr)
TOTAL.place(x=1180, y=575)

# PLACE ORDER BUTTON

ORDER=Button(root,text="PLACE ORDER",width=17,bg="red",bd=5,command=bill)
ORDER.place(x=1180, y=620)

# CLEAR BUTTON

clr= Button(root,text="CLEAR",width=17,bg="red",bd=5,command=clearl)
clr.place(x=1030,y=620)


# CREATED INPUT ENTRY POINTS

# ENTRY POINTS FROM e0 TO e9 WITH RESPECT TO EACH ITEM GIVEN IN FOOD MENU

e0=Entry(root,bd=5)
e0.place(x=370,y=220)

e1=Entry(root,bd=5)
e1.place(x=370,y=320)

e2=Entry(root,bd=5)
e2.place(x=370,y=420)

e3=Entry(root,bd=5)
e3.place(x=370,y=520)

e4=Entry(root,bd=5)
e4.place(x=370,y=620)

e5=Entry(root,bd=5)
e5.place(x=870,y=220)

e6=Entry(root,bd=5)
e6.place(x=870,y=320)

e7=Entry(root,bd=5)
e7.place(x=870,y=420)

e8=Entry(root,bd=5)
e8.place(x=870,y=520)

e9=Entry(root,bd=5)
e9.place(x=870,y=620)

# ADD-ONS MENUE ENTRY

ecola=Entry(root,bd=5,width=8)
ecola.place(x=1280,y=220)

etup=Entry(root,bd=5,width=8)
etup.place(x=1280,y=320)

epep=Entry(root,bd=5,width=8)
epep.place(x=1280,y=420)

# NAME & NUMBER ENTRY PIONTS

enem=Entry(root,bd=5)
enem.place(x=280,y=20)

enum=Entry(root,bd=5)
enum.place(x=280,y=60)


# TOTAL ENTRY POINT WTH RESPECT TO TOTAL ALL THE ITEM INPUTS FROM FOOD MENU CALCULATED WITH EACH ITEM PRICE

total=Entry(root,bd=5)
total.place(x=1030,y=575)


dateotime()
root.mainloop()
