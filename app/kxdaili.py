import requests
import re
import time
from progress.bar import Bar


def kxdaili_main():
    headers = {
        'User-Agent': 'User-Agent,Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'
    }
    all_ip_port = []
    print('正在爬取 【开心代理】')
    bar = Bar('【开心代理】', max=10, fill='#', suffix='%(percent)d%%')       # 进度条
    for i in range(1, 11):              # 爬取10页
        try:
            bar.next()
            res = requests.get("http://www.kxdaili.com/dailiip/1/{}.html".format(str(i)), headers=headers, timeout=5)
            res.encoding = 'utf-8'
            res = res.text.replace('\r\n', '').replace(' ', '').replace('\t', '')
            time.sleep(1)
            ip_all = re.findall('<tbody>(.*?)</tbody>', res)[0].replace('class="warning"', '')         # 每页15个IP
            ip_ip_port = re.findall('<tr><td>(.*?)</td><td>高匿</td><td>', ip_all)     # 提取所有IP
            for j in ip_ip_port:
                j = j.split('</td><td>')
                all_ip_port.append(j)       # IP和端口存到列表
            res = requests.get("http://www.kxdaili.com/dailiip/2/{}.html".format(str(i)), headers=headers, timeout=5)
            res.encoding = 'utf-8'
            res = res.text.replace('\r\n', '').replace(' ', '').replace('\t', '')
            time.sleep(1)
            ip_all = re.findall('<tbody>(.*?)</tbody>', res)[0].replace('class="warning"', '')
            ip_ip_port = re.findall('<tr><td>(.*?)</td><td>普匿</td><td>', ip_all)  # 提取所有IP
            for j in ip_ip_port:
                j = j.split('</td><td>')
                all_ip_port.append(j)  # IP和端口存到列表
        except:
            pass
    bar.finish()
    print('【开心代理】爬取完成！爬取IP 【' + str(len(all_ip_port)) + '】 个')
    return all_ip_port
