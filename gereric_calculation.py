import math
class Solution:
    def gen_Cal(it,num01,num02,b): 
        #Dictionary for All Number Systems
        for_Hexa ={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        #Reversing The dictionary for output
        reversed_Hexa = {value: key for key, value in for_Hexa.items()}
        number_01=num01
        number_02=num02
        #concatination of strings wiht 0 
        number_01='0'+number_01
        number_02='0'+number_02
        #initial carry_in value = 0 
        carry_in=0
        #getting base from argument
        base=b
        # conversion of strings to intgers 
        for_cal=[]
        for_cal2=[]
        for each in number_01:
            for key,v in for_Hexa.items():
                if key==each:
                    for_cal.append(v)
        for each in number_02:
            for key,v in for_Hexa.items():
                if key==each:
                    for_cal2.append(v)    
        #length constraint (1st number should be greater than 2nd number) and appending the int list
        # with 0 to make them equal in length          
        if len(for_cal)>len(for_cal2):
            for x in range(len(for_cal)-len(for_cal2)):
                for_cal2.insert(0,0)
        if len(for_cal)>=len(for_cal2):
            ans=[]
            print(for_cal)
            print(for_cal2)
            # x is for while loop
            x=len(for_cal)
            print(x)
            carry_out=0   
            xx=len(for_cal)-1
            xxx=len(for_cal2)-1    
            while x>0: 
                #implementation of carry_out equation
                carry_out=math.floor((for_cal[xx]+for_cal2[xxx]+carry_in)/base) #FLOOR FUCNTION FROM MATH LIBRARY
                count=0
                for each in range(base):  #0 to base-1 (for example if base 16, it will iterate from 0 to 15)
                    if count==0:
                        #balancing the equation
                        if each==(for_cal[xx]+for_cal2[xxx]+carry_in)-(base*carry_out):
                            ans.append(each)
                            carry_in=carry_out
                            count=count+1
                #indexes of 1st list and 2nd list             
                xx=xx-1
                xxx=xxx-1
                x=x-1
            ans.reverse()
            #converting the answer to Alphabets if required
            ans1=[]
            for each in ans:
                for key,v in reversed_Hexa.items():
                    if key==each:
                        ans1.append(v)
            my_string = ''.join(ans1)
            print(my_string)
        else:
            print("First Number should be greater the 2nd number")
            print("Try Again!")
#start of main function
print("Generic Calculator")
for_if=0
while for_if!=5:
    print("Generic Addition")
    print("Press 1: Binary")
    print("Press 2: Decimal")
    print("Press 3: Octal")
    print("Press 4: Hexa-Decimal")
    print("Press 5: Exit")
    for_if=int(input())
    s1=Solution()
    if for_if==1:
        print("Input Number Range: 0-1")
        number01=input("Enter 1st Number: ")
        number02=input("Enter 2nd Number: ")
        s1.gen_Cal(number01,number02,2)
    if for_if==2:
        print("Input Number Range: 0-9")
        number01=input("Enter 1st Number: ")
        number02=input("Enter 2nd Number: ")
        s1.gen_Cal(number01,number02,10)
    if for_if==3:
        print("Input Number Range: 0-7")
        number01=input("Enter 1st Number: ")
        number02=input("Enter 2nd Number: ")
        s1.gen_Cal(number01,number02,8)
    if for_if==4:
        print("Number Range: 0-9 ,Alphabets: A-F")
        number01=input("Enter 1st Number: ")
        number02=input("Enter 2nd Number: ")
        s1.gen_Cal(number01,number02,16)
#END OF PROGRAM