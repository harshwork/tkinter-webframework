from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class Swimmingpool:
    def __init__(self,root):
        self.root=root
        self.root.title("CSJM SWIM_POOL MANAGEMENT")
        self.root.geometry("1540x800+0+0")
        bg_color = "sky blue"
        fg_color = "red"
        button_bg_color = "#4CAF50"  # Green
        button_fg_color = "BLUE"
        self.root.configure(bg=bg_color)


        
        self.var_slot=StringVar()
        self.var_name=StringVar()
        self.var_id=StringVar()
        self.var_gender=StringVar()
        self.var_age=StringVar()
        self.var_phone=StringVar()
        self.var_guardiannm=StringVar()
        self.var_guardianph=StringVar()
        self.var_blood=StringVar()
        self.var_membership=StringVar()


        lbltitle = Label(self.root, bd=18, relief=RIDGE, text="CSJM SWIM_POOL MANAGEMENT",
                         fg=fg_color, bg=bg_color, font=("times new roman", 35, "bold"))
        lbltitle.pack(side=TOP, fill=X) 

        
        Dataframe = Frame(self.root, bd=18, relief=RIDGE, bg=bg_color)
        Dataframe.place(x=0, y=100, width=1350, height=330)
        Dataframe = LabelFrame(Dataframe, bd=8, relief=RIDGE, padx=5, font=("times new roman", 20,),
                               text="REGISTRATION", bg=bg_color, fg=fg_color)
        Dataframe.place(x=0, y=5, width=1300, height=280)


        lblSlot=Label(Dataframe,text="SLOT BOOKING:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSlot.grid(row=0,column=0,sticky=W)
        comSlot=ttk.Combobox(Dataframe,textvariable=self.var_slot,font=("times new roman",12,"bold"),width="32")
        comSlot["values"]=("MORNING 5am to 7am","MORNING 7am to 8am","MORNING 8am to 9am","MORNING 9am to 10am","EVENING 4pm to 5pm","EVENING 5pm to 6pm","EVENING 6pm to 7pm")
        comSlot.grid(row=0,column=1)


        lblNAME=Label(Dataframe,text="NAME:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNAME.grid(row=1,column=0,sticky=W)
        txtNAME=Entry(Dataframe,textvariable=self.var_name,font=("times new roman",13,"bold"),width="33")
        txtNAME.grid(row=1,column=1)


        lblID=Label(Dataframe,text="REFERENCE ID:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblID.grid(row=2,column=0,sticky=W)
        txtID=Entry(Dataframe,textvariable=self.var_id,font=("times new roman",13,"bold"),width="33")
        txtID.grid(row=2,column=1)



        lblGENDER=Label(Dataframe,text="GENDER:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblGENDER.grid(row=3,column=0,sticky=W)
        comGENDER=ttk.Combobox(Dataframe,textvariable=self.var_gender,font=("times new roman",12,"bold"),width="32")
        comGENDER["values"]=("male","female")
        comGENDER.grid(row=3,column=1)



        lblage=Label(Dataframe,text="AGE:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblage.grid(row=4,column=0,sticky=W)
        txtage=Entry(Dataframe,textvariable=self.var_age,font=("times new roman",13,"bold"),width="33")
        txtage.grid(row=4,column=1)



        lblPHONE=Label(Dataframe,text="PHONE:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPHONE.grid(row=5,column=0,sticky=W)
        txtPHONE=Entry(Dataframe,textvariable=self.var_phone,font=("times new roman",13,"bold"),width="33")
        txtPHONE.grid(row=5,column=1)



        lblGUARDIAN=Label(Dataframe,text="GUARDIAN NAME:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblGUARDIAN.grid(row=0,column=2,sticky=W)
        txtGUARDIAN=Entry(Dataframe,textvariable=self.var_guardiannm,font=("times new roman",13,"bold"),width="33")
        txtGUARDIAN.grid(row=0,column=3)


        lblGUARDIAN_PH=Label(Dataframe,text="GUARDIAN PHONE No.",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblGUARDIAN_PH.grid(row=1,column=2,sticky=W)
        txtGUARDIAN_PH=Entry(Dataframe,textvariable=self.var_guardianph,font=("times new roman",13,"bold"),width="33")
        txtGUARDIAN_PH.grid(row=1,column=3)


        lblblood=Label(Dataframe,text="BLOOD GROUP:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblblood.grid(row=2,column=2,sticky=W)
        comblood=ttk.Combobox(Dataframe,textvariable=self.var_blood,font=("times new roman",12,"bold"),width="32")
        comblood["values"]=("A+","B+","O+","AB+","A-","B-","O-","AB-")
        comblood.grid(row=2,column=3)

        lblMEMBERSHIP=Label(Dataframe,text="MEMBERSHIP DURATION",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMEMBERSHIP.grid(row=3,column=2,sticky=W)
        comMEMBERSHIP=ttk.Combobox(Dataframe,textvariable=self.var_membership,font=("times new roman",12,"bold"),width="32")
        comMEMBERSHIP["values"]=("1 MONTH","3 MONTH","6 MONTH","12 MONTH")
        comMEMBERSHIP.grid(row=3,column=3)

    
        Buttonframe = Frame(Dataframe, bd=2, relief=RIDGE, bg=bg_color)
        Buttonframe.place(x=1100, y=10, width=180, height=200)

        btn_add = Button(Buttonframe, text="SAVE", command=self.add_data, font=("Helvetica", 12, "bold italic"), width=18, bg='green', fg='white')
        btn_add.grid(row=0, column=0, pady=3)

        btn_update = Button(Buttonframe, text="UPDATE", command=self.update_data, font=("Helvetica", 12, "bold italic"), width=18, bg='blue', fg='white')
        btn_update.grid(row=1, column=0, pady=3)

        btn_delete = Button(Buttonframe, text="DELETE", command=self.delete_data, font=("Helvetica", 12, "bold italic"), width=18, bg='orange', fg='black')
        btn_delete.grid(row=2, column=0, pady=3)

        btn_clear = Button(Buttonframe, text="CLEAR", command=self.reset_data, font=("Helvetica", 12, "bold italic"), width=18, bg='purple', fg='white')
        btn_clear.grid(row=3, column=0, pady=3)

        btn_exit = Button(Buttonframe, text="EXIT", font=("Helvetica", 12, "bold italic"), width=18, bg='red', fg='white')
        btn_exit.grid(row=4, column=0, pady=3)





        Detailsframe=Frame(self.root,bd=10,relief=RIDGE,bg="blue")
        Detailsframe.place(x=0,y=430,width=1350,height=250)

        
        search_frame=LabelFrame(Detailsframe,bg='blue',bd=7,relief=RIDGE,text='Search Tab',font=("times new roman",10,'bold'))
        search_frame.place(x=0,y=2,width=1330,height=60)

        search_by=Label(search_frame,font=("times new roman",10,'bold'),text="search by",fg='sky blue',bg='blue')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=("times new roman",10,'bold'),width=18)
        com_txt_search['value']=("select option","phone","id")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)
        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("times new roman",10,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,command=self.search_data,text="Search",font=("times new roman",10,'bold'),width=18,bg='blue',fg='sky blue')
        btn_search.grid(row=0,column=3,padx=5)

        btn_Showall=Button(search_frame,text="Show all",command=self.fetch_data,font=("times new roman",10,'bold'),width=18,bg='blue',fg='sky blue')
        btn_Showall.grid(row=0,column=4,padx=5)

        
        
        table_frame=Frame(Detailsframe,bd=7,relief=RIDGE,bg="blue")
        table_frame.place(x=0,y=65,width=1330,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.pool_table=ttk.Treeview(table_frame,columns=("name","id","age","gender","slot","phone no","guardiannm","guardianph","blood grp","membership"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.pool_table.xview)
        scroll_y.config(command=self.pool_table.yview)

        self.pool_table.heading("name",text="NAME OF PARTICIPANT")
        self.pool_table.heading("id",text="ID")
        self.pool_table.heading("age",text="AGE")
        self.pool_table.heading("gender",text="GENDER")
        self.pool_table.heading("slot",text="SLOT")
        self.pool_table.heading("phone no",text="PHONE NO")
        self.pool_table.heading("guardiannm",text="GUARDIAN NM")
        self.pool_table.heading("guardianph",text="GUARDIAN PH")
        self.pool_table.heading("blood grp",text="BLOOD GRP")
        self.pool_table.heading("membership",text="MEMBERSHIP")

        self.pool_table["show"]="headings"


        self.pool_table.column("name",width=100)
        self.pool_table.column("id",width=100)
        self.pool_table.column("age",width=100)
        self.pool_table.column("gender",width=100)
        self.pool_table.column("slot",width=100)
        self.pool_table.column("phone no",width=100)
        self.pool_table.column("guardiannm",width=100)
        self.pool_table.column("guardianph",width=100)
        self.pool_table.column("blood grp",width=100)
        self.pool_table.column("membership",width=100)


        self.pool_table.pack(fill=BOTH,expand=1)
        self.pool_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        

    def add_data(self):
        if self.var_slot.get()==""or self.var_id.get()=="":
            messagebox.showerror("error",'Incomplete Data')
        else:
            try:    
                conn=mysql.connector.connect(host='localhost',username='root',password='pasword',database='swimmingdata')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into registered_students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                            self.var_name.get(),
                                            self.var_id.get(),
                                            self.var_age.get(),
                                            self.var_slot.get(),
                                            self.var_gender.get(),
                                            self.var_phone.get(),
                                            self.var_guardiannm.get(),
                                            self.var_guardianph.get(),
                                            self.var_blood.get(),
                                            self.var_membership.get()               ) )   
                
                
                
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student Added",parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'due To:{str(es)}',parent=self.root)
     
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='pasword',database='swimmingdata')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from registered_students')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.pool_table.delete(*self.pool_table.get_children())
            for i in data:
                self.pool_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,EVENINGt=""):
        cursor_row=self.pool_table.focus()
        content=self.pool_table.item(cursor_row)
        data=content['values']
        
        self.var_name.set(data[0])
        self.var_id.set(data[1])
        self.var_age.set(data[2])
        self.var_slot.set(data[3])
        self.var_gender.set(data[4])
        self.var_phone.set(data[5])
        self.var_guardiannm.set(data[6])
        self.var_guardianph.set(data[7])
        self.var_blood.set(data[8])
        self.var_membership.set(data[9]) 

    
    def update_data(self):
           if self.var_slot.get()==""or self.var_id.get()=="":
            messagebox.showerror("error",'Incomplete data')
           else:
               try:
                   update=messagebox.askyesno('update','Data will be Updated')
                   if update>0:    
                       conn=mysql.connector.connect(host='localhost',username='root',password='pasword',database='swimmingdata')
                       my_cursor=conn.cursor()
                       my_cursor.execute('update registered_students set name=%s,age=%s,slot=%s,gender=%s,phone=%s,guardiannm=%s,guardianph=%s,blood=%s,membership=%s where id=%s', (
                           self.var_name.get(),
                           self.var_age.get(),
                           self.var_slot.get(),
                           self.var_gender.get(),
                           self.var_phone.get(),
                           self.var_guardiannm.get(),
                           self.var_guardianph.get(),
                           self.var_blood.get(),
                           self.var_membership.get(),
                           self.var_id.get()              
                       ))
                       
                   else:
                       if not update:
                           return 
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo('success','Updated Sucessfully',parent=self.root)
               except Exception as es:
                   messagebox.showerror('Error',f'due To:{str(es)}',parent=self.root)

    
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("error","Incomplete data")
        else:
            try:
                Delete=messagebox.askyesno("delete", "Data will be Deleted",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='paswword',database='swimmingdata')
                    my_cursor=conn.cursor()
                    sql="delete from registered_students where id=%s"
                    value=(self.var_id.get())
                    my_cursor.execute(sql,(value,))
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete", "detetion Sucess",parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'due To:{str(es)}',parent=self.root)

    
    def reset_data(self):
        self.var_name.set("")
        self.var_id.set("select id")
        self.var_age.set("")
        self.var_slot.set("select slot")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_guardiannm.set("")
        self.var_guardianph.set("")
        self.var_blood.set("select blood group")
        self.var_membership.set("select membership") 
    

    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get=='':
            messagebox.showerror('Error',"Select any Option")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='paswword',database='swimmingdata')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from registered_students where ' + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.pool_table.delete(*self.pool_table.get_children())
                    for i in rows:
                        self.pool_table.insert("",END,values=i)
                    conn.commit
                    conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'due To:{str(es)}',parent=self.root)



                    

if __name__=="__main__":
    root=Tk()
    obj=Swimmingpool(root)
    root.mainloop()

        