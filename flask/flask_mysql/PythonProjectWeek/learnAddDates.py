


from datetime import *
#import datetime


#datevar2=datetime.date.today()
#currentDate = datetime.strptime(datevar2,'%d/%m/%Y').date()
#print(currentDate)
print("*"*80)

#timedelta(newvar)
#newvar.days+=45
#d = timedelta()


newvar=datetime.today()
print(newvar)
numberDays=20
end_date = newvar + timedelta(days=numberDays)  #date_1 should be my currentDate
print(end_date)

numberDays=20
date_from_now = (datetime.now() + timedelta(days=numberDays) ).strftime('%m-%d-%Y')  #strftime('%Y-%m-%d')
print("7"*80)
print(date_from_now)

#currentDate = datetime.strptime(str(end_date),'%d/%m/%Y').date()

#end_date=end_date.days()
#######below worked
# start_date = "10/10/11"
# date_1 = datetime.strptime(start_date, "%m/%d/%y")

# end_date = date_1 + timedelta(days=20)
# print(end_date)
###end below worked#########

#need a time delta and add the time delta

#print(newvar)