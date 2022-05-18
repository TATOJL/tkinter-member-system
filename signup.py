from re import T
from tkinter import *
from tkinter.messagebox import showinfo,showerror,askyesno
import pymssql
from sqlalchemy import true
from tkcalendar import *
from PIL import Image,ImageTk
def main():
  
  #主視窗
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
  #
  #註冊函數
  def signup(): 
      #把資料插入資料庫
      def insert():
      # Connect to the database
      # create a pymysql.connect object 'connection'
           iconn = pymssql.connect(server='127.0.0.1',
                                 user='sa',
                                 password='password',
                                 database='mis')
           icur=iconn.cursor(as_dict=True)                     
           icur.execute('INSERT INTO members_data VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(     
                 nact, 
                 npwd,
                 nadd , 
                 nemail, 
                 ntel, 
                 nname,   
                 nbirth)
             )
           iconn.commit()
           icur.close()
           iconn.close() 
           showinfo('歡迎','註冊成功') 
           window_signup.destroy()                     

    
     #點擊註冊   
      def signup_cilck():
          #獲取輸入資料
          global nact,npwd,npwdf,nadd,nemail,ntel,nname,nbirth
          nact=new_act.get()
          npwd=new_pwd.get()
          npwdf=new_pwd_confirm.get()
          nadd=new_add.get()
          nemail=new_email.get()
          ntel=new_tel.get()
          nname=new_name.get()
         
          conn = pymssql.connect(server='127.0.0.1',
                             user='sa',
                             password='password',
                             database='mis')
          cur = conn.cursor() 
          try:
             nbirth=ecal.get()
          except NameError: 
             showerror('錯誤','資料不得為空') 
          else:
              while True: 
                  sql = "SELECT * FROM members_data WHERE member_account = '"+ nact +"'"
                  cur.execute(sql)
                  data = cur.fetchone()
                  if not data == None:
                     showerror('錯誤','此帳號已被註冊!!!')
                     break
                  if npwd !=npwdf :
                     showerror('錯誤','密碼前後不一致')
                     break
                  if nact=="" or npwd=="" or nadd=="" or nemail =="" or ntel=="" or nname=="" :
                     showerror('錯誤','資料不得為空') 
                     break
                  cur.close()
                  conn.close()
                  insert()
                  break          
  
             
        
          #.        
      #點擊獲取日期 
      def cal_cilck():
          global ecal
          window_cal=Toplevel(window_signup)
          window_cal.title("calendar")
          window_cal.geometry("350x300")
          cal=Calendar(window_cal, selectmode='day', year=2000 ,mouth=1,day=1)
          cal.pack(pady=20)
          def grab_date():
              newday =StringVar(window_signup) 
              newday.set(cal.get_date())  
              ecal.config(textvariable=newday)
              window_cal.destroy()
          bcal=Button(window_cal, text='確認' ,command=grab_date)        
          bcal.pack(pady=20)  
          ecal=Entry(window_signup,textvariable=new_birth) 
          ecal.place(x=150,y=290)
          window_cal.mainloop() 
      #新建註冊介面
      window_signup= Toplevel(window)
      window_signup.geometry('380x400')
      window_signup.title('註冊')
      #帳號變數及標籤、輸入框
      new_act= StringVar()
      Label(window_signup,text='帳號：').place(x=30,y=10)
      Entry(window_signup,textvariable=new_act).place(x=150,y=10)
      #密碼變數及標籤、輸入框
      new_pwd= StringVar()
      Label(window_signup,text='輸入密碼：').place(x=30,y=50)
      Entry(window_signup,textvariable=new_pwd,show='*').place(x=150,y=50)    
      #重複密碼變數及標籤、輸入框
      new_pwd_confirm= StringVar()
      Label(window_signup,text='確認密碼：').place(x=30,y=90)
      Entry(window_signup,textvariable=new_pwd_confirm,show='*').place(x=150,y=90) 
      #地址
      new_add= StringVar()
      Label(window_signup,text='地址：').place(x=30,y=130)
      Entry(window_signup,textvariable=new_add).place(x=150,y=130)
      #email變數及標籤、輸入框
      new_email= StringVar()
      Label(window_signup,text='email：').place(x=30,y=170)
      Entry(window_signup,textvariable=new_email).place(x=150,y=170)
      #電話變數及標籤、輸入框
      new_tel= StringVar()
      Label(window_signup,text='電話：').place(x=30,y=210)
      Entry(window_signup,textvariable=new_tel).place(x=150,y=210)
      #名稱變數及標籤、輸入框
      new_name= StringVar()
      Label(window_signup,text='名稱：').place(x=30,y=250)
      Entry(window_signup,textvariable=new_name).place(x=150,y=250)
      #生日 變數及標籤、輸入框
      new_birth= StringVar()
      Label(window_signup,text='生日：').place(x=30,y=290)
     
      
      #獲取日期按鈕
      Button(window_signup, text='獲取日期' ,command=cal_cilck).place(x=300,y=290,width=60)
      #確認註冊按鈕
      bt_confirm_sign_up= Button(window_signup,text='確認註冊',
                                   command=signup_cilck)
      bt_confirm_sign_up.place(x=100,y=330 ,width=100)   
    
  #登入的函數
  def login():
      member_act=var_member_act.get()
      member_pwd=var_member_pwd.get()
    #   from datetime import datetime
    #   current_time=datetime.today().replace(microsecond=0) 
      conn = pymssql.connect(server='127.0.0.1',
                             user='sa',
                             password='password',
                             database='mis')
      cur = conn.cursor() 
      while True:
            # if member_act=='' or member_pwd=='' :
            #         showerror('警告','帳號或密碼為空')
            #         break 
            sqlact = "SELECT * FROM members_data WHERE member_account = '"+ member_act +"'"
            cur.execute(sqlact)       
            actdata = cur.fetchone()
            sqlpwd = "SELECT * FROM members_data WHERE member_password = '"+ member_pwd +"'"
            cur.execute(sqlpwd)       
            pwddata = cur.fetchone() 
            if  not actdata ==None :
                if not pwddata ==None:
                  showinfo('歡迎','登入成功') 
                  window.destroy()
                  break 
                else:
                  showerror('警告','密碼錯誤')
                  break
            is_signup=   askyesno('確認','您還沒有註冊，是否現在註冊')
            if is_signup==True:
                      signup()
                      break
            else:
                      break            
            # for y in data2:
            #     if str(member_act) == y['member_account'] :
            #         if str(member_pwd) ==y['member_password']:
            #             showinfo('歡迎','登入成功')
            #             # cur.execute('INSERT INTO members_record VALUES(\'{}\',\'{}\')'.format(
            #             #     y['member_id'],
            #             #     current_time)
            #             # ) 
            #             conn.commit()
            #             cur.close()
            #             conn.close() 
            #             window.destroy()
            #             break
            #         else:
            #              showerror('警告','密碼錯誤')
            #              break
            #     elif member_act=='' or member_pwd=='' :
            #              showerror('警告','帳號或密碼為空')
            #              break
            #     #不在資料庫中彈出是否註冊的輸入框
            #     else:
                #   is_signup=   askyesno('確認','您還沒有註冊，是否現在註冊')
                #   if is_signup==True:
                #       signup()
                #       break
                #   else:
                #       break                 
  def quit():
      is_quit=askyesno('確認','是否退出?')
      if is_quit==True:
            window.destroy()
      
  #登入 註冊按鈕
  bt_login= Button(window,text='登入',command=login)
  bt_login.place(x=130,y=230)
  bt_logup= Button(window,text='註冊',command=signup)
  bt_logup.place(x=220,y=230)
  bt_logquit= Button(window,text='退出',command=quit)
  bt_logquit.place(x=320,y=230)
  #主迴圈
  window.mainloop()
if __name__ == '__main__':
    main()
