import requests
from bs4 import BeautifulSoup
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

request = requests.get("https://info.cern.ch/hypertext/WWW/TheProject.html")
soup = BeautifulSoup(request.content, 'html.parser').get_text()

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template("template.html")

update_time = datetime.now()

with open("index.html", "w", encoding="utf-8") as webpage:
    webpage.write(template.render(datetime=update_time, body_text=soup))
    webpage.close()