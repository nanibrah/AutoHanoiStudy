import datetime
import time
from os import system
system('title Thời gian còn lại trước khi đóng. Không  muốn thì đóng tab')
future_date = datetime.datetime.now() + datetime.timedelta(seconds=604800)
while True:
    curr_date = datetime.datetime.now()
    rem_time = future_date - curr_date
    total_seconds = int(rem_time.total_seconds())

    if total_seconds > 0:
        days, h_remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(h_remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        print("Time Left: {} days, {} hours, {} minutes, {} seconds".format(days, hours, minutes, seconds))
        time.sleep(1)
    else:
        system('TASKKILL /F /IM cmd.exe /T')
        break