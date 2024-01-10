from datetime import date as date_n

def NumberOfDays(date_1, date_2):
    return (date_2 - date_1).days

date_1 = date_n(2025, 9, 23)
date_2 = date_n(2025, 9, 25)
print ("Number of Days between the given Dates are: ", NumberOfDays(date_1, date_2), "days")