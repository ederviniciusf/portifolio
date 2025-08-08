import scrapy

class MercadolivreBot(scrapy.Spider):
    name = "MercadoLivre_Bot"
    start_urls = ["https://lista.mercadolivre.com.br/instrumentos-musicais/instrumentos-corda/guitarras/_Container_lp-instrumentos-musicais?forceContainer=true#c_container_id=MLB1258945-1&c_id=%2Fsplinter%2Fspecial&c_element_order=1&c_campaign=guitarras&c_label=%2Fsplinter%2Fspecial&c_uid=4f50bd60-7481-11f0-9a74-ddafb0a1c0ba&c_element_id=4f50bd60-7481-11f0-9a74-ddafb0a1c0ba&c_global_position=5&deal_print_id=4f530750-7481-11f0-82df-ebee94a1c56f&c_tracking_id=4f530750-7481-11f0-82df-ebee94a1c56f"]

    custom_settings = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'DOWNLOAD_DELAY': 3  # Atraso de 3 segundos entre as solicitações
    }
                    

    def parse(self, response):
        SELECTOR = ".ui-search-layout__item"
        itens = []

        for objeto in response.css(SELECTOR):
            item = {}
            NOME_SELECTOR = ".poly-component__title-wrapper ::text"
            item['nome'] = objeto.css(NOME_SELECTOR).extract_first()

            print(item)
            itens.append(item)
        
        print("Total de itens: ", len(itens))