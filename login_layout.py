import tkinter as tk
from tkinter.messagebox import showinfo 
def main():
    def login():
          showinfo(title="登入成功", message="登入成功 ", )
  
    
    
    win = tk.Tk()
    win.title("會員登入系統".center(100))
    win.geometry("500x200")
    win.resizable(0,0)
    alabel=tk.Label(text="帳號:")
    plabel=tk.Label(text="密碼:")
    btnLogin=tk.Button(text="登入", command= login)
    btnRegister=tk.Button(text="註冊"  )
    aentry=tk.Entry()
    pentry=tk.Entry()
     #
    alabel.grid(row=0,column=0 , ipadx=120, pady=30) 
    plabel.grid(row=1,column=0, pady=10)
    aentry.grid(row=0,column=1)
    pentry.grid(row=1,column=1)
    btnLogin.grid(row=2,column=0, pady=10)
    btnRegister.grid(row=2,column=1)
    #
    win.mainloop()
if __name__ =='__main__':
    main()