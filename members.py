"""
This is the file for members functions
"""
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

def checkInput(name:str, phone:str, street:str, city:str, state:str, zipcode:str):
    if(not name.isalpha()):
        raise ValueError(f"name contains only letters")
    if(not phone.isdigit()):
        raise ValueError(f"phone number needs to be only digits")
    if(not city.isalpha()):
        raise ValueError(f"city needs to be only letter")
    if(len(state)>2 or state.isdigit()):
        raise ValueError(f"state needs be only 2 characters, and needs to be letter")
    if(len(zipcode)>5 or not zipcode.isdigit()):
        raise ValueError(f"zipcode needs to be less than 5 digits")
    return True
    
    
def createMember():
    name  = input("What is your name[eg. jack]: ").lower()
    phone = input("What is your phone number[eg. 503-123-4567]: ").lower()
    street = input("What is your address[eg. 1234 NW Hello St]: ").lower()
    city = input("City[eg. portland, seattle]: ").lower()
    state = input("State[eg. or, wa]: ").lower()
    zipcode = input("Zipcode[eg. 97201]: ")
    checkInput(name, phone,street, city, state, zipcode)
    return [name, phone, street, city, state, zipcode]


def findMember(phone:str)->str:
    try:
        #check if the user data is exist
        dirname = "./membersInfo"
        files = os.listdir(dirname)
        for file in files:
            if (file.find(phone) > 0):
                with open(f"{dirname}/{file}", 'r') as f:
                    info = f.read()
                    print(info)
                return file
            else:
                continue
    except Exception as e:
        print(f"Error: at findMember function{e}")


def main():
    #createMember()
    #addService("jack", "9714701489")
    #files = os.listdir('./membersInfo')
    #for i in files:
    #    print(i)
    #print(type(findMember("1112223333")))
    return 0

if __name__ == "__main__":
    main()


