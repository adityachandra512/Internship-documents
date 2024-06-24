import calendar
year = int(input("Enter the year for which you want the calendar: "))
cal = calendar.TextCalendar(calendar.SUNDAY)
cal_text = cal.formatyear(year)
print(cal_text)
