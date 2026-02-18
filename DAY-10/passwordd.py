
#! WAP to validate pin, it must contain 4 digits, it should not have 3 continous numbers eg.123 one digit should not repeat 3 times eg.123

pin1=int(input("Enter pin: "))
pin=str(pin1)


for i in range(len(pin)-2):
    if len(pin)==4:
        if (pin[i]==pin[i+1]==pin[i+2]) or (pin[i+1]==pin[i+2]== pin[i+3]):
            print("Repeating Numbers in the PIN")
            break
        elif (int(pin[i])+1==int(pin[i+1])==int(pin[i+2])-1) or (int(pin[i+1])+1==int(pin[i+2])==int(pin[i+3])-1):
            
            print("Sequence of numbers in the pin")
            break
        
        elif (int(pin[i])==int(pin[i+1])+1==int(pin[i+2])+2) or (int(pin[i+1])==int(pin[i+2])+1==int(pin[i+3])+2):
            
            print("Sequence of numbers in the pin")
            break


        else:
            print('Valid Pin')
            break
    else:
      
      print("Invalid length")
      break