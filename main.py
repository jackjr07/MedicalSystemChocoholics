"""
Funciton requriments:
    - main weekly reports
        - member weekly report
        - provider weekly report
    - services reports

Data Center:
    - memberReport
    - proiderReport
    - providerDirectory
    - eft
    - summaryReport


Users:
    - providers -> healthcare providers
    - memeber -> patients
    - users -> the person that interact with program

"""
import members

def space():
    print("============================")

def menu():
    print("Welcome to Chocan program\n")
    print("Please choose this following Options:\n")
    userType = input("[1] Members\n[2] Providers\n[3] Reports\n Answer: ")
    if(userType == "1"):
        return memberMenu()

def memberMenu():
    print("Choose these options\n")
    option = input("[1] Create new member\n[2] Add member service\n[3] Find member information\n Answer: ")
    if(option == "1"):
        temp = members.createMember()
        user = members.Members(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5])
        user.print()
    elif(option == "2"):
        name = input("What is member's name: ")
        phone = input("What is member's phone number: ")
        if(len(phone)>10):
            print('Error: The phone number is longer then 10 digits')
            space()
            return menu()
        else:
            members.addService(name, phone)

    elif(option == "3"):
        name = input("What is member's name: ")
        phone = input("What is member's phone number: ")
        if(len(phone)>10):
            print('Error: The phone number is longer then 10 digits')
            space()
            return menu()
        else:
            members.findMember(name,phone)


def main():
    menu()
    return 0

if __name__ == "__main__":
    main()



