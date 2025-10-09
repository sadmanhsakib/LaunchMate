import webbrowser
import os
import datetime
from dotenv import load_dotenv

load_dotenv(".env")

lifetime_counter = 0
today_counter = 0

# creating a new log file if there is no log file
if not (os.path.exists("log.csv")):
    # creates a new log file
    with open("log.csv", 'w') as file:
        # writing the header
        file.write("Lifetime-Counter,Today-Counter,Date,Time")

log_file = "log.csv"


def main():
    try:
        with open(log_file, 'r') as file:
            # getting the counter values
            lines = file.readlines()
            parts = lines[-1].split(',')
            lifetime_counter = int(parts[0])
            today_counter = int(parts[1])
            
    # handling the case when the log file is empty
    except ValueError:
        lifetime_counter = 1
        today_counter = 1
    
    # running the functions to open the sites and log the event
    open()
    log_event(lifetime_counter, today_counter)


def open():
    # for opening the websites
    url_list = os.getenv("URLS")
    
    # checking for empty list
    if url_list != None:
        for url in url_list.split(','):
            webbrowser.open(url)

    # for opening the applications through their shortcuts
    app_list = os.getenv("SHORTCUTS")
    
    # checking for empty list
    if url_list != None:
        for app in app_list.split(','):
            os.startfile(app)


def log_event(lifetime_counter, today_counter):
    # getting the current date and time
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    
    # updating the counter values before logging
    lifetime_counter += 1
    
    if is_new_day():
        today_counter = 1
    else:
        today_counter += 1
    
    # logging the current run time in log file
    with open(log_file, 'a') as file:
        file.write(f"\n{lifetime_counter},{today_counter},{current_date},{current_time}")


def is_new_day():
    isNewDay = False
    
    with open(log_file, 'r') as file:
        # getting the information from the log file
        lines = file.readlines()
        parts = lines[-1].split(',')
        last_date = parts[2]
        
        # getting today's date
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        
        if last_date != today:
            isNewDay = True
            
        return isNewDay
    
if __name__ == "__main__":
    main()