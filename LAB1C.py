# functions:
# collection of instructions
# collection of code

#LAB1c
#ANTONIO MARTINEZ

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for anyone reading your documentation

#VARIABLE DICTIONARY---------_______________----------___________---------------___________
# max    = maximum capacity of the room
# ppl    = Amount of people who want to attend the event



######### functions ####################

def capacity(mc):
    print(input(" enter max capacity: "))
    return mc
def attendees(ppl):
    print(input("enter number of attendees: "))
    return ppl
def register(df):
    df = capacity(mc) - attendees(ppl)
    
    return df


""
#####################initialized Variables #################

mc = 0
ppl = 0
roomCount = 0
df = (mc) - (ppl)
####################################################################
print("WELCOME TO THE FIRE REGULATORY PROGRAM ")

print()

#answer = input("Enter y to start: ")

totalRoomNum =  int(input("\nHow many rooms would you like to check:"))

while totalRoomNum > roomCount:

    mc = capacity(mc)
    
    ppl = attendees(ppl) 
    
    register(df) = mc - ppl
    

    
roomCount += 1


if   totalRoomNum <= roomCount:
        print("thank you, \tGoodbye!")
        


   
    