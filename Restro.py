import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image




root=tk.Tk()
root.geometry("1920x1280")

# Background Image

img=ImageTk.PhotoImage(Image.open("Restaurant.jpg"))
label=tk.Label(image=img)
label.grid(row=0,column=0)



#================================ Frame 1 f1 ===================================





# LabelFrame to Assign a Frame With LAbel On it


f1=tk.LabelFrame(root,text="\t Restaurant Billing Software",bd=10,font="arial 16 bold",width=1200,height=40,fg="white",bg="black")
f1.place(x=150,y=15)










#============================== Frame 2 f2 =====================================






#************* Fast Food f2 Starts **************



# LabelFrame FastFood


f2=tk.LabelFrame(root ,text="\t Fast Foods",bd=15,font="arial 16 bold",width=400,bg="silver",fg="black")
f2.place(x=100,y=70,height=500)



def check():
    if var.get() == 0:
        e1.configure(state ="disabled")
    else:
        e1.configure(state ="normal")


# Burger

var = tk.IntVar()#var

burger = tk.IntVar()#burger


checkbox_1=tk.Checkbutton(f2,text="Burger :25 ",variable=var,bg="silver",font="arial 14 bold",command=check)
checkbox_1.place(x=10,y=5)

e1=tk.Entry(f2,font="arial 16 bold",textvariable=burger,bd=3,width=10,state='disabled')
e1.place(x=220,y=5)

# Chawmin

var1 = tk.IntVar()#var

chowmein = tk.IntVar()#chawmein

def check2():
    if var1.get() == 0:
        e2.configure(state ="disabled")
    else:
        e2.configure(state ="normal")


checkbox_2=tk.Checkbutton(f2,text="Chowmein :50",variable=var1,bg="silver",font="arial 14 bold",command=check2)
checkbox_2.place(x=10,y=50)

e2=tk.Entry(f2,font="arial 16 bold",textvariable=chowmein,bd=3,width=10,state='disabled')
e2.place(x=220,y=50)

# Pasta

var2 = tk.IntVar()#var

pasta = tk.IntVar()#pasta

def check3():
    if var2.get() == 0:
        e3.configure(state ="disabled")
    else:
        e3.configure(state ="normal")




checkbox_3=tk.Checkbutton(f2,text="Pasta :120 ",variable=var2,bg="silver",font="arial 14 bold",command=check3)
checkbox_3.place(x=10,y=100)

e3=tk.Entry(f2,font="arial 16 bold",textvariable=pasta,bd=3,width=10,state='disabled')
e3.place(x=220,y=100)


# Veg Roll

var3 = tk.IntVar()#var

vegroll = tk.IntVar()#vegroll

def check4():
    if var3.get() == 0:
        e4.configure(state ="disabled")
    else:
        e4.configure(state ="normal")


checkbox_4=tk.Checkbutton(f2,text="VegRoll :100 ",variable=var3,bg="silver",font="arial 14 bold",command=check4)
checkbox_4.place(x=10,y=150)

e4=tk.Entry(f2,font="arial 16 bold",textvariable=vegroll,bd=3,width=10,state='disabled')
e4.place(x=220,y=150)

# Chicken Roll

var4 = tk.IntVar()#var

chickenroll = tk.IntVar()#chickenroll

def check5():
    if var4.get() == 0:
        e5.configure(state ="disabled")
    else:
        e5.configure(state ="normal")


checkbox_5=tk.Checkbutton(f2,text="ChickenRoll :150 ",variable=var4,bg="silver",font="arial 14 bold",command=check5)
checkbox_5.place(x=10,y=200)

e5=tk.Entry(f2,font="arial 16 bold",textvariable=chickenroll,bd=3,width=10,state='disabled')
e5.place(x=220,y=200)

#************ Fast Food f2 Ends Here ****************



#==================================== Frame 3 f3 =============================================================


#************* Drinks F3 Starts ********************


# LabelFrame Drinks
f3=LabelFrame(root,text="\t Drinks",bd=15,font="arial 16 bold",width=400,bg="silver",fg="black")
f3.place(x=550,y=70,height=500)





# Pepsi

var11 = tk.IntVar()#var

pepsi = tk.IntVar()#pepsi

def check11():
    if var11.get() == 0:
        e11.configure(state ="disabled")
    else:
        e11.configure(state ="normal")


checkbox_11=tk.Checkbutton(f3,text="Pepsi :35 ",variable=var11,bg="silver",font="arial 14 bold",command=check11)
checkbox_11.place(x=10,y=5)

e11=tk.Entry(f3,font="arial 16 bold",textvariable=pepsi,bd=3,width=10,state='disabled')
e11.place(x=220,y=5)

# CocaCola

var22 = tk.IntVar()#var

cocacola = tk.IntVar()#cocacola

