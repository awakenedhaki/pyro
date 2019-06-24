import scrapy


class ProblemItem(scrapy.Item):
    id_ = scrapy.Field()
    title = scrapy.Field()
    statement = scrapy.Field()
    given = scrapy.Field()
    return_ = scrapy.Field()
    dataset = scrapy.Field()
    output = scrapy.Field()
    topics = scrapy.Field()
