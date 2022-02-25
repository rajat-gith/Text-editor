from cgitb import text
from tkinter import *
import tkinter
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter.tix import WINDOW
from tokenize import Triple
master = Tk()

master.attributes('-fullscreen',True)
master.configure(background='white')
# def save_file():
#     """Save the current file as a new file."""
#     filepath = asksaveasfilename(
#         defaultextension="txt",
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
#     )
#     if not filepath:
#         return
#     with open(filepath, "w") as output_file:
#         text = txt_edit.get(1.0, tkinter.END)
#         output_file.write(text)
#         output_file.close()
#     WINDOW.title(f"Text Editor Application - {filepath}")


def save_file():
        text_file=filedialog.asksaveasfilename(defaultextension=".",initialdir="E:\codebase",title="Save File",filetypes=(("Text Files",".txt"),("HTML Files",".html"),("Python Files",".py"),("ALL Files",".*")))
        if text_file:
            name=text_file
            name=name.replace("E:\codebase","")
            master.title(f'{name}- TextPad!')

            text_file=open(text_file,'w')
            text_file.write(my_text.get(1.0,END))
            text_file.close()


def dt():
    save_file()
    master.destroy()
    
def openNewWindow():
	newWindow = Toplevel(master)
	newWindow.attributes('-fullscreen',True)
	newWindow.configure(background='black')
	Button(newWindow,
		text="SUBMIT CODE",command=dt).pack(pady=10)

def editor():
    openNewWindow()

    edit=Toplevel(master)
    edit.attributes('-fullscreen',True)
    
    e=Entry(edit,bg="#25262d",fg="#ffb229")
    e.pack()
    
    # b=Button(edit,text="save",command=save_file)
    # b.pack(pady=10,side=BOTTOM)

Label(master,text="WELCOME TO THE BLANK CODE CONTEST OF ENIGMA").pack()	

def start():
    btn = Button(master,text ="START CODING",command = editor)
    btn.pack(pady=10,side=BOTTOM)

start()


Button(master,text="QUIT",command=master.destroy).pack()


master.mainloop()
