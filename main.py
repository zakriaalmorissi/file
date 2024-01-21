
import tkinter as tk 
from tkinter import ttk 
from PIL import Image,ImageTk
import csv
from tkinter import filedialog




app = tk.Tk()
app.geometry("1450x850+50+50")
app.resizable(True,True)

# frames
frame_1= tk.Frame(app,bg='lightblue')
frame_1.place(relheight=1,relwidth=0.055,relx=0.0,rely=0.0)
frame_2 = tk.Frame(app,bg='gray')
frame_2.place(relheight=0.9,relwidth=0.5,relx=0.060,rely=0.075)
frame_3 = tk.Frame(app,bg='lightblue')
frame_3.place(relheight=0.9,relwidth=0.4,relx=0.58,rely=0.075)
frame_4 = tk.Frame(app,bg="white",height=46,width=405)
frame_4.place(relx=0.060,rely=0.0)

# buttons


home_button = tk.Button(frame_1,text="Home",width=10,relief=tk.GROOVE)
home_button.place(relwidth=1,relx=0.0,rely=0.1)

statics_button = tk.Button(frame_1, text="Statics",width=10,relief=tk.GROOVE)
statics_button.place(relwidth=1,relx=0.0,rely=0.2)

orders_button = tk.Button(frame_1,text="Orders",width=10,relief=tk.GROOVE)
orders_button.place(relwidth=1,relx=0.0,rely=0.3)

setting_button = tk.Button(frame_1, text="Setting", width=10,relief=tk.GROOVE)
setting_button.place(relwidth=1,relx=0.0, rely=0.370)


# search bar widgets

search_image = ImageTk.PhotoImage(Image.open("images/bar.png"))
tk.Label(frame_4,image=search_image).place(relx=0.0,rely=0.0)

search_entry = tk.Entry(frame_4,width=45,background="white",bd=0)
search_entry.place(relx=0.025,rely=0.25)

search_icon = ImageTk.PhotoImage(Image.open("images/search_icon.png"))
search_button = tk.Button(frame_4,image=search_icon,width=23,bd=0)
search_button.place(relx=0.898,rely=0.21)



tk.Label(app, text="Categories",width=21,font=("Arial Bold",9),bg="white").place(relheight=0.030,relwidth=0.060,relx=0.061,rely=0.075)
tk.Label(app, text="Cart",width=20,font=("Arial Bold",11)).place(relx=0.72,rely=0.070)
tk.Label(frame_2,text="___________",bg="white").place(relx=0.0,rely=0.034,relwidth=1,relheight=0.0014)


# ------categories buttons-----

# function to display a new frame for the menu and its widgets
def frame_change():
    # remove button_7 from the parent Frame
    button_7.place_forget()
    # new frame for the menu
    menu_frame = tk.Frame(frame_2,bg="white")
    menu_frame.place(relheight=0.95,relwidth=1,relx=0.0,rely=0.035)

    # Treeview for displaying data 
    treeview = ttk.Treeview(menu_frame,columns=["Meal name","Meal price","Meal quantity"],show="headings")
    # headings
    treeview.heading("Meal name",text="Meal Name")
    treeview.heading("Meal price",text="Meal Price")
    treeview.heading("Meal quantity",text="Meal Quantity")

    # columns 
    treeview.column("Meal name",width=150,anchor=tk.CENTER)
    treeview.column("Meal price",width=150,anchor=tk.CENTER)
    treeview.column("Meal quantity",width=150,anchor=tk.CENTER)

    treeview.pack(fill="both",expand=True)

    def back():
        button.place_forget()
        menu_frame.place_forget()
        button_7.place(relwidth=0.15,relheight=0.033,relx=0.851,rely=0.0)


    button = tk.Button(frame_2,text="Go back",width=14,bd=0,activebackground="#FF0000",relief=tk.GROOVE,command=back)
    button.place(relwidth=0.15,relheight=0.033,relx=0.851,rely=0.0)






            

button_0 = tk.Button(frame_2,text="",width=14,bg='white',bd=0)
button_0.place(relwidth=0.113,relheight=0.033,relx=0.125,rely=0.0)

button_1 = tk.Button(frame_2,text="",width=14,bg='white',bd=0)
button_1.place(relwidth=0.1,relheight=0.033,relx=0.240,rely=0.0)

