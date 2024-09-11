"""
urllib contains tools for working with URLs
#urllib.request contains a function called urlopen(), it can open a URL in a program
"""
import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
#urlopen() returns an HTTPResponse object
page = urlopen(url)

print(page)


#HTTPResponse object's .read() method reuturns a sequence of bytes.
#.decode() can decode the bytes to a string using UTF-8
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
#Extract Text from HTML with String Methods
#.find() can search through the text of the HTML
#.find() seraches for the index of a title
title_index = html.find("<title>")
print(title_index)

start_index = title_index + len("<title>")
print(start_index)

end_index = html.find("</title>")
print(end_index)

title = html[start_index:end_index]
print(title)

url = "http://olympus.realpython.org/profiles/poseidon"

url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
print(title)

#regular expressions or regexes are a way to specify patterns in strings
#Regular expressions aren't particular to Python.It's a general programming concept

#regular expression use special characters called metacharacters 
#metacharacters can denote different patterns
# e.g. you use .findall() to find any text within a string that matches a pattern
re.findall("ab*c", "ac")
re.findall("ab*c", "abcd")
re.findall("ab*c", "acc")
re.findall("ab*c", "abcac")
re.findall("ab*c", "abdc")
re.findall("ab*c", "ABC")
re.findall("ab*c", "ABC", re.IGNORECASE)

re.findall("a.c", "abc")
re.findall("a.c", "abbc")
re.findall("a.c", "ac")
re.findall("a.c", "acc")


#The pattern .* inside a regular expression stands for 
#any character repeated any number of times.


re.findall("a.*c", "abc")
re.findall("a.*c", "abbc")
re.findall("a.*c", "ac")
re.findall("a.*c", "acc")

match_results = re.search("ab*c", "ABC", re.IGNORECASE)
match_results.group()

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
print(string)

#Python's regular expression try to find the longest possible match
#re.sub() can find and replace everything between "<" and ">"


#find.() method would have a hard time dealing with incosistencies
#but with regular expressions, you can handle this code quick:

# regex_soup.py

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)

# Check Understanding
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


