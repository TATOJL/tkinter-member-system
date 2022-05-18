from tkinter import *
from test2 import login,register
from PIL import Image,ImageTk
from signup import signup
#視窗

window=Tk()
window.title('會員登入系統'.center(100))
#放置圖片
canvas=Canvas(window,height=300,width=500)
imagefile=ImageTk.PhotoImage(Image.open('sea.jpg'))
image=canvas.create_image(0,0,anchor='nw',image=imagefile)
window.resizable(0,0)
canvas.pack(side='top')
#標籤 
input_act=Label(window,text='帳號:').place(x=130,y=90 )
input_pwd=Label(window,text='密碼:').place(x=130,y=160)
#輸入框
var_member_act=StringVar()
entry_member_act=Entry(window,textvariable=var_member_act)
entry_member_act.place(x=210,y=90  )
#密碼輸入框
var_member_pwd= StringVar()
entry_member_pwd= Entry(window,textvariable=var_member_pwd,show='*')
entry_member_pwd.place(x=210,y=160)




#退出的函數

#登入 註冊按鈕
blogin= Button(window,text='登入',command=login)
blogin.place(x=130,y=230)
blogup= Button(window,text='註冊',command= signup )
blogup.place(x=220,y=230)
blogquit= Button(window,text='退出',command=quit)
blogquit.place(x=320,y=230)
#主迴圈
window.mainloop()

