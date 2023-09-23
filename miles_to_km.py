from tkinter import *
# from tkinter import ttk
import ttkbootstrap as ttk

window=ttk.Window(themename="darkly") # ttkbootstrap er option
window.title("Converter")
window.geometry("300x180")

def convert():
    mile=input_int.get()
    km=mile*1.61
    out_str.set(km)

label=ttk.Label(window,text="Miles To Km",font="calibri 24 bold")
label.pack()

#input
my_fram=ttk.Frame(window)
input_int=IntVar()
entry=ttk.Entry(my_fram,textvariable=input_int)
btn=ttk.Button(my_fram,text="Convert",command=convert)
entry.pack(side="left",padx=10)
btn.pack(side="left")
my_fram.pack(pady=10)

#output
out_str=StringVar()
outlbl=ttk.Label(window,text="output",font="calibri 24",textvariable=out_str)
outlbl.pack(pady=5)


window.mainloop()

