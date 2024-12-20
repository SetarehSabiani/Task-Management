from ttkbootstrap import Window, Button, Label, LabelFrame, Separator, Frame, PRIMARY, SUCCESS, DANGER, \
   WARNING, Notebook
# from tkinter.ttk import Style
from PresentationLayer.frame1 import Frame1
# --------Window~
theme = ["journal", "darkly"]
# style=Style(theme[0])
window = Window(title="Task Management",themename=theme[0],  iconphoto="image/todolist.png")
# window.style(style)
window.geometry("1200x700")
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

task_label = Label(window, text="TASK MANAGEMENT", font=('Helvetica', 20), bootstyle="info", padding=10)
task_label.grid(row=0, column=0)
# --------Theme
theme_frame = LabelFrame(text="Theme")
theme_frame.grid(row=0, column=6)

# Help for change theme
def change_to_light():
    pass

def change_to_dark():
    window.configure()

button_light = Button(theme_frame, text="Light", bootstyle="light",command=change_to_light)
button_light.grid(row=0, column=0, padx=10, pady=10, sticky="e")

button_dark = Button(theme_frame, text="dark", bootstyle="dark",command=change_to_dark)
button_dark.grid(row=0, column=1, padx=10, sticky="w")

# ---------Frame

notebook = Notebook(window, bootstyle=DANGER)
notebook.grid(row=1, column=0, columnspan=5, pady=10, padx=20, sticky="nsew")
frame1 = Frame(notebook)
frame2 = Frame(notebook)
frame3 = Frame(notebook)
label2 = Label(frame2, text="This is Frame 2")
label2.grid(row=0, column=0, pady=10, padx=20)
label3 = Label(frame3, text="This is Frame 3")
label3.grid(row=0, column=0, pady=10, padx=20)
notebook.add(frame1, text='All Task')
notebook.add(frame2, text='Tab 2')
notebook.add(frame3, text='Tab 3')

Frame1(frame1)


button_frame = LabelFrame(text="Button Menu")
button_frame.grid(row=1, column=6, rowspan=4, pady=10, padx=20, sticky="nsew")

add_button = Button(button_frame, text="Add Task", bootstyle=PRIMARY)
add_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
update_button = Button(button_frame, text="Update Task", bootstyle=WARNING)
update_button.grid(row=1, column=1, padx=10, pady=(0, 10))
delete_button = Button(button_frame, text="Delete Task", bootstyle=DANGER)
delete_button.grid(row=2, column=1, pady=(0, 10))
done_button = Button(button_frame, text="Task Done", bootstyle=SUCCESS)
done_button.grid(row=3, column=1, pady=(0, 10))

window.mainloop()
