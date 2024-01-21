failed_login_list = [ 119, 101, 99, 91, 22, 105, 108, 85, 88, 90, 264]
print (sorted(failed_login_list))
print (max(failed_login_list))

def analyze_logins (username, current_day_logins):
    print ("Current day login total for", username, "is", current_day_logins)
analyze_logins("Venu", 8)

def analyze_logins (username, current_day_logins,average_day_logins): 
     
     print ("Current day login total for", username, "is", current_day_logins)
     
     print ("Average logins per day for", username, "is", average_day_logins)
     
     login_ratio = current_day_logins / average_day_logins

     return login_ratio

login_analysis = analyze_logins ("Franco Rizzi", 8,2)
if login_analysis >= 3:
     print ("Alert!. This account has more login activity than normal.")
else: 
     print("All good here")

print("Franco Rizzi", "logged in", login_analysis, "times as much as they do on an average day")






