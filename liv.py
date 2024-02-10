from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk

window = CTk()

set_default_color_theme('green')

# window.config(background='white')

window.title('Library Management System')
window.geometry('1360x690')
window.resizable(False, False)
window.iconbitmap('icons/books_97178.ico')

# Database ------

def addingBook():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()

    # c.execute('''CREATE TABLE IF NOT EXISTS books_table(
    #           ID INTEGER PRIMARY KEY AUTOINCREMENT,
    #           b_name text,
    #           b_id integer,
    #           b_author text,
    #           b_genre text
    # )''')

    c.execute('INSERT INTO books_table(b_name,b_id,b_author,b_genre) VALUES(?,?,?,?)',
              (book_name.get(),book_id.get(),book_author.get(),book_genre.get()))

    conn.commit()
    conn.close()

    book_name.delete(0, END)
    book_id.delete(0, END)
    book_author.delete(0, END)
    book_genre.delete(0, END)


def addingstds():
    con = sqlite3.connect('students.db')
    c = con.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS stds_table(
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              f_name text,
              l_name text,
              lib_id integer

    )''')

    c.execute('INSERT INTO stds_table(f_name,l_name,lib_id) VALUES(?,?,?)',
              (std_fname.get(),std_lname.get(),std_id.get()))

    con.commit()
    con.close()
    std_fname.delete(0, END)
    std_lname.delete(0, END)
    std_id.delete(0, END)

def issuingBook():
    conb = sqlite3.connect('books.db')
    cb = conb.cursor()

    cons = sqlite3.connect('students.db')
    cs = cons.cursor()

    conn = sqlite3.connect('student_book_pair.db')
    c = conn.cursor()

    # fetching book db data
    cb.execute('SELECT * FROM books_table WHERE b_id=?', (issue_book_id.get(),))
    b_record = cb.fetchone()
    cs.execute('SELECT * FROM stds_table WHERE lib_id=?', (issue_std_id.get(),))
    s_record = cs.fetchone()
   

#     c.execute('''
#         CREATE TABLE IF NOT EXISTS std_book_pair_table(
#               ID INTEGER PRIMARY KEY AUTOINCREMENT,
#               b_name text,
#               b_id integer,
#               b_author text,
#               b_genre text,
#               s_fname text,
#               s_lname text,
#               s_libid integer
#         )
# ''')

    c.execute('INSERT INTO std_book_pair_table(b_name,b_id,b_author,b_genre,s_fname,s_lname,s_libid) VALUES(?,?,?,?,?,?,?)',
              (b_record[1],b_record[2],b_record[3],b_record[4],s_record[1],s_record[2],s_record[3]))

    conn.commit()
    conn.close()

    cb.execute('DELETE FROM books_table WHERE b_id='+issue_book_id.get())

    conb.commit()
    conb.close()

    cons.commit()
    cons.close()

    print(b_record)
    print(s_record)

    issue_book_id.delete(0, END)
    issue_std_id.delete(0, END)

def receivingBook():
    conb = sqlite3.connect('books.db')
    cb = conb.cursor()

    conn = sqlite3.connect('student_book_pair.db')
    c = conn.cursor()

    # fetching book db data
    c.execute('SELECT * FROM std_book_pair_table WHERE b_id=?', (issue_book_id.get(),))
    bs_record = c.fetchone()
    
    cb.execute('INSERT INTO books_table(b_name,b_id,b_author,b_genre) VALUES(?,?,?,?)',
              (bs_record[1],bs_record[2],bs_record[3],bs_record[4]))


    conb.commit()
    conb.close()

    c.execute('DELETE FROM std_book_pair_table WHERE b_id='+issue_book_id.get())


    conn.commit()
    conn.close()

    
   
   
    issue_book_id.delete(0, END)
    issue_std_id.delete(0, END)


# ------ Database

# Images ------
books_btn_icon = Image.open('Images/books_97178.png')
issue_btn_icon = Image.open('Images/pointinghand_100160.png')
stds_btn_icon = Image.open('Images/groups_people_people_1715.png')
published_btn_icon = Image.open('Images/teacherreading_89190.png')
# ------ Images



