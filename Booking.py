import csv
import Room_info
class booking():
    def __init__(self):
        pass

    def confirm_booking(self):
        confirm = input("Do You want to confirm Booking[yes / no]:")
        if(confirm == "yes"):
            obj_4.yes()
        elif(confirm == "no"):
            obj_4.no()
        else:
            print("Please enter the valid input")
            obj_4.confirm_booking()

    def yes(self):
        print("Enter your Details:")
        Name= input("Enter your name: ")
        contact=input("Enter your contact number:")
        mail=input("Enter your mail id:")
        personal_details=[]
        personal_details.append(Name)
        personal_details.append(contact)
        personal_details.append(mail)
        with open('Database.csv','a',newline="") as f:
            d =csv.writer(f)
            d.writerow( personal_details)
        with open('Database.csv','r') as f:
            d=csv.reader(f)
            print(personal_details)
            print("-------Personal Details-------")
            for i in personal_details:
                print(i)
        obj_4.payment()
    
    def no(self):
        print("Redirecting you to home page")
        from user_login import user_login
        obj= user_login()
        obj.login()

    def payment(self):
        print("Make Payment mode")
        print(Room_info.price)
        
obj_4 = booking()
obj_4.confirm_booking()