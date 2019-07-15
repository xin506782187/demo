# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:56:40 2019

@author: Lenovo
"""

import urllib.request as r


q=r.quote(input('请输入要查询的宝贝：'))
url='https://s.taobao.com/search?q={}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190402&ie=utf8&ajax=true'.format(q)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
	         'cookie':'t=0020d827122cc255a5243c70b445fc1c; cookie2=17864243a541556dbf6688b9e235b9d2; _tb_token_=e4a8eb5eaab73; cna=u0wsFZj8nnICAXj0P14pWj9I; tg=0; enc=X6t6AYH9g6Msc4Cd3nUlMzr3i7WE6VoMGV1AnQ3dGoLjjw4xS3F2NVHLU%2BpKXap1ZaVmk%2FegCH6bVwkeFlWWjg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; swfstore=166219; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; v=0; unb=2559142561; sg=%E7%88%B719; _l_g_=Ug%3D%3D; skt=7361f4d821fea258; cookie1=BxvDRvxZ8zJfDYZv8QJ9pcVT1rmG9u6eua6imAK2p3Y%3D; csg=afe1d082; uc3=vt3=F8dByEnV3N7ZqkzFyIY%3D&id2=UU23CgHyG7PpOA%3D%3D&nk2=UUxLt8Ei5t8R&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; existShop=MTU1NDM0MzkxNw%3D%3D; tracknick=24k%5Cu4E36%5Cu946B%5Cu7237; lgc=24k%5Cu4E36%5Cu946B%5Cu7237; _cc_=URm48syIZQ%3D%3D; dnk=24k%5Cu4E36%5Cu946B%5Cu7237; _nk_=24k%5Cu4E36%5Cu946B%5Cu7237; cookie17=UU23CgHyG7PpOA%3D%3D; JSESSIONID=5F6FA26DDF71EF8CC95ED03218C33F0E; alitrackid=login.taobao.com; lastalitrackid=login.taobao.com; uc1=cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie21=UtASsssmeW6lpyd%2BB%2B3t&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=UoTZ4Mzxku7b5Q%3D%3D&tag=8&lng=zh_CN; mt=ci=27_1; l=bBaNqzC7v-wKB74tBOCaCuI8Uh7OSIRYSuPRwdxvi_5aR6Y1RL_OlgO4WFv6Vj5RsEYB4ATie6p9-etki; isg=BNfX-ImZR4sS1cMHR4qprxVQZkvhtKkN4RIsmSkE86YNWPeaMew7zpV6vrhjtYP2; whl=-1%260%260%261554343930821'}
url = r.Request(url,headers=headers)
tao=r.urlopen(url).read().decode('utf-8')

import json
tb=json.loads(tao)

from prettytable import PrettyTable
x=PrettyTable(['商品名称','商品价格','购买人数','评论人数','邮费','商铺名称','商铺图标','商铺地址'])


def baby(a):
    item_loc=tb['mods']['itemlist']['data']['auctions'][a]['item_loc']  #商品名称
    nick=tb['mods']['itemlist']['data']['auctions'][a]['nick']          #商品价格
    raw_title=tb['mods']['itemlist']['data']['auctions'][a]['raw_title']#
    view_fee=tb['mods']['itemlist']['data']['auctions'][a]['view_fee']
    view_price=tb['mods']['itemlist']['data']['auctions'][a]['view_price']
    view_sales=tb['mods']['itemlist']['data']['auctions'][a]['view_sales']
    comment_count=tb['mods']['itemlist']['data']['auctions'][a]['comment_count']
    icon=tb['mods']['itemlist']['data']['auctions'][a]['icon']
    if len(icon) ==1:
        icon=icon[0]['innerText']
    else:
        icon=icon[1]['innerText']
    x.align['商品名称'] = '1'
    x.padding_width = 1
    view_price = float(view_price)
    x.sortby='商品价格'
    if len(raw_title) >15:
        raw_title = raw_title[0:15] + '...'
    if view_fee == '0.00':
        view_fee = view_fee.replace('0.00','包邮')
    view_sales = view_sales[:-3]
    x.add_row([raw_title,view_price,view_sales,comment_count,view_fee,nick,icon,item_loc])
for i in range(0,47):
    baby(i)
print(x)
input('输入回车退出....')




