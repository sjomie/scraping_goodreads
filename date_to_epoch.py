import datetime
from module.normalize_date import normalize_date

def date_to_epoch(date_string):

    date_string = normalize_date(date_string)

    date_object = datetime.datetime.strptime(date_string, "%B %d, %Y")
    epoch_start = datetime.datetime(1970, 1, 1)
    time_delta = date_object - epoch_start
    epoch_time = time_delta.total_seconds()

    return epoch_time

# print(date_to_epoch("January 5, 30"))
# print(date_to_epoch("January 5, 300"))
# print(date_to_epoch("January 5, 3000"))
# print(date_to_epoch("January 5, 3"))
