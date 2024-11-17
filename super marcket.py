from tkinter import * 
from tkinter import messagebox
win = Tk()
win.geometry('700x400')
win.resizable(0,0)
win.configure()
win.title('مدیریت کتابخانه ')
# function=====================

# Widget=======================
lbl_name=Label(win,text = 'نام کالا :',font='btitr 15')
lbl_name.place(x=32,y=20)

ent_name = Entry(win,font='btitr 12')
ent_name.place(x=120,y=23)

lbl_buy=Label(win,text = 'قیمت خرید :',font='btitr 15')
lbl_buy.place(x=350,y=20)

ent_buy = Entry(win,font='btitr 12')
ent_buy.place(x=450,y=23)


lbl_sell=Label(win,text = 'قیمت فروش :',font='btitr 15')
lbl_sell.place(x=20,y=80)

ent_sell = Entry(win,font='btitr 12')
ent_sell.place(x=120,y=83)


lbl_number=Label(win,text = 'تعداد :',font='btitr 15 ')
lbl_number.place(x=375,y=80)

ent_number = Entry(win,font='btitr 12')
ent_number.place(x=450,y=83)

btn_insert=Button(win,text='اضافه کردن',width=17,font='btetr 12 bold')
btn_insert.place(x=452,y=120)

btn_search=Button(win,text='جستوجو کالا',width=17,font='btetr 12 bold')
btn_search.place(x=452,y=160)

btn_delete=Button(win,text='حذف کالا',width=17,font='btetr 12 bold')
btn_delete.place(x=452,y=200)

btn_edit=Button(win,text='ویرایش',width=17,font='btetr 12 bold')
btn_edit.place(x=452,y=240)


btn_ext=Button(win,text='خروج',width=17,font='btetr 12 bold')
btn_ext.place(x=452,y=280)


# lst_box=Listbox(height=12)
sb = Scrollbar(win)
sb.place(x=415,y=120)
lst_box=Listbox(win,yscrollcommand=sb.set,width=65,height=12)
sb.configure(YView=lst_box)
lst_box.place(x=20,y=120)

win.mainloop()