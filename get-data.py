import requests
import csv
import time


def get_lawmakers(filename, url):
    r = requests.get(url)
    data = r.json()
    lawmakers = data["data"]

    with open(filename, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Title", "Full Name", "Last", "First", "District", "Party", "ID"])
        for lawmaker in lawmakers:
            fullname = "{} {}".format(
                lawmaker["FirstName"],
                lawmaker["LastName"]
            )

            csvwriter.writerow([
                lawmaker.get("Title"),
                fullname,
                lawmaker.get("LastName"),
                lawmaker.get("FirstName"),
                lawmaker.get("District"),
                lawmaker.get("Party"),
                lawmaker.get("PersonID")
            ])



get_lawmakers(
    "house-info.csv",
    "https://legislature.vermont.gov/people/loadAll/2020/House?_=1547739869592"
    )


time.sleep(2)

get_lawmakers(
    "senate-info.csv",
    "https://legislature.vermont.gov/people/loadAll/2020/Senate?_=1547743220354"
)
