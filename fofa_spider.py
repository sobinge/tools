# encoding=utf-8
import requests
import base64
import time
import re
import sys


headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
	"Cookie": "_fofapro_ars_session=5517108c67e8c667f2834573b6fe2a63; path=/; expires=Tue, 26 May 2020 15:58:41 -0000; HttpOnly"
	}
print (headers)
search=input("请根据fofa语法输入搜索的对象:\n")
searchbs64=(str(base64.b64encode(search.encode('utf-8')),'utf-8'))
pageurl=requests.get('https://fofa.so/result?qbase64='+searchbs64,headers=headers)
pagenum=re.findall('>(\d*)</a> <a class="next_page" rel="next"',pageurl.text)
print("经探测一共"+pagenum[0]+"页数据")
doc=open("1.txt","a")
for i in range(1,int(pagenum[0])+1):
	finurl=requests.get('https://fofa.so/result?page='+str(i)+'&qbase64='+searchbs64,headers=headers)
	while finurl.status_code==429:

		finurl=requests.get('https://fofa.so/result?page='+str(i)+'&qbase64='+searchbs64,headers=headers)

	finurl=re.findall('<a target="_blank" href="(.*)">.* <i class="fa fa-link">',finurl.text)
	for j in finurl:
		print(j)
		doc.write(j+'\n')
	print("写入第"+str(i)+"页的url")
doc.close()
print('爬取完成')
