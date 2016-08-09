import time

#weekdays =  ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
weekdays = [1,2,3,4,5,6,7]
Months = [1,2,3,4,5,6,7,8,9,10,11,12]

days_in_month = {4:30,6:30,9:30, 11:30, 1:31, 3:31, 5:31, 7:31, 8:31, 10:31, 12:31, 2:28}


start_year = 1901
start_month = 1
start_day = 1


end_year = 2000
end_month = 12
end_day = 31

year=start_year
month=start_month
day=start_day
weekday = 1

sundays=0
while not (day == end_day and month == end_month and year==end_year):
	#time.sleep(0.1)
	#print str(weekday) + " " + str(day) + " " + str(month) + " " + str(year)
	
	#Sunday happens
	if day==1:
		if weekday == 7:
			sundays+=1
			print str(weekday) + " " + str(day) + " " + str(month) + " " + str(year)
	
	#February weird case
	if month==2:
		if year%4==0:
			days_in_month[2] = 29
		if str(year).find('000'):
			if year %400==0:
				days_in_month[2] = 29
			else:
				days_in_month[2] = 28
		else:
			days_in_month[2] = 28	

	#Last day of month
	if days_in_month[month]==day:
		day=1
		if month==12:
			year+=1
			month=1
		else:
			month +=1
	else:
		day+=1
	
	weekday+=1
	if weekday==8:
		weekday=1


print sundays

#weekday day mon year
