from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

def scrape_product_info(url):
    # Open the URL and read the content
    with urlopen(url) as response:
        html = response.read()
    
    # Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all product elements (adjust the selector based on the website's structure)
    products = soup.find_all('div', class_='product-item')
    
    # List to store product information
    product_list = []
    
    for product in products:
        # Extract product name
        name = product.find('h2', class_='product-name').text.strip()
        
        # Extract product price
        price = product.find('span', class_='price').text.strip()
        
        # Extract product rating
        rating = product.find('div', class_='rating').get('data-rating', 'N/A')
        
        # Append product info to the list
        product_list.append([name, price, rating])
    
    return product_list

def save_to_csv(product_list, filename):
    # Write product information to CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Price', 'Rating'])  # Write header
        writer.writerows(product_list)

# Main execution
if __name__ == "__main__":
    # URL of the e-commerce website 
    url = https://www.flipkart.com/sony-playstation-5-console-825-gb/p/itm62f0f8b3c0bfb?pid=GMCGHMTYZ8BUBMFB&lid=LSTGMCGHMTYZ8BUBMFBE2W9DE&marketplace=FLIPKART&q=ps5+console&store=4rr%2Fx1m&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&fm=Search&iid=d1beacfb-eee0-4306-98e7-23f76f12f19a.GMCGHMTYZ8BUBMFB.SEARCH&ppt=sp&ppn=sp&ssid=tfysrn4j400000001723214845482&qH=63cbe5d6e6345fd8
    # Scrape product information
    products = scrape_product_info(url)
    
    # Save to CSV file
    save_to_csv(products, 'product_info.csv')
    
    print(f"Product information has been saved to product_info.csv")
