from datetime import timezone
import datetime
import pytz
import tzlocal


'''current_time = datetime.datetime.now()
print(current_time)

utc_datetime = datetime.datetime.utcnow()
print(utc_datetime)

time_dict = {"time":utc_datetime}

print(time_dict)'''




  
  
# Getting the current date
# and time
'''dt = datetime.datetime.now(timezone.utc)
  
utc_time = dt.replace(tzinfo=timezone.utc)
print(utc_time)

time_dict = {"time":utc_time}
print(time_dict)

utc_timestamp = utc_time.timestamp()
  
print(utc_timestamp)'''


'''ist_time = tzlocal.get_localzone()
print(ist_time)

real_ist_time = utc_datetime.replace(tzinfo=pytz.utc).astimezone(ist_time)

print(real_ist_time)'''




result = db.objects.insert_one(

    {"last_modified": datetime.datetime.utcnow()})