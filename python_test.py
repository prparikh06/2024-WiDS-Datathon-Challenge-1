# start off your script with any module you will be inputting. it's good practice
from datetime import date, datetime # import the date and datetime objects from the datetime module

def get_days():
    # prompt the user to input birthday
    bday = input('Please enter your birthday (yyyy-mm-dd):\n')
    
    # the variable bday is a string. we need to convert it into a datetime object
    date_format = '%Y-%m-%d'
    bday_date = datetime.strptime(bday, date_format)
    
    # get today's date
    today = datetime.today()

    # get the number of days: today - birthday
    result = today - bday_date
    
    # return the number of days
    return result

name = input('Hello! Please enter your name:\n')
print('\nName entered: '+ name + '\n')

days = get_days()
print('\nYou are %s days old!\n' % days)



