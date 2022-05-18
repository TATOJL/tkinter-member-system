while True:
    print('Account name:')
    name = input()
    if name != 'a':
        continue
    print('Password, please:')
    password = input()
    if password == 'p':
        break

print('Welcome to Self Learning Success!')
# import pymysql
# conn = pymysql.connect(host='localhost',user='root',passwd='',db='my_python_db',charset='utf8')
# cur = conn.cursor()

# def myindex():
#     print("管理者登入系統")
#     print("*----------------*")
#     print("1.登入")
#     print("2.註冊帳號")
#     print("3.結束程式")
    
# def myindex2():
#     print("請選擇您要做的項目")
#     print("*-------------*")
#     print("1.查詢所有員工的資料")
#     print("11.查詢員工的資料")
#     print("2.修改員工資料")
#     print("3.刪除員工的帳號")
#     print("4.離開")         

# def login_staff():
#     while True:
#         acc=input("請輸入帳號")
#         if acc == "":break   
#         sql_1="SELECT sf_name,sf_account,sf_pwd FROM staff_info WHERE sf_account ='" + acc + "' AND sf_del ='0'"
#         cur.execute(sql_1)
#         staff_acc= cur.fetchone()   
#         print(staff_acc)
#         if (staff_acc==None):
#             print("{}帳號不存在".format(acc))
#             continue
#         mypwd=staff_acc[2]
#         print(mypwd)
#         pwd=input("請輸入密碼")
#         if pwd=="": break  
#         if (mypwd != pwd):
#             print("密碼錯誤")
#         else:
#             print()
#             print("登入成功")
#             print()
#             mymenu2()
#             break   
        
# def get_staff_info():
#     sql = "SELECT sf_pk,sf_name,sf_account,sf_pwd,sf_level,sf_del FROM staff_info WHERE sf_del = 0 "
#     cur.execute(sql)
#     staff_data = cur.fetchall()
#     return staff_data

# def get_staff_info_one():
    
#     choose=input("請輸入您要搜尋的欄位 1. 姓名 2. 帳號")
#     if(choose=='1'):
#         name=input("請輸入姓名:")
#         sql_1="SELECT sf_name,sf_account,sf_pwd FROM staff_info WHERE sf_name ='" + name + "' AND sf_del ='0'"
                
#     else:
#         account=input("請輸入帳號:")
#         sql_1="SELECT sf_name,sf_account,sf_pwd FROM staff_info WHERE sf_account ='" + account + "' AND sf_del ='0'"
        
#     cur.execute(sql_1)
#     staff_data= cur.fetchone()     
#     return staff_data

# def Insert_staff_data():
#     while True:
#         name=input("請輸入姓名")
#         if name == "" : 
#             print("姓名不能為空")
#             continue
            
#         acc=input("請輸入帳號")
#         if acc == "" :
#             print("帳號不能為空")
#             continue
#         sql = "SELECT * FROM staff_info WHERE sf_account = '"+ acc + "'"
#         cur.execute(sql)
#         data = cur.fetchone()
#         if not data == None:
#             print("{}帳號已存在".format(acc))
#             continue
#         pwd = input("請輸入密碼")
#         sql_insert = "INSERT INTO staff_info(sf_name,sf_account,sf_pwd,create_user,update_user)VALUES('"+name+"','"+acc+"','"+pwd+"','"+name+"','"+name+"')" 
#         #print(sql_insert)
#         cur.execute(sql_insert)
#         conn.commit() 
#         print("{}已註冊成功".format(acc))
#         break

# def mymenu2():        
#     while True:
#         myindex2()
#         item=int(input("請輸入您執行的動作"))
#         if item == 1 :
#             staff_info=get_staff_info();
#             print(staff_info)
#         elif item == 11 :
#             info=get_staff_info_one()
#             print(info)
                
#         elif item == 2 :
#             print("edit")
#         elif item == 3 :
#             print("刪除資料")
#         elif item == 4 :
#             break            
    
# def mymenu():
#     while True:
#         myindex() #呼叫起始介面
#         num = int(input("請輸入您要執行的動作"))
#         print()
#         if num == 1 :
#             login_staff()
#         elif num == 2 :
#             Insert_staff_data()
#             print("登入功能")
#         elif num == 3 :
#             break #離開迴圈

# #主程式
# mymenu()
  

# #關閉資料庫連線
# cur.close()
# conn.close()