# frames --------

left_f = CTkFrame(window, width=200, height=650, fg_color='#2CC985', border_color='#000000', border_width=5)
left_f.place(x=20, y=20)

# bottom_f = CTkFrame(window, width=1000, height=300, fg_color='#2CC985', border_color='#000000', border_width=5)
# bottom_f.place(x=300, y=360)

# ------ frames

# ------ functions
stds_top_f = None
books_top_f = None
books_bottom_f = None
stds_right_f = None
published_bottom_f = None
issue_top_f = None
issue_bottom_f = None
right_f = None

def books():
    
    f_books_btn = CTkButton(left_f, text='Books', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), fg_color='#ffffff', text_color='#2CC985', image=CTkImage(light_image=books_btn_icon, dark_image=books_btn_icon))
    f_books_btn.place(x=20, y=240)

    issue_btn = CTkButton(left_f, text='Issue', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), image=CTkImage(light_image=issue_btn_icon, dark_image=issue_btn_icon), command=issues)
    issue_btn.place(x=20, y=300)

    stds_btn = CTkButton(left_f, text='Students', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), image=CTkImage(light_image=stds_btn_icon, dark_image=stds_btn_icon), command=stds)
    stds_btn.place(x=20, y=360)
    
    published_btn = CTkButton(left_f, text='Published', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), image=CTkImage(light_image=published_btn_icon, dark_image=published_btn_icon), command=published)
    published_btn.place(x=20, y=420)

    global books_top_f
    global books_bottom_f

    books_top_f = CTkFrame(window, width=400, height=250, fg_color='#ffffff')
    books_top_f.place(x=560, y=30)

    books_bottom_f = CTkFrame(window, width=1000, height=300, fg_color='#2CC985', border_color='#000000', border_width=5)
    books_bottom_f.place(x=275, y=395)

    global book_name
    global book_id
    global book_author
    global book_genre

    book_name_label = CTkLabel(books_top_f, text='Name:', font=('Cooper Black', 24, 'bold')).place(x=20, y=20)
    book_name = CTkEntry(books_top_f, width=250 , font=('Cooper Black', 24), placeholder_text='Harry Potter')
    book_name.place(x=120, y=17)
    
    book_id_label = CTkLabel(books_top_f, text='Id:', font=('Cooper Black', 24, 'bold')).place(x=40, y=60)
    book_id = CTkEntry(books_top_f, width=250 , font=('Cooper Black', 24), placeholder_text='008')
    book_id.place(x=120, y=60)

    book_author_label = CTkLabel(books_top_f, text='Author:', font=('Cooper Black', 24, 'bold')).place(x=10, y=104)
    book_author = CTkEntry(books_top_f, width=250 , font=('Cooper Black', 24), placeholder_text='J.K. Rowling')
    book_author.place(x=120, y=104)


    book_genre_label = CTkLabel(books_top_f, text='Genre:', font=('Cooper Black', 24, 'bold')).place(x=20, y=148)
    book_genre = CTkEntry(books_top_f, width=250 , font=('Cooper Black', 24), placeholder_text='Fantasy')
    book_genre.place(x=120, y=148)

    add_book_btn = CTkButton(books_top_f, text='Add', text_color='#ffffff', width=360, font=('Cooper Black', 24, 'bold'), command=addingBook)
    add_book_btn.place(x=10, y=190)

    if issue_bottom_f is not None:
        issue_bottom_f.destroy()
    if right_f is not None:
        right_f.destroy()
    if issue_top_f is not None:
        issue_top_f.destroy()
    if stds_top_f is not None:
        stds_top_f.destroy()
    if stds_right_f is not None:
        stds_right_f.destroy()
    if published_bottom_f is not None:
        published_bottom_f.destroy()
    
    b_table = ttk.Treeview(books_bottom_f, columns=['S.N.', 'Name', 'Id', 'Author', 'Genre'], show='headings')
    b_table.heading('S.N.', text='S.N.', anchor=CENTER)
    b_table.heading('Name', text='Book\'s Name', anchor=CENTER)
    b_table.heading('Id', text='Book Id', anchor=CENTER)
    b_table.heading('Author', text='Author', anchor=CENTER)
    b_table.heading('Genre', text='Genre', anchor=CENTER)
    b_table.pack(padx=5, pady=5, expand=True)

    conn = sqlite3.connect('books.db')
    c=conn.cursor()

    c.execute('SELECT * FROM books_table')
    records = c.fetchall()
    for record in records:
        b_table.insert(parent='', index=END, values=(str(record[0]),str(record[1]),str(record[2]),str(record[3]),str(record[4])))

    conn.close()



