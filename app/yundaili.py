import requests
import re
import time
from progress.bar import Bar


def yundaili_main():
    headers = {
        'User-Agent': 'User-Agent,Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'
    }
    all_ip_port = []
    print('正在爬取 【云代理】')
    bar = Bar('【云代理】', max=7, fill='#', suffix='%(percent)d%%')       # 进度条
    for i in range(1, 8):
        try:
            bar.next()
            res = requests.get("http://www.ip3366.net/free/?stype=1&page={}".format(str(i)), headers=headers,
                               timeout=5)
            res.encoding = 'GBK'
            res = res.text.replace('\r\n', '').replace(' ', '')
            time.sleep(1)
            ip_all = re.findall('<tbody>(.*?)</tbody>', res)[0]
            ip_ip = re.findall('<tr><td>(.*?)</td>', ip_all)     # 提取所有IP
            for l in ip_ip:
                ip_port = re.findall(l + '</td><td>(.*?)</td>', ip_all)[0]  # 提取所有端口
                all_ip_port.append([l, ip_port])  # 合并IP和端口存到列表
            res = requests.get("http://www.ip3366.net/free/?stype=2&page={}".format(str(i)), headers=headers,
                               timeout=5)
            res.encoding = 'GBK'
            res = res.text.replace('\r\n', '').replace(' ', '')
            time.sleep(1)
            ip_all = re.findall('<tbody>(.*?)</tbody>', res)[0]
            ip_ip = re.findall('<tr><td>(.*?)</td>', ip_all)  # 提取所有IP
            for l in ip_ip:
                ip_port = re.findall(l + '</td><td>(.*?)</td>', ip_all)[0]  # 提取所有端口
                all_ip_port.append([l, ip_port])  # 合并IP和端口存到列表
        except:
            pass
    bar.finish()
    print('【云代理】爬取完成！爬取IP 【' + str(len(all_ip_port)) + '】 个')
    return all_ip_port