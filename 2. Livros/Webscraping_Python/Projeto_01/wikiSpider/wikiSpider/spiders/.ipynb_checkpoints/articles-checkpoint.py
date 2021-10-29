import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    
    #nome do nosso, agora sim, crawler
    name = 'articles'
    
    #Restringindo os links ao domínio do Wikipedia
    allowed_domains = ['wikipedia.org']
    
    #URL de início
    start_urls = ['https://pt.wikipedia.org/wiki/Jeff_Bezos']
    
    #Estabelecendo as regras de crawling e fazendo o controle das requisições. 
    #Obs. a regra é basicamente pegar todas as páginas.
    
    rules = [Rule(LinkExtractor(allow=r'.*'), callback ='parse_items', follow=True)]
    
    #Método que a partir do response do Link Extractor, extrai as informações do site
    def parse_items(self,response):
        
        url = response.url
        title = response.css('h1::text').extract_first()
        
        #O XPath é uma espécie de caminho alternativo do seletor CSS, sem o açúcar sintático
        #Estamos utilizando ele para obter o texto da página
        text = response.xpath('//div[@id="mw-content-text"]//text()').extract()

        #Último update
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()

        print()
        print('A URL é: ',url)
        print('O título do artigo é: ', title)
        print('O início do texto é: ', text[0:20])
        print(lastUpdated)
        print()