import schedule
import time
from src.pipeline import run_pipeline


def job():
    print("Running scheduled pipeline...")
    run_pipeline()

def start_scheduler(time_to_run="09:00"):
    # Schedule the job to run every day at 9:00 AM
    schedule.every().day.at(time_to_run).do(job)
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")