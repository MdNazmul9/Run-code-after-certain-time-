import schedule
import time

def do_nothing():
    print("Ehsan Marketing")

schedule.every(3).seconds.do(do_nothing)
while 1:
    schedule.run_pending()
    time.sleep(1)
