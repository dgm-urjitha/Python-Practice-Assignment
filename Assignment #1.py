#!/usr/bin/env python3
#Assignment-1 Lakshmi Urjitha Dhadigam

def main():
#display a welcome message
    
    print("Even or Odd Checker")
    print()
    
    EvenOROdd()
    
#separate function EvenOROdd  

def EvenOROdd():

    while(1):
    
        number = int(input("Enter an integer: "))
   
        if (number%2==0):
            print ("This is an even number.")
        else:
            print ("This is an odd number.")

        print()
        
        decision=input("Continue? (y/n) ")[0]
        print ("===========================")
        if (decision=='y'):
            continue
        else:
            print ("Bye!")
            break
        
main()      
#EvenOROdd()

    