button_2 = tk.Button(frame_2,text="",width=14,bg='white',bd=0)
button_2.place(relwidth=0.1,relheight=0.033,relx=0.342,rely=0.0)


button_3 = tk.Button(frame_2,text="",width=14,bg='white',bd=0)
button_3.place(relwidth=0.1,relheight=0.033,relx=0.443,rely=0.0)

button_4 = tk.Button(frame_2,text="",width=14,bg='white',bd=0)
button_4.place(relwidth=0.1,relheight=0.033,relx=0.545,rely=0.0)


button_5 = tk.Button(frame_2,text="",width=14,bg='white',bd=0)
button_5.place(relwidth=0.1,relheight=0.033,relx=0.647,rely=0.0)


button_6 = tk.Button(frame_2,text="",width=14,bg='white',bd=0)
button_6.place(relwidth=0.1,relheight=0.033,relx=0.749,rely=0.0)

button_7 = tk.Button(frame_2,text="Go to Menu",width=14,bd=0,activebackground="#FF0000",
                     relief=tk.GROOVE,command=frame_change)
button_7.place(relwidth=0.15,relheight=0.033,relx=0.854,rely=0.0)


def cotegory_names():
    names = []
    with open("file.csv") as file :
                files = file.readlines() 
                for num in files:
                    num = num.strip()
                    names.append(num)
                if len(names) == 1:
                    button_0.config(text=names[0])

                elif len(names) == 2:
                    button_0.config(text=names[0])
                    button_1.config(text=names[1])


                elif  len(names) == 3:
                    button_0.config(text=names[0])
                    button_1.config(text=names[1])
                    button_2.config(text=names[2])
                
                elif  len(names) == 4:
                    button_0.config(text=names[0])
                    button_1.config(text=names[1])
                    button_2.config(text=names[2])
                    button_3.config(text=names[3])
                
                elif  len(names) == 5:
                    button_0.config(text=names[0])
                    button_1.config(text=names[1])
                    button_2.config(text=names[2])
                    button_3.config(text=names[3])
                    button_4.config(text=names[4])
                print(len(names))   



#_____________________________________________________________________________________________________________            


# add button for the categories 
load_image= ImageTk.PhotoImage(Image.open("images/add_2.jpeg"))
def add():
    # Toplevel window for the user to create cotegories and inserting products
    window = tk.Toplevel(app)
    window.geometry("500x500+260+200")
    window.title("Cotegories")
    window.resizable(False,False)
    window.config(background="gray")
    # entries widgets
    tk.Label(window,text="Cotegory name:",font=("Microsoft Yahei UI Light",11),bg="lightblue").place(x=5,y=10)
    name_entry = tk.Entry(window)
    name_entry.place(x=140,y=12)

    tk.Label(window,text="Meal name:",font=("Microsoft Yahei UI Light",11),bg="lightblue").place(x=5,y=60)
    title = tk.Entry(window,width=40)
    title.place(x=110,y=65)

    tk.Label(window,text="Meal price:",font=("Microsoft Yahei UI Light",11),bg="lightblue").place(x=5,y=120)
    price = tk.Entry(window)
    price.place(x=100,y=125)

    # image button
    tk.Label(window,text="Select Image  (optional):",background="white",font=("Microsoft Yahie UI Light",11)).place(x=5,y=220)
    open_image = tk.Button(window,image=load_image)
    open_image.place(x=20,y=250)


    def save():
        names = []
        print(names)
        name = name_entry.get()
        name = name.strip()
        cotegory_names()

        with open("file.csv") as file :
            files = file.readlines()
            
            for num in files:
                num = num.strip()
                names.append(num)

        if name in names:
            cotegory_names()
          
        if name:
            with open("file.csv","a") as file:
                file = file.write(f"{name}\n")
            cotegory_names()

    save_button = tk.Button(window,text="Save",width=12,relief=tk.GROOVE,command=save)
    save_button.place(x=390,y=450)

    cancel_button = tk.Button(window,text="Cancel",width=12,relief=tk.GROOVE,command=window.destroy)
    cancel_button.place(x=280,y=450)
#_________________________________________----------------------______________________________________________________________________


add_image = ImageTk.PhotoImage(Image.open("images/add_1.jpeg"))
add_button = tk.Button(frame_2,image=add_image,relief=tk.GROOVE,command=add)
add_button.place(relx=0.0060,rely=0.041)








cotegory_names()
app.mainloop()
