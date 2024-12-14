import customtkinter as ctk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from Modules.wdata import *
from Modules.build import build
from Modules.debug import *

# ------------------------------------------------------------------------------ #

class Variables:
    mcolor = "#2a2a2b"
    bobico = "Files/Images/bobthebuilder.ico"

    white = "white"

# ------------------------------------------------------------------------------ #

var = Variables()
root = ctk.CTk()
root.title("Bob The Builder")
root.geometry("850x520")
root.config(
    bg=var.mcolor
)
root.iconbitmap(var.bobico)

# ------------------------------- UI ------------------------------------------- #

tabs = ctk.CTkTabview(root)
tabs.pack(fill="both", expand=True)

tabs.add("Home")
home = tabs.tab("Home")
tabs.add("Templates")
templates = tabs.tab("Templates")
tabs.add("Builder")
builder = tabs.tab("Builder")

class UI:
    def __init__(self):
        pass

    def home(self):
        welc = Label(home, text="Bob The Builder 1.0", bg=var.mcolor, fg=var.white, font=("bold", 15))
        welc.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    def templates(self):
        inf = Label(templates, text="Select a Template", bg=var.mcolor, fg=var.white, font=("bold", 15))
        inf.pack(side="bottom")

        def wtemp(sel):
            writeTEMPLATE(sel,)

        tmps = ["Basic | Payload: JSON", "Basic | Payload: URL Format"]
        dropdown = ctk.CTkOptionMenu(templates, values=tmps, command=wtemp)
        dropdown.place(x=20, y=20)

    def builder(self):
        name = ctk.CTkEntry(builder, placeholder_text="Checker's Name")
        name.place(x=10, y=170)

        api1 = ctk.CTkEntry(builder, placeholder_text="API #1")
        api1.place(x=10, y=55)
        api2 = ctk.CTkEntry(builder, placeholder_text="API #2")
        api2.place(x=10, y=115)

        good1 = ctk.CTkEntry(builder, placeholder_text="Success Message")
        good1.place(x=170, y=55)

        bad1 = ctk.CTkEntry(builder, placeholder_text="Bad Message")
        bad1.place(x=330, y=55)

        userF = ctk.CTkEntry(builder, placeholder_text="User Field Name")
        userF.place(x=170, y=115)
        passF = ctk.CTkEntry(builder, placeholder_text="Password Field Name")
        passF.place(x=330, y=115)

        def bld():
            name_ = name.get()

            api1_ = api1.get()
            api2_ = api2.get()

            good1_ = good1.get()
            bad1_ = bad1.get()

            user_ = userF.get()
            pass_ = passF.get()

            if verifyAPI(api1_) == False:
                messagebox.showerror(title="Error", message="Invalid API")
                return

            with open("Files/template.json", "r") as f:
                d_ = json.load(f)
                template = d_['template']
            basic = ["Basic | Payload: JSON", "Basic | Payload: URL Format"]

            if template in basic:
                if build(api1_, good1_, bad1_, user_, pass_, name_) == False:
                    messagebox.showerror(title="Error", message="Make sure you have selected a template and don't leave out the text boxes empty")
                

        build_ = ctk.CTkButton(builder, text="Build", command=bld)
        build_.pack()

    def main(self):
        self.home()
        self.templates()
        self.builder()

        root.mainloop()

# ------------------------------------------------------------------------------ #