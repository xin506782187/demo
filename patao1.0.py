# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:56:40 2019

@author: Lenovo
"""
import urllib.request as r
while True:
    w=input('请输入要查询的宝贝(输入0退出)：')
    if w == '0':
        break
    q=r.quote(w)
    url='https://s.taobao.com/search?q={}&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'.format(q)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
	         'cookie':'t=0020d827122cc255a5243c70b445fc1c; cna=u0wsFZj8nnICAXj0P14pWj9I; tg=0; enc=X6t6AYH9g6Msc4Cd3nUlMzr3i7WE6VoMGV1AnQ3dGoLjjw4xS3F2NVHLU%2BpKXap1ZaVmk%2FegCH6bVwkeFlWWjg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; uc3=vt3=F8dByEnV3N7ZqkzFyIY%3D&id2=UU23CgHyG7PpOA%3D%3D&nk2=UUxLt8Ei5t8R&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; tracknick=24k%5Cu4E36%5Cu946B%5Cu7237; lgc=24k%5Cu4E36%5Cu946B%5Cu7237; _cc_=URm48syIZQ%3D%3D; mt=ci=27_1; swfstore=172837; JSESSIONID=EF8A93884FEA9D48028492AE957B70A2; l=bBaNqzC7v-wKBs19BOCa5uI8Uh79sIRYmuPRwdxvi_5BY6Ls82_OlGQIkFp6Vj5RsrYB4ATie6p9-etui; isg=BC4udCZa_rEh3gpY1tmA2PRzf4Qwh_BaYBGlZlj3mzHsO86VwL3UOWW59-dy5-pB'}
  
    url = r.Request(url,headers=headers)
    tao=r.urlopen(url).read().decode('utf-8')
    
    import json
    tb=json.loads(tao)
    
    from prettytable import PrettyTable
    x=PrettyTable(['网购','就来','淘宝','商城'])
    by=tb['mods']['itemlist']['data']['auctions']
    def baby(a):
        item_loc=by[a]['item_loc']
        nick=by[a]['nick']
        raw_title=by[a]['raw_title']
        view_fee=by[a]['view_fee']
        view_price=by[a]['view_price']
        view_sales=by[a]['view_sales']
        comment_count=by[a]['comment_count']
        icon=len(by[a]['icon'])
        if icon ==1:
            icon=by[a]['icon'][0]['innerText']
        else:
            icon=by[a]['icon'][1]['innerText']
        x.align['网购'] = '1'
        x.vertical_char='*'
        view_price = float(view_price)
        if len(raw_title) >10:
            raw_title = raw_title[0:10] + '...'
        if view_fee == '0.00':
            view_fee = view_fee.replace('0.00','包邮')
        view_sales = view_sales[:-3]
        return str(raw_title)+'\n'+'￥'+str(view_price)+' '\
        +'销量:'+str(view_sales)+'\n'+str(view_fee)+'  '+'评论:'\
        +str(comment_count)+'\n'+str(nick)+'  '+str(item_loc)+'\n'\
        +str(icon)+'\n'+'------------------------------'
    j=0
    for i in range(0,11):
            x.add_row([baby(j),baby(j+1),baby(j+2),baby(j+3)])
            j+=4
    print(x)




