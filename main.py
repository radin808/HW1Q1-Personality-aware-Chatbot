name = ""
age = ""

# Ask first question
answer = input("Hi, this is Pchatbot, can I talk to you?\n")

# Handle first question response
if answer in ['Y', 'y']:
    # Ask second question
    name = input("What is your name?\n")
    # Respond to second question
    print("Nice to meet you, " + name + ".")
    # Ask third question
    answer = input("How are you doing today?\n")
    # Handle third question response
    if answer.lower() in ['good', "i'm great", "i'm good", 'fine']:
        print("I'm glad you're feeling well, " + name + ".")
        age = input("How old are you?\n")
        if int(age) > 18 and answer.lower() in ['good', "i'm great", "i'm good", 'fine']:
            print("You are ready to drive.")
        else:
            print("Still taking the bus!")
    elif answer.lower() in ['bad', 'not okay', "i'm not feeling good"]:
        print("Have some time to yourself to recharge!")
    else:
        print("I see!")
else:
    print("Okay! Talk to you soon!")