import requests
import re
import time
from progress.bar import Bar


def kuaidaili_main():
    headers = {
        'User-Agent': 'User-Agent,Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'
    }
    all_ip_port = []
    print('正在爬取 【快代理】')
    bar = Bar('【快代理】', max=10, fill='#', suffix='%(percent)d%%')       # 进度条
    for i in range(1, 11):              # 爬取10页
        try:
            bar.next()
            res = requests.get("https://www.kuaidaili.com/free/inha/{}/".format(str(i)), headers=headers,
                               timeout=5).text.replace('\n', '').replace(' ', '')
            time.sleep(1)
            ip_all = re.findall('<tbody>(.*?)</tbody>', res)[0]         # 每页15个IP
            ip_ip = re.findall('<tddata-title="IP">(.*?)</td>', ip_all)     # 提取所有IP
            ip_port = re.findall('<tddata-title="PORT">(.*?)</td>', ip_all)     # 提取所有端口
            for j, k in zip(ip_ip, ip_port):
                all_ip_port.append([j, k])          # 合并IP和端口存到列表
            res = requests.get("https://www.kuaidaili.com/free/intr/{}/".format(str(i)), headers=headers,
                               timeout=5).text.replace('\n', '').replace(' ', '')
            time.sleep(1)
            ip_all = re.findall('<tbody>(.*?)</tbody>', res)[0]  # 每页15个IP
            ip_ip = re.findall('<tddata-title="IP">(.*?)</td>', ip_all)  # 提取所有IP
            ip_port = re.findall('<tddata-title="PORT">(.*?)</td>', ip_all)  # 提取所有端口
            for j, k in zip(ip_ip, ip_port):
                all_ip_port.append([j, k])  # 合并IP和端口存到列表
        except:
            pass
    bar.finish()
    print('【快代理】爬取完成！爬取IP 【' + str(len(all_ip_port)) + '】 个')
    return all_ip_port
