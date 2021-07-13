from os import makedirs
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import Scale, Tk, Frame, Label, Button
from tkinter.ttk import Notebook,Entry
############welcome########


def Welcome(self):
    root=Tk() 
    root.title("School Management System")
    root.geometry("1550x800")
    root.minsize(200,100)
    root.maxsize(1550,1000)
    image=Image.open("img.jpg")
    image=image.resize((1550,800),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(image)
    label=Label(root,image=photo)
    label.place(x=0,y=0,relheight=1,relwidth=1)
        
    button=Button(root,
                  text="Click here to continue",
                  font=("arial", 20 ,"bold"),
                  fg="white",
                  bg="black",
                  height = 4,
                  width=30,
                  command=lambda : page_1(self) & root.destroy()
                  ).place(x=600,
                          y=700,
                          width=400,
                          height=60,)
    root.mainloop()    
    
#'''''''''''''login window'''''''''''''''
def page_1(Event):
    root1 = Tk()
    root1.title("School Management System")
    root1.geometry("1550x800")
    root1.config(bg = "#EDBB99")
    #""""""login frame""""""'
    f1 = Frame(root1, bg = "white", borderwidth=6, relief=SUNKEN )
    f1.place(x = 450, y = 200, height=450, width=500)
    title = Label( f1, text = "Login Window", font = ("Impact", 30, "bold"), fg="black", bg="white", )
    title.place(x = 120, y =30 )
    desc = Label( f1, text = '"Login according to your status"', font = ("arial", 15, "bold"), fg="black", bg="white", )
    desc.place(x = 90, y =100 )
    button1=Button(f1,
                  text="TEACHER",
                  font=("arial", 19 ,"bold"),
                  fg="black",
                  bg="#8DB7EC",
                  height = 4,
                  width=50,
                  command=lambda : teacher_login(Event) & root1.destroy()
                  ).place(x=40,
                          y=160,
                          width=420,
                          height=40,)
    button2=Button(f1,
                  text="STUDENT",
                  font=("arial", 19 ,"bold"),
                  fg="black",
                  bg="#8DB7EC",
                  height = 4,
                  width=50,
                  command=lambda : student_login(Event) & root1.destroy()
                  ).place(x=40,
                          y=250,
                          width=420,
                          height=40,)
    button3=Button(f1,
                  text="ADMINISTRATOR",
                  font=("arial", 19 ,"bold"),
                  fg="black",
                  bg="#8DB7EC",
                  height = 4,
                  width=50,
                  command=lambda : administrator_login(Event) & root1.destroy()
                  ).place(x=32,
                          y=340,
                          width=420,
                          height=40,)
    back=Button(root1,
                  text="Back",
                  font=("arial", 18 ,"bold"),
                  bg="white",
                  fg="black",
                  height = 1,
                  width=3,
                  command=lambda : Welcome(Event) & root1.destroy()
                  ).place(x=9,
                          y=720,
                          width=100,
                          height=50,)
    


#'''''''''''''teacher_login'''''''''''''


def teacher_login(Event_2):
    root2 = Tk()
    root2.title("Teacher Login")
    root2.geometry("1550x800")
    root2.config(bg = "#EDBB99")
    f1 = Frame(root2, bg = "white", borderwidth=6, relief=SUNKEN )
    f1.place(x = 480, y = 200, height=450, width=500)
    title = Label( f1, text = "Login as a Teacher", font = ("Arial", 25, "bold"), fg="black", bg="white", )
    title.place(x = 100, y =30 )
    back=Button(root2,
                  text="Back",
                  font=("arial", 18 ,"bold"),
                  bg="white",
                  fg="black",
                  height = 1,
                  width=3,
                  command=lambda : page_1(Event_2) & root2.destroy()
                  ).place(x=9,
                          y=720,
                          width=100,
                          height=50,)
    #username
    user_3=Label(f1,text= "Username:" ,font="Time 20 bold").place(x = 90, y =140)
    global username_3
    global password_3
    password_3=Label(f1,text="Password:" ,font="Time 20 bold").place(x = 90, y =210 )
    
    username_3=StringVar()
    password_3=StringVar()
   
    user_3Entry=Entry(f1,font="Time 20 bold", textvariable=username_3).place(x=90, y = 180, width = 350, height = 35)
    password_3Entry=Entry(f1,font="Time 20 bold",textvariable=password_3).place(x=90, y = 260, width = 350, height = 35)
    #login button
    button3=Button(f1,
                  text="LOGIN",
                  font=("arial", 19 ,"bold"),
                  fg="black",
                  bg="#8DB7EC",
                  height = 4,
                  width=50,
                  command=lambda : loggin_2(username_3.get(), password_3.get()) & root2.destroy()
                  ).place(x=50,
                          y=340,
                          width=420,
                          height=40,)

#'''''''''''''student_login'''''''''''''
def student_login(Event_3):
    root3 = Tk()
    root3.title("Student Login")
    root3.geometry("1550x800")
    root3.config(bg = "#EDBB99")
    f1 = Frame(root3, bg = "white", borderwidth=6, relief=SUNKEN )
    f1.place(x = 480, y = 200, height=450, width=500)
    title = Label( f1, text = "Login as a Student", font = ("Arial", 25, "bold"), fg="black", bg="white", )
    title.place(x = 100, y =30 )
    back=Button(root3,
                  text="Back",
                  font=("arial", 18 ,"bold"),
                  bg="white",
                  fg="black",
                  height = 1,
                  width=3,
                  command=lambda : page_1(Event_3) & root3.destroy()
                  ).place(x=9,
                          y=720,
                          width=100,
                          height=50,)
    #username
    user_4=Label(f1,text="Username :",font="Time 20 bold").place(x = 90, y =140)
    pass_4=Label(f1,text="Password :",font="Time 20 bold").place(x = 90, y =210 )
    username_4=StringVar()
    password_4=StringVar()

    user_4Entry=Entry(f1,font="Time 20 bold", textvariable=username_4).place(x=90, y = 180, width = 350, height = 35)
    pass_4Entry=Entry(f1,font="Time 20 bold",textvariable=password_4).place(x=90, y = 260, width = 350, height = 35)
    
    
    #login button
    button3=Button(f1,
                  text="LOGIN",
                  font=("arial", 19 ,"bold"),
                  fg="black",
                  bg="#8DB7EC",
                  height = 4,
                  width=50,
                  command=lambda : loggin_3(username_4.get(), password_4.get()) & root3.destroy()
                  ).place(x=50,
                          y=340,
                          width=420,
                          height=40,)

    
#'''''''''''''administrator_login'''''''''''''
def administrator_login(Event_3):
    root4 = Tk()
    root4.title("Administrator Login")
    root4.geometry("1550x800")
    root4.config(bg = "#EDBB99")
    f1 = Frame(root4, bg = "white", borderwidth=6, relief=SUNKEN )
    f1.place(x = 480, y = 200, height=450, width=500)
    title = Label( f1, text = "Login as an Administrator", font = ("Arial", 25, "bold"), fg="black", bg="white", )
    title.place(x = 30, y =30 )
    back=Button(root4,
                  text="Back",
                  font=("arial", 18 ,"bold"),
                  bg="white",
                  fg="black",
                  height = 1,
                  width=3,
                  command=lambda : page_1(Event_3) & root4.destroy()
                  ).place(x=9,
                          y=720,
                          width=100,
                          height=50,)

    
 #username
    user=Label(f1,text="Username :",font="Time 20 bold").place(x = 90, y =140)
    password=Label(f1,text="Password :",font="Time 20 bold").place(x = 90, y =210 )
    
    username=StringVar()
    password=StringVar()
    
    userEntry=Entry(f1,font="Time 20 bold", textvariable = username).place(x=90, y = 180, width = 350, height = 35)
    passwordEntry=Entry(f1,font="Time 20 bold", textvariable = password).place(x=90, y = 260, width = 350, height = 35)
    button3=Button(f1,
                  text="LOGIN",
                  font=("arial", 19 ,"bold"),
                  fg="black",
                  bg="#8DB7EC",
                  height = 4,
                  width=50,
                  command=lambda :loggin(username.get(), password.get()) & root4.destroy()
                  ).place(x=50,
                          y=340,
                          width=420,
                          height=40,)




 
   

  
       
    

    
    
    
   
#''''''''''administrator_portal''''''''''''''''
def administrator_portal(Event):
    root = Tk()
    root.title("Administrator Portal")
    root.geometry("1550x800")
    root.config(bg = "#EDBB99")
    root.title("Administrator Portal")
    back=Button(root,
                text="Back",
                font=("arial", 18 ,"bold"),
                bg="white",
                fg="black",
                height = 1,
                width=3, 
                command=lambda : administrator_login(Event) & root.destroy()
                ).place(x=9,
                          y=720,
                          width=100,
                          height=50,)
    f2 = Frame(root, bg = "white", relief ="sunken", borderwidth = 4)
    f2.place(x = 480, y = 200, height=450, width=500)
    button1=Button(f2,
                  text="Add teachers",
                  font=("arial", 19 ,"bold"),
                  fg="black",
                  bg="#8DB7EC",
                  height = 4,
                  width=50,
                  command=lambda : add_teachers(Event) & root.destroy()
                  ).place(x=40,
                          y=100,
                          width=420,
                          height=40,)          
    button2=Button(f2,
                  text="add students",
                  font=("arial", 19 ,"bold"),
                  fg="black",
                  bg="#8DB7EC",
                  height = 4,
                  width=50,
                  command=lambda : add_students(Event) & root.destroy()
                  ).place(x=40,
                          y=190,
                          width=420,
                          height=40,)

    button3=Button(f2,
                  text="remove students",
                  font=("arial", 19 ,"bold"),
                  fg="black",
                  bg="#8DB7EC",
                  height = 4,
                  width=50,
                  command=lambda : remove_students(Event) & root.destroy()
                  ).place(x=40,
                          y=280,
                          width=420,
                          height=40,)

    button3=Button(f2,
                  text="remove teachers",
                  font=("arial", 19 ,"bold"),
                  fg="black",
                  bg="#8DB7EC",
                  height = 4,
                  width=50,
                  command=lambda : remove_teachers(Event) & root.destroy()
                  ).place(x=40,
                          y=370,
                          width=420,
                          height=40,)

                      
                      
    #'''''''''Register teachers '''''''''''''''''                 
    def add_teachers(Event):
        root = Tk()
        root.title("add_teachers")
        root.geometry("1550x800")
        root.config(bg = "#EDBB99")
        back=Button(root,
                    text="Back",
                    font=("arial", 18 ,"bold"),
                    bg="white",
                    fg="black",
                    height = 1,
                    width=3, 
                    command=lambda : administrator_portal(Event) & root.destroy()
                    ).place(x=9,
                            y=720,
                            width=100,
                            height=50,)
        f1 = Frame(root, bg = "white", borderwidth=6, relief=SUNKEN )
        f1.place(x = 480, y = 30, height=600, width=500)
        title = Label( f1, text = "Register Teachers", font = ("Arial", 25, "bold"), fg="black", bg="white", )
        title.place(x = 30, y =30 )
        user_2=Label(f1,text="Username :",font="Time 20 bold").place(x = 90, y =140)
        pass_2=Label(f1,text="Password :",font="Time 20 bold").place(x = 90, y =210 )
        
        username_2=StringVar()
        password_2=StringVar()
        
        user_2Entry=Entry(f1,font="Time 20 bold", textvariable = username_2).place(x=90, y = 180, width = 350, height = 35)
        pass_2Entry=Entry(f1,font="Time 20 bold", textvariable = password_2).place(x=90, y = 260, width = 350, height = 35)


        #'''''''''''''phone'''''''''''
        phone_2=Label(f1,text="Phone Number :",font="Time 20 bold").place(x = 90, y =310)
        subject=Label(f1,text="Subject :",font="Time 20 bold").place(x = 90, y =400 )
        
        phone_2=StringVar()
        
        subject=StringVar()
        


        phone_2Entry=Entry(f1,font="Time 20 bold", textvariable = phone_2).place(x=90, y = 370, width = 350, height = 35)
        subjectEntry=Entry(f1,font="Time 20 bold", textvariable = subject).place(x=90, y = 450, width = 350, height = 35)
        button3=Button(f1,
                  text="submit",
                  font=("arial", 19 ,"bold"),
                  fg="black",
                  bg="#8DB7EC",
                  height = 4,
                  width=50,
                  command=lambda :submit_2(username_2.get(), password_2.get(),phone_2.get(), subject.get()) & root.destroy()
                  ).place(x=50,
                          y=500,
                          width=420,
                          height=40,)
        def submit_2(name,password,phone, subject):
            file=open('teacher.txt','a')
            file.write(name+ "," + password+ "," + phone +"," +subject+"\n")
            administrator_portal(Event)
            file.close()

    #'''''''''''Register Students''''''''''''''' 
    def add_students(Event):
        root = Tk()
        root.title("add_teachers")
        root.geometry("1550x800")
        root.config(bg = "#EDBB99")
        root.title("add_students")
        back=Button(root,
                    text="Back",                                                                                                                                         
                    font=("arial", 18 ,"bold"),
                    bg="white",
                    fg="black",
                    height = 1,
                    width=3, 
                    command=lambda : administrator_portal(Event) & root.destroy()
                    ).place(x=9,
                            y=720,
                            width=100,
                            height=50,)
        f1 = Frame(root, bg = "white", borderwidth=6, relief=SUNKEN )
        f1.place(x = 480, y = 30, height=550, width=500)
        title = Label( f1, text = "Register Students", font = ("Arial", 25, "bold"), fg="black", bg="white", )
        title.place(x = 30, y =30 )
        user=Label(f1,text="Username :",font="Time 20 bold").place(x = 90, y =140)
        passwo=Label(f1,text="Password :",font="Time 20 bold").place(x = 90, y =210 )
        
        username=StringVar()
        password=StringVar()
        
        
        userEntry=Entry(f1,font="Time 20 bold", textvariable = username).place(x=90, y = 180, width = 350, height = 35)
        passwoEntry=Entry(f1,font="Time 20 bold", textvariable = password).place(x=90, y = 260, width = 350, height = 35)


        #'''''''''''''phone'''''''''''
        phone=Label(f1,text="Phone Number :",font="Time 20 bold").place(x = 90, y =310)
        roll=Label(f1,text="Roll number :",font="Time 20 bold").place(x = 90, y =400 )
        
        phone=StringVar()
        global roll_no
        roll_no=StringVar()
        


        phoneEntry=Entry(f1,font="Time 20 bold", textvariable = phone).place(x=90, y = 360, width = 350, height = 35)
        roll_noEntry=Entry(f1,font="Time 20 bold", textvariable = roll_no).place(x=90, y = 450, width = 350, height = 35)
        button3=Button(f1,
                  text="submit",
                  font=("arial", 19 ,"bold"),
                  fg="black",
                  bg="#8DB7EC",
                  height = 4,
                  width=50,
                  command=lambda :submit(username.get(), password.get(),phone.get(), roll_no.get()) & root.destroy()
                  ).place(x=50,
                          y=500,
                          width=420,
                          height=40,)
        def submit(name,password,phone, roll_no):
            file=open('student.txt','a')
            file.write(name+ "," + password+","+phone+","+roll_no+"\n")
            administrator_portal(Event)
            file.close()
            

#'''''''''remove_students'''''''
def remove_students(Event):
    root = Tk()
    root.title("remove_students")
    root.geometry("1550x800")
    root.config(bg = "#EDBB99")
    back=Button(root,
                text="Back",                                                                                                                                         
                font=("arial", 18 ,"bold"),
                bg="white",
                fg="black",
                height = 1,
                width=3, 
                command=lambda : administrator_portal(Event) & root.destroy()
                ).place(x=9,
                        y=720,
                        width=100,
                        height=50,)
    f1 = Frame(root, bg = "white", borderwidth=6, relief=SUNKEN )
    f1.place(x = 480, y = 30, height=600, width=500)
    title = Label( f1, text = "Remove Students", font = ("Arial", 25, "bold"), fg="black", bg="white", )
    title.place(x = 30, y =30 )
    user_5=Label(f1,text="Username :",font="Time 20 bold").place(x = 90, y =140)
    pass_5=Label(f1,text="Password :",font="Time 20 bold").place(x = 90, y =210 )
    
    username_5=StringVar()
    password_5=StringVar()
    
    user_5Entry=Entry(f1,font="Time 20 bold", textvariable = username_5).place(x=90, y = 180, width = 350, height = 35)
    pass_5Entry=Entry(f1,font="Time 20 bold", textvariable = password_5).place(x=90, y = 260, width = 350, height = 35)


    #'''''''''''''phone'''''''''''
    phoe_5=Label(f1,text="Phone Number :",font="Time 20 bold").place(x = 90, y =310)
    rol_5=Label(f1,text="Roll number :",font="Time 20 bold").place(x = 90, y =400 )
    
    phone_5=StringVar()
    
    roll_no5=StringVar()
    


    phoe_5Entry=Entry(f1,font="Time 20 bold", textvariable = phone_5).place(x=90, y = 370, width = 350, height = 35)
    rol_5Entry=Entry(f1,font="Time 20 bold", textvariable = roll_no5).place(x=90, y = 450, width = 350, height = 35)
    button8=Button(f1,
                text="submit",
                font=("arial", 19 ,"bold"),
                fg="black",
                bg="#8DB7EC",
                height = 4,
                width=50,
                command=lambda :deleted(username_5.get(), password_5.get(),phone_5.get(), roll_no5.get()) & root.destroy()
                ).place(x=50,
                        y=500,
                        width=420,
                        height=40,)
    def deleted(nam,passwor,phone,roll):
            with open("student.txt", "r") as file_input:
                with open("new_std.txt", "w") as output: 
                    for line in file_input:
                        if line.strip("\n") != nam+","+passwor+","+phone+","+roll:

                            output.write(line)
            administrator_portal(Event)

#'''''''''remove_teachers'''''''
def remove_teachers(Event):
    root = Tk()
    root.title("remove_teachers")
    root.geometry("1550x800")
    root.config(bg = "#EDBB99")
    back=Button(root,
                text="Back",                                                                                                                                         
                font=("arial", 18 ,"bold"),
                bg="white",
                fg="black",
                height = 1,
                width=3, 
                command=lambda : administrator_portal(Event) & root.destroy()
                ).place(x=9,
                        y=720,
                        width=100,
                        height=50,)
    f1 = Frame(root, bg = "white", borderwidth=6, relief=SUNKEN )
    f1.place(x = 480, y = 30, height=600, width=500)
    title = Label( f1, text = "Remove teachers", font = ("Arial", 25, "bold"), fg="black", bg="white", )
    title.place(x = 30, y =30 )
    user_6=Label(f1,text="Username :",font="Time 20 bold").place(x = 90, y =140)
    pass_6=Label(f1,text="Password :",font="Time 20 bold").place(x = 90, y =210 )
    
    username_6=StringVar()
    password_6=StringVar()
    
    user_6Entry=Entry(f1,font="Time 20 bold", textvariable = username_6).place(x=90, y = 180, width = 350, height = 35)
    pass_6Entry=Entry(f1,font="Time 20 bold", textvariable = password_6).place(x=90, y = 260, width = 350, height = 35)


    #'''''''''''''phone'''''''''''
    phoe_6=Label(f1,text="Phone Number :",font="Time 20 bold").place(x = 90, y =310)
    subject_5=Label(f1,text="subject :",font="Time 20 bold").place(x = 90, y =400 )
    
    phone_6=StringVar()
    
    subject_no5=StringVar()
    


    phoe_6Entry=Entry(f1,font="Time 20 bold", textvariable = phone_6).place(x=90, y = 370, width = 350, height = 35)
    subject_5Entry=Entry(f1,font="Time 20 bold", textvariable = subject_no5).place(x=90, y = 450, width = 350, height = 35)
    button8=Button(f1,
                text="submit",
                font=("arial", 19 ,"bold"),
                fg="black",
                bg="#8DB7EC",
                height = 4,
                width=50,
                command=lambda :deleted_2(username_6.get(), password_6.get(),phone_6.get(), subject_no5.get()) & root.destroy()
                ).place(x=50,
                        y=500,
                        width=420,
                        height=40,)
    def deleted_2(nam,passwor,phone,subject):
            with open("teacher.txt", "r") as file_input:
                with open("new_teac.txt", "w") as output: 
                    for line in file_input:
                        if line.strip("\n") != nam+","+passwor+","+phone+","+subject:

                            output.write(line)
           



#''''''''file handle for administrator login'''''''''
def loggin(name,password):
    
    success=False
    file=open('admin_login.txt','r')
    for i in file:
        a,b,c = i.split(",")
        if (a==name and b==password):
            success=True
            break

    file.close()
    if success == True:
        administrator_portal(Event)
    else:
        messagebox.showerror("Error", "Incorrect username or password")
        administrator_login()
        
    
#''''''''file handle for teacher login'''''''''
def loggin_2(name,password):
    
    success=False
    file=open('teacher.txt','r')
    for i in file:
        a,b,c,d = i.strip().split(",")
        if (a==name and b==password):
            success=True
            

    
    
            root4 = Tk()
            

            root4.title("teacher details")
            root4.geometry("1550x800")
            root4.config(bg = "#EDBB99")
            back=Button(root4,
                        text="Back",
                        font=("arial", 18 ,"bold"),
                        bg="white",
                        fg="black",
                        height = 1,
                        width=3, 
                        command=lambda : teacher_login(Event) & root4.destroy()
                        ).place(x=9,
                                y=720,
                                width=100,
                                height=50,)
            heading= Label(root4, text = 'Teacher Details', font = ("arial", 30, "bold") )
            heading.place(x=0,y=0,height=100,width=1550)
            f2 = Frame(root4, bg = "white", relief ="sunken", borderwidth = 4)
            f2.place(x = 500, y = 180, height=530, width=500)
            L1 = Label(f2, text = 'name :',bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=0, column= 0)
            L2 = Label(f2, text = 'password :',bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=1, column= 0)
            L3 = Label(f2, text = 'phone :',bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=2, column= 0)
            L4 = Label(f2, text = 'subject :',bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=3, column= 0)
            # ------------------------
            L11 = Label(f2, text = a ,bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=0, column= 1)
            L22 = Label(f2, text = b,bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=1, column= 1)
            L33 = Label(f2, text = c,bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=2, column= 1)
            L44 = Label(f2, text = d,bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=3, column= 1)
            button2=Button(root4,
                  text="Student marks",
                  font=("arial", 19 ,"bold"),
                  fg="black",
                  bg="#8DB7EC",
                  height = 4,
                  width=50,
                  command=lambda : student_marks (Event) & root4.destroy()
                  ).place(x=1200,
                          y=720,
                          width=350,
                          height=70,)
            button2=Button(root4,
                  text="Student details",
                  font=("arial", 19 ,"bold"),
                  fg="black",
                  bg="#8DB7EC",
                  height = 4,
                  width=50,
                  command=lambda : student_details (Event) & root4.destroy()
                  ).place(x=1200,
                          y=630,
                          width=350,
                          height=70,)
                                                  
            break

       
   

       


#''''''''file handle for students login'''''''''
def loggin_3(name,password):
    success=False
    file=open('student.txt','r')
    for i in file:
        a,b,c,d = i.strip().split(",")
        if (a==name and b==password):
            success=True
    
            root4 = Tk()
            root4.title("student details")
            root4.geometry("1550x800")
            root4.config(bg = "#EDBB99")
            back=Button(root4,
                        text="Back",
                        font=("arial", 18 ,"bold"),
                        bg="white",
                        fg="black",
                        height = 1,
                        width=3, 
                        command=lambda : teacher_login(Event) & root4.destroy()
                        ).place(x=9,
                                y=720,
                                width=100,
                                height=50,)
            heading= Label(root4, text = 'Student Details', font = ("arial", 30, "bold") )
            heading.place(x=0,y=0,height=100,width=1550)
            f2 = Frame(root4, bg = "white", relief ="sunken", borderwidth = 4)
            f2.place(x = 500, y = 180, height=530, width=500)
            L1 = Label(f2, text = 'name :',bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=0, column= 0)
            L2 = Label(f2, text = 'password :',bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=1, column= 0)
            L3 = Label(f2, text = 'phone :',bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=2, column= 0)
            L4 = Label(f2, text = 'roll number :',bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=3, column= 0)
            # ------------------------
            L11 = Label(f2, text = a ,bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=0, column= 1)
            L22 = Label(f2, text = b,bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=1, column= 1)
            L33 = Label(f2, text = c,bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=2, column= 1)
            L44 = Label(f2, text = d,bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=3, column= 1)
            
                                                  
            break
        
   

        
    


#''''''''''''''''''''''student marks'''''''''''
def student_marks(Event):
    root4 = Tk()
    root4.title("student marks")
    root4.geometry("1550x800")
    root4.config(bg = "#EDBB99")
    back=Button(root4,
                  text="Back",
                  font=("arial", 18 ,"bold"),
                  bg="white",
                  fg="black",
                  height = 1,
                  width=3, 
                  command=lambda : teacher_login(Event) & root4.destroy()
                  ).place(x=9,
                          y=720,
                          width=100,
                          height=50,)
    f1 = Frame(root4, bg = "white", borderwidth=6, relief=SUNKEN )
    f1.place(x = 480, y = 30, height=270, width=500)
    title = Label( f1, text = "enter roll number", font = ("Arial", 25, "bold"), fg="black", bg="white", )

    title.place(x = 30, y =30 )
    user=Label(f1,text="roll_no :",font="Time 20 bold").place(x = 90, y =140)
    roll_no=StringVar()
    userEntry=Entry(f1,font="Time 20 bold", textvariable=roll_no).place(x=90, y = 180, width = 350, height = 35)
    button3=Button(f1,
                  text="edit marks",
                  font=("arial", 19 ,"bold"),
                  fg="black",
                  bg="#8DB7EC",
                  height = 4,
                  width=50,
                  command=lambda :get_roll_no(roll_no.get()) & root4.destroy()
                  ).place(x=50,
                          y=230,
                          width=420,
                          height=40)
def get_roll_no(no):
    success=False
    file=open('student.txt','r')
    for i in file:

       
        a,b,c,d = i.strip().split(",")
        
        if (no==c):
            success=True
            break

    file.close()
    if success == True:
        edit_marks(Event)
    else:
        messagebox.showerror("Error", "roll no doesn't exist")
        student_marks(Event)
    


def edit_marks(Event):
    root4 = Tk()
    root4.title("edit marks")
    root4.geometry("1550x800")
    root4.config(bg = "#EDBB99")
    back=Button(root4,
                  text="Back",
                  font=("arial", 18 ,"bold"),  
                  bg="white",
                  fg="black",
                  height = 1,
                  width=3, 
                  command=lambda : teacher_login(Event) & root4.destroy()
                  ).place(x=9,
                          y=720,
                          width=100,
                          height=50,)

    f1 = Frame(root4, bg = "white", borderwidth=6, relief=SUNKEN )
    f1.place(x = 480, y = 30, height=700, width=500)
    title = Label( f1, text = "Enter Marks", font = ("Arial", 25, "bold"), fg="black", bg="white", )
    title.place(x = 30, y =30 )
    phy_2=Label(f1,text="physics :",font="Time 20 bold").place(x = 90, y =140)
    chem_2=Label(f1,text="chemistry :",font="Time 20 bold").place(x = 90, y =210 )
    
    physics_2=StringVar()
    chemistry_2=StringVar()
    
    phy_2Entry=Entry(f1,font="Time 20 bold", textvariable = physics_2).place(x=90, y = 180, width = 350, height = 35)
    chem_2Entry=Entry(f1,font="Time 20 bold", textvariable = chemistry_2).place(x=90, y = 260, width = 350, height = 35)


    
    maths_2=Label(f1,text="mathematics :",font="Time 20 bold").place(x = 90, y =310)
    comp=Label(f1,text="computer :",font="Time 20 bold").place(x = 90, y =400 )
    
    mathematics_2=StringVar()
    
    computer=StringVar()
    


    maths_2Entry=Entry(f1,font="Time 20 bold", textvariable = mathematics_2).place(x=90, y = 370, width = 350, height = 35)
    compEntry=Entry(f1,font="Time 20 bold", textvariable = computer).place(x=90, y = 450, width = 350, height = 35)
    button3=Button(f1,
                text="submit",
                font=("arial", 19 ,"bold"),
                fg="black",
                bg="#8DB7EC",
                height = 4,
                width=50,
                command=lambda :marks_2(physics_2.get(), chemistry_2.get(),mathematics_2.get(), computer.get()) & root4.destroy()
                ).place(x=50,
                        y=500,
                        width=420,
                        height=40,)
    def marks_2(phy,chem,maths, comp):
        file=open('marks.txt','a')
        file.write(phy+ "," + chem+ "," + maths +"," +comp+"\n")
        student_marks(Event)
        file.close()
    


#''''''''student_details'''''''''''''


def student_details(Event):
    root4 = Tk()
    root4.title("student details")
    root4.geometry("1550x800")
    root4.config(bg = "#EDBB99")
    file=open('student.txt','r')
    f2 = Frame(root4, bg = "white", relief ="sunken", borderwidth = 4)
    f2.place(x = 500, y = 180, height=530, width=500)
    
    r=0
    co=1
    m=1
    
    f2 = Frame(root4, bg = "white", relief ="sunken", borderwidth = 4)
    f2.place(x = 500, y = 180, height=530, width=500)
    for i in file:
        n = str(m)
        L1 = Label(f2, text = 'student:'+ n ,bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=r, column= 0)
        
        a,b,c,d = i.strip().split(",")
        L11 = Label(f2, text = a,bg="white",font="Time 25 bold", padx=10,pady=10).grid(row=r, column=co)
        r+=1
        m+=1
    

  



APP=Welcome(Tk)

    
    
    

