from tkinter import *
window=Tk()

# add widgets here


window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_bmi():
    time=int(weight_entry.get())
    rate=int(height_entry.get())/100
    principle=int(username.get())
    si = time*rate*principle
    result_label.destroy()
    a= si+principle
    
    
    output_message=Label(result_frame,text="your SI is "+str(si)+" and your amount is "+str(a), bg = "lightcyan", font=("Calibri", 12), width=42)
    output_message.place(x=20, y=40)
    output_message.pack()

app_label=Label(window, text="SI CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Principle", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)


height_label=Label(window, text="Rate", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
height_label.place(x=20, y=140)

height_entry=Entry(window, text="", bd=2, width=22)
height_entry.place(x=150, y=142)


weight_label=Label(window, text="Time", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
weight_label.place(x=20, y=190)

weight_entry=Entry(window, text="", bd=2, width=22)
weight_entry.place(x=150, y=192)


calculate_button = Button(window, text="Calculate", fg="black", bg="lightcyan", command=calculate_bmi)
calculate_button.place(x=20, y=250)


result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()
window.mainloop()