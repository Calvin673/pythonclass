
from text_to_voice import to_voice
import usa_holidays as usa_holidays


prompt = "Enter a month to check for holidays (e.g., January, February, etc.): "
print(prompt)
to_voice(prompt)
month = int(input(">"))

to_voice("Welcome to the USA Holidays Checker!")
        

        
result = usa_holidays.findHolidays2(month)
if result:
    print(result)
    to_voice(result)
            
            
else:
    warning = "No input specified. Please try again."
    to_voice(warning)
    print(warning)