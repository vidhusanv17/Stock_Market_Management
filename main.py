from tkinter import *
import codecs
from tkinter import ttk
import mysql.connector as s
from tkinter import messagebox
import pickle as p


#Colour of the empty labels
colour='cyan'

f_l_c='slateblue'

wd=Tk()
wd.geometry('1680x1050')

f=Frame(wd,height=500,width=700,bg='purple',bd=40)
f.place(relx=0.5,rely=0.4,anchor=CENTER)

c='purple'
emp1=Label(f,bg=c)
emp1.grid(row=1,column=0)
emp2=Label(f,bg=c)
emp2.grid(row=3,column=0)
emp3=Label(f,bg=c)
emp3.grid(row=7,column=0)
emp4=Label(f,bg=c)
emp4.grid(row=2,column=0)
emp5=Label(f,bg=c)
emp5.grid(row=8,column=0)

l_wel=Label(f,text='WELCOME TO PRODUCTS MANAGER',font=('bold',40),bg=f_l_c)
l_wel.grid(row=0,column=0)

l_do=Label(f,text='Do you want to create an account?',font=('bold',20),bg=f_l_c)
l_do.grid(row=3,column=0)

"""CREATION OF ACCOUNT"""

def acc_creation():
   
    f.place_forget()
   
    f_reply=Frame(wd,bg='cyan',bd=35)
    f_reply.place(relx=0.5,rely=0.4,anchor=CENTER)
   
    emp6=Label(f_reply,bg=colour)
    emp6.grid(row=0,column=0,columnspan=2)
   
    emp7=Label(f_reply,bg=colour)
    emp7.grid(row=1,column=0,columnspan=2)
   
    emp8=Label(f_reply,bg=colour)
    emp8.grid(row=3,column=0,columnspan=2)
   
    emp9=Label(f_reply,bg=colour)
    emp9.grid(row=5,column=0,columnspan=2)
   
    emp10=Label(f_reply,bg=colour)
    emp10.grid(row=7,column=0,columnspan=2)
   
    #LABELS AND ENTRY BOXES
    username_Label=Label(f_reply,text='Username',bg='slateblue',font=('bold',20))
    username_Label.grid(row=2,column=0)
   
    username_box=Entry(f_reply)
    username_box.grid(row=2,column=1)
   
    #emailid_Label=Label(f_reply,text='Email id',bg='yellow',font=('bold',20))
    #emailid_Label.grid(row=4,column=0)
   
    emailid_box=Entry(f_reply)
    emailid_box.insert(0,'123d')
    #emailid_box.grid(row=4,column=1)
   
    pass_Label=Label(f_reply,text='Password',bg='slateblue',font=('bold',20))
    pass_Label.grid(row=6,column=0)
   
    pass_box=Entry(f_reply,show="*")
    pass_box.grid(row=6,column=1)
   
    def acc_create():
       
        u=str(username_box.get()).strip()
        e=str(emailid_box.get()).strip()
        p=str(pass_box.get()).strip()
        if u=='':
            messagebox.showinfo('','Please enter a valid username')
            return
        elif (u.replace('_','')).isalnum() is False:
            messagebox.showinfo('','Enter username without special characters other than \"_\"')
            return
        elif e=='':
            messagebox.showinfo('','Please enter a valid email id')
            return
        elif p=='':
            messagebox.showinfo('','Please enter a valid password')
            return
       
        con=s.connect(host="127.0.0.1",user="root",passwd="",database="tkinter")
        cursor=con.cursor()
        #checking whether username already exists or not
        cursor.execute("create table if not exists acc (username varchar(25),emailid varchar(25),password varchar(25))")
        cursor.execute('select * from acc where username like "{}";'.format(u))
        rs=cursor.fetchall()
        if any(rs)==False:
            cursor.execute('insert into acc values("{}","{}","{}")'.format(u,e,p))
            cursor.execute('commit;')
            messagebox.showinfo('','Account successfully created')
            #STORING THE ACCOUNT NAME THAT IS TO BE AUTO SIGNED IN NEXT TIME
            cursor.execute('create table if not exists cur_user(username varchar(25));')
            cursor.execute('delete from cur_user;')
            cursor.execute('insert into cur_user values("{}");'.format(u))
            cursor.execute('commit;')
        else:
            messagebox.showinfo('','Please choose a different username')
            return
        f_reply.destroy()
        f.place(relx=0.5,rely=0.4,anchor=CENTER)
    create_account_box=Button(f_reply,text='Create Account',font=('bold',20),bg='red',command=acc_create)
    create_account_box.grid(row=8,column=1,sticky=SE)
   
    def close_reply_f():
        f_reply.after(0,f_reply.destroy())
        f.place(relx=0.5,rely=0.4,anchor=CENTER)
   
    close_button=Button(f_reply,text='X',bg='red',command=close_reply_f)
    close_button.place(relx=0.98,rely=0.03,anchor=NE)

create_acc=Button(f,text='Create an account',font=('bold',20),command=acc_creation,bg=f_l_c)
create_acc.grid(row=6,column=0)

def signin():
    f.place_forget()
   
    s_f=Frame(wd,bg='cyan',bd=10)
    s_f.place(relx=0.5,rely=0.4,anchor=CENTER)
   
    emp11=Label(s_f,bg=colour)
    emp11.grid(row=0,column=0,columnspan=2)
   
    emp12=Label(s_f,bg=colour)
    emp12.grid(row=1,column=0,columnspan=2)
   
    username_Label=Label(s_f,text='Username',font=('bold',20),bg='slateblue')
    username_Label.grid(row=2,column=0)
   
    username_box=Entry(s_f)
    username_box.grid(row=2,column=1)
   
    emp13=Label(s_f,bg=colour)
    emp13.grid(row=3,column=0,columnspan=2)
   
    pass_Label=Label(s_f,text='Password',font=('bold',20),bg='slateblue')
    pass_Label.grid(row=4,column=0)
     
    pass_box=Entry(s_f,show="*")
    pass_box.grid(row=4,column=1)
       
    emp14=Label(s_f,bg=colour)
    emp14.grid(row=5,column=0,columnspan=2)
       
    def close_s_f():
        s_f.place_forget()
        f.place(relx=0.5,rely=0.4,anchor=CENTER)
       
    def sign():
        global u
        u=str(username_box.get()).strip()
        p=str(pass_box.get()).strip()
        if u=='':
            messagebox.showinfo('','Username required')
            return
        con=s.connect(host="127.0.0.1",user="root",passwd="",database="tkinter")
        cursor=con.cursor()
        cursor.execute("create table if not exists acc (username varchar(25),emailid varchar(25),password varchar(25));")
        cursor.execute('select password from acc where username like "{}";'.format(u))
        rs=cursor.fetchone()
        if bool(rs)==False:
            messagebox.showinfo('','Please enter proper username')
            return
        if p==rs[0:1][0]:
            messagebox.showinfo('',f'Welcome {u}!\n😊')
            cursor.execute('create table if not exists cur_user(username varchar(25));')
            cursor.execute('delete from cur_user;')
            cursor.execute('insert into cur_user values("{}");'.format(u))
            cursor.execute('commit;')
            s_f.place_forget()
            sec_page()#  <<<<<<<----------
        else:
            messagebox.showinfo('','Please recheck your password')
            return
       
    sign_in_b=Button(s_f,text='Sign in',font=('bold',20),command=sign)
    sign_in_b.grid(row=6,column=1,sticky=SE)
   
    close_b=Button(s_f,text='X',bg='red',command=close_s_f)
    close_b.place(relx=0.98,rely=0.03,anchor=NE)
   
