from src.cron import start_scheduler

print("Application started")
print("Scheduled job runs everyday at London market session opening time (9:00 AM)")

if __name__ == "__main__":
    start_scheduler("07:04")