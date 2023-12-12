from tkinter import *
from PIL import Image, ImageTk  # pip install pillow 
from tkinter import ttk,messagebox,simpledialog
import sqlite3
import pandas as pd
from datetime import datetime
import requests
class RMS1:
    def __init__(self, new_win):
        self.order_quantity = pd.DataFrame(columns=["Customer Name", "Contact", "Item", "Quantity", "Order Date"])
        self.new_win =new_win
        self.new_win.geometry("1250x450+0+200")
        self.new_win.resizable(False,False)
        self.new_win.focus_force()
        self.new_win.config(background="white")
       
        self.new_win.title(" BAKERY MANAGEMENT SYSTEM")
        #--------- Title _-------------
        l={"Red","Yellow","Violet","MediumSlateBlue","Lime","Aqua","Blue","white","BlanchedAlmond","HoneyDew"}
        for i in l:
         title = Label(self.new_win, text="Manage Customer Details", font=("goudy old style", 20, "bold"),bg="#033055", fg=i)
         title.place(x=15, y=15, width=1215, height=35)
        #------Variables--------------
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_changes=StringVar()
        self.var_eny_order=StringVar()

        # -------------Widgets-----------------
        lbl_cursename=Label(self.new_win,text="Customer Name",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=60)
        lbl_duration=Label(self.new_win,text="Contact Number",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=100)
        lbl_Changes=Label(self.new_win,text="Order Quantity",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=140)
        lbl_Description=Label(self.new_win,text="Order",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=180)
        #--------------- Widgets Enterys---------------
        self.eny_customername=Entry(self.new_win,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_customername.bind("<FocusIn>",lambda e: self.eny_customername.configure(background="BlACK",fg="light yellow"))
        self.eny_customername.bind("<FocusOut>",lambda e: self.eny_customername.configure(background="light yellow",fg="black"))
        self.eny_customername.place(x=200,y=60,width=200)
        self.eny_number=Entry(self.new_win,textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_number.bind("<FocusIn>",lambda e: self.eny_number.configure(background="BlACK",fg="light yellow"))
        self.eny_number.bind("<FocusOut>",lambda e: self.eny_number.configure(background="light yellow",fg="black"))
        self.eny_number.place(x=200,y=100,width=200)
        self.eny_order_quantity=Entry(self.new_win,textvariable=self.var_changes,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_order_quantity.bind("<FocusIn>",lambda e: self.eny_order_quantity.configure(background="BlACK",fg="light yellow"))
        self.eny_order_quantity.bind("<FocusOut>",lambda e: self.eny_order_quantity.configure(background="light yellow",fg="black"))
        self.eny_order_quantity.place(x=200,y=140,width=200)
        
        self.eny_order=Entry(self.new_win,textvariable=self.var_eny_order,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_order.bind("<FocusIn>",lambda e: self.eny_order.configure(background="BlACK",fg="light yellow"))
        self.eny_order.bind("<FocusOut>",lambda e: self.eny_order_quantity.configure(background="light yellow",fg="black"))
        self.eny_order.place(x=200,y=190,width=200,height=30)

        #------------------------Butions------------------------------
        self.btc=Button(self.new_win,text="Save",font=("goudy old style ",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btc.place(x=10,y=390,width=120,height=50)
        self.btu=Button(self.new_win,text="Update",font=("goudy old style ",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.Update)
        self.btu.place(x=150,y=390,width=120,height=50)
        self.btd=Button(self.new_win,text="Delete",font=("goudy old style ",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btd.place(x=290,y=390,width=120,height=50)
        self.btc=Button(self.new_win,text="Clear",font=("goudy old style ",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btc.place(x=435,y=390,width=120,height=50)
        #---------------serach panel------------------------------
        self.var_ser_course=StringVar()
        ser_cursename1=Label(self.new_win,text="Order ID ",font=("goudy old style",15,"bold"),bg="white").place(x=650,y=60)
        ser_cursename=Entry(self.new_win,textvariable=self.var_ser_course,font=("goudy old style",15,"bold"),bg="light yellow")
        ser_cursename.bind("<FocusIn>",lambda e:  ser_cursename.configure(background="BlACK",fg="light yellow"))
        ser_cursename.bind("<FocusOut>",lambda e:  ser_cursename.configure(background="light yellow",fg="black"))
        ser_cursename.place(x=750,y=60,width=150)
        ser_Bution=Button(self.new_win,text="Search",font=("goudy old style ",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.serach)
        ser_Bution.place(x=910,y=60,width=140,height=35)
        save_Bution=Button(self.new_win,text="Download Sheet",font=("goudy old style ",15,"bold"),bg="#D3164C",fg="white",cursor="hand2",command=self.Sheet_excel)
        save_Bution.place(x=1065,y=60,width=165,height=35)
        #-------------------------content-------------------------------
        self.c_Farame=Frame(self.new_win,bd=2,relief=RIDGE)
        self.c_Farame.place(x=650,y=120,width=600,height=300)
        self.scroll_y=Scrollbar(self.c_Farame,orient=VERTICAL)
        self.scroll_x=Scrollbar(self.c_Farame,orient=HORIZONTAL)
        #----------------------table---------------------------
        self.eny_table=ttk.Treeview(self.c_Farame,columns=("Cid","Name","duration","charges","description"),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_x.config(command=self.eny_table.xview)
        self.scroll_y.config(command=self.eny_table.yview)
        self.eny_table.heading("Cid",text="ID")
        self.eny_table.heading("Name",text=" Customer Name")
        self.eny_table.heading("duration",text="Customer Number")
        self.eny_table.heading("charges",text="Order Quantity ")
        self.eny_table.heading("description",text="Order Type")
        self.eny_table["show"]="headings"

        self.eny_table.column("Cid",width=10)
        self.eny_table.column("Name",width=90)
        self.eny_table.column("duration",width=90)
        self.eny_table.column("charges",width=50)
        self.eny_table.column("description",width=70)
        self.eny_table.pack(fill=BOTH,expand=True)
        self.eny_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        #+===============================+++++++++clear data+++++++++++++++++++++++++++++

    def Sheet_excel(self):
        response = messagebox.askquestion("Download Order Sheet", "Do you want to download All data ?", parent=self.new_win)
        if response == "yes":
            for i in self.eny_table.get_children():
                data=list(self.eny_table.item(i,"values"))
                c_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                add_quantity = pd.DataFrame([[data[1], data[2], data[3], data[4], c_date]], 
                                 columns=["Customer Name", "Contact", "Item", "Quantity", "Order Date"])
                self.order_quantity = pd.concat([self.order_quantity, add_quantity], ignore_index=True)
                self.order_quantity.drop_duplicates(subset=None, keep="first", inplace=True)
            path = "BMS.csv"
            self.order_quantity.to_csv(path, index=False)
            messagebox.showinfo("Success","Download csv Successfully",parent=self.new_win)
          
            
             
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("") 
        self.var_changes.set("")
        self.var_ser_course.set("")
        self.var_eny_order.set("")
        self.eny_customername.configure(state=NORMAL)
#---------------------delete data in table------------------------------
    def delete(self):
        # Use a context manager to handle the connection and cursor
        try:
            with sqlite3.connect(database="rms.db") as con:
                cursor = con.cursor()

                # Check if the course name is provided
                if not self.var_course.get():
                    messagebox.showerror("Error", "Course name should be required", parent=self.new_win)
                else:
                    # Check if the course exists
                    cursor.execute("SELECT * FROM course WHERE name=?", (self.var_course.get(),))
                    row = cursor.fetchone()

                    if row is None:
                        messagebox.showerror("Error", "Select a course from the list first", parent=self.new_win)
                    else:
                        # Confirm the deletion
                        op = messagebox.askyesno("Confirm", "Do you want to delete?", parent=self.new_win)

                        if op:
                            # Delete the course
                            cursor.execute("DELETE FROM course WHERE name=?", (self.var_course.get(),))
                            con.commit()
                            
                            # Show a success message
                            messagebox.showinfo("Delete", "Course deleted successfully", parent=self.new_win)

                            # Clear the entry and any other fields
                            self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
#===========================================================get data in table++++++++++++++++
    def get_data(self,ev):
         self.eny_customername.config(state="readonly")
         r=self.eny_table.focus()
         content=self.eny_table.item(r)
         row=content["values"]
         self.var_course.set(row[1])
         self.var_duration.set(row[2])
         self.var_changes.set(row[3])
         self.eny_order.delete('1.0',END)
         self.eny_order.insert(END, row[4])
#-----------------------add data In db----------------------------------------
    def add(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Customer  name should be required",parent=self.new_win)
            else: 
                curser.execute("Select * from course where name=?",(self.var_course.get(),))
                row=curser.fetchone()
                if row != None:
                    messagebox.showerror("Error","Customer name already present",parent=self.new_win)
                else:
                    print(self.var_course.get())
                    print(self.var_duration.get())
                    print(self.var_changes.get())   
                    print(self.eny_order.get())
                    curser.execute("insert into course (name,duration,charges,description)values(?,?,?,?)",(self.var_course.get(),self.var_duration.get(),self.var_changes.get(),self.eny_order.get()))
                    con.commit()
                    messagebox.showinfo("Success","Order Added Successfully",parent=self.new_win)    
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
#------------------------------update---------------------------------------------------------------------
    def Update(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
                curser.execute("Select * from course where name=?",(self.var_course.get(),))
                row=curser.fetchone()
                if row == None:
                    messagebox.showerror("Error","Select Course From list",parent=self.new_win)
                else:
                    curser.execute("update course set duration=?,charges=?,description=? where name=?",
                    (self.var_duration.get(),self.var_changes.get(),self.eny_order.get(),self.var_course.get()))
                    con.commit()
                    messagebox.showinfo("Success","Order  UPDATE Successfully",parent=self.new_win)    
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
#-----------------------Show data in table----------------------------------------      
    def show(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            curser.execute("Select * from course")
            rows=curser.fetchall()
            self.eny_table.delete(*self.eny_table.get_children())
            for row in rows:
                self.eny_table.insert('', END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    #-------------------------Search the data in table --------------------
    def serach(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            curser.execute(f"Select * from course where name LIKE '%{self.var_ser_course.get()}%'")
            rows=curser.fetchall()
            self.eny_table.delete(*self.eny_table.get_children())
            for row in rows:
                self.eny_table.insert('', END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
if __name__ == "__main__":
    ob = Tk()
    obj = RMS1(ob)
    ob.mainloop()
 
