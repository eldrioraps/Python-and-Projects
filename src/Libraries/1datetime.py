# from datetime import datetime

# # current date and time
# now = datetime.now()
# print("Current date and time:", now)

# # individual components
# print("Year:", now.year)
# print("Month:", now.month)
# print("Day:", now.day)
# print("Hour:", now.hour)
# print("Minute:", now.minute)
# print("Second:", now.second)


# from datetime import date, time, datetime
# today = date.today()
# print("Today's date:", today)
# current_time = datetime.now().time()
# print("Current time:", current_time)


# from datetime import datetime
# now = datetime.now()
# print("Default:", now)
# # formatted output
# print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))
# print("Date only:", now.strftime("%d-%b-%Y"))
# print("12-hour time:", now.strftime("%I:%M %p"))
# print("Weekday name:", now.strftime("%A"))


# from datetime import datetime, timedelta

# today = datetime.now()
# print("Today:", today)

# # add 7 days
# future = today + timedelta(days=7)
# print("7 days later:", future)

# # subtract 30 minutes
# past = today - timedelta(minutes=30)
# print("30 minutes earlier:", past)

# from datetime import timedelta

# # works fine
# delta = timedelta(days=30)


from datetime import datetime, timedelta

def calculate_age(dob_str):
    """
    Calculate approximate age using timedelta.
    dob_str should be in 'YYYY-MM-DD' format.
    """
    # Convert input string to datetime
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    today = datetime.now()
    
    # Difference in days
    diff = today - dob  # this gives a timedelta object
    total_days = diff.days
    
    # Approximate conversions
    years = total_days // 365
    months = (total_days % 365) // 30
    days = (total_days % 365) % 30
    
    print(f"Date of Birth: {dob.date()}")
    print(f"Today: {today.date()}")
    print(f"Age: {years} years, {months} months, {days} days ")

# Example usage
calculate_age("1998-07-15")
