# Log Analyzer Applcation

logs=[
    "2026-09-21 10:32:15 | INFO | user=vishesh | action=login | ip=192.168.1.10",
    "2026-09-21 10:35:42 | ERROR | user=rahul | action=payment | amount=499 | error=Payment Failed",
    "2026-09-21 10:36:10 | WARNING | user=amit | action=login | ip=192.168.1.25",
    "2026-09-21 10:40:21 | INFO | user=vishesh | action=logout",
    "2026-09-21 10:45:33 | ERROR | user=neha | action=payment | amount=999 | error=Card Declined",
    "2026-09-21 10:50:12 | INFO | user=rahul | action=login | ip=192.168.1.30",
    "2026-09-21 10:55:45 | WARNING | user=neha | action=login | ip=192.168.1.40",
]


# show all logs 

def show_all_logs():

    for log in logs:
        print(log)

show_all_logs()


# search a log  

def search_log():
    keyword=input("enter you what you want to search   : ").strip()

    if "" in keyword:
        print("keyword can not be empty")

    found=False

    for log in logs:
        if keyword.lower()==log.lower():
            print(log)
            found=True

    if not found:
        print("No matching logs found")

search_log()