def check22():
    if var22.get() == 0:
        e22.configure(state ="disabled")
    else:
        e22.configure(state ="normal")


checkbox_22=tk.Checkbutton(f3,text="CocaCola :50",variable=var22,bg="silver",font="arial 14 bold",command=check22)
checkbox_22.place(x=10,y=50)

e22=tk.Entry(f3,font="arial 16 bold",textvariable=cocacola,bd=3,width=10,state='disabled')
e22.place(x=220,y=50)

# MilkShake

var33 = tk.IntVar()#var

milkshake = tk.IntVar()#milkshake

def check33():
    if var33.get() == 0:
        e33.configure(state ="disabled")
    else:
        e33.configure(state ="normal")


checkbox_33=tk.Checkbutton(f3,text="MilkShake :100 ",variable=var33,bg="silver",font="arial 14 bold",command=check33)
checkbox_33.place(x=10,y=100)

e33=tk.Entry(f3,font="arial 16 bold",textvariable=milkshake,bd=3,width=10,state='disabled')
e33.place(x=220,y=100)


# ChocoShake

var44= tk.IntVar()#var

chocoshake= tk.IntVar()#chocoshake

def check44():
    if var44.get() == 0:
        e44.configure(state ="disabled")
    else:
        e44.configure(state ="normal")


checkbox_44=tk.Checkbutton(f3,text="ChocoShake :120 ",variable=var44,bg="silver",font="arial 14 bold",command=check44)
checkbox_44.place(x=10,y=150)

e44=tk.Entry(f3,font="arial 16 bold",textvariable=chocoshake,bd=3,width=10,state='disabled')
e44.place(x=220,y=150)

# MixShaKe

var55 = tk.IntVar()#var

mixshake = tk.IntVar()#mixshake

def check55():
    if var55.get() == 0:
        e55.configure(state ="disabled")
    else:
        e55.configure(state ="normal")


checkbox_55=tk.Checkbutton(f3,text="MixShake :140 ",variable=var55,bg="silver",font="arial 14 bold",command=check55)
checkbox_55.place(x=10,y=200)

e55=tk.Entry(f3,font="arial 16 bold",textvariable=mixshake,bd=3,width=10,state='disabled')
e55.place(x=220,y=200)


def reset_all():

    
    
    burger.set("0")
    chowmein.set("0")
    pasta.set("0")
    vegroll.set("0")
    chickenroll.set("0")
    pepsi.set("0")
    cocacola.set("0")
    milkshake.set("0")
    chocoshake.set("0")
    mixshake.set("0")

    
    
    fast_food.set("")
    fast_food_tax.set("")
    drinks.set("")
    drinks_tax.set("")
    total_amt.set("")
    
    var.set(0)
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var11.set(0)
    var22.set(0)
    var33.set(0)
    var44.set(0)
    var55.set(0)

    e1.configure(state='disabled')
    e2.configure(state='disabled')
    e3.configure(state='disabled')
    e4.configure(state='disabled')
    e5.configure(state='disabled')
    e11.configure(state='disabled')
    e22.configure(state='disabled')
    e33.configure(state='disabled')
    e44.configure(state='disabled')
    e55.configure(state='disabled')


#******************** Dinks f3 Ends Here ********************





#======================================= Frame 5 f5 ===========================================




#============== Bill generate ========================

# LabelFrame Total Amount OF Order And Prizes

f5=LabelFrame(root,text="\t Billing Area",bd=15,font="arial 16 bold",width=1200,bg="silver",fg="black")
f5.place(x=150,y=580,height=250)

#========== variables for f5 Billing Area ===========

# Labels And texts


fast_food=tk.StringVar()
fast_food_tax=tk.StringVar()
drinks=tk.StringVar()
drinks_tax=tk.StringVar()
total_amt=tk.StringVar()


f_food=tk.Label(f5,text="Fast Food Cost :",bg="silver",font="arial 12 bold")
f_food.place(x=30,y=10)
f_food_entry=tk.Entry(f5,font="arial 14 bold",textvariable=fast_food,width=20)
f_food_entry.place(x=220,y=10)

f_food_tax=tk.Label(f5,text="Fast Food Tax :",bg="silver",font="arial 12 bold")
f_food_tax.place(x=30,y=50)
f_food_tax_entry=tk.Entry(f5,font="arial 14 bold",textvariable=fast_food_tax,width=20)
f_food_tax_entry.place(x=220,y=50)

d_drinks=tk.Label(f5,text="Drinks Cost :",bg="silver",font="arial 12 bold")
d_drinks.place(x=30,y=90)
d_drinks_entry=tk.Entry(f5,font="arial 14 bold",textvariable=drinks,width=20)
d_drinks_entry.place(x=220,y=90)

