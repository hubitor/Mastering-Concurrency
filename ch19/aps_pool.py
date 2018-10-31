from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler

def tick():
    print(f'From process {os.getpid()}: The time is {datetime.now()}')

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_executor('processpool')
    scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()

    try:
        while True:
            time.sleep(2)
            print(f'Printing from main process {os.getpid()}')
    except KeyboardInterrupt:
        scheduler.shutdown()
