from tkinter import *
from tkinter import messagebox
from tkinter import Menu,Tk,Frame
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename,asksaveasfile

#For adding new tasks in the list
def new():
    object=adder.get()
    if object!="":
        box.insert(END,object)
        adder.delete(0,"end")
    else:
        messagebox.showwarning("Warning!","Please enter something\nI need to work😔")
#for removing particular tasks of a list
def delete():
    selected_items = box.curselection()
  
    for selected_object in selected_items[::-1]:
        box.delete(selected_object)

t=Tk()
t.title("My To Do List")
frame= Frame(t)
frame.pack()
box=Listbox(frame,width=30,height=10,font=('Times New Roman',21),activestyle=NONE,selectmode=MULTIPLE)
box.pack(side=LEFT,fill=BOTH)

#Making the list of tasks
List=[]
for objects in List:
    box.insert(END,objects)

#for scrolling tasks in a list
scrolly=Scrollbar(frame)
scrolly.pack(side=RIGHT,fill=Y)

#entry box for entering new items to the list
adder=Entry(t,font=('Arial',18))
adder.pack()

#frame for buttons
button=Frame(t)
button.pack()

#button for adding tasks to the list
Addbutton=Button(button,text="Add stuff",command=new,font=("Times New Roman",18),bg='light green')
Addbutton.pack(fill=BOTH,expand=True,side=LEFT)

#button for deleting particular tasks in the list
Removebutton=Button(button,text="Remove stuff",command=delete,font=("Times New Roman",18),bg='red')
Removebutton.pack(fill=BOTH,expand=True,side=RIGHT)

#save as option
def SaveAs():
    file= filedialog.asksaveasfilename(filetypes=[("txt file",".txt")],defaultextension=".txt",initialdir="G:\My Drive\To Do Lists")
    if file:
        store= open(file,'w')#creates a file object
        store.write()
        store.close()
    else:
        print("File not chosen")
#open option
def Open():
    file=filedialog.askopenfilename(filetypes=[("txt file",".txt")],defaultextension=".txt",initialdir="G:\My Drive\To Do Lists")
    store= open(file,'w')
    store.write()
    store.close()

#Save option
def Save():
    file= filedialog.asksaveasfile(filetypes=[("txt file",".txt")],defaultextension=".txt",initialdir="G:\My Drive\To Do Lists")
    if file:
        store= open(file,'w')
        store.write()
        store.close()
    else:
        print("File not chosen")
#creating menu option 
Menuoption = Menu(t)
t.config(menu=Menuoption)

#creating file menu
Files = Menu(Menuoption, tearoff=0)
Files.add_command(label='Open',command= Open)
Files.add_command(label='Save',command= Save)
Files.add_command(label='Save As',command= SaveAs)
Files.add_separator()

#creating exit menu
Files.add_command(label='Exit',command=t.destroy)

#adding file menu to menu option
Menuoption.add_cascade(label="File",menu=Files)

t.mainloop()
