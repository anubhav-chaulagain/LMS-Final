from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox

win = Tk()
win.config(bg='white')
win.title('Login')
win.geometry('900x500')
win.resizable(False, False)
win.iconbitmap('icons/register_login_signup_icon_219991.ico')

def lib():
    import liv
    

def signingIn():
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()
    c.execute('SELECT *, oid FROM registration_table')
    records = c.fetchall()
    valid_user = bool()

    for record in records:
        if str(record[0])==username.get():
            valid_user = True
            break
        
    conn.commit()
    conn.close()


    if str(username.get()).lower()=='username' :
        messagebox.showerror('Login Error', 'Given credentials can not be username')

    elif str(password.get()).lower()=='password':
         messagebox.showerror('Login Error', 'Given credentials can not be password')

    elif len(str(password.get()))<=8:
        messagebox.showerror('Login Error', 'Password should be greater than 8 characters')

    elif valid_user:
        messagebox.showerror('Login Error', 'Username already exists')

    
    else:
        conn = sqlite3.connect('registration.db')
        c = conn.cursor()

    #     c.execute(
    #         '''
    #     CREATE TABLE registration_table(
    #     username text,
    #     password text
    #     )
    # '''
    # )
        
        c.execute(
            'INSERT INTO registration_table VALUES (:name, :pass)',
            {
                'name':username.get(),
                'pass':password.get()
            }
        )


        conn.commit()
        conn.close()


def logingIn():
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()

    c.execute('SELECT *, oid FROM registration_table')
    records = c.fetchall()
    global login_successful
    login_successful = False

    for record in records:
        if str(record[0])==l_username.get() and str(record[1])==l_password.get():
            login_successful = True
            break
    
    global lib

    if login_successful:
        win.destroy()
        lib()

    else:
        messagebox.showerror('Login Error', 'Given credentials do not match')

    conn.commit()
    conn.close()


# Log In Image and frame

log_img = CTkImage(light_image=Image.open('Images/login.png'), size=(500, 327))
log_label = CTkLabel(win,text='', image=log_img).place(x=50, y=70)


# Log In 

def logIn():

    lm_frame = Frame(win, width=275, height=280, border=0)
    lm_frame.config(background='white')
    lm_frame.place(x=600, y=100)

    log_label = CTkLabel(lm_frame, text='Log In', text_color='#57a1f8', font=('Microsoft YaHei UI Light', 23, 'bold')).place(relx=.4, rely=.05)

    global l_username
    global l_password

    l_username = CTkEntry(lm_frame, placeholder_text='Username', width=175, font=('Microsoft YaHei UI Light', 16), border_width=0)
    l_username.place(x=70, y=70)

    l_password = CTkEntry(lm_frame, placeholder_text='Password', width=175, font=('Microsoft YaHei UI Light', 16), border_width=0)
    l_password.place(x=70, y=110)


    l_btn = CTkButton(lm_frame, text='Log In', width=175, text_color='white',corner_radius=32, hover_color='#1d2a2b',command=logingIn)
    l_btn.place(x=70 , y=160)

    l_dyhaa = CTkLabel(lm_frame, text='Create a new account', text_color='black', font=('Microsoft YaHei UI Light', 12))
    l_dyhaa.place(x=50, y=200)

    # Create a transparent image
    transparent_image = Image.new('RGBA', (1, 1), (0, 0, 0, 0))
    transparent_photo = ImageTk.PhotoImage(transparent_image)

    sign_up_btn = Button(lm_frame, text='Sign In', foreground='#57a1f8', font=('Microsoft YaHei UI Light', 11, 'bold'), background='white', border=0, cursor='hand2', command=signIn)
    sign_up_btn.place(x=180, y=200)



# Log In ------------------------------------------------------------------------------------------------------------------


# Sign Up 
    
def signIn():
    m_frame = Frame(win, width=275, height=280, border=0)
    m_frame.config(background='white')
    m_frame.place(x=600, y=100)

    sign_label = CTkLabel(m_frame, text='Sign In', text_color='#57a1f8', font=('Microsoft YaHei UI Light', 23, 'bold')).place(relx=.4, rely=.05)

    global username
    global password

    username = CTkEntry(m_frame, placeholder_text='Username', width=175, font=('Microsoft YaHei UI Light', 16), border_width=0)
    username.place(x=70, y=70)

    password = CTkEntry(m_frame, placeholder_text='Password', width=175, font=('Microsoft YaHei UI Light', 16), border_width=0)
    password.place(x=70, y=110)


    btn = CTkButton(m_frame, text='Sign In', width=175, text_color='white',corner_radius=32, hover_color='#1d2a2b', command=signingIn)
    btn.place(x=70 , y=160)

    dyhaa = CTkLabel(m_frame, text='Already have an account?', text_color='black', font=('Microsoft YaHei UI Light', 11))
    dyhaa.place(x=50, y=200)

    # Create a transparent image
    transparent_image = Image.new('RGBA', (1, 1), (0, 0, 0, 0))
    transparent_photo = ImageTk.PhotoImage(transparent_image)

    login_btn = Button(m_frame, text='Log In', foreground='#57a1f8', font=('Microsoft YaHei UI Light', 11, 'bold'), background='white', border=0, cursor='hand2', command=logIn)
    login_btn.place(x=180, y=200)

# Sign up ----------------------------------------------------------------------------------------------------------------
signIn()


win.mainloop()