"""
This contains all the services functions
"""
import members
import providers
from datetime import datetime
import os

def addService():
    try:
        #Service Template
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
        
        #find member's file, and provide's file
        memberFile = members.findMember(memberNumber)
        providerFile = providers.findProvider(providerNumber)

        #Adding to member file
        with open(f"membersInfo/{memberFile}", "a") as file:
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
        print("Added service - Member")
        
        #adding to provider file
        with open(f"providersInfo/{providerFile}", "a") as file:
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
        print("Added service - Provider")
    except:
        print("Error occured at services.addService function")

def main():
    addService()
    return 0

if __name__ == "__main__":
    main()
