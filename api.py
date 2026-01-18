import requests


class Api:
    def __init__(self):
        self.api = "http://worldtimeapi.org/api/timezone"

    def view_date(self):
        area = "Africa"
        region = "Johannesburg"
        get_data = requests.get(f"{self.api}/{area}//{region}")


        if get_data.status_code == 200:
            print(f"Successfully got the data with this code: {get_data.status_code}")
            data = get_data.json()


        print(data)
        # convert them to usable things
        date = []
        change = 0
        time = []
        for i in data["datetime"]:
            if i == ".":
                break
            if i.isalpha():
                change +=1 
                continue
            if  change > 0:
                time.append(i)
            else:
                date.append(i)

        print(f"Current Time Zone : {data["timezone"]}")
        print(f"Current Date      :  {''.join(date)}")
        print(f"Current Time      : {''.join(time)}")
        print(f"Day               : sunday")



current = Api()
current.view_date()