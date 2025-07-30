import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url, output_file):
    try:
        # Send HTTP request
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status codes
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Scraping a table - adjust selectors based on actual page structure
        table = soup.find('table', {'class': 'data-table'})  # Update class name
        rows = table.find_all('tr')
        
        # Extract data
        data = []
        for row in rows[1:]:  # Skip header row
            cols = row.find_all('td')
            data.append([col.text.strip() for col in cols])
        
        # Create DataFrame and save
        df = pd.DataFrame(data)
        df.to_csv(output_file, index=False)
        print(f"Data successfully scraped and saved to {output_file}")
        
        return df
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# Example usage
url = "https://example.com/data-table"  # Replace with target URL
output_file = "scraped_data.csv"
scraped_data = scrape_website(url, output_file)