def issues():
    f_issue_btn = CTkButton(left_f, text='Issue', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), fg_color='#ffffff', text_color='#2CC985', image=CTkImage(light_image=issue_btn_icon, dark_image=issue_btn_icon), command=issues)
    f_issue_btn.place(x=20, y=300)

    books_btn = CTkButton(left_f, text='Books', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), image=CTkImage(light_image=books_btn_icon, dark_image=books_btn_icon), command=books)
    books_btn.place(x=20, y=240)

    stds_btn = CTkButton(left_f, text='Students', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), image=CTkImage(light_image=stds_btn_icon, dark_image=stds_btn_icon), command=stds)
    stds_btn.place(x=20, y=360)

    published_btn = CTkButton(left_f, text='Published', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), image=CTkImage(light_image=published_btn_icon, dark_image=published_btn_icon), command=published)
    published_btn.place(x=20, y=420)

    global issue_top_f

    issue_top_f = CTkFrame(window, width=400, height=250, fg_color='#ffffff')
    issue_top_f.place(x=290, y=80)

    global issue_bottom_f
    global right_f

    issue_bottom_f = CTkFrame(window, width=1000, height=300, fg_color='#2CC985', border_color='#000000', border_width=5)
    issue_bottom_f.place(x=275, y=425)

    right_f = CTkFrame(window, width=500, height=350, fg_color='#2CC985', border_color='#000000', border_width=5)
    right_f.place(x=730, y=80)

    global issue_book_id
    global issue_std_id

    book_id_label = CTkLabel(issue_top_f, text='Book Id:', font=('Cooper Black', 24, 'bold')).place(x=5, y=20)
    issue_book_id = CTkEntry(issue_top_f, width=250 , font=('Cooper Black', 24), placeholder_text='008')
    issue_book_id.place(x=120, y=17)

    std_id_label = CTkLabel(issue_top_f, text='Lib. Id:', font=('Cooper Black', 24, 'bold')).place(x=10, y=75)
    issue_std_id = CTkEntry(issue_top_f, width=250 , font=('Cooper Black', 24), placeholder_text='230232')
    issue_std_id.place(x=120, y=72)

    issue_book_btn = CTkButton(issue_top_f, text='Issue', text_color='#ffffff', width=360, font=('Cooper Black', 24, 'bold'), command=issuingBook)
    issue_book_btn.place(x=10, y=140)

    receive_book_btn = CTkButton(issue_top_f, text='Receive', text_color='#ffffff', width=360, font=('Cooper Black', 24, 'bold'), command=receivingBook)
    receive_book_btn.place(x=10, y=180)

    if books_top_f is not None:
        books_top_f.destroy()
    if books_bottom_f is not None:
        books_bottom_f.destroy()
    if stds_right_f is not None:
        stds_right_f.destroy()
    if stds_top_f is not None:
        stds_top_f.destroy()
    if published_bottom_f is not None:
        published_bottom_f.destroy()

    b_table = ttk.Treeview(issue_bottom_f, columns=['S.N.', 'Name', 'Id', 'Author', 'Genre'], show='headings')
    b_table.heading('S.N.', text='S.N.', anchor=CENTER)
    b_table.heading('Name', text='Book\'s Name', anchor=CENTER)
    b_table.heading('Id', text='Book Id', anchor=CENTER)
    b_table.heading('Author', text='Author', anchor=CENTER)
    b_table.heading('Genre', text='Genre', anchor=CENTER)
    b_table.pack(padx=5, pady=5, expand=True)

    conn = sqlite3.connect('books.db')
    c=conn.cursor()

    c.execute('SELECT * FROM books_table')
    records = c.fetchall()
    for record in records:
        b_table.insert(parent='', index=END, values=(str(record[0]),str(record[1]),str(record[2]),str(record[3]),str(record[4])))

    conn.close()

    def item_select(_):
        selected_item = b_table.item(b_table.selection())['values']
        issue_book_id.delete(0, END)
        issue_book_id.insert(0, selected_item[2])

    b_table.bind('<<TreeviewSelect>>',  item_select)



    # student table
    s_table = ttk.Treeview(right_f, columns=['f', 'l', 'Id'], show='headings')
    s_table.heading('f', text='First', anchor=CENTER)
    s_table.heading('l', text='Last', anchor=CENTER)
    s_table.heading('Id', text='Lib Id', anchor=CENTER)
    s_table.pack(padx=5, pady=5, expand=True)


    conn = sqlite3.connect('students.db')
    c=conn.cursor()

    c.execute('SELECT * FROM stds_table')
    records = c.fetchall()
    for record in records:
        s_table.insert(parent='', index=END, values=(str(record[1]),str(record[2]),str(record[3])))

    conn.close()

    def std_item_select(_):
        selected_item = s_table.item(s_table.selection())['values']
        issue_std_id.delete(0, END)
        issue_std_id.insert(0, selected_item[2])

    s_table.bind('<<TreeviewSelect>>',  std_item_select)

