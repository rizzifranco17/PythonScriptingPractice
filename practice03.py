def alert():
    for i in range (3):
        print ("Potential security issue. investigate further.")
alert()

def list_to_string ():
    username_list = ["Franco Rizzi", "Malena Espinosa", "Venu", "Pedro Bordese"]
    for i in username_list:
        print (i)
list_to_string()

def list_to_string ():
    username_list = ["Franco Rizzi", "Malena Espinosa", "Venu", "Pedro Bordese"]
    sum_variable = ""
    for i in username_list:
        sum_variable = sum_variable + i + ", "
        print (sum_variable)
list_to_string() 