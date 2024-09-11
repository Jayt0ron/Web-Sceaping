import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

#URL to scrape
url = "https://tfwiki.net/wiki/Bumblebee_(Movie)/toys"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

# Open URL and read the page content
try:
    page = urlopen(req)
    html = page.read().decode("utf-8")
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Parse the html
soup = BeautifulSoup(html, "html.parser")

#Find the div
toc_div = soup.find('div', id = "toctitle") 
print(toc_div.prettify())
# list to store the toys
toy_list =[]


# Check if the div was found
if toc_div:
    # Find all <li> elements within the div
    toy_items = toc_div.find_all('li')

    # Extract the text from each <li> element and add to the list
    for item in toy_items:
        toy_name = item.get_text(strip=True)
        toy_list.append(toy_name)


    # Count the number of toys
    num_toys = len(toy_list)
    print(f"Number of toys listed: {num_toys}")


    # Create a DataFrame from the list of toy names
    df = pd.DataFrame({'toy_name': toy_list})

    # Save the DataFrame to a CSV file
    df.to_csv('toys_list.csv', index=False)
    print("Toy names have been written to 'toys_list.csv'")
else:
  print("No div with id 'toc' found.")