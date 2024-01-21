approved_users = ["Franco Rizzi", "Malena Espinosa", "Venu", "Pedro bordese"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg","4n482ts"]
print (approved_users)
print (approved_devices)
print (approved_users[0])
print (approved_devices[0])

new_user = "Luciano Ceschini"
new_device = "3rcv4w6"
approved_users.append(new_user)
approved_devices.append(new_device)

print (approved_users)
print (approved_devices)

remover_user = "Pedro bordese"
removed_device = "4n482ts"

approved_users.remove(remover_user)
approved_devices.remove(removed_device)
print (approved_users)
print (approved_devices)

approved_users = ["Franco Rizzi", "Malena Espinosa", "Venu", "Pedro bordese"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg","4n482ts"]

username = "Venu" 
if username in approved_users:
    print ("The username", username, "is approved to access the system")
else: 
    print ("The username",username, "is not approved to access the system")


approved_users = ["Franco Rizzi", "Malena Espinosa", "Venu", "Pedro bordese"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg","4n482ts"]
username = "Venu"
device_id = "2ye3lzg"
ind = approved_users.index (username)
if username in approved_users and device_id == approved_devices[ind]:
    print ("The username", username, "is approved to access the system")
    print (device_id, "is the assigned device for", username)
elif username in approved_users and device_id != approved_devices [ind]:
    print ("The user", username, "is approved to access the system, but" ,device_id, "is not ther assigned device")


approved_users = ["Franco Rizzi", "Malena Espinosa", "Venu", "Pedro bordese"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg","4n482ts"]
username = "Venu"
device_id = "8rp2k75"
ind = approved_users.index (username)
if username in approved_users and device_id == approved_devices[ind]:
    print ("The username", username, "is approved to access the system")
    print (device_id, "is the assigned device for", username)
elif username in approved_users and device_id != approved_devices [ind]:
    print ("The user", username, "is approved to access the system, but" ,device_id, "is not ther assigned device")


approved_users = ["Franco Rizzi", "Malena Espinosa", "Venu", "Pedro bordese"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg","4n482ts"]

def login (username , device_id):
    if username in approved_users:
        print ("The user", username, "is approved to access the system ")
        ind = approved_users.index(username)
        if device_id == approved_devices [ind]:
            print (device_id, "is the assigned device for",username)
        else: 
            print (device_id, "is not the assigned device for", username)
    else:
                print("The username", username, "is not approved to access the system.")


login ("Franco Rizzi","8rp2k75" )
login ("Venu","hl0s5o1" )
login ("Malena Espinosa", "hl0s5o1")
