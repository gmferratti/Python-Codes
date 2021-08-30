import scrapy

class ArticleSpider(scrapy.Spider):
    
    #nome do nosso "crawler"
    name = 'article'
    
    #Método que inicia os requests
    def start_requests(self):
        
        #lista de urls que queremos obter informações
        
        start_links = [
            'https://pt.wikipedia.org/wiki/Steve_Jobs',
            'https://pt.wikipedia.org/wiki/Bill_Gates',
            'https://pt.wikipedia.org/wiki/Jeff_Bezos'
        ] 
        
        #Fazemos o request e em seguida já chamamos o método parse por meio do callback
        request = [scrapy.Request(url = link, callback = self.parse) for link in start_links]
        
        return request
    
    #Método que a partir da resposta dos requests (responses), extrai as informações do site
    def parse(self,response):
        
        url = response.url
        title = response.css('h1::text').extract_first()
        
        print()
        print('A URL é: ',url)
        print('O título do artigo é: ', title)
        print()