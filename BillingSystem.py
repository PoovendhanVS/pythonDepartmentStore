from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import ttk

con = mysql.connector.connect(host='localhost',user='root',password='toor',database='BillingSys_DB')

FnyStore = Tk()
FnyStore.title('Department Store')
FnyStore.geometry('1400x500')

lblPnm = Label(FnyStore,text='Product Name')

lblPnm.grid(row=0,column=0)

ipPnm = StringVar()
txtBoxPnm = Entry(FnyStore,textvariable=ipPnm)
txtBoxPnm.grid(row=0,column=1)

lblPrice = Label(FnyStore,text='Product Price')
lblPrice.grid(row=1,column=0)

ipPrc = IntVar()
txtBoxPrice = Entry(FnyStore,textvariable=ipPrc)
txtBoxPrice.grid(row=1,column=1)

lblQty = Label(FnyStore,text='Number of quantity')
lblQty.grid(row=2,column=0)

ipQty = IntVar()
txtBoxQty = Entry(FnyStore,textvariable=ipQty)
txtBoxQty.grid(row=2,column=1)

def Insert():
    ctvt = con.cursor()
    qry = 'insert into Product(PName,Price,Quantity,TotalCost) values(%s,%s,%s,%s)'

    pname = ipPnm.get()
    pprice = ipPrc.get()
    pqty = ipQty.get()
    tolcst = pprice * pqty

    vals = (pname,pprice,pqty,tolcst)
    ctvt.execute(qry,vals)
    con.commit()
    messagebox.showinfo(title='Sending Data',message='Data has been Stored')

def Show():
    ctvt = con.cursor()
    qry = 'select * from Product'
    ctvt.execute(qry)
    result = ctvt.fetchall()

    tv = ttk.Treeview(FnyStore,columns=(1,2,3,4,5))
    tv.place(x=100,y=150)

    tv.heading(1,text='ID')
    tv.column(1,anchor=CENTER)
    tv.heading(2,text='Product Name')
    tv.column(2,anchor=CENTER)
    tv.heading(3,text='Price')
    tv.column(3,anchor=CENTER)
    tv.heading(4,text='Quantity')
    tv.column(4,anchor=CENTER)
    tv.heading(5,text='Total Cost')
    tv.column(5,anchor=CENTER)

    for v in result:
        tv.insert('','end',values=v)

def Delete():
    ctvt   = con.cursor()
    qry = 'delete '

DelId = IntVar()
Label(FnyStore,text='Delete ID').grid(row=5,column=0)
Entry(FnyStore,textvariable=DelId).grid(row=5,column=1)

def Update():
    ctvt   = con.cursor()
    qry = 'update Product SET PName = pname,Price = pprice,Quantity = pqty WHERE ID=pudid;'
    pname = ipPnm.get()
    pprice = ipPrc.get()
    pqty = ipQty.get()
    pudid = ipUp.get()
    val = (pname,pprice,pqty,pudid)
    ctvt.execute(qry,val)
    con.commit()
    messagebox.showinfo(title='Deleting Msg',message='Data has been Deleted')

btnSubmit = Button(FnyStore,text='Submit',command=Insert).grid(row=3,column=0)

btnShow = Button(FnyStore,text='Show',command=Show).grid(row=3,column=1)

btnDel = Button(FnyStore,text='Delete',command=Delete).grid(row=4,column=0)

btnUpdate = Button(FnyStore,text='Update',command=Update).grid(row=6,column=0)



FnyStore.mainloop()