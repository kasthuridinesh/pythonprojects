from datetime import datetime
import datetime


# Task 1 finding expire date after 10 years
def policy_expire_date():
    today_date = datetime.date.today()
    expire_date = datetime.date(today_date.year + 10, today_date.month, today_date.day)

    if 4 <= today_date.day <= 20 or 24 <= today_date.day <= 31:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][today_date.day % 10 - 1]

    print("Today date is:", today_date.strftime(f'%d{suffix}%B %Y'))
    print("Today date is:", expire_date.strftime(f'%d{suffix}%B %Y'))

    # print("Expire date is:", expire_date)


# # Task 2
def registration_date():
    current_Date = datetime.datetime.today()
    print('Current Date: ' + str(current_Date))

    if 4 <= current_Date.day <= 20 or 24 <= current_Date.day <= 31:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][current_Date.day % 10 - 1]

    registarion_Date = datetime.datetime.today() - datetime.timedelta(days=8 * 365)
    print('Registarion_Date is: ' + str(registarion_Date))

    expire_Date = datetime.datetime.today() + datetime.timedelta(days=365)

    print("Current date is:", "\n", current_Date.strftime(f'%d{suffix}%B %Y'))
    print("Registar date is:", "\n", registarion_Date.strftime(f'%d{suffix}%B %Y'))
    print("Expire date is:", expire_Date.strftime(f'%d{suffix}%B %Y'))


registration_date()

# Task 3
def timeleft():
    # Assign the registration date of the policy
    registrationDate = datetime.datetime(year=2015, month=4, day=1)
    # Get the current date and time
    todayDate = datetime.datetime.now()
    # Calculate the time left for the policy to expire
    timeLeft = todayDate - registrationDate
    print("Time left for policy to expire: ", timeLeft)


# # Task 4(a)
def timestamp():
    current_date = datetime.datetime.now()
    time_stamp = current_date.timestamp()
    print("The timestamp of the current date is:", time_stamp)


# Task(b)
def datetime_Timestamp():
    time_stamp = ""
    if time_stamp != "":
        date_time = datetime.datetime.fromtimestamp(time_stamp).strftime("%d %B %Y %H:%M %p")
        print("Getting time stamp of given is", date_time)
    else:
        print("Pass correct timestamp")
