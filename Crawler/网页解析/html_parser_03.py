# coding:utf-8
import lxml.html
import lxml.cssselect
import csv

class scrap_callback:

    def __init__(self):
        # 创建csv文件，并写入表头字段
        self.file = csv.writer('conutries.csv','a+','utf-8')
        self.fields = ('area','population','iso','country',
          'capital','continent','tld','currency_code',
          'currency_name','phone','postal_code_format',
          'postal_code_regex','languages','neighbours')
        self.file.writerow(self.fields)

    def __call__(self, html):
        row = []
        for field in self.fields:
            tree = lxml.html.fromstring(html)
            lxml.html.tostring(tree, pretty_print=True)
            td = tree.cssselect('tr#places_%s__row > td.w2p_fw' % field)[0]
            row.append(td.text_content())
        self.file.writerow(row)



if __name__ == '__main__':
    pass