d_drinks_tax=tk.Label(f5,text="Drinks Tax :",bg="silver",font="arial 12 bold")
d_drinks_tax.place(x=30,y=130)
d_drinks_tax_entry= tk.Entry(f5,textvariable=drinks_tax,font="arial 14 bold",width=20)
d_drinks_tax_entry.place(x=220,y=130)

total_amount=tk.Label(f5,text="Total Amount :",bg="silver",font="arial 12 bold")
total_amount.place(x=30,y=170)
total_entry= tk.Entry(f5,textvariable=total_amt,font="arial 14 bold",width=20)
total_entry.place(x=220,y=170)







#========================================= Frame 4 f4 ===================================







#****************** Billing System STarts ***********************

# LabelFrame Billing System 
f4=LabelFrame(root,text="\t Billing Area",bd=15,font="arial 16 bold",width=400,bg="silver",fg="black")
f4.place(x=1000,y=70,height=500)

# Food & Drinks

l1=Label(f4,text="Food & Drinks :",bg="silver",font="arial 10 bold",fg="black")
l1.place(x=10,y=10)

# Quantity
l7=Label(f4,text="Quantity :",bg="silver",font="arial 10 bold",fg="black")
l7.place(x=160,y=10)

# Amount
l44=Label(f4,text="Amount :",bg="silver",font="arial 10 bold",fg="black")
l44.place(x=280,y=10)


# Function

def bill():

    global l2
    global l3
    global l4
    global l5
    global l6
    global l7
    global l8
    global l9
    global l11
    global l22
    global l33
    global l44
    global l55
    global l66
    global l77
    global l88
    global l111
    global l222
    global l333
    global l444
    global l555
    global l666
    global l777
    global l888
    global l999
    global l_2
    global l_3
    
#============= FAstFood Column =============
    

    
    l2=Label(f4,text="Burger \t\t\t"+ e1.get(),bg="silver",font="arial 10 bold",fg="black").place(x=10,y=40)
    l3=Label(f4,text="Chowmein \t\t"+ e2.get(),bg="silver",font="arial 10 bold",fg="black").place(x=10,y=60)
    l4=Label(f4,text="Pasta \t\t\t"+ e3.get(),bg="silver",font="arial 10 bold",fg="black").place(x=10,y=80)
    l5=Label(f4,text="VegRoll \t\t\t"+ e4.get(),bg="silver",font="arial 10 bold",fg="black").place(x=10,y=100)
    l6=Label(f4,text="ChickenRoll \t\t"+ e5.get(),bg="silver",font="arial 10 bold",fg="black").place(x=10,y=120)
    l8=Label(f4,text="Pepsi :\t\t\t"+ e11.get(),bg="silver",font="arial 10 bold",fg="black").place(x=10,y=140)
    l9=Label(f4,text="CocoCola :\t\t"+ e22.get(),bg="silver",font="arial 10 bold",fg="black").place(x=10,y=160)
    l11=Label(f4,text="MilkShake :\t\t"+ e33.get(),bg="silver",font="arial 10 bold",fg="black").place(x=10,y=180)
    l22=Label(f4,text="ChocoShake :\t\t"+ e44.get(),bg="silver",font="arial 10 bold",fg="black").place(x=10,y=200)
    l33=Label(f4,text="MixShake :\t\t"+ e55.get(),bg="silver",font="arial 10 bold",fg="black").place(x=10,y=220)   
   
    

#========= Amount ================
    

    
    l55=Label(f4,text=("Rs - " + str( burger.get()*25)))
    l55.place(x=280,y=40)

    l66=Label(f4,text=("Rs - " + str( chowmein.get()*50)))
    l66.place(x=280,y=60)

    l77=Label(f4,text=("Rs - " + str( pasta.get()*120)))
    l77.place(x=280,y=80)

    l88=Label(f4,text=("Rs - " + str( vegroll.get()*100)))
    l88.place(x=280,y=100)

    l111=Label(f4,text=("Rs - " + str( chickenroll.get()*150)))
    l111.place(x=280,y=120)

    l222=Label(f4,text=("Rs - " + str( pepsi.get()*35)))
    l222.place(x=280,y=140)

    l333=Label(f4,text=("Rs - " + str( cocacola.get()*50)))
    l333.place(x=280,y=160)

    l444=Label(f4,text=("Rs - " + str( milkshake.get()*100)))
    l444.place(x=280,y=180)

    l555=Label(f4,text=("Rs - " + str( chocoshake.get()*120)))
    l555.place(x=280,y=200)

    l666=Label(f4,text=("Rs - " + str( mixshake.get()*140)))
    l666.place(x=280,y=220)


