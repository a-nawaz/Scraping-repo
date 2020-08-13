import requests
from bs4 import BeautifulSoup
from csv import DictWriter

def scrapper():
	url = "http://quotes.toscrape.com"
	next_url = "/page/1"
	with open("scraped_data.csv", "w", encoding="utf-8") as file:
		headers = ["quote", "author", "url", "born", "location"]
		data_scrapper = DictWriter(file, fieldnames=headers)
		data_scrapper.writeheader()
		while next_url:
			print(url + next_url)
			print("Starting Data Scraping.......")
			response = requests.get(url + next_url)
			soup = BeautifulSoup(response.text, "html.parser")
			quotes = soup.select(".quote")
			next_button = soup.select(".next")
			next_url = next_button[0].find("a")["href"] if next_button else None
			for quote in quotes:
				my_quote = quote.select(".text")[0].get_text()
				my_author = quote.select(".author")[0].get_text()
				my_about_url = quote.find("a")["href"]
				response = requests.get(url + my_about_url)
				soup = BeautifulSoup(response.text, "html.parser")
				my_born_date = soup.select(".author-born-date")[0].get_text()
				my_born_location = soup.select(".author-born-location")[0].get_text()
				data_scrapper.writerow({
					"quote": my_quote,
					"author": my_author,
					"url": my_about_url,
					"born": my_born_date,
					"location": my_born_location
					})
					

scrapper()