def stds():
    f_stds_btn = CTkButton(left_f, text='Students', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'),  fg_color='#ffffff', text_color='#2CC985', image=CTkImage(light_image=stds_btn_icon, dark_image=stds_btn_icon), command=stds)
    f_stds_btn.place(x=20, y=360)

    books_btn = CTkButton(left_f, text='Books', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), image=CTkImage(light_image=books_btn_icon, dark_image=books_btn_icon), command=books)
    books_btn.place(x=20, y=240)

    issue_btn = CTkButton(left_f, text='Issue', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), image=CTkImage(light_image=issue_btn_icon, dark_image=issue_btn_icon), command=issues)
    issue_btn.place(x=20, y=300)

    published_btn = CTkButton(left_f, text='Published', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), image=CTkImage(light_image=published_btn_icon, dark_image=published_btn_icon), command=published)
    published_btn.place(x=20, y=420)

    global stds_top_f

    stds_top_f = CTkFrame(window, width=400, height=250, fg_color='#ffffff')
    stds_top_f.place(x=560, y=30)

    global stds_right_f
    global std_fname
    global std_lname
    global std_id

    std_fname_label = CTkLabel(stds_top_f, text='First:', font=('Cooper Black', 24, 'bold')).place(x=20, y=20)
    std_fname = CTkEntry(stds_top_f, width=250 , font=('Cooper Black', 24), placeholder_text='SpongeBob')
    std_fname.place(x=120, y=17)
    
    std_lname_label = CTkLabel(stds_top_f, text='Last:', font=('Cooper Black', 24, 'bold')).place(x=25, y=75)
    std_lname = CTkEntry(stds_top_f, width=250 , font=('Cooper Black', 24), placeholder_text='SquarePants')
    std_lname.place(x=120, y=70)

    std_id_label = CTkLabel(stds_top_f, text='Lib. Id:', font=('Cooper Black', 24, 'bold')).place(x=10, y=127)
    std_id = CTkEntry(stds_top_f, width=250 , font=('Cooper Black', 24), placeholder_text='230232')
    std_id.place(x=120, y=123)


    add_stds_btn = CTkButton(stds_top_f, text='Add', text_color='#ffffff', width=360, font=('Cooper Black', 24, 'bold'), command=addingstds)
    add_stds_btn.place(x=10, y=190)

    if issue_bottom_f is not None:
        issue_bottom_f.destroy()
    if right_f is not None:
        right_f.destroy()
    if books_top_f is not None:
        books_top_f.destroy()
    if issue_top_f is not None:
        issue_top_f.destroy()
    if books_bottom_f is not None:
        books_bottom_f.destroy()
    if published_bottom_f is not None:
        published_bottom_f.destroy()

    

    stds_right_f = CTkFrame(window, width=500, height=350, fg_color='#2CC985', border_color='#000000', border_width=5)
    stds_right_f.place(x=450, y=320)

    
    # student table
    s_table = ttk.Treeview(stds_right_f, columns=['f', 'l', 'Id'], show='headings')
    s_table.heading('f', text='First', anchor=CENTER)
    s_table.heading('l', text='Last', anchor=CENTER)
    s_table.heading('Id', text='Lib Id', anchor=CENTER)
    s_table.pack(padx=5, pady=5, expand=True)

    
    conn = sqlite3.connect('students.db')
    c=conn.cursor()

    c.execute('SELECT * FROM stds_table')
    records = c.fetchall()
    for record in records:
        s_table.insert(parent='', index=END, values=(str(record[1]),str(record[2]),str(record[3])))

    conn.close()


