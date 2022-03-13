# Chocoholics Anonymous

**CS300 - Chocoholics Anonymous Project**<br />
I have 4 main core models<br />
1. Member
> This is the member, that use the serivces. 

- Members object has 6 initial parameters: name, phone, street, city, state, zipcode.
- I have checkInput function to elimicate the protential invalid input from user
- After member created, I create the file with the file name according to member.name-member.phone.
: Since phone number will be unique anyway, in this case our users account will be unique too.
- Find member function will find the user based on their phone number. In the file directory. Return with print user's info on the screen and also return the file name to the funciton. Incase we would need to modified the file in the future.
2. Provider
3. Service
4. Report

***Run Unit testing***<br />

```
python3 models_test.py -v -b
```
- This will show you all the test case, and each test's result.
However, this will hide print statement


```
python3 models_test.py
```
- This will run all the test with print statement



