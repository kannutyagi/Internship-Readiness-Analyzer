from tkinter import *
from home import newinterface1
from home import newinterface2

frame = Tk()
frame.geometry("1366x768")
frame.title("Interactive Learning Application | By Kanishka Tyagi")
frame.configure(bg="#F5F7FA")

title = Label(frame,text="Internship Readiness Analyzer",font=("Segoe UI", 36, "bold"), 
                  fg="#1F4E79",bg="#F5F7FA"
             )

subtitle = Label(frame,text="Evaluate your readiness for IT internships based on your skills",
        font=("Segoe UI", 16),fg="#555555",bg="#F5F7FA"
                )
guide = Label(frame,text="Analyze your skills or explore the roadmap to improve your internship readiness",
                  font=("Segoe UI", 12),fg="#4B5563",bg="#F5F7FA")

credit = Label(frame,text="Built by Kanishka Tyagi",font=("Segoe UI", 10),fg="#9CA3AF",
                      bg="#F5F7FA")
A1 = Button(frame,text="Start Assessment",font=("Segoe UI", 16, "bold"),
        fg="white",bg="#3776AB",command = lambda:newinterface1(frame)
           )
S1 = Button(frame,text="View Skill Roadmap",font=("Segoe UI", 16, "bold"),
        fg="white",bg="#4CAF50",command=lambda:newinterface2(frame)
           )


title.place(x=350,y=20)
subtitle.place(x=400,y=90)

guide.place(x=360,y=420)
credit.place(x=580,y=700)

A1.place(x=540, y=250)
S1.place(x=525, y=350)

newinterface1(frame) # it tells home.py that use this window or interface
newinterface2(frame)

frame.mainloop()