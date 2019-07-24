from lxml import etree
text = '''
<div>
  <ul>
    <li class="item-1">
      <a href="link1.html">first item</a>
    </li>
    <li class="item-1">
      <a href="link2.html">second item</a>
    </li>
    <li class="item-inactive">
      <a href="link3.html">third item</a>
    </li>
    <li class="item-1">
      <a href="link4.html">fourth item</a>
    </li>
    <li class="item-0">
      a href="link5.html">fifth item</a>
  </ul>
</div>
'''

html = etree.HTML(text)

#获取href的列表和title的列表
# href_list = html.xpath("//li[@class='item-1']/a/@href")
# title_list = html.xpath("//li[@class='item-1']/a/text()")
# print(title_list)


# for href in href_list:
#     item = {}
#     item['href'] = href
#     # 根据href的索引遭到title_list相对的索引
#     item['title'] = title_list[href_list.index(href)]
#     print(item)
# for href,title in zip(href_list,title_list):
#     print(href,title)


el_list = html.xpath('//a')
for el in el_list:
    # print(el.xpath('//text()'))  错误的
    print(el.xpath('./text()'))
    print(el.xpath('.//text()'))
    print(el.xpath('text()'))