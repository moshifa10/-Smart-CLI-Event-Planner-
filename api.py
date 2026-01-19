import requests


class Api:
    def __init__(self):
        self.api = "http://worldtimeapi.org/api/timezone"
        self.holiday = "https://date.nager.at/api/v3/publicholidays"

    def view_date(self):
        area = "Africa"
        region = "Johannesburg"
        headers = {"User-Agent": "Mozilla/5.0"}
        get_data = requests.get(f"{self.api}/{area}/{region}", headers=headers, timeout=5)


        if get_data.status_code == 200:
            print(f"Successfully got the data with this code: {get_data.status_code}")
            data = get_data.json()
        # print(get_data.connection)
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


    def public_holidays(self,country_code, year=2026):
        country_code = country_code.upper()
        get_data = requests.get(f"{self.holiday}/{year}/{country_code}")

        if get_data.status_code == 200:
            print(f"Successfully got the data with this code: {get_data.status_code}")
        print(get_data.status_code)
        data = get_data.json()
        # print(data)

        print(f"Public Holidays in South Africa ({year}):")
        for index,each_holiday in enumerate(data, start=1):
            date, name = each_holiday['date'], each_holiday['name']
            print(f"{index}. {name}        - {date}")
        


# current = Api()
# current.view_date()
# current.public_holidays(country_code="ZA")