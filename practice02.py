system = "OS 3"
if system == "OS 2":
    print ("no update needed")
else:
    print ("Update Needed")

system = "OS 2"
if system == "OS 2":
    print ("No Update Needed")
elif system == "OS 1" or system == "OS 3":
    print ("Update Needed")


approved_user1 = "Franco Rizzi"
approved_user2 = "Malena Espinosa"

username = "Franco Rizzi"
if username == approved_user1 or username == approved_user2 :
    print ("This user has access to this device")
else: 
    print ("This user does not have have access to this device")


organization_hours = True
if organization_hours == True :
    print ("Login attempt made during organizations hours")
else:
    print ("Login attempt made outside of organizationg hours")

approved_list = ["Franco Rizzi", "Malena Espinosa", "Venu", "Pedro Bordese"]
username = "Venu"
organization_hours = True
if organization_hours == True and  username in approved_list:
    print ("Login attempt made by an approved user during organization hours")
else:
    print ("Username not approved or login attempt made outside of organization hours")
