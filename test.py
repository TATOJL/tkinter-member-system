from tkinter import *
from tkinter.messagebox import showinfo,showerror,askyesno
def layout():
  import pickle
  from PIL import Image,ImageTk
  #視窗
  window=Tk()
  window.title('會員登入系統'.center(100))
  #畫布放置圖片
  canvas=Canvas(window,height=300,width=500)
  imagefile=ImageTk.PhotoImage(Image.open('sea.jpg'))
  image=canvas.create_image(0,0,anchor='nw',image=imagefile)
  window.resizable(0,0)
  canvas.pack(side='top')
  #標籤 使用者名稱密碼
  Label(window,text='帳號:').place(x=130,y=90 )
  Label(window,text='密碼:').place(x=130,y=160)
  #使用者名稱輸入框
  var_member_act=StringVar()
  entry_member_act=Entry(window,textvariable=var_member_act)
  entry_member_act.place(x=210,y=90  )
  #密碼輸入框
  var_member_pwd= StringVar()
  entry_member_pwd= Entry(window,textvariable=var_member_pwd,show='*')
  entry_member_pwd.place(x=210,y=160)
   
  #登入函數
  def login():
      #輸入框獲取使用者名稱密碼
      member_act=var_member_act.get()
      member_pwd=var_member_pwd.get()
     #從本地字典獲取使用者資訊，如果沒有則新建本地資料庫
      try:
          with open('member_info.pickle','rb') as member_file:
              members_info=pickle.load(member_file)
      except FileNotFoundError:
          with open('member_info.pickle','wb') as member_file:
              members_info={'admin':'admin'}
              pickle.dump(members_info,member_file)
      #判斷使用者名稱和密碼是否匹配
      if member_act in members_info:
          if member_pwd == members_info[member_act]:
                 showinfo(title='welcome',
                           message='歡迎您：'+member_act)
          else:
                 showerror(message='密碼錯誤')
      #使用者名稱密碼不能為空
      elif member_act=='' or member_pwd=='' :
             showerror(message='帳號或密碼為空')
      #不在資料庫中彈出是否註冊的框
      else:
          is_signup=   askyesno('歡迎','您還沒有註冊，是否現在註冊')
          if is_signup:
              signup()
  #註冊函數
  def signup():
      #確認註冊時的相應函數
      def signtowcg():
          global nname
          global nact
          #獲取輸入框內的內容
          nact=new_act.get()
          npwd=new_pwd.get()
          npwdf=new_pwd_confirm.get()
          nadd=new_add.get()
          nemail=new_email.get()
          ntel=new_tel.get()
          nname=new_name.get()
          nbirth=new_birth.get()
   
          #本地載入已有使用者資訊,如果沒有則已有使用者資訊為空
          try:
              with open('member_info.pickle','rb') as member_file:
                  exist_member_info=pickle.load(member_file)
          except FileNotFoundError:
              exist_member_info={}           
              
          #檢查使用者名稱存在、密碼為空、密碼前後不一致
          if nact in exist_member_info:
                 showerror('錯誤','帳號已存在')
          elif not (nact and npwd and nadd and nemail and ntel and nname and nbirth ):
               print(nact and npwd and nadd and nemail and ntel and nname and nbirth !='' )
               showerror('錯誤','資料不得為空')
          elif npwd !=npwdf:
               showerror('錯誤','密碼前後不一致')
          #註冊資訊沒有問題則將使用者名稱密碼寫入資料庫
          else:
              exist_member_info[nact]=npwd
              with open('member_info.pickle','wb') as member_file:
                  pickle.dump(exist_member_info,member_file)
                  showinfo('歡迎','註冊成功')
                  
              #註冊成功關閉註冊框
              window_sign_up.destroy()
      #新建註冊介面
      window_sign_up= Toplevel(window)
      window_sign_up.geometry('330x400')
      window_sign_up.title('註冊')
      #帳號變數及標籤、輸入框
      new_act= StringVar()
      Label(window_sign_up,text='帳號：').place(x=10,y=10)
      Entry(window_sign_up,textvariable=new_act).place(x=150,y=10)
      #密碼變數及標籤、輸入框
      new_pwd= StringVar()
      Label(window_sign_up,text='輸入密碼：').place(x=10,y=50)
      Entry(window_sign_up,textvariable=new_pwd,show='*').place(x=150,y=50)    
      #重複密碼變數及標籤、輸入框
      new_pwd_confirm= StringVar()
      Label(window_sign_up,text='確認密碼：').place(x=10,y=90)
      Entry(window_sign_up,textvariable=new_pwd_confirm,show='*').place(x=150,y=90) 
      #地址
      new_add= StringVar()
      Label(window_sign_up,text='地址：').place(x=10,y=130)
      Entry(window_sign_up,textvariable=new_add).place(x=150,y=130)
      #email變數及標籤、輸入框
      new_email= StringVar()
      Label(window_sign_up,text='email：').place(x=10,y=170)
      Entry(window_sign_up,textvariable=new_email).place(x=150,y=170)
      #電話變數及標籤、輸入框
      new_tel= StringVar()
      Label(window_sign_up,text='電話：').place(x=10,y=210)
      Entry(window_sign_up,textvariable=new_tel).place(x=150,y=210)
      #名稱變數及標籤、輸入框
      new_name= StringVar()
      Label(window_sign_up,text='名稱：').place(x=10,y=250)
      Entry(window_sign_up,textvariable=new_name).place(x=150,y=250)
      #生日 變數及標籤、輸入框
      new_birth= StringVar()
      Label(window_sign_up,text='生日：').place(x=10,y=290)
      Entry(window_sign_up,textvariable=new_birth).place(x=150,y=290)

      #確認註冊按鈕及位置變數及標籤、輸入框
      bt_confirm_sign_up= Button(window_sign_up,text='確認註冊',
                                   command=signtowcg)
      bt_confirm_sign_up.place(x=100,y=330 ,width=100)
  #退出的函數
  
  #登入 註冊按鈕
  bt_login= Button(window,text='登入',command=login)
  bt_login.place(x=130,y=230)
  bt_logup= Button(window,text='註冊',command=signup)
  bt_logup.place(x=220,y=230)
  bt_logquit= Button(window,text='退出',command=quit)
  bt_logquit.place(x=320,y=230)
  #主迴圈
  window.mainloop()
layout()
