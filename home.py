from tkinter import *
from python_page import python_level_description
from sql_page import sql_level_description
from topic import suggest_improvement

def newinterface1(frame):
        frame1 = Toplevel(frame)
        frame1.title("Assessment Window")
        frame1.geometry("1366x768")
        frame1.configure(bg="#F3F4F6")

        title1 = Label(frame1,text="Skill Readiness Assessment",font=("Segoe UI", 32, "bold"),
            fg="#1F4E79",bg="#EEF2F7"
                      )
        subtitle1 = Label(frame1,text = "Evaluate your technical readiness for IT internships",
                          font = ("Segoe UI", 17),fg = "#212835",bg="#EEF2F7"
                          )
        instruction = Label(frame1,text = "Please select your current skill level in each category below",
                            font = ("Segoe UI", 14),fg = "#212835",bg="#EEF2F7"
                            )
        
        x = IntVar()
        python_card = Frame(frame1,bg="#E5E7EB",width=300,height=160)
        pyskill = Label(python_card,text = "Python Proficiency Level", font=("Segoe UI", 12, "bold"),
                        fg = "#1F2933",bg="#EEF2F7")
        Poption1 = Radiobutton(python_card,text ="Beginner",font=("Segoe UI", 10),fg="#4A4A4A",bg="#EEF2F7",variable = x,value=1)
        Poption2 = Radiobutton(python_card,text ="Intermediate",font=("Segoe UI", 10),fg="#4A4A4A",bg="#EEF2F7",variable = x,value=2)
        Poption3 = Radiobutton(python_card,text ="Advanced",font=("Segoe UI", 10),fg="#4A4A4A",bg="#EEF2F7",variable = x,value=3)

        y = IntVar()
        sql_card = Frame(frame1,bg="#E5E7EB",width=300,height=160)
        sqskill = Label(sql_card,text = "SQL Proficiency Level", font=("Segoe UI", 12, "bold"),
                        fg = "#1F2933",bg="#EEF2F7")
        Soption1 = Radiobutton(sql_card,text ="Beginner",font=("Segoe UI", 10),fg="#4A4A4A",bg="#EEF2F7",variable = y,value=1)
        Soption2 = Radiobutton(sql_card,text ="Intermediate",font=("Segoe UI", 10),fg="#4A4A4A",bg="#EEF2F7",variable = y,value=2)
        Soption3 = Radiobutton(sql_card,text ="Advanced",font=("Segoe UI", 10),fg="#4A4A4A",bg="#EEF2F7",variable = y,value=3)

        z = IntVar()
        problem_card = Frame(frame1,bg="#E5E7EB",width=300,height=160)
        problem_solving = Label(problem_card,text = "Problem Solving Frequency", font=("Segoe UI", 12, "bold"),
                        fg = "#1F2933",bg="#EEF2F7")
        Pro_option1 = Radiobutton(problem_card,text ="Rarely",font=("Segoe UI", 10),fg="#4A4A4A",bg="#EEF2F7",variable = z,value=1)
        Pro_option2 = Radiobutton(problem_card,text ="Sometimes",font=("Segoe UI", 10),fg="#4A4A4A",bg="#EEF2F7",variable = z,value=2)
        Pro_option3 = Radiobutton(problem_card,text ="Regularly",font=("Segoe UI", 10),fg="#4A4A4A",bg="#EEF2F7",variable = z,value=3)

        experience = Label(frame1,text = "Number of Projects Completed", font=("Segoe UI", 12, "bold"),
                        fg = "#1F2933",bg="#EEF2F7")
        exp_entry = Entry(frame1,width=35,font=("Segoe UI", 11),fg="#6B7280", bg="#FFFFFF")

        exp_entry.insert(0, "Enter number of projects...")
        exp_entry.config(highlightbackground="#94A3B8",highlightthickness=1,bd=2)

        def clear_placeholder(event):
               if exp_entry.get() == "Enter number of projects...":
                  exp_entry.delete(0, END)
                  exp_entry.config(fg="#000000")

        def add_placeholder(event):
               if exp_entry.get() == "":
                  exp_entry.insert(0, "Enter number of projects...")
                  exp_entry.config(fg="#9CA3AF")

        exp_entry.bind("<FocusIn>", clear_placeholder)
        exp_entry.bind("<FocusOut>", add_placeholder)

        res = Label(frame1,text="📊 Internship Readiness Result",font=("Segoe UI", 14, "bold"), fg ="#1F2933",bg="#EEF2F7")
        res_output = Label(frame1,text="",font=("Segoe UI", 12, "bold"), fg="#1F2933",bg="#E8F0FE",highlightbackground="#3B82F6"
                ,highlightthickness=2, width = 35,relief="ridge")
        
        def update():
                py = x.get()
                sq = y.get()
                pro_s = z.get()
                num_project = exp_entry.get()
                if num_project == "" or num_project == "Enter number of projects...":
                        num_project = 0
                else:
                        num_project = int(num_project)
                        if num_project<=2:
                                num_project = 1
                        elif num_project<=4:
                                num_project = 2
                        else:
                                num_project = 3
                total = py + sq + pro_s + num_project
                percentage = int((total / 12) * 100)

                strength = python_level_description(py)
                improve = suggest_improvement(py, sq)

                res_output.config(text=f"You are {percentage}% ready\nStrength: {strength}\nImprove: {improve}")

        
        submit1 = Button(frame1,text="Submit Assessment",font=("Segoe UI", 12, "bold"),fg = "#E7FFE8",bg="#4CAF50",command = update)

        title1.place(x=400, y=20)
        subtitle1.place(x=420, y=90)

        instruction.place(x=100, y=150)
        
        python_card.place(x=80,y=200)
        pyskill.place(x=10, y=10)
        Poption1.place(x=10, y=40)
        Poption2.place(x=10, y=70)
        Poption3.place(x=10, y=100)

        sql_card.place(x=480,y=200)
        sqskill.place(x=10, y=10)
        Soption1.place(x=10, y=40)
        Soption2.place(x=10, y=70)
        Soption3.place(x=10, y=100)
         
        problem_card.place(x=880,y=200)
        problem_solving.place(x=10, y=10)
        Pro_option1.place(x=10, y=40)
        Pro_option2.place(x=10, y=70)
        Pro_option3.place(x=10, y=100)

        experience.place(x=100, y=420)
        exp_entry.place(x=100, y=460)

        submit1.place(x=550,y=470)

        res.place(x=100, y=520)
        res_output.place(x=100, y=560)
    

