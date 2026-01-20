import usa_holidays as usa_holidays

while True:
    month = int(input("Enter a month to check for holidays (e.g., January, February, etc.): "))
    result = usa_holidays.findHolidays2(month)
    if result is not None:
        print(result)
    else:
        print("No input specified. Please try again.")