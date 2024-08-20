from tkinter import *
from tkinter import ttk


color1 = "#1e1f1e" #Black
color2 = "#feffff" #White
color3 = "#38576b" #Blue
color4 = "#ECEFF1" #Gray
color5 = "#FFAB40" #Orange
color6 = "#ff1100" #Red

window = Tk()
window.title("Calculator")
window.geometry("235x305")
window.config(bg=color1)



#--Frames
frame_screen = Frame(window, width= 235, height= 50, bg = color3)
frame_screen.grid(row=0, column= 0)

frame_body = Frame(window, width= 235, height= 268, bg= color4)
frame_body.grid(row=1, column= 0)

#--Label
text_value = StringVar()
app_label = Label(frame_screen, textvariable=text_value, width=16, height = 2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 17 bold"), bg = color2, fg= color1 )
app_label.place(x=0, y= 0)

##--Buttons services

b_clean = Button(frame_body, text="C", width=11, height= 2, bg=color5, fg=color6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_clean.place(x= 0, y=0)
b_percent = Button(frame_body, text="%", width=5, height= 2, bg=color5, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_percent.place(x=120, y=0)
b_divide = Button(frame_body, text="/", width=5, height= 2, bg=color5, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_divide.place(x=180, y=0)
b_multiply = Button(frame_body,text="*",width=5, height=2,  bg=color5, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_multiply.place(x=180, y=52)
b_minus = Button(frame_body,text="-",width=5, height=2,  bg=color5, fg=color1, font=("Ivy 13  bold"), relief=RAISED, overrelief=RIDGE)
b_minus.place(x=180, y=104)
b_plus = Button(frame_body,text="+",width=5, height=2,  bg=color5, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_plus.place(x=180, y=154)
b_equal = Button(frame_body,text="=",width=5, height=2,  bg=color5, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_equal.place(x=180, y=204)
b_dot = Button(frame_body,text=".",width=5, height=2,  bg=color5, fg=color1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_dot.place(x=120, y=204)

#--buttons numbers
b_1 = Button(frame_body,text="1",width=5, height=2, bg=color3, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=52)
b_2 = Button(frame_body,text="2",width=5, height=2,  bg=color3, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=60, y=52)
b_3 = Button(frame_body,text="3",width=5, height=2,  bg=color3, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=120, y=52)
b_4 = Button(frame_body,text="4",width=5, height=2,  bg=color3, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=104)
b_5 = Button(frame_body,text="5",width=5, height=2,  bg=color3, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=104)
b_6 = Button(frame_body,text="6",width=5, height=2,  bg=color3, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=104)
b_7 = Button(frame_body,text="7",width=5, height=2,  bg=color3, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=154)
b_8 = Button(frame_body,text="8",width=5, height=2,  bg=color3, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=60, y=154)
b_9 = Button(frame_body,text="9",width=5, height=2,  bg=color3, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=120, y=154)
b_0 = Button(frame_body,text="0",width=11, height=2,  bg=color3, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=204)

#--Math functions

def calcular():
    a = eval("9/9")

    app_label.set(a)


window.mainloop()