
from ttkbootstrap import Window, Button, PRIMARY, SUCCESS, WARNING, INFO, DANGER, OUTLINE, Checkbutton, BooleanVar, \
    TOOLBUTTON, TOGGLE, ROUND, SQUARE, Combobox, DateEntry, Floodgauge, VERTICAL, HORIZONTAL, Label, LabelFrame, Meter, \
    Notebook, Frame, Progressbar, STRIPED, Radiobutton, StringVar

window = Window(title="Sample", iconphoto="images/InstaPhoto.png", themename="darkly")

primary_button = Button(window, text="Primary", bootstyle=PRIMARY)
primary_button.grid(row=0, column=0, pady=10, padx=20)

success_button = Button(window, text="Success", bootstyle=SUCCESS)
success_button.grid(row=0, column=1, pady=10, padx=20)

warning_button = Button(window, text="Warning", bootstyle=WARNING)
warning_button.grid(row=0, column=2, pady=10, padx=20)

info_button = Button(window, text="Info", bootstyle=INFO)
info_button.grid(row=0, column=3, pady=10, padx=20)

danger_button = Button(window, text="Danger", bootstyle=DANGER)
danger_button.grid(row=0, column=4, pady=10, padx=20)

outline_primary_button = Button(window, text="Primary", bootstyle=OUTLINE + PRIMARY)
outline_primary_button.grid(row=1, column=0, pady=10, padx=20)

outline_success_button = Button(window, text="Success", bootstyle=OUTLINE + SUCCESS)
outline_success_button.grid(row=1, column=1, pady=10, padx=20)

outline_warning_button = Button(window, text="Warning", bootstyle=OUTLINE + WARNING)
outline_warning_button.grid(row=1, column=2, pady=10, padx=20)

outline_info_button = Button(window, text="Info", bootstyle=OUTLINE + INFO)
outline_info_button.grid(row=1, column=3, pady=10, padx=20)

outline_danger_button = Button(window, text="Danger", bootstyle=OUTLINE + DANGER)
outline_danger_button.grid(row=1, column=4, pady=10, padx=20)

primary_checkbutton = Checkbutton(window, text="Primary", bootstyle=PRIMARY)
primary_checkbutton.grid(row=2, column=0, pady=10, padx=20)

success_checkbutton = Checkbutton(window, text="Success", bootstyle=SUCCESS)
success_checkbutton.grid(row=2, column=1, pady=10, padx=20)

warning_checkbutton = Checkbutton(window, text="Warning", bootstyle=WARNING)
warning_checkbutton.grid(row=2, column=2, pady=10, padx=20)

info_checkbutton = Checkbutton(window, text="Info", bootstyle=INFO)
info_checkbutton.grid(row=2, column=3, pady=10, padx=20)

danger_variable = BooleanVar(value=True)

danger_checkbutton = Checkbutton(window, text="Danger", variable=danger_variable, bootstyle=DANGER)
danger_checkbutton.grid(row=2, column=4, pady=10, padx=20)


def show_danger_value():
    print(danger_variable.get())
    danger_variable.set(not danger_variable.get())


submit_button = Button(window, text="Get Danger Value", command=show_danger_value)
submit_button.grid(row=2, column=5, pady=10, padx=20)

primary_checkbutton = Checkbutton(window, text="Primary", bootstyle=TOOLBUTTON + PRIMARY)
primary_checkbutton.grid(row=3, column=0, pady=10, padx=20)

success_checkbutton = Checkbutton(window, text="Success", bootstyle=TOOLBUTTON + SUCCESS)
success_checkbutton.grid(row=3, column=1, pady=10, padx=20)

warning_checkbutton = Checkbutton(window, text="Warning", bootstyle=TOOLBUTTON + WARNING)
warning_checkbutton.grid(row=3, column=2, pady=10, padx=20)

info_checkbutton = Checkbutton(window, text="Info", bootstyle=TOOLBUTTON + INFO)
info_checkbutton.grid(row=3, column=3, pady=10, padx=20)

danger_checkbutton = Checkbutton(window, text="Danger", bootstyle=TOOLBUTTON + DANGER)
danger_checkbutton.grid(row=3, column=4, pady=10, padx=20)

primary_checkbutton = Checkbutton(window, text="Primary", bootstyle=ROUND + TOGGLE)
primary_checkbutton.grid(row=4, column=0, pady=10, padx=20)

success_checkbutton = Checkbutton(window, text="Success", bootstyle=ROUND + TOGGLE + SUCCESS)
success_checkbutton.grid(row=4, column=1, pady=10, padx=20)

