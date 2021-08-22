import random
import qrcode 
import pymongo
client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")

logindb=client['loginaccount']
table1=logindb.orgnisation
table2=logindb.orgnisation
table3=logindb.orgnisation
table4=logindb.orgnisation
table5=logindb.orgnisation
records={
    'id':1003,
    'name':'david',
    'age':23,
    'phone':'7337573916'
         }
table1.insert_one(records)
records={
    'id':1004,
    'name':'sai',
    'age':21,
    'phone':'9390759283'
         }
table2.insert_one(records)
records={
    'id':1005,
    'name':'swaroop',
    'age':22,
    'phone':'1234567890'
         }
table3.insert_one(records)
records={
    'id':1009,
    'name':'Nanda',
    'age':25,
    'phone':'9390759283'
         }
table4.insert_one(records)
print("WELCOME TO ORGANISATION")
print("1.login\n2.Sign up")
m=int(input("enter a number:"))
if m==1:
    n=int(input("enter the user id:"))
    x=random.randint(100000,999999)
    im=qrcode.make("otp is"+str(x))
    im.show()
    d=int(input("enter the otp:"))
    if d==x:
        print("welcome user ")
        print("select  your queries by giving number as input \n1.Balance\n2.Current Recharge plan\n3.recharge plans\n4.data plan\n5.Exit")
        n=int(input("enter a number:"))
        if n==1:
            print("1.Main Balance")
            print("2.Data Balnce")
            print("3.MSG balance")
            print("4.exit")
            m=int(input("enter a number:"))
            if m==1:
                print("the balance is 150rs\nthanks")
            elif m==2:
                print("your data plan is 1.5gb/day plan\nthanks")
            elif m==3:
                print("300sms\nthanks")
            else:
                print("exit")
        elif n==2:
            print("your current recharge plan is 149rs,1.5gb/day,300sms\nThanks")
        elif n==3:
            print("your recharge plans are 149,199,299,399,599\nthanks")
        elif n==4:
            print("3GB 48RS\n6GB 98RS are for your number\nthanks")
        else:
            print("EXIT\nThanks")
    else:
        print("please enter the correct otp")
else:
    print("to create a coount please fill below details")
    _name_=input("enter your name:")
    a=int(input("enter your age:"))
    print("welcome to our company",_name_)
    print("your age is",a)
    d=random.randint(9000000000,10000000000)
    print("your new phone number is",d)
    z=random.randint(1000,9999)
    print("your new id is",z)
    records={
            "id":z,
            "name":_name_,
            "age":a,
            "phone":d
            }
    table5.insert_one(records)
