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
        print("**Member Created**")
        print(self.memberId, self.name)

    def __init__(self, name,  number, street, city, state, zipcode):
            self.memberId = number[1:]
            self.name = name
            self.number = number
            self.street = street
            self.city = city
            self.state = state
            self.zipcode = zipcode
            self.addToFile()

def createMember():
    name  = input("What is your name: ")
    phone = input("What is your phone number: ")
    street = input("What is your address: ")
    city = input("City: ")
    state = input("State: ")
    zipcode = input("Zipcode: ")
    return [name, phone, street, city, state, zipcode]

def findMember(phone:str) -> str:
    try:
        #check if the user data is exist
        dirname = "./membersInfo"
        files = os.listdir(dirname)
        """
        if(f"{*}{phone}.txt" in files):
            with open(f"{dirname}/{name}-{phone}.txt", "r") as file:
                info = file.read()
                print(info)
        """
        for file in files:
            if (file.find(phone) > 0):
                with open(f"{dirname}/{file}", 'r') as f:
                    info = f.read()
                    print(info)
                return file
    except:
        print("Error: at findMember function")


def main():
    #createMember()
    #addService("jack", "9714701489")
    #files = os.listdir('./membersInfo')
    #for i in files:
    #    print(i)
    findMember("9714701489")
    return 0

if __name__ == "__main__":
    main()