warning_checkbutton = Checkbutton(window, text="Warning", bootstyle=ROUND + TOGGLE + WARNING)
warning_checkbutton.grid(row=4, column=2, pady=10, padx=20)

info_checkbutton = Checkbutton(window, text="Info", bootstyle=ROUND + TOGGLE + INFO)
info_checkbutton.grid(row=4, column=3, pady=10, padx=20)

danger_checkbutton = Checkbutton(window, text="Danger", bootstyle=ROUND + TOGGLE + DANGER)
danger_checkbutton.grid(row=4, column=4, pady=10, padx=20)

primary_checkbutton = Checkbutton(window, text="Primary", bootstyle=SQUARE + TOGGLE)
primary_checkbutton.grid(row=5, column=0, pady=10, padx=20)

success_checkbutton = Checkbutton(window, text="Success", bootstyle=SQUARE + TOGGLE + SUCCESS)
success_checkbutton.grid(row=5, column=1, pady=10, padx=20)

warning_checkbutton = Checkbutton(window, text="Warning", bootstyle=SQUARE + TOGGLE + WARNING)
warning_checkbutton.grid(row=5, column=2, pady=10, padx=20)

info_checkbutton = Checkbutton(window, text="Info", bootstyle=SQUARE + TOGGLE + INFO)
info_checkbutton.grid(row=5, column=3, pady=10, padx=20)

danger_checkbutton = Checkbutton(window, text="Danger", bootstyle=SQUARE + TOGGLE + DANGER)
danger_checkbutton.grid(row=5, column=4, pady=10, padx=20)


def load_city(event):
    province = province_combobox.get()
    match province:
        case "Tehran":
            city_combobox.config(values=["Tehran", "Karaj", "Shahriar", "Pardis"])
        case "Azarbaijan Sharghi":
            city_combobox.config(values=["Tabriz"])
        case "Fars":
            city_combobox.config(values=["Shiraz", "Lar"])


province_combobox = Combobox(window, values=["Tehran", "Azarbaijan Sharghi", "Fars", "Golestan", "Isfahan"],
                             state="readonly")
province_combobox.grid(row=6, column=0, pady=10, padx=20)
province_combobox.bind("<<ComboboxSelected>>", load_city)

city_combobox = Combobox(window, state="readonly")
city_combobox.grid(row=6, column=1, pady=10, padx=20)

date_entry = DateEntry(window)
date_entry.grid(row=7, column=0, pady=10, padx=20)

gauge = Floodgauge(window, text="50%", bootstyle=DANGER, orient=HORIZONTAL)
gauge.grid(row=8, column=0, pady=10, padx=20)

gauge.configure(value=50)

label_frame = LabelFrame(window, text="Personal Information", bootstyle=DANGER)
label_frame.grid(row=10, column=0, columnspan=5, pady=10, padx=20, sticky="nsew")

error_label = Label(label_frame, text="Invalid value.", bootstyle=DANGER)
error_label.grid(row=0, column=0, pady=10, padx=20)

# meter=Meter(window,metersize=100,amountused=50)
# meter.grid(row=1, column=0, pady=10, padx=20)

notebook = Notebook(window, bootstyle=DANGER)
notebook.grid(row=11, column=0, columnspan=5, pady=10, padx=20, sticky="nsew")

frame1 = Frame(notebook)
frame2 = Frame(notebook)
frame3 = Frame(notebook)

label1 = Label(frame1, text="This Frame 1")
label1.grid(row=0, column=0, pady=10, padx=20)

label2 = Label(frame2, text="This Frame 2")
label2.grid(row=0, column=0, pady=10, padx=20)

label3 = Label(frame3, text="This Frame 3")
label3.grid(row=0, column=0, pady=10, padx=20)

notebook.add(frame1, text="Frame1")
notebook.add(frame2, text="Frame2")
notebook.add(frame3, text="Frame3")

progressbar = Progressbar(window, value=80, bootstyle=DANGER + STRIPED)
progressbar.grid(row=12, column=0, columnspan=5, pady=10, padx=20, sticky="ew")

progressbar.configure(value=50)

gender_variable = StringVar()

female_radiobutton = Radiobutton(window, text="Female", value="female", variable=gender_variable, bootstyle=DANGER)
female_radiobutton.grid(row=13, column=0, columnspan=5, pady=10, padx=20)

male_radiobutton = Radiobutton(window, text="Male", value="male", variable=gender_variable, bootstyle=PRIMARY)
male_radiobutton.grid(row=13, column=1, columnspan=5, pady=10, padx=20)

window.mainloop()
