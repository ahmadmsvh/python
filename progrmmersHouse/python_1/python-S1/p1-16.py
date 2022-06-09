print("calculating your age in minutes")

age_years=int(input("enter years of your age:\t"))
age_months=int(input("enter months of your age:\t"))
age_days=int(input("enter days of your age:\t"))

hour_to_minutes=60
day_to_minutes=24*hour_to_minutes
month_to_minutes=30*day_to_minutes
year_to_minutes=12*month_to_minutes

# age_minutes=(age_days+age_months*30+age_years*365)*24*60

age_minutes=(age_years*year_to_minutes+age_months*month_to_minutes+age_days*day_to_minutes)

print("your age in minutes is:\t%d\n" %age_minutes)