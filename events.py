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
        with open(file=FILE_NAME, mode="r+") as f:
            file_data = json.load(f)
            f.seek(0)
            file_data.append(data)
            json.dump(file_data, f, indent=4)


    def view_saved_events(self):
        try:
            with open(FILE_NAME, mode="r") as data:
                data = json.load(data)
                if len(data) > 0:
                    print("Your Events: \n")
                    for event in range(len(data)):
                        current_event = data[event]
                        print(f"[{event+1}] {current_event["tittle"]}\n    Date: {current_event['date']}\n    Time: {current_event['start_time']} - {current_event['end_time']}")

                else:
                    print("No Event yet!")
        except FileNotFoundError:
            print("Try checking your file path")

        


    def delete_event(self, id):
        try: 
            with open(file=FILE_NAME, mode="r") as data:
                data = json.load(data)

                for event in data:
                    if event["id"] == id:
                        print(f"Event ({event['tittle']}) deleted successfully.")
                        del event
            
        except FileNotFoundError:
            print(f"The file was not found check the path {FILE_NAME}")
    


my_events = Events()

# my_events.create_event(title="gym", date="2026-01-18", start_time="4", end_time="92")
# my_events.view_saved_events()
my_events.delete_event(2)