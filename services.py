"""
This contains all the services functions
"""
import members
import providers
from datetime import datetime
import os

class Service:

    def getTime(self):
        return datetime.now().strftime("%m-%d-%Y %H:%M")
    
    def getMonthWeek(self):
        return datetime.now().strftime("%m-%W")

    def updateFile(self):
        sc = f"Service code: {self.serviceCode}\n"
        d = f"Date of Service: {self.dateofService}\n"
        p = f"Provider Number: {self.providerNumber}\n"
        m = f"Member Number: {self.memberNumber}\n"
        c = f"Total Cost: {self.cost}\n"
        sn = f"Service Note: {self.note}\n"
        t = f"Created: {self.timeStamp}\n"
        el = "=============================================\n"
        info = [sc,d,p,m,c,sn,t,el]
        try:
            with open(f"membersInfo/{self.memberFile}", 'a') as file:
                file.writelines(info)
                file.close()
            with open(f"providersInfo/{self.providerFile}", 'a') as file:
                file.writelines(info)
                file.close()
        except Exception as e:
            print(f"Error occured at Service class - updateFile function: {e}")

    def makeReport(self):
        template = f"Member: {self.memberNumber}/Provider: {self.providerNumber}\nCost: {self.cost}\n"
        try:
            with open(f"reportsInfo/{self.monthweek}", 'a') as file:
                file.write(template)
                file.close()

        except Exception as e:
            print(f"Error is occured at Service class - makeReport: {e}")


    def __init__(self):
        self.date = input("Date of service[eg. 7]: ")
        self.month = input("month of the of service[1-12]: ")
        self.year = input("Year of the service[eg. 2022]: ")
        self.dateofService = f"{self.date}-{self.month}-{self.year}"
        self.serviceCode = input("Service Code[6 Digits]: ")
        self.providerNumber = input("Provider Number: ")
        self.memberNumber = input("Member Number: ")
        self.note = input("Service's note: ")
        self.cost = input("Total cost for this service: ")
        self.timeStamp = self.getTime()
        self.memberFile = members.findMember(self.memberNumber)
        self.providerFile = providers.findProvider(self.providerNumber)
        self.monthweek = self.getMonthWeek()
        self.updateFile()
        self.makeReport()


def getreport(month,week):
    try:
        with open(f"reportsInfo/{month}-{week}", 'r') as file:
            print(file.read())
    except Exception as e:
        print(f"Error is occured at Service class - getreport : {e}")

def main():
    getreport("00", "00")


    return 0

if __name__ == "__main__":
    main()
