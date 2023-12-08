import requests
from bs4 import BeautifulSoup
import json

# Replace the URL with the actual URL from the first response
url = "https://audiovault.net/shows"

# Send an HTTP request to the URL and get the content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table in the HTML
    table = soup.find('table')

    # Extract data from the table, including download links
    table_data = []
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        row_data = {
            'ID': cells[0].text.strip(),
            'Name': cells[1].text.strip(),
            'Download': cells[2].find('a')['href'].strip() if cells[2].find('a') else None
        }
        table_data.append(row_data)

    # Print or save the JSON result
    print(json.dumps(table_data, indent=2, ensure_ascii=False))

else:
    print(f"Failed to retrieve content. Status code: {response.status_code}")
