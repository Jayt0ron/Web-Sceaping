#Check your Understanding - 1
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
html_page = urlopen(url)
html_text = html_page.read().decode("utf-8")

for string in ["Name: ", "Favorite color: "]:
  string_start_idx = html_text.find(string)
  text_start_idx = string_start_idx + len(string)

  next_html_tag_offset = html_text[text_start_idx:].find("<")
  text_end_idx = text_start_idx + next_html_tag_offset

  raw_text = html_text[text_start_idx : text_end_idx]
  clean_text = raw_text.strip(" \r\n\t")
  print(clean_text)

#Check your Understanding - 2
from bs4 import BeautifulSoup

base_url = "http://olympus.realpython.org"

html_page = urlopen(base_url + "/profiles")
html_text = html_page.read().decode("utf-8")

soup = BeautifulSoup(html_text, "html.parser")

for link in soup.find_all("a"):
  link_url = base_url + link["href"]
  print(link_url)

#Check your Understanding - 3
import mechanicalsoup

browser = mechanicalsoup.Browser()

login_url = "http://olympus.realpython.org/login"
login_page = browser.get(login_url)
login_html = login_page.soup

form = login_html.form
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"
profiles_page = browser.submit(form, login_page.url)

print(profiles_page.soup.title)