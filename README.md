# Chocoholics Anonymous

**CS300 - Chocoholics Anonymous Project**<br />
I have 4 main core models<br />
1. Member
> This is the member, that use the serivces. 

- Members object has 6 initial parameters: name, phone, street, city, state, zipcode.
- I have checkInput function to elimicate the protential invalid input from user
- After member created, I create the file with the file name according to member.name-member.phone.
: Since phone number will be unique anyway, in this case our users account will be unique too.
- Find member function will find the user based on their phone number. In the file directory. Return with print user's info on the screen and also return the file name to the function. In case we would need to modify the file in the future.

2. Provider
> This is the provider, that provide the service to member

- Provider object has 3 initial parameters: name, phone, department.
- After the provider created, I create the file with the file name according to provider.name-provide.number
: Since phone number will be unique anyway, in this case our users account will be unique too.
- Find provider function will find the user based on their phone number. In the file directory. Return with print user's info on the screen and also return the file name to the function. In case we would need to modify the file in the future.

3. Service
> This is the service module, this is where all the services that member recived, and provider provided will be created. Then it will get added to member and provider file as their service log, as well as the weekly report.
- Service object has 8 initial parameters: Data, month and year of the service, service's code, provider's number, member's number, service's note, and total cost of the service.
- The program will generate the timestamp when this file is created
- After the service created, I add this service information to the member's file, and provider's file, then the weekly report.
- getreport function will get the report of what has been created during the month and weekly numbers that the services have been created. As a result, this is how the admin can get the weekly report for all service

***Run Unit testing***<br />
> I have added the initial member, and provider, and weekly report for testing purpose. 

**Command to run unittest**<br />

```
python3 models_test.py -v -b
```
- This will show you all the test cases, and each test's result.
However, this will hide the print statement


```
python3 models_test.py
```
- This will run all the test with print statement


***Walk Through***

> This is the gif show user how to interact with the program, what would be the expected input, and result.

1. Create Member
<img src="./gifWalkThrough/1" alt="CreateMember" height="500">



