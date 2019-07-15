# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:44:53 2019

@author: Lenovo
"""

import urllib.request as r
import json

i=0
while True:
    if i == 1:
        break
    url='https://s.taobao.com/search?q=%E8%A1%A3%E6%9C%8D&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44&ajax=true'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
	         'cookie':'t=0020d827122cc255a5243c70b445fc1c; cookie2=17864243a541556dbf6688b9e235b9d2; _tb_token_=e4a8eb5eaab73; cna=u0wsFZj8nnICAXj0P14pWj9I; tg=0; enc=X6t6AYH9g6Msc4Cd3nUlMzr3i7WE6VoMGV1AnQ3dGoLjjw4xS3F2NVHLU%2BpKXap1ZaVmk%2FegCH6bVwkeFlWWjg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; swfstore=166219; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; v=0; unb=2559142561; sg=%E7%88%B719; _l_g_=Ug%3D%3D; skt=7361f4d821fea258; cookie1=BxvDRvxZ8zJfDYZv8QJ9pcVT1rmG9u6eua6imAK2p3Y%3D; csg=afe1d082; uc3=vt3=F8dByEnV3N7ZqkzFyIY%3D&id2=UU23CgHyG7PpOA%3D%3D&nk2=UUxLt8Ei5t8R&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; existShop=MTU1NDM0MzkxNw%3D%3D; tracknick=24k%5Cu4E36%5Cu946B%5Cu7237; lgc=24k%5Cu4E36%5Cu946B%5Cu7237; _cc_=URm48syIZQ%3D%3D; dnk=24k%5Cu4E36%5Cu946B%5Cu7237; _nk_=24k%5Cu4E36%5Cu946B%5Cu7237; cookie17=UU23CgHyG7PpOA%3D%3D; JSESSIONID=5F6FA26DDF71EF8CC95ED03218C33F0E; alitrackid=login.taobao.com; lastalitrackid=login.taobao.com; uc1=cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie21=UtASsssmeW6lpyd%2BB%2B3t&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=UoTZ4Mzxku7b5Q%3D%3D&tag=8&lng=zh_CN; mt=ci=27_1; l=bBaNqzC7v-wKB74tBOCaCuI8Uh7OSIRYSuPRwdxvi_5aR6Y1RL_OlgO4WFv6Vj5RsEYB4ATie6p9-etki; isg=BNfX-ImZR4sS1cMHR4qprxVQZkvhtKkN4RIsmSkE86YNWPeaMew7zpV6vrhjtYP2; whl=-1%260%260%261554343930821'}

    uu = r.Request(url,headers = headers)
    data = r.urlopen(uu).read().decode('utf-8')
    da = json.loads(data)['mods']['itemlist']['data']['auctions']
    
    w = open('save100.csv','w',encoding='utf-8')
    w.writelines('商家名称,商品价格,购买人数,评论人数,邮费,商铺名称,发货地址\n')
    for i in range(0,47):
        if da[i]['view_fee'] == '0.00':
           da[i]['view_fee'] = '包邮'
        if da[i]['item_loc'] == '北京':
            w.writelines(str(da[i]['title'][0:10])+'...'+','+str(da[i]['view_price'])+','+\
            str(da[i]['view_sales'][0:-3])+','+str(da[i]['comment_count'])+\
            ','+str(da[i]['view_fee'])+','+str(da[i]['nick'])+','+str(da[i]['item_loc'])+'\n')
    w.close()
    i+=1



