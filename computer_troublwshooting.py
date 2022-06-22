# print "Push the power button... "
# boot_check = input "Did it boot up? "
# if boot_check = "yes" print "login with password"
# else power_check = input("Is it plugged in? ")
#    if power_check = "no" print "The computer is broken "
#    else plug_fix = input("Plug it in... did this fix the problem? ")
#        if plug_fix = "yes" print "Login with password "
#        else print("The computer is broken")



boot_check = input("Push the Power button... Did it boot up? ")

if boot_check == "yes":
    print("Login with password ")
else:
    power_check = input("Is it plugged in? ")
    if power_check == "no":
        print("The computer is broken ")
    else:        
        plug_fix = input("Plug it in... did this fix the problem? ")
        if plug_fix == "yes":
            print("Login with Password ")
        else:
            print("The computer is broken ")
