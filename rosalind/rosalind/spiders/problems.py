import scrapy

from ..items import ProblemItem

class ProblemsSpider(scrapy.Spider):
    name = 'problems'
    base_url = 'http://rosalind.info'
    start_urls = ['http://rosalind.info/problems/list-view/']

    def parse(self, response):
        hrefs = response.xpath('//td[2]/a/@href').extract()
        ids = response.xpath('//td[1]/text()').extract()
        for id_, href in zip(ids, hrefs):
            request = scrapy.Request(url = self.base_url + href,
                                     callback = self.parse_problem)
            request.meta['id_'] = id_
            yield request

    def parse_problem(self, response):
        problem = ProblemItem()
        problem['id_'] = response.meta['id_']

        title = response.xpath('//h1/text()').extract_first().strip()
        *statement, given, return_ = [
            ''.join(paragraph.xpath('.//text()').extract())
            for paragraph in response.xpath('//h2[contains(text(), "Problem")]/following-sibling::p')
        ]
        dataset = response.xpath('//h2[@id="sample-dataset"]/following-sibling::div[1]//text()').extract_first().strip()
        output = response.xpath('//h2[@id="sample-output"]/following-sibling::div[1]//text()').extract_first().strip()
        topics = response.xpath('//p[@class="topics"]/a/text()').extract()

        problem['title'] = title
        problem['statement'] = statement
        problem['given'] = given
        problem['return_'] = return_
        problem['dataset'] = dataset
        problem['output'] = output
        problem['topics'] = topics

        yield problem