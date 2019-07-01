from tkinter import *

def onClick():
    name = entryName.get()
    rollno = entryRollNo.get()
    email = entryEmail.get()
    phoneNo = entryPhoneNo.get()

    print("Button Clicked!")
    print("Data is:- ")
    print(name)
    print(rollno)
    print(email)
    print(phoneNo)


r = Tk()


lblTitle = Label(r,text = "Please enter your details:")
lblTitle.pack()

lblName= Label(r,text = "Enter your Name:")
lblName.pack()

entryName  = Entry(r)
entryName.pack()



lblRollNo = Label(r,text = "Enter your RollNo:")
lblRollNo.pack()

entryRollNo  = Entry(r)
entryRollNo.pack()



lblEmail= Label(r,text = "Enter your Email:")
lblEmail.pack()

entryEmail  = Entry(r)
entryEmail.pack()


lblPhoneNo= Label(r,text = "Enter your phone number:")
lblPhoneNo.pack()

entryPhoneNo  = Entry(r)
entryPhoneNo.pack()





btnOk = Button(r,text = "Submit ", command = onClick)
btnOk.pack()


r.mainloop()

