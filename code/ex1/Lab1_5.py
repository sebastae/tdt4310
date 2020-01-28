import urllib3
from xml.etree import ElementTree as ET


# RSS feed for https://ntnu.edu/vacancies with the field id=346d3f54-984e-45df-bed9-09d126dfc4e1
URL = "https://www.jobbnorge.no/apps/joblist/joblistbuilder.ashx"

http = urllib3.PoolManager()
req = http.request("GET", URL, fields={"id":"346d3f54-984e-45df-bed9-09d126dfc4e1"})


root = ET.fromstring(req.data.decode('utf-8'))

channel = root.find("channel")
items  = channel.findall("item")

print(f"Vacancies: {len(items)}")

titles = []
for item in items:
    titles.append(item.find("title").text)

p_titles = []

for title in titles:
    # Split removes the splitting term, and since all posts have <Title> - Søknadsfrist: <Deadline>, all we are left with is the name and deadline
    s = title.split(" - Søknadsfrist:")
    name = s[0]
    deadline = s[1]

    p_titles.append((name, deadline))

for n, d in p_titles:
    # Prints in format <Title> [<Deadline>]
    print(f"{n.strip()} [{d.strip()}]")