def published():
    published_btn = CTkButton(left_f, text='Published', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'),  fg_color='#ffffff', text_color='#2CC985', image=CTkImage(light_image=published_btn_icon, dark_image=published_btn_icon), command=published)
    published_btn.place(x=20, y=420)

    books_btn = CTkButton(left_f, text='Books', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), image=CTkImage(light_image=books_btn_icon, dark_image=books_btn_icon), command=books)
    books_btn.place(x=20, y=240)

    issue_btn = CTkButton(left_f, text='Issue', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), image=CTkImage(light_image=issue_btn_icon, dark_image=issue_btn_icon), command=issues)
    issue_btn.place(x=20, y=300)

    stds_btn = CTkButton(left_f, text='Students', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), image=CTkImage(light_image=stds_btn_icon, dark_image=stds_btn_icon), command=stds)
    stds_btn.place(x=20, y=360)

    global published_bottom_f

    published_bottom_f = CTkFrame(window, width=1050, height=300, fg_color='#2CC985', border_color='#000000', border_width=5)
    published_bottom_f.place(x=275, y=50)

    if issue_bottom_f is not None:
        issue_bottom_f.destroy()
    if right_f is not None:
        right_f.destroy()
    if books_top_f is not None:
        books_top_f.destroy()
    if issue_top_f is not None:
        issue_top_f.destroy()
    if books_bottom_f is not None:
        books_bottom_f.destroy()
    
    p_table = ttk.Treeview(published_bottom_f, columns=['S.N.', 'b_name', 'b_id', 's_fname', 's_id'], show='headings')
    p_table.heading('S.N.', text='S.N.', anchor=CENTER)
    p_table.heading('b_name', text='Book\'s Name', anchor=CENTER)
    p_table.heading('b_id', text='Book Id', anchor=CENTER)
    p_table.heading('s_fname', text='First Name', anchor=CENTER)
    p_table.heading('s_id', text='Lib Id', anchor=CENTER)
    p_table.pack(padx=5, pady=5, expand=True)

    conn = sqlite3.connect('student_book_pair.db')
    c=conn.cursor()

    c.execute('SELECT * FROM std_book_pair_table')
    records = c.fetchall()
    for record in records:
        p_table.insert(parent='', index=END, values=(str(record[0]),str(record[1]),str(record[2]),str(record[5]),str(record[7])))

    conn.close()

# functions --------



logo = CTkImage(light_image=Image.open('Images/liblogo.png'), dark_image=Image.open('Images/liblogo.png'), size=(190, 190))
lib_logo = CTkLabel(left_f, text='', image=logo)
lib_logo.place(x=5, y=20)

# ------ buttons

books_btn = CTkButton(left_f, text='Books', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), image=CTkImage(light_image=books_btn_icon, dark_image=books_btn_icon), command=books)
books_btn.place(x=20, y=240)

issue_btn = CTkButton(left_f, text='Issue', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), image=CTkImage(light_image=issue_btn_icon, dark_image=issue_btn_icon), command=issues)
issue_btn.place(x=20, y=300)

stds_btn = CTkButton(left_f, text='Students', width=160, font=('Microsoft YaHei UI Light', 23, 'bold'), image=CTkImage(light_image=stds_btn_icon, dark_image=stds_btn_icon), command=stds)
stds_btn.place(x=20, y=360)

# ------ buttons



issues()

window.mainloop()