import scraper
from scrapy import Selector

result_html = scraper.retrieve_results_html()
sel = Selector(text=result_html)

print(sel.xpath('//*[@class=\'nowrap time\']//text()').extract())
