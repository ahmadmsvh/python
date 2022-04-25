user_hour= int(input("enter hour: "))
user_minute= int(input("enter minut: "))

user_hour_to_minute=user_hour*60
user_minutes=user_hour_to_minute+user_minute

twentyfour_hours_to_minutes=24*60

remain_minutes_to_midnight=(twentyfour_hours_to_minutes)-(user_minutes)

print("remaining hours until midnight is: %d" %remain_minutes_to_midnight)