l_al=Label(f,text='Already have an account?',font=('bold',20),bg=f_l_c)
l_al.grid(row=9,column=0)
   
B_signin=Button(f,text='SIGN IN',font=('bold',20),command=signin)
B_signin.grid(row=10,column=0)

def sec_page():
   
    global cell_count
    cell_count=1
   
    f=open('shopdat.dat','rb')
    global u,d
    d=p.load(f)
    if u in d:
        f.close()
    else:
        f.close()
        d[u]=[]
        f=open('shopdat.dat','wb')
        p.dump(d,f)
        f.close()
       
    try:
        parameter_list=d[u][-1]
    except:
        parameter_list=[]
    print('**parameter_list@#@:\n\n',parameter_list)
    #$$$$$$$
    global gen_font_size,default_text,inter_cell_space,cell_bg_color,screen_border_color,lower_temp_border_colour,cell_border_colour,S_BASE,lines_to_display,cell_text_colour,gen_font_color,upper_colour,lower_colour,cell_holder_colour
   
    if parameter_list==[] or (type(parameter_list) is str):
        gen_font_size=25
        inter_cell_space=50
        default_text='Product Name:\nPrice                  :\nQty                     :\nOffer                  :\nMfd Date          :\nExp Date           :\nBatch No          :\nDesp                  :'
        lines_to_display=8
        cell_text_colour='black'
        cell_bg_color='white'
        gen_font_color='black'
        upper_colour='white'
        lower_colour='blue'
        cell_holder_colour='yellow'
        cell_border_colour='red'
        lower_temp_border_colour='maroon'
        screen_border_color='black'
    else:

        gen_font_size=parameter_list['gen_font_size']
        inter_cell_space=parameter_list['inter_cell_space']
        default_text=parameter_list['default_text']
        lines_to_display=parameter_list['lines_to_display']
        cell_text_colour=parameter_list['cell_text_colour']
        cell_bg_color=parameter_list['cell_bg_color']
        gen_font_color=parameter_list['gen_font_color']
        upper_colour=parameter_list['upper_color']
        lower_colour=parameter_list['lower_color']
        cell_holder_colour=parameter_list['cell_holder_color']
        cell_border_colour=parameter_list['cell_border_colour']
        lower_temp_border_colour=parameter_list['lower_temp_border_colour']
        screen_border_color=parameter_list['screen_border_color']
       
    #$$$$$$$
   
    S_BASE=Frame(wd,bg=screen_border_color)
    S_BASE.pack(fill=BOTH,expand=1)
   
    #___UPPER HALF______
    s_page_u=Frame(S_BASE,height=20,bg=upper_colour)
    s_page_u.pack(fill=X,padx=10,pady=10)
   
    settings_b=Button(s_page_u,text=' SETTINGS ',fg=gen_font_color,font=(('bold'),gen_font_size),command=lambda:third_page())
    settings_b.grid(row=0,column=0,padx=5,pady=10)
   
    search_box=Text(s_page_u,height=1,width=70,font=(('bold'),gen_font_size))
    search_box.grid(row=1,column=1)
    search_box.config(highlightbackground = "black", highlightcolor= "black")
   
   
   
   
    #___________
    s_page_d=Frame(S_BASE,bg=lower_temp_border_colour)
    s_page_d.pack(fill=BOTH,expand=1,padx=10,pady=10)
   
    #1)Create canvas
   
    canvas=Canvas(s_page_d,bg=lower_colour)
    canvas.pack(side=LEFT,fill=BOTH,expand=1,padx=10,pady=10)
   
    #2)Add scrollbar to the canvas
    global sb
    sb=ttk.Scrollbar(s_page_d,orient=VERTICAL,command=canvas.yview)
    sb.pack(side=RIGHT,fill=Y)
   
    #3)Configure the canvas
   
    canvas.configure(yscrollcommand=sb.set)
    canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion=canvas.bbox('all')))
   
    #4)Main frame inside the canvas
   
    """{<<<<<~^~^~^~>>>>>}"""
   
    def place():
        f=open('shopdat.dat','rb')
        global d,u,s_page_Main
        s_page_Main=Frame(canvas,bg=cell_holder_colour)
        canvas.create_window((180,50),window=s_page_Main,anchor='nw')
        d=p.load(f)
        f.close()
        if d[u]!=[] and type(d[u][-1]) is not str:
            d[u]=d[u][0:-1]
        global cell_count
        for thing in d[u]:
            #print(thing)
            exec(f'''global cell{cell_count}
cell{cell_count}=Text(s_page_Main,width=80,height=lines_to_display,bg=cell_bg_color,font=(('bold'),gen_font_size),fg=cell_text_colour,highlightbackground = cell_border_colour, highlightcolor= cell_border_colour)
cell{cell_count}.insert(1.0,'{thing}')
cell{cell_count}.grid(pady=inter_cell_space,padx=20)''')
            cell_count+=1
    place()
   
    global add_b
       
    def add():
        global cell_count,s_page_Main,gen_font_size,default_text,inter_cell_space,lines_to_display
        exec(f'''global cell{cell_count}
cell{cell_count}=Text(s_page_Main,width=80,height=lines_to_display,bg=cell_bg_color,font=(('bold'),gen_font_size),fg=cell_text_colour,highlightbackground = cell_border_colour, highlightcolor= cell_border_colour)
cell{cell_count}.insert(1.0,default_text)
cell{cell_count}.grid(padx=20,pady=inter_cell_space)''')
        cell_count+=1
        wd.attributes(('-fullscreen'),True)

        #wd.attributes(('-fullscreen'),True)
    add_b=Button(s_page_u,text=' Add ',fg=gen_font_color,command=lambda:add(),font=(('bold'),gen_font_size))
    add_b.grid(row=2,column=1,columnspan=2,pady=20)
   
   
    def save_change():
        l=[]
        global cell_count,s_page_Main,searching_or_not
        for i in range(1,cell_count):
            exec(r'''info=repr(cell?.get(1.0,END)[0:-1])
l.append(info)'''.replace('?',str(i)))
        L=[]
        flag=False
        for j in l:
            if j.strip('\'').replace('\\n','').strip()=='':
                flag=True
                continue
            L.append(j.strip('\''))
        f=open('shopdat.dat','rb')
        Data=p.load(f)
        if Data[u]!=[] and type(Data[u][-1]) is not str:
            parameter_list=Data[u][-1]
            f.close()
        else:
            parameter_list=[]
            f.close()
        f=open('shopdat.dat','wb')
        L.append(parameter_list)
        d[u]=L
        p.dump(d,f)
        f.close()
        if flag:
            global add_b,search_b
            if searching_or_not:
                add_b.config(state=NORMAL)
                search_b.config(text='SEARCH')
                searching_or_not=False
                search_box.delete("1.0", "end")
            cell_count=1
            s_page_Main.destroy()
            place()
        messagebox.showinfo('',f'Mr.{u} currently you have {cell_count-1} records!\n🧐\nAll Records Saved...😎👍')
   
    save_changes_b=Button(s_page_u,text='SAVE CHANGES',fg=gen_font_color,font=(('bold'),gen_font_size),command=lambda:save_change())
    save_changes_b.grid(row=2,column=3,padx=5)
   
    global searching_or_not,search_b
    searching_or_not=False
   
    search_b=Button(s_page_u,text=' SEARCH ',fg=gen_font_color,font=(('bold'),gen_font_size),command=lambda:search())
    search_b.grid(row=1,column=2)
   
    def search():
        global searching_or_not,cell_count
        if searching_or_not==False:
            search_words=search_box.get(1.0,END).strip().split(';')
            candids=[]
            f=open('shopdat.dat','rb')
            orig_data_list=p.load(f)[u]
            if type(orig_data_list[-1]) is not str:
                orig_data_list=orig_data_list[0:-1]
            data_list=orig_data_list[:]
            for string in search_words:
                for data in data_list:
                    if string in data and data not in candids:
                        candids.append(data)#codecs.decode(data, 'unicode_escape'))
                data_list=candids
                candids=[]
            if data_list==[]:
                messagebox.showinfo('',f'No Matches Mr.{u} !\n🧐')
                return
            elif data_list==orig_data_list:
                messagebox.showinfo('',f'Everything Matches Mr.{u}! \n🤨🤔🙄')
                return
            global gen_font_size,inter_cell_space,s_page_Main
            #Now data_list contains the cell strings that match the search words
            cell_counter=[]
            for k in data_list:
                cell_counter.append(orig_data_list.index(k)+1)
            for cellno in range(1,cell_count):
                if cellno not in cell_counter:
                    exec(f'''global cell{cellno}
cell{cellno}.grid_forget()''')
                    searching_or_not=True
            add_b.config(state=DISABLED)
            search_b.config(text='END SEARCH')
        else:
            add_b.config(state=NORMAL)
            searching_or_not=False
            search_box.delete("1.0", "end")
            search_b.config(text='SEARCH')
            cell_count=1
            s_page_Main.destroy()
            place()
        #close_search_b=Button(s_page_Main,text=' END SEARCH ',font=(('bold'),font_size))
        #close_search_b.place(relx=0.8,rely=0.1,anchor='ne')
   

    #5)Add the new frame to a window in the canvas
   
   
    canvas.create_window((180,50),window=s_page_Main,anchor='nw')
