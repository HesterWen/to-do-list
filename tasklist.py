import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
'''
widthxheight+xposition+yposition
positioned 400 pixels from the left and 100 pixels from the top of the screen
'''
root.resizable(False, False)
'''
the first controls horizontally; the second controls vertically
'''

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    
    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)
        
'''
task_entry.delete(0, END): Clears the content of the task_entry widget
after retrieving the task.
0:starting index
END is a constant provided by Tkinter that represents
the position at the end of the list.
So, listbox.insert(END, task) inserts the task at the end of the listbox.
the with statement here is used for safe file handling, automatically handling
the opening and closing of the file, and ensuring that resources are
managed properly.
'''

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listbox.delete(ANCHOR)

'''
listbox.get(ANCHOR) retrieves the item that is currently selected in the listbox.
ANCHOR is a Tkinter constant representing the currently selected item.
'''

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
          tasks = taskfile.readlines()
        
        for task in tasks:
          if task != '\n':
              task_list.append(task)
              listbox.insert(END, task)
    except:
        file = open('tasklist.txt', 'w')
        file.close()

'''
if~'\n':
If it's not a newline character,
it means there is a task, and the code inside
the if block is executed.
listbox.insert(END, task): Inserts the task into the listbox widget
at the END position.
'''
        
#icon
Image_icon = PhotoImage(file = "images/task.png")
root.iconphoto(False, Image_icon)

#top bar
TopImage = PhotoImage(file = "images/topbar.png")
Label(root, image = TopImage).pack()

dockImage = PhotoImage(file = "images/dock.png")
Label(root, image = dockImage, bg = "#32405b").place(x = 30, y = 25)

'''
bg=background;
"#32405b" is a hexadecimal color code representing a shade of blue.
 #RRGGBB
'''

noteImage = PhotoImage(file = "images/task.png")
Label(root, image = noteImage, bg = "#32405b").place(x = 340, y = 25)

heading = Label(root, text = "All Task", font = "arial 20 bold", fg = "white", bg = "#32405b")
heading.place(x = 130, y = 20)

'''
fg stands for "foreground," and it is used to
set the text color of a widget.
'''
#main
frame = Frame(root, width = 400, height = 50, bg = "white")
frame.place(x = 0, y = 180)

task = StringVar()
task_entry = Entry(frame, width = 18, font = "arial 20", bd = 0)
task_entry.place(x = 10, y = 7)
task_entry.focus()

'''
bd stands for "border." The bd option is used to set the width
of the border around a widget. It controls the size of the border,
which is the space between the interior content of the widget
and its outer edge.
bd=0 sets the border width of the Entry widget to zero,
effectively removing the border. 
'''

button = Button(frame, text = "Add", font = "arial 20 bold", width = 6, bg = "#5a95ff", fg = "#fff", bd = 0, command = addTask)
button.place(x = 300, y = 0)

'''
 addTask function should be called when the button is clicked.
The command parameteressentially associates the function
with the button's click event
'''

#listbox
frame1 = Frame(root, bd = 3, width = 700, height = 280, bg = "#32405b")
frame1.pack(pady = (160, 0))

listbox = Listbox(frame1, font = ('arial', 12), width = 40, height = 16, bg = "#32405b", fg = "white", cursor = "hand2", selectbackground = "#5a95ff")
listbox.pack(side = LEFT, fill = BOTH, padx = 2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side = RIGHT, fill = BOTH)

'''
When the mouse is over the Listbox, the cursor will
change to a hand shape, suggesting to the user that the listbox
is interactive and can be clicked or selected.
"arrow" for a standard arrow cursor, "cross" for a crosshair cursor,etc.
The value "hand2" is commonly used to indicate a clickable
or interactive area
padx is a geometry manager option that stands for "horizontal padding."
when you create a widget using the Button class, you can use the padx
option to control the horizontal padding of the button's text or image
padx=10 means that there will be 10 pixels of padding added on the left
and right sides of the button's text. This extra space helps create
some distance between the text and the edges of the button,
improving the visual appearance.
'''

listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)


openTaskFile()

#delete 
Delete_icon = PhotoImage(file = "images/delete.png")
Button(root, image = Delete_icon, bd = 0, command = deleteTask).pack(side = BOTTOM, pady = 13)

'''
pack() method is a geometry manager that organizes widgets in blocks
before placing them in the parent widget. When you call pack() on a widget,
it causes the widget to be displayed and fitted to its content,
and it adjusts the size of the parent widget accordingly.
.pack(side=BOTTOM, pady=13): Calls the pack() method on the Button widget
and specifies the packing options.
side=BOTTOM means that the widget will be packed at the bottom of
its parent widget.
'''

root.mainloop()
