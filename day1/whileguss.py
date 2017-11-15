#Author
age_of_you=45
count=0
while count<3:
    gass_age=int(input("gassage:"))
    if gass_age==age_of_you:
        print("oye")
        break
    elif gass_age<age_of_you:
        print("too small")
    else:
        print("too big")
    count+=1
    if count ==3:
        countine_confirm=input("agein?Y|N:")
        if countine_confirm != "n":
            count=0
        else:
            print("thank you")
#else:
 #   print("try too many times.. fuck off")
