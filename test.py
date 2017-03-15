import Tkinter
parent_widget = Tkinter.Tk()
label_widget = Tkinter.Label(parent_widget, text="Hello, welcome to this Short Term Memory Test")
label_widget.pack()
Tkinter.mainloop()

parent_widget = Tkinter.Tk()
v = Tkinter.IntVar()
v.set(1)
radiobutton_widget1 = Tkinter.Radiobutton(parent_widget,
                                   text="New User",
                                   variable=v, value=1,
                                   indicatoron=False)
radiobutton_widget2 = Tkinter.Radiobutton(parent_widget,
                                   text="Returning User",
                                   variable=v, value=2,
                                   indicatoron=False)
radiobutton_widget1.pack()
radiobutton_widget2.pack()
Tkinter.mainloop()

parent_widget = Tkinter.Tk()
entry_widget = Tkinter.Entry(parent_widget)
entry_widget.insert(0, "Please type in your name")
entry_widget.pack()
Tkinter.mainloop()

parent_widget = Tkinter.Tk()
checkbutton_widget = Tkinter.Checkbutton(parent_widget,
                                    text="Justin Wang")
checkbutton_widget.select()
checkbutton_widget.pack()
Tkinter.mainloop()
