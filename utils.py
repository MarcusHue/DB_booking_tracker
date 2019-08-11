
import datetime as dt 


def clean_convert_time(time_string):
    time_object = time_string.split()
    if (len(time_object) >1):
        planned_time = dt.datetime.strptime(time_object[0],'%H:%M').time()
        planned_time = dt.datetime.combine(dt.date.today(), planned_time)
        actual_time = dt.datetime.strptime(time_object[1],'%H:%M').time()
        actual_time = dt.datetime.combine(dt.date.today(), actual_time)
        time_object = {'planned_time': planned_time, 'actual_time':actual_time}
    else:
        planned_time = dt.datetime.strptime(time_object[0],'%H:%M').time()
        planned_time = dt.datetime.combine(dt.date.today(), planned_time)
        time_object = {'planned_time': planned_time, 'actual_time':planned_time}
    return(time_object)
