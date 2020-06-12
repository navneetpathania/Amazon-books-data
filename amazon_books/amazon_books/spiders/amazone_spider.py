import scrapy
from ..items import AmazonBooksItem
from bs4 import BeautifulSoup
import lxml
class AmazonSpider(scrapy.Spider):
	name = 'amazon'
	start_urls = ['https://www.amazon.com/gp/bestsellers/books/283155/ref=s9_acsd_ri_bw_clnk/ref=s9_acsd_ri_bw_c2_x_c2cl?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-10&pf_rd_r=YYCRWVVG1TFJAWJT5NEW&pf_rd_t=101&pf_rd_p=d2e01c79-7462-4300-8d41-3633536344dc&pf_rd_i=283155']

	def parse(self,response):
		item = AmazonBooksItem()
		soup = BeautifulSoup(response.text,'lxml')
		all_books = soup.findAll('li',class_='zg-item-immersion')
		for book in all_books:
			content = book.contents[0].contents[0].contents[1]
			image = content.contents[0].contents[0].contents[0].contents[0]['src']
			# print(content.contents[0].contents[0].contents[0].contents[0]['src'])
			# print(content.contents[0].contents[2].text)
			title = content.contents[0].contents[2].text
			# print(content.contents[1].contents[0].text)
			author = content.contents[1].contents[0].text
			try:
				price = content.contents[6].contents[0].contents[0].contents[0].text
				# print(price)
			except:
				price = 'Nan'

			item['title'] = title
			item['author'] = author
			item['price'] = price
			item['image'] = image

			yield item