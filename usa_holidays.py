def findHolidays(month):
    if month == 1:
        holidays ="New Year's Day on January 1st."
        holidays ="Birthday of Martin Luther King, Jr. (Third Monday in January)"
        holidays ="Inauguration Day (January 20, every 4 years following a presidential election)"
    elif month == 2:
        holidays ="Washington's Birthday (Also known as Presidents Day; third Monday in February)"
    elif month in (3, 4, 8):
        holidays ="No holidays in this month."
    elif month == 5:
        holidays ="Memorial Day (Last Monday in May)"
    elif month == 6:
        holidays ="Juneteenth National Independence Day (June 19)"
    elif month == 7:
        holidays ="Independence Day (July 4)"
    elif month == 9:
        holidays ="Labor Day (First Monday in September)"
    elif month == 10:
        holidays ="Columbus Day (Second Monday in October)"
    elif month == 11:
        holidays ="Veterans Day (November 11)"
        holidays ="Thanksgiving Day (Fourth Thursday in November)"
    elif month == 12:
        holidays ="Christmas Day (December 25)"
    else:
        holidays ="No input specified. Please try again."
    return holidays

def findHolidays2(month):
    holidays = ""
    match month:
        case 1:
            holidays =  "New Year's Day on January 1st. Birthday of Martin Luther King, Jr. (Third Monday in January)"
        case 2:
            holidays =  "Washington's Birthday (Also known as Presidents Day; third Monday in February)"
        case 5:
            holidays =  "Memorial Day (Last Monday in May)"
        case 6:
            holidays =  "Juneteenth National Independence Day (June 19)"
        case 7:
            holidays =  "Independence Day (July 4)"
        case 9:
            holidays =  "Labor Day (First Monday in September)"
        case 10:
            holidays =  "Columbus Day (Second Monday in October)"
        case 11:
            holidays =  "Veterans Day (November 11) Thanksgiving Day (Fourth Thursday in November)"
        case 12:
            holidays =  "Christmas Day (December 25)"
        case 3 | 4 | 8:
            holidays =  "No holidays in this month."
    return holidays
        





