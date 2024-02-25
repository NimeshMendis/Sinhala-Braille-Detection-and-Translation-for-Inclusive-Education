import tkinter as tk
import cv2
from tkinter import ttk
from tkinter import *
import customtkinter
from customtkinter import *
from PIL import Image, ImageTk

from texttobraille import *
from preprocess import filter
from translate import translate
from firebase import *

# set color and themes
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# root window
root = customtkinter.CTk()
root.geometry(f"{1280}x{720}")
root.title('Braille Translation')


# configure the tabs
style = ttk.Style()
style.layout('Tabless.TNotebook.Tab', []) # new style with tabs turned off
tabControl = ttk.Notebook(root, style='Tabless.TNotebook') #hide the tab bar

tab1 = CTkFrame(tabControl)
tab2 = CTkFrame(tabControl)

tabControl.add(tab1, text ='Text to Braille')
tabControl.add(tab2, text ='Braille to Text')
tabControl.pack(expand = 1, fill ="both")


# function for changing tabs
def newtab(tabname):
    tabControl.select(tabname)


# function for combo box
def combobox_callback(choice):
    print(choice)


# theme change function
def theme_switch():
    customtkinter.set_appearance_mode(theme_switch_var.get())


# translation function for text o braille translation
def translateToBraille():

    # get input from textbox
    inp = plain_textbox.get(1.0, "end-1c")
    print(inp)

    # call translate functions
    txt = normalize(inp)
    out, _ = translate_to_braille(txt)
    print("Normalized =", txt)
    print("Translated =", out)

    # display normalized output

    normalize_textbox.configure(state='normal')
    normalize_textbox.delete("1.0", "end")
    normalize_textbox.insert('end', txt)
    normalize_textbox.configure(state='disabled')

    # display the translation output
    braille_textbox.configure(state='normal')
    braille_textbox.delete("1.0", "end")
    braille_textbox.insert('end', out)
    braille_textbox.configure(state='disabled')


# functions for display and reset on braille display
def display():
    inp = plain_textbox.get(1.0, "end-1c")
    db.child("IOTGreenhouse").update({"braille": inp})
    db.child("IOTGreenhouse").update({"braille_display": "true"})
    print(inp)

def reset():
    db.child("IOTGreenhouse").update({"braille_reset": "true"})
    print("RESET")


# function for inserting image and sending it to translation
def select_image():
    global panelA
    language = combobox.get()
    path = filedialog.askopenfilename()
    if len(path) > 0:
        image = cv2.imread(path)
        filter(image)

        image2 = cv2.imread('temp_storage/sinhalaprocessed.jpg')
        image3, translated_text = translate(image2, language)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)

        width, height = image.size
        image = image.resize((int(800), int(height * 700/width)), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)


        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        image2 = Image.fromarray(image2)
        image2 = image2.resize((int(800), int(height * 700 / width)), Image.LANCZOS)
        image2 = ImageTk.PhotoImage(image2)

        image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2RGB)
        image3 = Image.fromarray(image3)
        image3 = image3.resize((int(800), int(height * 700 / width)), Image.LANCZOS)
        image3 = ImageTk.PhotoImage(image3)


        if panelA is None:
            # the panels are not used but the canvas does not update without them
            panelA = Label(tab2, image=image)
            panelA.image = image
            panelA = Label(tab2, image=image2)
            panelA.image = image2
            panelA = Label(tab2, image=image3)
            panelA.image = image3

            canvas.delete("all")
            canvas2.delete("all")
            canvas3.delete("all")
            canvas.create_image(10, 10, anchor=NW, image=image)
            canvas2.create_image(10, 10, anchor=NW, image=image2)
            canvas3.create_image(10, 10, anchor=NW, image=image3)

            final_textbox.configure(state='normal')
            final_textbox.delete("1.0", "end")
            final_textbox.insert('end', translated_text)
            final_textbox.configure(state='disabled')
            panelA = None

        else:
            # update the panels
            panelA.configure(image=image)
            panelA.image = image