def newinterface2(frame):
        frame2 = Toplevel(frame)
        frame2.title("Skill Roadmap")
        frame2.geometry("1366x768")
        frame2.configure(bg="#F3F4F6")

        title2 = Label(frame2,text="Internship Preparation Roadmap",font=("Segoe UI", 32, "bold"),
            fg="#1F4E79",bg="#EEF2F7"
                      )
        subtitle2 = Label(frame2,text = "Recommended path to strengthen your internship readiness",
                          font = ("Segoe UI",14),fg = "#6B7280",bg="#EEF2F7"
                          )
        intro = Label(frame2,text="Follow these steps to improve your technical skills for internships",
        font=("Segoe UI", 14), fg="#212835", bg="#EEF2F7")

        beginner_card = Frame(frame2,bg="#E5E7EB",width=300,height=160)
        beginner_title = Label(beginner_card,text="Getting Started", font=("Segoe UI", 12, "bold"),
                     fg="#111827",bg="#E5E7EB")

        beginner1 = Label(beginner_card,text="Learn Python basics",font=("Segoe UI", 10),bg="#E5E7EB")
        beginner2 = Label(beginner_card,text="Understand SQL fundamentals",font=("Segoe UI", 10),bg="#E5E7EB")
        beginner3 = Label(beginner_card,text="Build 1 mini project",font=("Segoe UI", 10),bg="#E5E7EB")



        intermediate_card = Frame(frame2,bg="#E5E7EB",width=300,height=160)
        intermediate_title = Label(intermediate_card,text="Skill Development",font=("Segoe UI", 12, "bold"),
                         fg="#111827",bg="#E5E7EB")

        intermediate1 = Label(intermediate_card,text="Practice advanced Python",font=("Segoe UI", 10),bg="#E5E7EB")
        intermediate2 = Label(intermediate_card,text="Learn SQL Joins",font=("Segoe UI", 10),bg="#E5E7EB")
        intermediate3 = Label(intermediate_card,text="Build 2 real projects", font=("Segoe UI", 10),bg="#E5E7EB")

        

        advanced_card = Frame(frame2,bg="#E5E7EB",width=300,height=160)
        advanced_title = Label(advanced_card,text="Internship Ready",font=("Segoe UI", 12, "bold"),
                       fg="#111827",bg="#E5E7EB")

        advanced1 = Label(advanced_card,text="Work on real-world projects",font=("Segoe UI", 10),bg="#E5E7EB")
        advanced2 = Label(advanced_card,text="Optimize database queries",font=("Segoe UI", 10),bg="#E5E7EB")
        advanced3 = Label(advanced_card,text="Practice problem solving",font=("Segoe UI", 10),bg="#E5E7EB")
       
        action = Label(frame2,text="🚀 Start with Step 1 to begin your internship journey",font=("Segoe UI", 12),
                                  fg="#4B5563",bg="#EEF2F7")
        
        final_msg = Label(frame2,text="Consistent practice and project work will improve your readiness", font=("Segoe UI", 14),
                   fg="#1F2937",bg="#EEF2F7")


        title2.place(x=350,y=20)
        subtitle2.place(x=400,y=90)
        intro.place(x=300,y=180)

        beginner_card.place(x=80,y=250)
        beginner_title.place(x=10,y=10)
        beginner1.place(x=10,y=50)
        beginner2.place(x=10,y=80)
        beginner3.place(x=10,y=110)
      
        intermediate_card.place(x=480,y=250)
        intermediate_title.place(x=10,y=10)
        intermediate1.place(x=10,y=50)
        intermediate2.place(x=10,y=80)
        intermediate3.place(x=10,y=110)

        advanced_card.place(x=880,y=250)
        advanced_title.place(x=10,y=10)
        advanced1.place(x=10,y=50)
        advanced2.place(x=10,y=80)
        advanced3.place(x=10,y=110)

        action.place(x=400,y=590)

        final_msg.place(x=300,y=460)