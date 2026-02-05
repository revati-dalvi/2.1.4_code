#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as Authentication

# main window
root = Authentication.Tk()
root.wm_geometry("300x300")

# 4) changing the title 
root.title("Secure GUI")

#5) add code before entering mainloop 
frame_login = Authentication.Frame(root)

#6+15) create grid by calling method/updating it 
frame_login.grid(row=0, column=0, sticky="news") 

#16) creating 


#7) creating lable widegt 
lbl_username = Authentication.Label(frame_login, text='Username:')
lbl_username.pack()

# 12) adding entery widget for username 
ent_username = Authentication.Entry(frame_login, bd=3)
ent_username.pack(padx=50, pady=10)

#9) adding frame_login and text option w/ font matching above 
lbl_password = Authentication.Label(frame_login,text="Password:",) 
lbl_password.pack()

#13) adding entery widget for password 
ent_password = Authentication.Entry(frame_login, bd=3, show="*")
ent_password.pack(padx=50, pady=10)




'''#14) adding a button program called log in 
btn_login = Authentication.Button (root, text="Login")
btn_login.grid(row=10, column=0, padx=50, pady=20)'''

root.mainloop()