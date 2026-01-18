from api import Api
from events import Events
import argparse

api = Api()
events = Events()

'''
==============================
 SMART CLI EVENT PLANNER
==============================
1. View today's date & time
2. View public holidays for a country
3. Create a local event
4. View saved events
5. Delete an event
6. Exit
'''

parser = argparse.ArgumentParser(description="This is my Smart CLI event planner")
parser.add_argument("-t", "--today", help="View today's date and time", action="store_true")
parser.add_argument("-o", "--holiday", help="View holidays", action="store_true")
parser.add_argument("-v","--view", help="View holidays", action="store_true")
parser.add_argument("-c", "--create", nargs="+", help="This is create flag where you add events tittle, date, start_time and end_time")
parser.add_argument("-d", "--delete", help="Delete an event using id of your choice", nargs="+")

args = parser.parse_args()  

if args.today:
    api.view_date()

elif args.holiday:
    api.public_holidays(country_code="ZA")

elif args.view:
    events.view_saved_events()

elif args.create:
    tittle, date, start_time, end_time = args.create
    events.create_event(title=tittle, date=date, start_time=start_time, end_time=end_time)

elif args.delete:
    events.delete_event(int(args.delete[0]))