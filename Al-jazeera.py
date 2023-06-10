from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

# Set up Selenium webdriver
driver = webdriver.Chrome(executable_path= r"C:\Users\Apple Computer\Downloads\Compressed\chromedriver")  # Replace with the path to your Chrome webdriver
driver.get("https://www.aljazeera.com")
time.sleep(3)  # Wait for the page to load

# Scroll the page to load all links
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Create a BeautifulSoup object with the page source
soup = BeautifulSoup(driver.page_source, "html.parser")

article_links = []
for link in soup.find_all('a', class_='u-clickable-card__link'):
    article_links.append(link["href"])

print(len(article_links))
print(article_links)

# Create a list to store the extracted data
data = []

for l in article_links:
    try:
        driver.get("https://www.aljazeera.com" + l)
        time.sleep(2)  # Wait for the page to load
        print(driver.current_url)
        artical_link = driver.current_url
        soup = BeautifulSoup(driver.page_source, "html.parser")

        main_heading = soup.find('h1').text
        print(main_heading)

        detail = soup.find('p', class_='article__subhead css-1wt8oh6').text
        print(detail)

        topics = soup.find('div', class_='topics')
        tag_links = topics.find_all('a')
        tags = [link.text for link in tag_links]
        print(tags)

        div_element = soup.find('div', class_='date-simple css-1yjq2zp')
        date_text = div_element.find('span', attrs={'aria-hidden': 'true'}).text
        print(date_text)

        source = soup.find('div', class_='article-source').text.strip()
        print(source)
        # Append the extracted data to the list
        row = [main_heading, detail, date_text, artical_link, source]
        row.extend(tags)
        data.append(row)
    except Exception as e:
        print(f"An error occurred: {e}")

print(data)
print('done')

# Save the data to a CSV file
filename = 'today_News.csv'
header = ['Main Heading', 'Detail', 'Date', 'Artical_Link', 'Source', 'Tag 1', 'Tag 2', 'Tag 3', 'Tag 4', 'Tag 5']
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print(f'Data has been saved to {filename}')

# Close the Selenium webdriver
driver.quit()
