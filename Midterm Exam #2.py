from tkinter import *
def buttoncolor(): btn1.configure(bg="yellow", fg="black")
window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400+20+10")
btn1 = Button(window, text = "Click to change color", command=buttoncolor)
btn1.place(x= 190, y=180)

window.mainloop()



