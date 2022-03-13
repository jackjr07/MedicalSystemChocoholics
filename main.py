import members
import providers
import services

def space():
    print("============================")

def menu():
    print("Welcome to Chocan program\n")
    print("Please choose this following Options:\n")
    userType = input("[1] Members\n[2] Providers\n[3] Service\n[4] Reports\n[0] EXIT\nAnswer: ")
    if(userType == "1"):
        return memberMenu()
    if(userType == "2"):
        return providerMenu()
    if(userType == "3"):
        return serviceMenu()
    if(userType == "4"):
        return reportMenu()
    if(userType == "0"):
        print("Thank you")
        exit()
    else:
        print(f"Invalid input - Please try again")
        space()
        return menu()


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
            members.findMember(phone)
            space()
            return menu()

def providerMenu():
    print("Choose these options\n")
    option = input("[1] Create new provider\n[2] Find member information\n Answer: ")
    if (option == "1"):
        temp = providers.createProvider()
        user = providers.Provider(temp[0], temp[1], temp[2])
        user.print()
        space()
        return menu()
    elif(option == "2"):
        providerNumber = input("What is provider's number: ")
        if(len(providerNumber) > 10):
            print("Error: The phone number is longer than 10 digits")
            space()
            return menu()
        else:
            providers.findProvider(providerNumber)
            space()
            return menu()

def serviceMenu():
    print("Choose these options\n")
    option = input("[1] Add service\n Answer: ")
    if(option == "1"):
        newService = services.Service()
        space()
        return menu()

def reportMenu():
    print("Choose these options\n")
    option = input("[1] Get weekly report\n Answer: ")
    if(option == "1"):
        month = input("Which month [1-12]: ")
        week = input("which week [1-53]: ")
        services.getreport(month, week)
        space()
        return menu()

def main():
    menu()
    return 0

if __name__ == "__main__":
    main()



