def power4(number):
    count=0

    if (number &(~(number&(number-1)))):
          

      while(number>1):

         number>>=1

         count+=1

    if (count%2==0):
       
       return True
    
    else:
       return False
    
number=int(input("enter your number"))



if (power4(number)):
   
   print(number,"is power of 4")
           


