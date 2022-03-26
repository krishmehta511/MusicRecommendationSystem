from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as m
import time
import json

def splash(username):
    splash_win= Tk()

    splash_win.title("Music Recommendation App")

    splash_win.geometry("4500x3000")

    splash_win.overrideredirect(True)

    splash_label= Label(splash_win, text= "Welcome "+username, fg= "green",font= ('Times New Roman', 90))
    splash_label.place(x=400,y=350)
    def mainWin():
        splash_win.destroy()
        win= Tk()
        win.title("Music Recommendation App")
        win.geometry("4500x3000")
        #mood buttons
        print("Hi")
 
    splash_win.after(2000, mainWin)
    def print():
        print("Hi")

    
mainWindow = Tk() #initialize
mainWindow.title("Login")
mainWindow.geometry("4500x3000")
mainWindow.config()


image1 = Image.open("login.jpg")
image1 = image1.resize((1530,795), Image.ANTIALIAS)
test1 = ImageTk.PhotoImage(image1)
label1 = Label(image=test1)
label1.image = test1
label1.place(x = 0, y = 0)
# canvas=Canvas(mainWindow, width=900, height=400)
# canvas.place(x=300,y=200)

#LOGIN PASSWORD CHECK
def login_check():
    fd=open("login.json")
    dct=json.load(fd)
    username1=user_name.get()
    
    username=username1.lower()
    password1=password.get()
    flag=0
    for i in dct.keys():
        if dct[i]["username"]==username and dct[i]["password"]==password1:
            splash(username1)
            user_name.delete(0,END)
            password.delete(0,END)
            flag=1
            break

    else:
        user_name.delete(0,END)
        password.delete(0,END)
        m.showerror(title="Error",message="Username and Password don't match")
        error_label=Label(mainWindow,text="Username and Password don't match",fg="black",font=("Times New Roman", 20, "bold"))
        error_label.place(x=350,y=550)
        login_done = Button(mainWindow,text="Login",bg='#C6E2FF',width=10,font="poppins 12 bold",command= login_check)
        login_done.place(x=450,y=500)
        



#REGISTRATION INFO SAVING
def get_regIngo():
    
    username=user_name1.get()
    username=username.lower()
    password=password1.get()
    age=age2.get()
    gender=gender1.get()
    
    try:
        fd=open("login.json")
        dct=json.load(fd)
        
        dct[len(dct.keys())+1]={"username":username,"password":password,"age":age,"gender":gender}
        print(len(dct.keys()))
    except:
        
        dct={1:{"username":username,"password":password,"age":age,"gender":gender}}
        print(len(dct.keys()))

    ls=json.dumps(dct)
    print(dct)
    fh=open('login.json','w')
    fh.write(ls)
    fh.close()
    m.showinfo(title="Registration Done",message='''Registration successful
Please Login to continue''')
    gender1.delete(0,END)
    age2.delete(0,END)
    password1.delete(0,END)
    user_name1.delete(0,END)

#print(username,password,age,gender)
#LOGIN PART
Login_label=Label(mainWindow,text="LOGIN",fg="red",font="poppins 25 bold")
Login_label.place(x=420,y=170)
Reg_label=Label(mainWindow,text="REGISTER",fg="red",font="poppins 25 bold")
Reg_label.place(x=870,y=170)
username = Label(mainWindow,text="Username:",fg="blue", font="poppins 15 bold")
username.place(x=350,y=270)
user_name=Entry(mainWindow, font="poppins 15 bold")
user_name.place(x=450,y=270)
pass_word = Label(mainWindow,text="Password ",fg="blue", font="poppins 15 bold")
pass_word.place(x=350,y=370)
password=Entry(mainWindow,show="*", font="poppins 15 bold")
password.place(x=450,y=370)
print(password.get())
# canvas.create_line(460,80,460,250, fill="green", width=5)
login_done = Button(mainWindow,text="Login",bg='#C6E2FF',width=10,font="poppins 12 bold",command= login_check)
login_done.place(x=450,y=500)

#REGISTRATION PART 
sign_in = Button(mainWindow,text="Register",bg='#C6E2FF',width=10,font="poppins 12 bold",command=get_regIngo)
sign_in.place(x=900,y=500)
username1 = Label(mainWindow,text="Username:",fg="red", font="poppins 15 bold")
username1.place(x=800,y=270)
user_name1=Entry(mainWindow, font="poppins 15 bold")
user_name1.place(x=900,y=270)
pass_word1 = Label(mainWindow,text="Password ",fg="red", font="poppins 15 bold")
pass_word1.place(x=800,y=320)
password1=Entry(mainWindow, font="poppins 15 bold")
password1.place(x=900,y=320)
age1=Label(mainWindow,text="Age ",fg="red", font="poppins 15 bold")
age1.place(x=800,y=370)
age2=Entry(mainWindow, font="poppins 15 bold")
age2.place(x=900,y=370)
gender=Label(mainWindow,text="Gender ",fg="red", font="poppins 15 bold")
gender.place(x=800,y=420)
gender1=Entry(mainWindow, font="poppins 15 bold")
gender1.place(x=900,y=420)









mainloop()