# configure tab 1 grid
tab1.columnconfigure(0, weight=0)
tab1.columnconfigure(1, weight=3)
tab1.columnconfigure(2, weight=0)
tab1.rowconfigure(0, weight=0)
tab1.rowconfigure(1, weight=1)
tab1.rowconfigure(2, weight=0)
tab1.rowconfigure(3, weight=1)
tab1.rowconfigure(4, weight=0)
tab1.rowconfigure(5, weight=1)


# create sidebar and objects inside for tab 1
sidebar = customtkinter.CTkFrame(tab1, width=20, corner_radius=0)
sidebar.grid(column=0, row=0, rowspan=6, padx=(0,20), sticky="nsew")

logo_label = customtkinter.CTkLabel(sidebar, text="Text to Braille", font=customtkinter.CTkFont(size=20, weight="bold"),
                                    anchor=CENTER)
logo_label.grid(column=0, row=0, padx=20, pady=(20, 10))

button1 = customtkinter.CTkButton(sidebar, text="Change tab", font= ("TkDefaultFont", 12, "bold"), command= lambda: newtab(tab2), anchor=CENTER)
button1.grid(column=0, row=1, padx=40, pady=5, sticky="nsew")

button2 = customtkinter.CTkButton(sidebar, text="Translate", font= ("TkDefaultFont", 12, "bold"), command= lambda: translateToBraille(), anchor=CENTER)
button2.grid(column=0, row=2, padx=40, pady=5, sticky="n")

theme_switch_var = customtkinter.StringVar(value="Dark")
theme_switch = customtkinter.CTkSwitch(sidebar, text="Dark mode", command=theme_switch, variable=theme_switch_var,
                                       onvalue="Dark", offvalue="Light")
theme_switch.grid(column=0, row=3, padx=40, pady=20, sticky="s")
sidebar.rowconfigure(2, weight=1)


# main section of tab 1
plain_label = CTkLabel(tab1, text="Enter text to translate:", font=("Helvetica", 15, "bold"),
                       width=20)
plain_label.grid(column=1, row=0, sticky="nw", padx=10, pady=2)


plain_textbox = customtkinter.CTkTextbox(tab1, width=200, height=300, font=("Helvetica", 30))
plain_textbox.grid(column=1, row=1, sticky="nsew", padx=5, pady=10)

normalize_label = CTkLabel(tab1, text="Normalized text:", font=("Helvetica", 15, "bold"))
normalize_label.grid(column=1, row=2, sticky="nw", padx=10, pady=2)

normalize_textbox = customtkinter.CTkTextbox(tab1, width=200, height=300, state=DISABLED, font=("Helvetica", 30))
normalize_textbox.grid(column=1, row=3, sticky="nsew", padx=5, pady=10)

braille_label = CTkLabel(tab1, text="Translated text:", font=("Helvetica", 15, "bold"))
braille_label.grid(column=1, row=4, sticky="nw", padx=10, pady=2)

braille_textbox = customtkinter.CTkTextbox(tab1, width=200, height=300, state=DISABLED, font=("Helvetica", 30))
braille_textbox.grid(column=1, row=5, sticky="nsew", padx=5, pady=10)


# right section of tab 1

sidebar_right = customtkinter.CTkFrame(tab1, width=20, corner_radius=0)
sidebar_right.grid(column=2, row=0, rowspan=6, padx=(20,0), sticky="nsew")

display_label = CTkLabel(sidebar_right, text="Braille Display:", font=("Helvetica", 15, "bold"),
                       width=20)
display_label.grid(column=0, row=1, sticky="n", padx=40, pady=(10,50))

button_display = customtkinter.CTkButton(sidebar_right, text="Display", font= ("TkDefaultFont", 12, "bold"),
                                         command= lambda: display(), anchor=CENTER, fg_color="green")
button_display.grid(column=0, row=2, padx=40, pady=5, sticky="n")

button_reset = customtkinter.CTkButton(sidebar_right, text="Reset", font= ("TkDefaultFont", 12, "bold"),
                                       command= lambda: reset(), anchor=CENTER, fg_color="red")
