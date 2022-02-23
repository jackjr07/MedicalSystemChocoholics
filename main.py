"""
&&& Check input quality
Funciton requriments:
    - main weekly reports
        X member weekly report
        X provider weekly report
    X services reports

Data Center:
    - memberReport
    - proiderReport
    - providerDirectory
    - eft
    - summaryReport


Users:
    X providers -> healthcare providers
    X memeber -> patients
    X users -> the person that interact with program

"""
import members
import providers
import services

def space():
    print("============================")

def menu():
    print("Welcome to Chocan program\n")
    print("Please choose this following Options:\n")
    userType = input("[1] Members\n[2] Providers\n[3] Reports\n Answer: ")
    if(userType == "1"):
        return memberMenu()
    if(userType == "2"):
        return providerMenu()
    if(userType == "3"):
        return serviceMenu()

def memberMenu():
    print("Choose these options\n")
    option = input("[1] Create new member\n[2] Find member information\n Answer: ")
    if(option == "1"):
        temp = members.createMember()
        user = members.Members(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5])
        user.print()
        return menu()
    elif(option == "2"):
        phone = input("What is member's phone number: ")
        if(len(phone)>10):
            print('Error: The phone number is longer then 10 digits')
            space()
            return menu()
        else:
            print(members.findMember(phone))
            return menu()

def providerMenu():
    print("Choose these options\n")
    option = input("[1] Create new provider\n[2] Find member information\n Answer: ")
    if (option == "1"):
        temp = providers.createProvider()
        user = providers.Provider(temp[0], temp[1], temp[2])
        user.print()
        return menu()
    elif(option == "2"):
        providerNumber = input("What is provider's number: ")
        if(len(providerNumber) > 10):
            print("Error: The phone number is longer than 10 digits")
            space()
            return menu()
        else:
            print(providers.findProvider(providerNumber))
            return menu()

def serviceMenu():
    print("Choose these options\n")
    option = input("[1] Add service\n Answer: ")
    if(option == "1"):
        services.addService()
        return menu()

        
        

     

def main():
    menu()
    return 0

if __name__ == "__main__":
    main()



