#Author Mike

age_of_you=45
for i in range(3):
    gass_age=int(input("gassage:"))
    if gass_age==age_of_you:
        print("oye")
        break
    elif gass_age<age_of_you:
        print("too small")
    else:
        print("too big")
else:
    print("try too many times.. fuck off")
