#LAB1B
#ANTONIO MARTINEZ

#STARTING DOCUMENTATION:
#-program prompt
#-pseudocode
#-notes for you to remember
#-guidelines / information for anyone reading your documentation

#VARIABLE DICTIONARY---------_______________----------___________---------------___________
# max    = maximum capacity of the room
# ppl    = Amount of people who want to attend the event

#####################initialized Variables ######################################

max = 0
ppl = 0
print()
print()
####################################################################
####################################################################
print("WELCOME TO THE FIRE REGULATORY PROGRAM ")

print()

answer = input("Enter y to start: ")

while answer == "Y" or answer == "y":

    max = int(input("\tWhat is the Capacity of the Room?  "))
    print()
    ppl = int(input("\tHow many People are attending? "))

    available = max - ppl
    remove = ppl - max

    if max >= ppl:
        print("\t It's SAFE!")
        print("\t Available Space: ", available)
        print()
    if max < ppl:
        print("\t It's NOT Safe!")
        print("\t Remove this many people: ", remove)
        print()
    if   answer == "n" or "N":
        print("thank you, \tGoodbye!")

    answer = input("\tWould you like to check another room? [y/n]:  ")
    while answer != "y" or  answer != "Y" or answer != "n" or answer != "N":
        
        while answer == "y" or answer == "Y":

                max = int(input("\tWhat is the Capacity of the Room?  "))

                ppl = int(input("\tHow many People are attending? "))
    
                available = max - ppl
                remove = ppl - max

                if max >= ppl:
                    print("\t It's SAFE!")
                    print("\t Available Space: ", available)
                if max < ppl:
                    print("\t It's NOT Safe!")
                    print("\t Remove this many people: ", remove)

                answer = input("\tWould you like to check another room? [y/n]:  ")

                if   answer == "n" or "N":
                    print("thank you, \tGoodbye!")
    