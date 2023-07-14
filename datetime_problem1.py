from datetime import date, timedelta
start_date = date(2023,7,1)
end_date = date(2023,7,31)
holidays_list = [date(2023,7,3),date(2023,7,24)]
difference_days = end_date - start_date
all_days_list=[]
count=0
weekday_list=[]

for x in range(difference_days.days):
	all_days = (start_date + timedelta(x+1))
	all_days_list.append(all_days)

for y in all_days_list:
	if y.weekday() < 5 : 
		weekday_list.append(y)
		count +=1
final_day_list= list(set(weekday_list) - set(holidays_list))
print('Number of working days is:', len(final_day_list))
print('List of working days:',final_day_list)
