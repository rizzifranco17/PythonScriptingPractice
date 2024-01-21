employee_id = 4185
employee_id = str (employee_id)
print (employee_id)
if len(employee_id)< 5: 
    employee_id = "E" + employee_id
    print (employee_id)

device_id = "r262c36"
print (device_id[0:3])

url = "https:// exampleURL1.com"
ind = url.index(".com")
print (url[ind:ind+4])
print (url[8:ind])