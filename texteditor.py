from distutils import text_file
from tkinter import *
from tkinter import filedialog
from tkinter import font
import time
from unicodedata import name


def text_editor():
    root = Tk()
    root.title("Code Editor")
    root.geometry("1220x660")
    my_frame=Frame(root)
    my_frame.pack(pady=5)
    root.attributes('-fullscreen',True) 

    text_scroll=Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT,fill=Y)

    my_text=Text(my_frame,width=150,height=30,font=("Helvetica",16),selectbackground="yellow",selectforeground="black",undo=True,yscrollcommand=text_scroll.set)
    my_text.pack(pady=10)

    text_scroll.config(command=my_text.yview)

    my_menu=Menu(root)
    root.config(menu=my_menu)

    def save_as_file():
        text_file=filedialog.asksaveasfilename(defaultextension=".*",initialdir="E:\codebase",title="Save File",filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("Python Files","*.py"),("ALL Files",".*")))
        if text_file:
            name=text_file
            name=name.replace("E:\codebase","")
            root.title(f'{name}- TextPad!')

            text_file=open(text_file,'w')
            text_file.write(my_text.get(1.0,END))
            text_file.close()
    """clock_label=Label(my_frame,font=("Helvetica",30),text="Hello")
    clock_label.pack()
    clock_label.place(relx = 0.97,rely = 0.03,anchor = 'ne')"""
    b1=Button(my_frame, text="Quit", command=root.destroy)
    b1.pack(side=BOTTOM,padx=15,pady=15)
    b2=Button(my_frame,text="Save",command=save_as_file).pack()
    root.mainloop()


    
def splash_screen():
    root1 = Tk()
    root1.title("Code Editor")
    my_frame1=Frame(root1)
    my_frame1.pack(pady=5)
    root1.attributes('-fullscreen',True) 
    b1=Button(my_frame1,text="START CODING",command=text_editor)
    b1.pack()
    b2=Button(my_frame1,text="QUIT",command=root1.destroy)
    b2.pack(side=BOTTOM,padx=15,pady=405)
    root1.mainloop()

def main():
    splash_screen()
main()