import json

# here It will be the events where user uses to store data and post
FILE_NAME = "data.json"
class Events:
    def __init__(self):
        self.id = 1

    def create_event(self, title, date, start_time, end_time):
        user_data = {
            "id": self.id,
            "tittle": title,
            "date": date,
            "start_time": start_time,
            "end_time": end_time
        }
        self.write_to_json(user_data)
        print(f"Event created successfully!")
        self.id += 1
    
    def write_to_json(self, data):
        with open(file=FILE_NAME, mode="a") as file:
            json.dump(data, file, indent=4)


    def view_saved_events(self):
        print("Your Events: ")
        if FILE_NAME:
            for count, event in enumerate( FILE_NAME):
                print(f"[{count}] {event["tittle"]}\n    Date: {event['date']}\n    Time: {event['start_time']} - {event['end_time']}")

        else:
            print("No Event yet!")
    
