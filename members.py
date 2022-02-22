"""
This is the file for members functions
"""
from datetime import datetime
import os

class Members:

    def addToFile(self):
        with open(f"membersInfo/{self.name}-{self.number}.txt", "w") as file:
            intro = "Member Information\n"
            mId = f"Member Id: {self.memberId}\n"
            name = f"Name: {self.name}\n"
            number = f"Number: {self.number}\n"
            address = f"Address: {self.street}-{self.city}-{self.state}-{self.zipcode}\n"
            el = "=============================================\n"
            file.writelines([intro, mId, name, number, address, el,el])
            file.close()

    def print(self):
        print("**User Created**")
        print(self.memberId, self.name)

    def __init__(self, name,  number, street, city, state, zipcode):
            self.memberId = number[1:]
            self.name = name
            self.number = number
            self.street = street
            self.city = city
            self.state = state
            self.zipcode = zipcode
            self.allServices = []
            self.addToFile()


def createMember():
    name  = input("What is your name: ")
    phone = input("What is your phone number: ")
    street = input("What is your address: ")
    city = input("City: ")
    state = input("State: ")
    zipcode = input("Zipcode: ")
    return [name, phone, street, city, state, zipcode]

def addService(name:str, phone:str):
    try:
        date = input("Date of service[eg. 7]: ")
        month = input("month of the of service[1-12]: ")
        year = input("Year of the service[eg. 2022]: ")
        dateofService = f"{date}-{month}-{year}"
        serviceCode = input("Service Code[6 Digits]: ")
        providerNumber = input("Provider Number: ")
        memberNumber = input("Member Number: ")
        note = input("Service's note: ")
        ts = datetime.now()
        timeStamp = ts.strftime("%m-%d-%Y %H:%M")

        with open(f"membersInfo/{name}-{phone}.txt", "a") as file:
            info = "Service\t"
            service = f"Service code: {serviceCode}\n"
            date = f"Date of Service: {dateofService}\n"
            p = f"Provider Number: {providerNumber}\n"
            m = f"Member Number: {memberNumber}\n"
            sn = f"Service Note: {note}\n"
            t = f"Created: {timeStamp}\n"
            el = "=============================================\n"
            file.writelines([info, service, date, p, m, sn,t,el])
            file.close()
        print("Added service")
    except:
        print("Error occured at members.addService function")

def findMember(name:str, phone:str):
    try:
        #check if the user data is exist
        dirname = "./membersInfo"
        files = os.listdir(dirname)
        if(f"{name}-{phone}.txt" in files):
            with open(f"{dirname}/{name}-{phone}.txt", "r") as file:
                info = file.read()
                print(info)
    except:
        print("Error: at findMember function")


def main():
    #createMember()
    #addService("jack", "9714701489")
    #files = os.listdir('./membersInfo')
    #for i in files:
    #    print(i)
    #findMember("jack", "9714701489")
    return 0

if __name__ == "__main__":
    main()


