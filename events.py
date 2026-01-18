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
        try:
            with open(FILE_NAME, mode="r") as data:
                data = json.loads(data)
                if FILE_NAME:
                    print("Your Events: ")
                    for count, event in enumerate( FILE_NAME):
                        print(f"[{count}] {event["tittle"]}\n    Date: {event['date']}\n    Time: {event['start_time']} - {event['end_time']}")
        except FileNotFoundError:
            print("Try checking your file path")

        else:
            print("No Event yet!")


    def delete_event(self, id):
        try: 
            with open(file=FILE_NAME, mode="r") as data:
                data = json.loads(data)

                for event in data:
                    if event["id"] == id:
                        print(f"Event ({event['tittle']}) deleted successfully.")
                        del event
            
        except FileNotFoundError:
            print(f"The file was not found check the path {FILE_NAME}")
    
