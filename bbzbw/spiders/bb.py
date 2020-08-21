import scrapy
from ..items import BbzbwItem


class BbSpider(scrapy.Spider):
    name = 'bb'
    # allowed_domains = ['bb.com']
    start_urls = ['https://www.bibenet.com/database/toOwnerListPage.htm?messageLike=&type=1&provinceId=440000']
    post_url = 'https://www.bibenet.com/database/toOwnerDetail.json'
    base_page_url = 'https://www.bibenet.com/database/toOwnerListPage.htm?pageNum={}&pageSize=&type=1&provinceId=440000&messageLike=%E7%BD%AE%E4%B8%9A%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8'

    def start_requests(self):
        for i in range(1, 10):
            url = self.base_page_url.format(i)
            yield scrapy.Request(url=url, callback=self.parse)
        # 1238

    def parse(self, response):

        codes = response.xpath('//tbody/tr/@onclick').getall()
        for c in codes:
            code = c.replace('todetail(', '').replace(');', '')

            form_data = {
                'objectId': code
            }
            yield scrapy.FormRequest(url=self.post_url, formdata=form_data, callback=self.parse_infos)

    def parse_infos(self, response):
        false = False
        true = True
        # print(response.text)
        resp = eval(response.text)
        # for k, v in resp.items():
            # print('k: ', k)
            # print('v: ', v)

        info = resp['ownerDatabase']
        com_name = info['enterpriseName']
        contactsList = info['contactsList']
        for cont in contactsList:
            item = BbzbwItem()
            cont_name = cont['contact']
            cont_tel = cont['telePhone']
            item['com_name'] = com_name
            item['cont_name'] = cont_name
            item['cont_tel'] = cont_tel
            yield item