# beauty_soup.py

from bs4 import BeautifulSoup
from urllib.request import urlopen
import mechanicalsoup
import time




url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())

soup.find_all("img")

image1, image2 = soup.find_all("img")

image1.name

image1["src"]
image2["src"]

soup.title.string

soup.find_all("img", src="/static/dionysus.jpg")


browser = mechanicalsoup.Browser()

url = "http://olympus.realpython.org/login"
page = browser.get(url)

print(page)

type(page.soup)

page.soup

base_url = "http://olympus.realpython.org"

html_page = browser.get(base_url)

# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
profiles_page = browser.submit(form, login_page.url)

profiles_page.url

links = profiles_page.soup.select("a")

for link in links:
  address = (link["href"])
  text = link.text
  print(f"{text}: {address}")

browser = mechanicalsoup.Browser()
page = browser.get("http://olympus.realpython.org/dice")
tag = page.soup.select("#result")[0]
result = tag.text

print(f"The reuslt of your dice roll is: {result}")

#.sleep() method takes a single argument that reprents the number of seconds to sleep
print("I'm about to wait for five seconds...")
time.sleep(5)
print("Done waiting!")

browser = mechanicalsoup.Browser()

for i in range(4):
  page = browser.get("http://olympus.realpython.org/dice")
  tag = page.soup.select("#result")[0]
  result = tag.text
  print(f"The result of your dice roll is: {result}")
 
  # Wait 10 seconds if this isn't the last request
  if i < 3:
    time.sleep(10)

#techniques like this, you can scrape data from websites that update their data
#updates periodically(btw)