def third_page():
    S_BASE.pack_forget()
    third_p_base=Frame(wd,bg='grey',bd=10,highlightbackground = "red", highlightcolor= "red",highlightthickness=10)
    third_p_base.pack(fill=BOTH,expand=1)
    back_b=Button(third_p_base,text='MAIN PAGE',fg='violet red',font=('bold',gen_font_size),command=lambda:back_to_main_page())
    back_b.place(relx=0.01,rely=0.01,anchor='nw')
    log_out_b=Button(third_p_base,text=' CHANGE ACCOUNT ',fg='violet red',font=(('bold'),gen_font_size),command=lambda:first_page())
    log_out_b.place(relx=0.8,rely=0.01)
    def first_page():
        third_p_base.pack_forget()
        f.place(relx=0.5,rely=0.4,anchor=CENTER)
   
    def back_to_main_page():
        third_p_base.pack_forget()
        S_BASE.pack(fill=BOTH,expand=1)
    """_______Parameters______"""
   
    #Cell Parameters
    Label(third_p_base,height=4,bg='grey').grid(row=0,column=0)
    Label(third_p_base,text='CELL PARAMETERS :',fg='SlateBlue1',font=(('bold'),gen_font_size)).grid(row=1,column=1)
   
    Label(third_p_base,width=4,bg='grey').grid(row=14,column=3)
   
    global Default_txt_box,lines_to_display_box,space_btw_cells_box,color_of_text_box,bg_color_box,gen_font_size_box,gen_font_color_box,upper_color_box,lower_color_box,cell_holder_color_box,cell_border_colour_box,lower_temp_border_colour_box,screen_border_color_box
    Default_txt_l=Label(third_p_base,text='Default text in new cell:',font=(('bold'),gen_font_size))
    Default_txt_l.grid(row=2,column=2,sticky='w')
    Default_txt_box=Text(third_p_base,height=3,width=60,font=(('bold'),gen_font_size))
    Default_txt_box.grid(row=2,column=4,pady=3,sticky='w')
   
    lines_to_display_l=Label(third_p_base,text='Number of Lines to display:',font=(('bold'),gen_font_size))
    lines_to_display_l.grid(row=3,column=2,pady=5,sticky='w')
    lines_to_display_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    lines_to_display_box.grid(row=3,column=4,pady=5,sticky='w')
   
    space_btw_cells_l=Label(third_p_base,text='Space between cells:',font=(('bold'),gen_font_size))
    space_btw_cells_l.grid(row=4,column=2,pady=5,sticky='w')
    space_btw_cells_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    space_btw_cells_box.grid(row=4,column=4,pady=5,sticky='w')
   
    color_of_text_l=Label(third_p_base,text='Colour of text:',font=(('bold'),gen_font_size))
    color_of_text_l.grid(row=5,column=2,pady=5,sticky='w')
    color_of_text_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    color_of_text_box.grid(row=5,column=4,pady=5,sticky='w')
   
    bg_color_l=Label(third_p_base,text='Background colour of cell:',font=(('bold'),gen_font_size))
    bg_color_l.grid(row=6,column=2,pady=5,sticky='w')
    bg_color_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    bg_color_box.grid(row=6,column=4,pady=5,sticky='w')
   
    #General Parameters
    Label(third_p_base,height=4,bg='grey').grid(row=7,column=1)
    Label(third_p_base,text='GENERAL PARAMETERS :',fg='SlateBlue1',font=(('bold'),gen_font_size)).grid(row=8,column=1)
   
    gen_font_size_l=Label(third_p_base,text='Font size:',font=(('bold'),gen_font_size))
    gen_font_size_l.grid(row=9,column=2,pady=5,sticky='w')
    gen_font_size_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    gen_font_size_box.grid(row=9,column=4,pady=5,sticky='w')
   
    gen_font_color_l=Label(third_p_base,text='Text colour:',font=(('bold'),gen_font_size))
    gen_font_color_l.grid(row=10,column=2,sticky='w')
    gen_font_color_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    gen_font_color_box.grid(row=10,column=4,pady=5,sticky='w')
   
    #Label(third_p_base,height=4,bg='grey').grid(row=11,column=1)
   
    upper_color_l=Label(third_p_base,text='Upper template colour:',font=(('bold'),gen_font_size))
    upper_color_l.grid(row=11,column=2,sticky='w')
    upper_color_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    upper_color_box.grid(row=11,column=4,pady=5,sticky='w')
   
    lower_color_l=Label(third_p_base,text='Lower template colour:',font=(('bold'),gen_font_size))
    lower_color_l.grid(row=12,column=2,sticky='w')
    lower_color_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    lower_color_box.grid(row=12,column=4,pady=5,sticky='w')
   
    cell_holder_color_l=Label(third_p_base,text='Cell holder template colour:',font=(('bold'),gen_font_size))
    cell_holder_color_l.grid(row=13,column=2,sticky='w')
    cell_holder_color_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    cell_holder_color_box.grid(row=13,column=4,pady=5,sticky='w')
   
   
    cell_border_colour_l=Label(third_p_base,text='Cell border colour:',font=(('bold'),gen_font_size))
    cell_border_colour_l.grid(row=14,column=2,sticky='w')
    cell_border_colour_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    cell_border_colour_box.grid(row=14,column=4,pady=5,sticky='w')
   
    lower_temp_border_colour_l=Label(third_p_base,text='Lower template border colour:',font=(('bold'),gen_font_size))
    lower_temp_border_colour_l.grid(row=15,column=2,sticky='w')
    lower_temp_border_colour_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    lower_temp_border_colour_box.grid(row=15,column=4,pady=5,sticky='w')
   
    screen_border_color_l=Label(third_p_base,text='Screen border colour:',font=(('bold'),gen_font_size))
    screen_border_color_l.grid(row=16,column=2,sticky='w')
    screen_border_color_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    screen_border_color_box.grid(row=16,column=4,pady=5,sticky='w')
   
    apply_changes_b=Button(third_p_base,text=' APPLY CHANGES ',fg='green',highlightbackground = "black", highlightcolor= "cyan",highlightthickness=4,command=lambda:apply_changes(),font=(('bold'),gen_font_size))
    apply_changes_b.place(relx=0.8,rely=0.85)
   
   
    def insert_values():
        global Default_txt_box,lines_to_display_box,space_btw_cells_box,color_of_text_box,bg_color_box,gen_font_size_box,gen_font_color_box,upper_color_box,lower_color_box,cell_holder_color_box,cell_border_colour_box,lower_temp_border_colour_box,screen_border_color_box
        global gen_font_size,default_text,inter_cell_space,cell_bg_color,screen_border_color,lower_temp_border_colour,cell_border_colour,S_BASE,lines_to_display,cell_text_colour,gen_font_color,upper_colour,lower_colour,cell_holder_colour
       
        Default_txt_box.insert(1.0,default_text)
        gen_font_size_box.insert(1.0,gen_font_size)
        space_btw_cells_box.insert(1.0,inter_cell_space)
        lines_to_display_box.insert(1.0,lines_to_display)
        color_of_text_box.insert(1.0,cell_text_colour.strip())
        bg_color_box.insert(1.0,cell_bg_color)
       
        gen_font_color_box.insert(1.0,gen_font_color)
        upper_color_box.insert(1.0,upper_colour)
        lower_color_box.insert(1.0,lower_colour)
        cell_holder_color_box.insert(1.0,cell_holder_colour)
        cell_border_colour_box.insert(1.0,cell_border_colour)
        lower_temp_border_colour_box.insert(1.0,lower_temp_border_colour)
        screen_border_color_box.insert(1.0,screen_border_color)
    insert_values()
    def apply_changes():
        try :
            int(gen_font_size_box.get(1.0,END))
        except:
            messagebox.showinfo('',f'Unable to understand number "Font size:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
        try :
            int(space_btw_cells_box.get(1.0,END))
        except:
            messagebox.showinfo('',f'Unable to understand number "Space between cells:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
        try :
            int(lines_to_display_box.get(1.0,END))
        except:
            messagebox.showinfo('',f'Unable to understand number "Number of Lines to display:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
        try :
            Label(fg=color_of_text_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name $ "Colour of text:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
        try :
            Label(fg=bg_color_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Background colour of cell:" Mr.{u} !\n😲🧐🤔')
            return
       
        '''___General___'''
       
        try :
            Label(fg=gen_font_color_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Text colour:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
       
        try :
            Label(fg=upper_color_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Upper template colour:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
       
        try :
            Label(fg=lower_color_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Lower template colour:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
       
        try :
            Label(fg=cell_holder_color_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Cell holder template colour:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
       
        try :
            Label(fg=cell_border_colour_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Cell border colour:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
       
        try :
            Label(fg=lower_temp_border_colour_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Lower template border colour:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
       
        try :
            Label(fg=screen_border_color_box.get(1.0,END).strip()).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Screen border colour:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
       
        f=open('shopdat.dat','rb')
        celldata=p.load(f)
        f.close()
        f=open('shopdat.dat','wb')
        if type(celldata[u][-1]) is str:
            celldata[u].append({'default_text':Default_txt_box.get(1.0,END).strip(),'lines_to_display':int(lines_to_display_box.get(1.0,END).strip()),
                           'inter_cell_space':int(space_btw_cells_box.get(1.0,END).strip()),'cell_text_colour':color_of_text_box.get(1.0,END).strip(),
                           'cell_bg_color':bg_color_box.get(1.0,END).strip(),'gen_font_size':int(gen_font_size_box.get(1.0,END).strip()),
                           'gen_font_color':gen_font_color_box.get(1.0,END).strip(),'upper_color':upper_color_box.get(1.0,END).strip(),
                           'lower_color':lower_color_box.get(1.0,END).strip(),'cell_holder_color':cell_holder_color_box.get(1.0,END).strip(),
                           'cell_border_colour':cell_border_colour_box.get(1.0,END).strip(),'lower_temp_border_colour':lower_temp_border_colour_box.get(1.0,END).strip(),
                           'screen_border_color':screen_border_color_box.get(1.0,END).strip()})
            p.dump(celldata,f)
            f.close()
        else:
            celldata[u][-1]={'default_text':Default_txt_box.get(1.0,END).strip(),'lines_to_display':int(lines_to_display_box.get(1.0,END).strip()),
                           'inter_cell_space':int(space_btw_cells_box.get(1.0,END).strip()),'cell_text_colour':color_of_text_box.get(1.0,END).strip(),
                           'cell_bg_color':bg_color_box.get(1.0,END).strip(),'gen_font_size':int(gen_font_size_box.get(1.0,END).strip()),
                           'gen_font_color':gen_font_color_box.get(1.0,END).strip(),'upper_color':upper_color_box.get(1.0,END).strip(),
                           'lower_color':lower_color_box.get(1.0,END).strip(),'cell_holder_color':cell_holder_color_box.get(1.0,END).strip(),
                           'cell_border_colour':cell_border_colour_box.get(1.0,END).strip(),'lower_temp_border_colour':lower_temp_border_colour_box.get(1.0,END).strip(),
                           'screen_border_color':screen_border_color_box.get(1.0,END).strip()}
            p.dump(celldata,f)
            f.close()
        S_BASE.destroy()
        third_p_base.pack_forget()
        sec_page()
       
    """_______________________"""

wd.mainloop()

'''PROJECT - LAST HOPE'''

from tkinter import *
import codecs
from tkinter import ttk
import mysql.connector as s
from tkinter import messagebox
import pickle as p


#Colour of the empty labels
colour='cyan'

f_l_c='slateblue'

wd=Tk()
wd.geometry('1680x1050')

f=Frame(wd,height=500,width=700,bg='purple',bd=40)
f.place(relx=0.5,rely=0.4,anchor=CENTER)

c='purple'
emp1=Label(f,bg=c)
emp1.grid(row=1,column=0)
emp2=Label(f,bg=c)
emp2.grid(row=3,column=0)
emp3=Label(f,bg=c)
emp3.grid(row=7,column=0)
emp4=Label(f,bg=c)
emp4.grid(row=2,column=0)
emp5=Label(f,bg=c)
emp5.grid(row=8,column=0)

l_wel=Label(f,text='WELCOME TO PRODUCTS MANAGER',font=('bold',40),bg=f_l_c)
l_wel.grid(row=0,column=0)

l_do=Label(f,text='Do you want to create an account?',font=('bold',20),bg=f_l_c)
l_do.grid(row=3,column=0)

"""CREATION OF ACCOUNT"""

def acc_creation():
   
    f.place_forget()
   
    f_reply=Frame(wd,bg='cyan',bd=35)
    f_reply.place(relx=0.5,rely=0.4,anchor=CENTER)
   
    emp6=Label(f_reply,bg=colour)
    emp6.grid(row=0,column=0,columnspan=2)
   
    emp7=Label(f_reply,bg=colour)
    emp7.grid(row=1,column=0,columnspan=2)
   
    emp8=Label(f_reply,bg=colour)
    emp8.grid(row=3,column=0,columnspan=2)
   
    emp9=Label(f_reply,bg=colour)
    emp9.grid(row=5,column=0,columnspan=2)
   
    emp10=Label(f_reply,bg=colour)
    emp10.grid(row=7,column=0,columnspan=2)
   
    #LABELS AND ENTRY BOXES
    username_Label=Label(f_reply,text='Username',bg='slateblue',font=('bold',20))
    username_Label.grid(row=2,column=0)
   
    username_box=Entry(f_reply)
    username_box.grid(row=2,column=1)
   
    #emailid_Label=Label(f_reply,text='Email id',bg='yellow',font=('bold',20))
    #emailid_Label.grid(row=4,column=0)
   
    emailid_box=Entry(f_reply)
    emailid_box.insert(0,'123d')
    #emailid_box.grid(row=4,column=1)
   
    pass_Label=Label(f_reply,text='Password',bg='slateblue',font=('bold',20))
    pass_Label.grid(row=6,column=0)
   
    pass_box=Entry(f_reply,show="*")
    pass_box.grid(row=6,column=1)
   
    def acc_create():
       
        u=str(username_box.get()).strip()
        e=str(emailid_box.get()).strip()
        p=str(pass_box.get()).strip()
        if u=='':
            messagebox.showinfo('','Please enter a valid username')
            return
        elif (u.replace('_','')).isalnum() is False:
            messagebox.showinfo('','Enter username without special characters other than \"_\"')
            return
        elif e=='':
            messagebox.showinfo('','Please enter a valid email id')
            return
        elif p=='':
            messagebox.showinfo('','Please enter a valid password')
            return
       
        con=s.connect(host="127.0.0.1",user="root",passwd="",database="tkinter")
        cursor=con.cursor()
        #checking whether username already exists or not
        cursor.execute("create table if not exists acc (username varchar(25),emailid varchar(25),password varchar(25))")
        cursor.execute('select * from acc where username like "{}";'.format(u))
        rs=cursor.fetchall()
        if any(rs)==False:
            cursor.execute('insert into acc values("{}","{}","{}")'.format(u,e,p))
            cursor.execute('commit;')
            messagebox.showinfo('','Account successfully created')
            #STORING THE ACCOUNT NAME THAT IS TO BE AUTO SIGNED IN NEXT TIME
            cursor.execute('create table if not exists cur_user(username varchar(25));')
            cursor.execute('delete from cur_user;')
            cursor.execute('insert into cur_user values("{}");'.format(u))
            cursor.execute('commit;')
        else:
            messagebox.showinfo('','Please choose a different username')
            return
        f_reply.destroy()
        f.place(relx=0.5,rely=0.4,anchor=CENTER)
    create_account_box=Button(f_reply,text='Create Account',font=('bold',20),bg='red',command=acc_create)
    create_account_box.grid(row=8,column=1,sticky=SE)
   
    def close_reply_f():
        f_reply.after(0,f_reply.destroy())
        f.place(relx=0.5,rely=0.4,anchor=CENTER)
   
    close_button=Button(f_reply,text='X',bg='red',command=close_reply_f)
    close_button.place(relx=0.98,rely=0.03,anchor=NE)

create_acc=Button(f,text='Create an account',font=('bold',20),command=acc_creation,bg=f_l_c)
create_acc.grid(row=6,column=0)

def signin():
    f.place_forget()
   
    s_f=Frame(wd,bg='cyan',bd=10)
    s_f.place(relx=0.5,rely=0.4,anchor=CENTER)
   
    emp11=Label(s_f,bg=colour)
    emp11.grid(row=0,column=0,columnspan=2)
   
    emp12=Label(s_f,bg=colour)
    emp12.grid(row=1,column=0,columnspan=2)
   
    username_Label=Label(s_f,text='Username',font=('bold',20),bg='slateblue')
    username_Label.grid(row=2,column=0)
   
    username_box=Entry(s_f)
    username_box.grid(row=2,column=1)
   
    emp13=Label(s_f,bg=colour)
    emp13.grid(row=3,column=0,columnspan=2)
   
    pass_Label=Label(s_f,text='Password',font=('bold',20),bg='slateblue')
    pass_Label.grid(row=4,column=0)
     
    pass_box=Entry(s_f,show="*")
    pass_box.grid(row=4,column=1)
       
    emp14=Label(s_f,bg=colour)
    emp14.grid(row=5,column=0,columnspan=2)
       
    def close_s_f():
        s_f.place_forget()
        f.place(relx=0.5,rely=0.4,anchor=CENTER)
       
    def sign():
        global u
        u=str(username_box.get()).strip()
        p=str(pass_box.get()).strip()
        if u=='':
            messagebox.showinfo('','Username required')
            return
        con=s.connect(host="127.0.0.1",user="root",passwd="",database="tkinter")
        cursor=con.cursor()
        cursor.execute("create table if not exists acc (username varchar(25),emailid varchar(25),password varchar(25));")
        cursor.execute('select password from acc where username like "{}";'.format(u))
        rs=cursor.fetchone()
        if bool(rs)==False:
            messagebox.showinfo('','Please enter proper username')
            return
        if p==rs[0:1][0]:
            messagebox.showinfo('',f'Welcome {u}!\n😊')
            cursor.execute('create table if not exists cur_user(username varchar(25));')
            cursor.execute('delete from cur_user;')
            cursor.execute('insert into cur_user values("{}");'.format(u))
            cursor.execute('commit;')
            s_f.place_forget()
            sec_page()#  <<<<<<<----------
        else:
            messagebox.showinfo('','Please recheck your password')
            return
       
    sign_in_b=Button(s_f,text='Sign in',font=('bold',20),command=sign)
    sign_in_b.grid(row=6,column=1,sticky=SE)
   
    close_b=Button(s_f,text='X',bg='red',command=close_s_f)
    close_b.place(relx=0.98,rely=0.03,anchor=NE)
   
l_al=Label(f,text='Already have an account?',font=('bold',20),bg=f_l_c)
l_al.grid(row=9,column=0)
   
B_signin=Button(f,text='SIGN IN',font=('bold',20),command=signin)
B_signin.grid(row=10,column=0)

def sec_page():
   
    global cell_count
    cell_count=1
   
    f=open('shopdat.dat','rb')
    global u,d
    d=p.load(f)
    if u in d:
        f.close()
    else:
        f.close()
        d[u]=[]
        f=open('shopdat.dat','wb')
        p.dump(d,f)
        f.close()
       
    try:
        parameter_list=d[u][-1]
    except:
        parameter_list=[]
    print('**parameter_list@#@:\n\n',parameter_list)
    #$$$$$$$
    global gen_font_size,default_text,inter_cell_space,cell_bg_color,screen_border_color,lower_temp_border_colour,cell_border_colour,S_BASE,lines_to_display,cell_text_colour,gen_font_color,upper_colour,lower_colour,cell_holder_colour
   
    if parameter_list==[] or (type(parameter_list) is str):
        gen_font_size=25
        inter_cell_space=50
        default_text='Product Name:\nPrice                  :\nQty                     :\nOffer                  :\nMfd Date          :\nExp Date           :\nBatch No          :\nDesp                  :'
        lines_to_display=8
        cell_text_colour='black'
        cell_bg_color='white'
        gen_font_color='black'
        upper_colour='white'
        lower_colour='blue'
        cell_holder_colour='yellow'
        cell_border_colour='red'
        lower_temp_border_colour='maroon'
        screen_border_color='black'
    else:

        gen_font_size=parameter_list['gen_font_size']
        inter_cell_space=parameter_list['inter_cell_space']
        default_text=parameter_list['default_text']
        lines_to_display=parameter_list['lines_to_display']
        cell_text_colour=parameter_list['cell_text_colour']
        cell_bg_color=parameter_list['cell_bg_color']
        gen_font_color=parameter_list['gen_font_color']
        upper_colour=parameter_list['upper_color']
        lower_colour=parameter_list['lower_color']
        cell_holder_colour=parameter_list['cell_holder_color']
        cell_border_colour=parameter_list['cell_border_colour']
        lower_temp_border_colour=parameter_list['lower_temp_border_colour']
        screen_border_color=parameter_list['screen_border_color']
       
    #$$$$$$$
   
    S_BASE=Frame(wd,bg=screen_border_color)
    S_BASE.pack(fill=BOTH,expand=1)
   
    #___UPPER HALF______
    s_page_u=Frame(S_BASE,height=20,bg=upper_colour)
    s_page_u.pack(fill=X,padx=10,pady=10)
   
    settings_b=Button(s_page_u,text=' SETTINGS ',fg=gen_font_color,font=(('bold'),gen_font_size),command=lambda:third_page())
    settings_b.grid(row=0,column=0,padx=5,pady=10)
   
    search_box=Text(s_page_u,height=1,width=70,font=(('bold'),gen_font_size))
    search_box.grid(row=1,column=1)
    search_box.config(highlightbackground = "black", highlightcolor= "black")
   
   
   
   
    #___________
    s_page_d=Frame(S_BASE,bg=lower_temp_border_colour)
    s_page_d.pack(fill=BOTH,expand=1,padx=10,pady=10)
   
    #1)Create canvas
   
    canvas=Canvas(s_page_d,bg=lower_colour)
    canvas.pack(side=LEFT,fill=BOTH,expand=1,padx=10,pady=10)
   
    #2)Add scrollbar to the canvas
    global sb
    sb=ttk.Scrollbar(s_page_d,orient=VERTICAL,command=canvas.yview)
    sb.pack(side=RIGHT,fill=Y)
   
    #3)Configure the canvas
   
    canvas.configure(yscrollcommand=sb.set)
    canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion=canvas.bbox('all')))
   
    #4)Main frame inside the canvas
   
    """{<<<<<~^~^~^~>>>>>}"""
   
    def place():
        f=open('shopdat.dat','rb')
        global d,u,s_page_Main
        s_page_Main=Frame(canvas,bg=cell_holder_colour)
        canvas.create_window((180,50),window=s_page_Main,anchor='nw')
        d=p.load(f)
        f.close()
        if d[u]!=[] and type(d[u][-1]) is not str:
            d[u]=d[u][0:-1]
        global cell_count
        for thing in d[u]:
            #print(thing)
            exec(f'''global cell{cell_count}
cell{cell_count}=Text(s_page_Main,width=80,height=lines_to_display,bg=cell_bg_color,font=(('bold'),gen_font_size),fg=cell_text_colour,highlightbackground = cell_border_colour, highlightcolor= cell_border_colour)
cell{cell_count}.insert(1.0,'{thing}')
cell{cell_count}.grid(pady=inter_cell_space,padx=20)''')
            cell_count+=1
    place()
   
    global add_b
       
    def add():
        global cell_count,s_page_Main,gen_font_size,default_text,inter_cell_space,lines_to_display
        exec(f'''global cell{cell_count}
cell{cell_count}=Text(s_page_Main,width=80,height=lines_to_display,bg=cell_bg_color,font=(('bold'),gen_font_size),fg=cell_text_colour,highlightbackground = cell_border_colour, highlightcolor= cell_border_colour)
cell{cell_count}.insert(1.0,default_text)
cell{cell_count}.grid(padx=20,pady=inter_cell_space)''')
        cell_count+=1
        wd.attributes(('-fullscreen'),True)

        #wd.attributes(('-fullscreen'),True)
    add_b=Button(s_page_u,text=' Add ',fg=gen_font_color,command=lambda:add(),font=(('bold'),gen_font_size))
    add_b.grid(row=2,column=1,columnspan=2,pady=20)
   
   
    def save_change():
        l=[]
        global cell_count,s_page_Main,searching_or_not
        for i in range(1,cell_count):
            exec(r'''info=repr(cell?.get(1.0,END)[0:-1])
l.append(info)'''.replace('?',str(i)))
        L=[]
        flag=False
        for j in l:
            if j.strip('\'').replace('\\n','').strip()=='':
                flag=True
                continue
            L.append(j.strip('\''))
        f=open('shopdat.dat','rb')
        Data=p.load(f)
        if Data[u]!=[] and type(Data[u][-1]) is not str:
            parameter_list=Data[u][-1]
            f.close()
        else:
            parameter_list=[]
            f.close()
        f=open('shopdat.dat','wb')
        L.append(parameter_list)
        d[u]=L
        p.dump(d,f)
        f.close()
        if flag:
            global add_b,search_b
            if searching_or_not:
                add_b.config(state=NORMAL)
                search_b.config(text='SEARCH')
                searching_or_not=False
                search_box.delete("1.0", "end")
            cell_count=1
            s_page_Main.destroy()
            place()
        messagebox.showinfo('',f'Mr.{u} currently you have {cell_count-1} records!\n🧐\nAll Records Saved...😎👍')
   
    save_changes_b=Button(s_page_u,text='SAVE CHANGES',fg=gen_font_color,font=(('bold'),gen_font_size),command=lambda:save_change())
    save_changes_b.grid(row=2,column=3,padx=5)
   
    global searching_or_not,search_b
    searching_or_not=False
   
    search_b=Button(s_page_u,text=' SEARCH ',fg=gen_font_color,font=(('bold'),gen_font_size),command=lambda:search())
    search_b.grid(row=1,column=2)
   
    def search():
        global searching_or_not,cell_count
        if searching_or_not==False:
            search_words=search_box.get(1.0,END).strip().split(';')
            candids=[]
            f=open('shopdat.dat','rb')
            orig_data_list=p.load(f)[u]
            if type(orig_data_list[-1]) is not str:
                orig_data_list=orig_data_list[0:-1]
            data_list=orig_data_list[:]
            for string in search_words:
                for data in data_list:
                    if string in data and data not in candids:
                        candids.append(data)#codecs.decode(data, 'unicode_escape'))
                data_list=candids
                candids=[]
            if data_list==[]:
                messagebox.showinfo('',f'No Matches Mr.{u} !\n🧐')
                return
            elif data_list==orig_data_list:
                messagebox.showinfo('',f'Everything Matches Mr.{u}! \n🤨🤔🙄')
                return
            global gen_font_size,inter_cell_space,s_page_Main
            #Now data_list contains the cell strings that match the search words
            cell_counter=[]
            for k in data_list:
                cell_counter.append(orig_data_list.index(k)+1)
            for cellno in range(1,cell_count):
                if cellno not in cell_counter:
                    exec(f'''global cell{cellno}
cell{cellno}.grid_forget()''')
                    searching_or_not=True
            add_b.config(state=DISABLED)
            search_b.config(text='END SEARCH')
        else:
            add_b.config(state=NORMAL)
            searching_or_not=False
            search_box.delete("1.0", "end")
            search_b.config(text='SEARCH')
            cell_count=1
            s_page_Main.destroy()
            place()
        #close_search_b=Button(s_page_Main,text=' END SEARCH ',font=(('bold'),font_size))
        #close_search_b.place(relx=0.8,rely=0.1,anchor='ne')
   

    #5)Add the new frame to a window in the canvas
   
   
    canvas.create_window((180,50),window=s_page_Main,anchor='nw')
def third_page():
    S_BASE.pack_forget()
    third_p_base=Frame(wd,bg='grey',bd=10,highlightbackground = "red", highlightcolor= "red",highlightthickness=10)
    third_p_base.pack(fill=BOTH,expand=1)
    back_b=Button(third_p_base,text='MAIN PAGE',fg='violet red',font=('bold',gen_font_size),command=lambda:back_to_main_page())
    back_b.place(relx=0.01,rely=0.01,anchor='nw')
    log_out_b=Button(third_p_base,text=' CHANGE ACCOUNT ',fg='violet red',font=(('bold'),gen_font_size),command=lambda:first_page())
    log_out_b.place(relx=0.8,rely=0.01)
    def first_page():
        third_p_base.pack_forget()
        f.place(relx=0.5,rely=0.4,anchor=CENTER)
   
    def back_to_main_page():
        third_p_base.pack_forget()
        S_BASE.pack(fill=BOTH,expand=1)
    """_______Parameters______"""
   
    #Cell Parameters
    Label(third_p_base,height=4,bg='grey').grid(row=0,column=0)
    Label(third_p_base,text='CELL PARAMETERS :',fg='SlateBlue1',font=(('bold'),gen_font_size)).grid(row=1,column=1)
   
    Label(third_p_base,width=4,bg='grey').grid(row=14,column=3)
   
    global Default_txt_box,lines_to_display_box,space_btw_cells_box,color_of_text_box,bg_color_box,gen_font_size_box,gen_font_color_box,upper_color_box,lower_color_box,cell_holder_color_box,cell_border_colour_box,lower_temp_border_colour_box,screen_border_color_box
    Default_txt_l=Label(third_p_base,text='Default text in new cell:',font=(('bold'),gen_font_size))
    Default_txt_l.grid(row=2,column=2,sticky='w')
    Default_txt_box=Text(third_p_base,height=3,width=60,font=(('bold'),gen_font_size))
    Default_txt_box.grid(row=2,column=4,pady=3,sticky='w')
   
    lines_to_display_l=Label(third_p_base,text='Number of Lines to display:',font=(('bold'),gen_font_size))
    lines_to_display_l.grid(row=3,column=2,pady=5,sticky='w')
    lines_to_display_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    lines_to_display_box.grid(row=3,column=4,pady=5,sticky='w')
   
    space_btw_cells_l=Label(third_p_base,text='Space between cells:',font=(('bold'),gen_font_size))
    space_btw_cells_l.grid(row=4,column=2,pady=5,sticky='w')
    space_btw_cells_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    space_btw_cells_box.grid(row=4,column=4,pady=5,sticky='w')
   
    color_of_text_l=Label(third_p_base,text='Colour of text:',font=(('bold'),gen_font_size))
    color_of_text_l.grid(row=5,column=2,pady=5,sticky='w')
    color_of_text_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    color_of_text_box.grid(row=5,column=4,pady=5,sticky='w')
   
    bg_color_l=Label(third_p_base,text='Background colour of cell:',font=(('bold'),gen_font_size))
    bg_color_l.grid(row=6,column=2,pady=5,sticky='w')
    bg_color_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    bg_color_box.grid(row=6,column=4,pady=5,sticky='w')
   
    #General Parameters
    Label(third_p_base,height=4,bg='grey').grid(row=7,column=1)
    Label(third_p_base,text='GENERAL PARAMETERS :',fg='SlateBlue1',font=(('bold'),gen_font_size)).grid(row=8,column=1)
   
    gen_font_size_l=Label(third_p_base,text='Font size:',font=(('bold'),gen_font_size))
    gen_font_size_l.grid(row=9,column=2,pady=5,sticky='w')
    gen_font_size_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    gen_font_size_box.grid(row=9,column=4,pady=5,sticky='w')
   
    gen_font_color_l=Label(third_p_base,text='Text colour:',font=(('bold'),gen_font_size))
    gen_font_color_l.grid(row=10,column=2,sticky='w')
    gen_font_color_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    gen_font_color_box.grid(row=10,column=4,pady=5,sticky='w')
   
    #Label(third_p_base,height=4,bg='grey').grid(row=11,column=1)
   
    upper_color_l=Label(third_p_base,text='Upper template colour:',font=(('bold'),gen_font_size))
    upper_color_l.grid(row=11,column=2,sticky='w')
    upper_color_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    upper_color_box.grid(row=11,column=4,pady=5,sticky='w')
   
    lower_color_l=Label(third_p_base,text='Lower template colour:',font=(('bold'),gen_font_size))
    lower_color_l.grid(row=12,column=2,sticky='w')
    lower_color_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    lower_color_box.grid(row=12,column=4,pady=5,sticky='w')
   
    cell_holder_color_l=Label(third_p_base,text='Cell holder template colour:',font=(('bold'),gen_font_size))
    cell_holder_color_l.grid(row=13,column=2,sticky='w')
    cell_holder_color_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    cell_holder_color_box.grid(row=13,column=4,pady=5,sticky='w')
   
   
    cell_border_colour_l=Label(third_p_base,text='Cell border colour:',font=(('bold'),gen_font_size))
    cell_border_colour_l.grid(row=14,column=2,sticky='w')
    cell_border_colour_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    cell_border_colour_box.grid(row=14,column=4,pady=5,sticky='w')
   
    lower_temp_border_colour_l=Label(third_p_base,text='Lower template border colour:',font=(('bold'),gen_font_size))
    lower_temp_border_colour_l.grid(row=15,column=2,sticky='w')
    lower_temp_border_colour_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    lower_temp_border_colour_box.grid(row=15,column=4,pady=5,sticky='w')
   
    screen_border_color_l=Label(third_p_base,text='Screen border colour:',font=(('bold'),gen_font_size))
    screen_border_color_l.grid(row=16,column=2,sticky='w')
    screen_border_color_box=Text(third_p_base,height=1,width=30,font=(('bold'),gen_font_size))
    screen_border_color_box.grid(row=16,column=4,pady=5,sticky='w')
   
    apply_changes_b=Button(third_p_base,text=' APPLY CHANGES ',fg='green',highlightbackground = "black", highlightcolor= "cyan",highlightthickness=4,command=lambda:apply_changes(),font=(('bold'),gen_font_size))
    apply_changes_b.place(relx=0.8,rely=0.85)
   
   
    def insert_values():
        global Default_txt_box,lines_to_display_box,space_btw_cells_box,color_of_text_box,bg_color_box,gen_font_size_box,gen_font_color_box,upper_color_box,lower_color_box,cell_holder_color_box,cell_border_colour_box,lower_temp_border_colour_box,screen_border_color_box
        global gen_font_size,default_text,inter_cell_space,cell_bg_color,screen_border_color,lower_temp_border_colour,cell_border_colour,S_BASE,lines_to_display,cell_text_colour,gen_font_color,upper_colour,lower_colour,cell_holder_colour
       
        Default_txt_box.insert(1.0,default_text)
        gen_font_size_box.insert(1.0,gen_font_size)
        space_btw_cells_box.insert(1.0,inter_cell_space)
        lines_to_display_box.insert(1.0,lines_to_display)
        color_of_text_box.insert(1.0,cell_text_colour.strip())
        bg_color_box.insert(1.0,cell_bg_color)
       
        gen_font_color_box.insert(1.0,gen_font_color)
        upper_color_box.insert(1.0,upper_colour)
        lower_color_box.insert(1.0,lower_colour)
        cell_holder_color_box.insert(1.0,cell_holder_colour)
        cell_border_colour_box.insert(1.0,cell_border_colour)
        lower_temp_border_colour_box.insert(1.0,lower_temp_border_colour)
        screen_border_color_box.insert(1.0,screen_border_color)
    insert_values()
    def apply_changes():
        try :
            int(gen_font_size_box.get(1.0,END))
        except:
            messagebox.showinfo('',f'Unable to understand number "Font size:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
        try :
            int(space_btw_cells_box.get(1.0,END))
        except:
            messagebox.showinfo('',f'Unable to understand number "Space between cells:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
        try :
            int(lines_to_display_box.get(1.0,END))
        except:
            messagebox.showinfo('',f'Unable to understand number "Number of Lines to display:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
        try :
            Label(fg=color_of_text_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name $ "Colour of text:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
        try :
            Label(fg=bg_color_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Background colour of cell:" Mr.{u} !\n😲🧐🤔')
            return
       
        '''___General___'''
       
        try :
            Label(fg=gen_font_color_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Text colour:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
       
        try :
            Label(fg=upper_color_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Upper template colour:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
       
        try :
            Label(fg=lower_color_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Lower template colour:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
       
        try :
            Label(fg=cell_holder_color_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Cell holder template colour:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
       
        try :
            Label(fg=cell_border_colour_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Cell border colour:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
       
        try :
            Label(fg=lower_temp_border_colour_box.get(1.0,END)[:-1]).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Lower template border colour:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
       
        try :
            Label(fg=screen_border_color_box.get(1.0,END).strip()).destroy()
        except:
            messagebox.showinfo('',f'Unable to understand colour name "Screen border colour:" Mr.{u} !\n😲🧐🤔')
            return
        '''______'''
       
        f=open('shopdat.dat','rb')
        celldata=p.load(f)
        f.close()
        f=open('shopdat.dat','wb')
        if type(celldata[u][-1]) is str:
            celldata[u].append({'default_text':Default_txt_box.get(1.0,END).strip(),'lines_to_display':int(lines_to_display_box.get(1.0,END).strip()),
                           'inter_cell_space':int(space_btw_cells_box.get(1.0,END).strip()),'cell_text_colour':color_of_text_box.get(1.0,END).strip(),
                           'cell_bg_color':bg_color_box.get(1.0,END).strip(),'gen_font_size':int(gen_font_size_box.get(1.0,END).strip()),
                           'gen_font_color':gen_font_color_box.get(1.0,END).strip(),'upper_color':upper_color_box.get(1.0,END).strip(),
                           'lower_color':lower_color_box.get(1.0,END).strip(),'cell_holder_color':cell_holder_color_box.get(1.0,END).strip(),
                           'cell_border_colour':cell_border_colour_box.get(1.0,END).strip(),'lower_temp_border_colour':lower_temp_border_colour_box.get(1.0,END).strip(),
                           'screen_border_color':screen_border_color_box.get(1.0,END).strip()})
            p.dump(celldata,f)
            f.close()
        else:
            celldata[u][-1]={'default_text':Default_txt_box.get(1.0,END).strip(),'lines_to_display':int(lines_to_display_box.get(1.0,END).strip()),
                           'inter_cell_space':int(space_btw_cells_box.get(1.0,END).strip()),'cell_text_colour':color_of_text_box.get(1.0,END).strip(),
                           'cell_bg_color':bg_color_box.get(1.0,END).strip(),'gen_font_size':int(gen_font_size_box.get(1.0,END).strip()),
                           'gen_font_color':gen_font_color_box.get(1.0,END).strip(),'upper_color':upper_color_box.get(1.0,END).strip(),
                           'lower_color':lower_color_box.get(1.0,END).strip(),'cell_holder_color':cell_holder_color_box.get(1.0,END).strip(),
                           'cell_border_colour':cell_border_colour_box.get(1.0,END).strip(),'lower_temp_border_colour':lower_temp_border_colour_box.get(1.0,END).strip(),
                           'screen_border_color':screen_border_color_box.get(1.0,END).strip()}
            p.dump(celldata,f)
            f.close()
        S_BASE.destroy()
        third_p_base.pack_forget()
        sec_page()
       
    """_______________________"""

wd.mainloop()

