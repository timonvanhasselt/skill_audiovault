import requests
from bs4 import BeautifulSoup
import json

# Replace the URL with the actual URL from the first response
base_url = "https://audiovault.net/shows"

# Initialize an empty list to store the data from all pages
all_table_data = []

# Iterate through each page (assuming pagination parameter is 'page')
for page_number in range(1, 81):  # Assuming there are 80 pages
    # Construct the URL for the current page
    url = f"{base_url}?page={page_number}"

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

        # Append the data from the current page to the overall list
        all_table_data.extend(table_data)

    else:
        print(f"Failed to retrieve content for page {page_number}. Status code: {response.status_code}")

# Print or save the JSON result for all pages
print(json.dumps(all_table_data, indent=2, ensure_ascii=False))



