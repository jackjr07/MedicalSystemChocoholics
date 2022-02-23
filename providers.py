"""
This is the file for Providers functions
"""
from datetime import datetime
import os

class Provider:

    def addToFile(self):
        with open(f"providersInfo/{self.name}-{self.number}.txt", "w") as file:
            intro = "Provider Information\n"
            pId = f"Provider Id: {self.providerId}\n"
            name = f"Name: {self.name}\n"
            number = f"Number: {self.number}\n"
            department = f"Department: {self.department}\n"
            el = "=============================================\n"
            file.writelines([intro, pId, name, number, department, el,el])
            file.close()

    def print(self):
        print("**User Created**")
        print(self.providerId, self.name)

    def __init__(self, name,  number, department):
            self.providerId = number[1:]
            self.name = name
            self.number = number
            self.department = department
            self.addToFile()


def createProvider():
    name  = input("What is your name: ")
    phone = input("What is your phone number: ")
    dep = input("What is your department: ")
    return [name, phone, dep]

def findProvider(phone:str) -> str: 
    try:
        #check if the user data is exist
        dirname = "./providersInfo"
        files = os.listdir(dirname)
        for file in files:
            if (file.find(phone) > 0):
                print(file)
                return file
    except:
        print("Error: at findMember function")


def main():
    findProvider("123456789")

    return 0

if __name__ == "__main__":
    main()