button_reset.grid(column=0, row=3, padx=40, pady=5, sticky="n")

about_label = CTkLabel(sidebar_right, text="A project by \nComputational Intelligence \nand Robotics (CIR) "
                                           "\nresearch group at \nSri Lanka Technological Campus", font=("Helvetica", 20, "bold"), width=5)
about_label.grid(column=0, row=4, sticky="nw", padx=40, pady=(50, 5))


# tab 2 starts here


# configure tab 1 grid
tab2.columnconfigure(0, weight=0)
tab2.columnconfigure(1, weight=1)
tab2.columnconfigure(2, weight=1)
tab2.rowconfigure(0, weight=1)
tab2.rowconfigure(1, weight=1)
tab2.rowconfigure(2, weight=1)
tab2.rowconfigure(3, weight=1)
tab2.rowconfigure(4, weight=1)
tab2.rowconfigure(5, weight=1)


# create sidebar and objects inside for tab 2
sidebar2 = customtkinter.CTkFrame(tab2, width=20, corner_radius=0)
sidebar2.grid(column=0, row=0, rowspan=4, sticky="nsew")

logo_label2 = customtkinter.CTkLabel(sidebar2, text="Braille to Text ", font=customtkinter.CTkFont(size=20, weight="bold"))
logo_label2.grid(column=1, row=0, padx=20, pady=(20, 10))

# button for changing tab
tab2_button1 = customtkinter.CTkButton(sidebar2, text="Change tab", font = ("TkDefaultFont", 12, "bold"), command= lambda: newtab(tab1))
tab2_button1.grid(column=1, row=1, padx=40, pady=5, sticky="nsew")


# button for inserting image
insert_button1 = customtkinter.CTkButton(sidebar2, text="Insert", font = ("TkDefaultFont", 12, "bold"), command= select_image)
insert_button1.grid(column=1, row=2, padx=40, pady=5, sticky="nsew")


# drop down for language and method selection
combobox_var = customtkinter.StringVar(value="Sinhala")  # set initial value
combobox = customtkinter.CTkComboBox(master=sidebar2,
                                     values=["Sinhala", "English", "English(CNN)"],
                                     command=combobox_callback,
                                     variable=combobox_var)

combobox.grid(column=1, row=3, padx=40, pady=5, sticky="nsew")


# middle section for tab 2

panelA = None

canvas_label = CTkLabel(tab2, text="Original Image:", font=("Helvetica", 15, "bold"))
canvas_label.grid(column=1, row=0, sticky="nw", padx=10, pady=2)

canvas = Canvas(tab2, width=800, height=400, bg = "#FFFDD0")
canvas.grid(column=1, row=1, columnspan=1, sticky="nw", padx=10, pady=2)

canvas2_label = CTkLabel(tab2, text="Preprocessed Image:", font=("Helvetica", 15, "bold"))
canvas2_label.grid(column=2, row=0, sticky="nw", padx=10, pady=2)

canvas2 = Canvas(tab2, width=800, height=400, bg = "#FFFDD0")
canvas2.grid(column=2, row=1, columnspan=1, sticky="nw", padx=10, pady=2)

canvas3_label = CTkLabel(tab2, text="Detected Cells:", font=("Helvetica", 15, "bold"))
canvas3_label.grid(column=1, row=2, sticky="nw", padx=10, pady=2)

canvas3 = Canvas(tab2, width=800, height=400, bg = "#FFFDD0")
canvas3.grid(column=1, row=3, columnspan=1, sticky="nw", padx=10, pady=2)

canvas4_label = CTkLabel(tab2, text="Normalized Translation:", font=("Helvetica", 15, "bold"))
canvas4_label.grid(column=2, row=2, sticky="nw", padx=10, pady=2)

final_textbox = customtkinter.CTkTextbox(tab2, width=20, height=10, state=DISABLED, font=("Helvetica", 40), fg_color ="#FFFDD0", text_color ="Black")
final_textbox.grid(column=2, row=3, sticky="nsew", padx=5, pady=2)


root.mainloop()