#==================================== Total Amount ==================================================

    

    # Fast Food Tax

    l777=Label(f4,text="FastFood Tax::",fg="black",bg="silver",font="arial 14 bold")
    l777.place(x=80,y=300)   
    
    fast_food_tax = (
        (burger.get()*25)+(chowmein.get()*50)+(pasta.get()*120)+(vegroll.get()*100)+(chickenroll.get()*150)
        )*0.10
    l_1=Label(f4,text=("Rs - " + str(fast_food_tax)),fg="black",bg="silver",font="arial 14 bold")
    l_1.place(x=230,y=300)
    
    # Drink Tax
    
    l888=Label(f4,text="Drinks Tax :: ",fg="black",bg="silver",font="arial 14 bold")
    l888.place(x=80,y=350)

    drinks_tax=(
         (pepsi.get()*35)+(cocacola.get()*50)+(milkshake.get()*100)+(chocoshake.get()*120)+(mixshake.get()*140)
        )*0.05
    l_2=Label(f4,text=("Rs - " + str(drinks_tax)),fg="black",bg="silver",font="arial 14 bold")
    l_2.place(x=230,y=350)


    #Sum OF Fast Food Tax And Drink Tax
    
    s= fast_food_tax + drinks_tax
    
    # Total Calulation

    total_calculated=( ( burger.get()*25) + ( chowmein.get()*50) + ( pasta.get()*120) +
                       ( vegroll.get()*100) + ( chickenroll.get()*150) + ( pepsi.get()*35) +
                       ( cocacola.get()*50) + ( milkshake.get()*100) + ( chocoshake.get()*120) +
                       ( mixshake.get()*140)                       
                       )

    l999=Label(f4,text="Total :: ",fg="black",bg="silver",font="arial 14 bold")
    l999.place(x=80,y=400)
   
    l_3=Label(f4,text=("Rs - " + str(total_calculated + s )),fg="black",bg="silver",font="arial 14 bold")
    l_3.place(x=230,y=400)
    

    







#********** Billing System Ends Here ************




#======================================== Frame 5 f5 Buttons==============================================



#=========== Billing Area Calculation =========



# Total Button Working




def total():

#=========== Fast Food ===========
    
    # total_of_fast_food is Just a Variable/// any name can be given

    total_of_fast_food=(
        (burger.get()*25)+(chowmein.get()*50)+(pasta.get()*120)+(vegroll.get()*100)+(chickenroll.get()*150)
        )

    
    #fast_food is The variable used in Entry Box of Fast Food Cost

    fast_food.set("Rs "+str(total_of_fast_food))



    # total_fast_food_tax is Just a Variable/// any name can be given

    total_fast_food_tax=(
        (burger.get()*25)+(chowmein.get()*50)+(pasta.get()*120)+(vegroll.get()*100)+(chickenroll.get()*150)
        )*0.10

    
    #fast_food_tax is The variable used in Entry Box of Fast Food Cost

    fast_food_tax.set("Rs "+ str(total_fast_food_tax))



#============================================ Drinks ==========================================================
    
    # total_drinks is Just a Variable/// any name can be given 
    total_drinks=(
        (pepsi.get()*35)+(cocacola.get()*50)+(milkshake.get()*100)+(chocoshake.get()*120)+(mixshake.get()*140)
        )
    #drinks is The variable used in Entry Box of Fast Food Cost
    drinks.set("Rs "+str(total_drinks))

    # total_Drinks_tax is Just a Variable/// any name can be given 
    total_drinks_tax=(
         (pepsi.get()*35)+(cocacola.get()*50)+(milkshake.get()*100)+(chocoshake.get()*120)+(mixshake.get()*140)
        )*0.05
    #drinks_tax is The variable used in Entry Box of Fast Food Cost
    drinks_tax.set("Rs "+str(total_drinks_tax))


#====================================================== Overall Total Amount To pAy ============================


    
    # Total Amount To Fetch Taking A new Variable
    total_amount_fetch=( total_of_fast_food + total_fast_food_tax + total_drinks + total_drinks_tax
                  
       )
    # Total Amount USing total Variable
    total_amt.set("Rs "+str(total_amount_fetch))
    


    






#================== Total Button =====================


t_total=tk.Button(f5,text="Total Cost",bg="gray",bd=5,fg="white",font="arial 16 bold",padx=32,pady=10,command=total)
t_total.place(x=500,y=10)

#================= Bill Generate ===================


t_bill=tk.Button(f5,text="Bill Generate",bg="gray",bd=5,fg="white",font="arial 16 bold",padx=20,pady=10,command=bill)
t_bill.place(x=500,y=50)



#============== Exit Button ======================


t_exit=tk.Button(f5,text="Exit",bg="gray",bd=5,fg="white",font="arial 16 bold",padx=45,pady=10 ,command=root.destroy)
t_exit.place(x=750,y=10)


#================= Reset Button ==================


t_total=tk.Button(f5,text="Reset",bg="gray",bd=5,fg="white",font="arial 16 bold",padx=35,pady=10,command=reset_all)
t_total.place(x=750,y=50)





root.mainloop()
