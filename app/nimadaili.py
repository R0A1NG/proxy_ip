import requests
import re
import time
from progress.bar import Bar


def nimadaili_main():
    headers = {
        'User-Agent': 'User-Agent,Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'
    }
    all_ip_port = []
    print('正在爬取 【泥马代理】')
    bar = Bar('【泥马代理】', max=700, fill='#', suffix='%(percent)d%%')       # 进度条
    for i in range(1, 701):
        try:
            bar.next()
            # 免费
            res = requests.get("http://www.nimadaili.com/putong/{}/".format(str(i)), headers=headers,
                               timeout=5).text.replace('\n', '').replace(' ', '').replace('\t', '')
            time.sleep(1)
            ip_all = re.findall('<tbody>(.*?)</tbody>', res)[0]
            ip_ip = re.findall('<tr><td>(.*?)</td>', ip_all)     # 提取所有IP
            for j in ip_ip:
                j = j.split(':')
                all_ip_port.append(j)         # 合并IP和端口存到列表
            if i <= 350:
                # 高匿
                res = requests.get("http://www.nimadaili.com/gaoni/{}/".format(str(i)), headers=headers,
                                   timeout=5).text.replace('\n', '').replace(' ', '').replace('\t', '')
                time.sleep(1)
                ip_all = re.findall('<tbody>(.*?)</tbody>', res)[0]
                ip_ip = re.findall('<tr><td>(.*?)</td>', ip_all)  # 提取所有IP
                for j in ip_ip:
                    j = j.split(':')
                    all_ip_port.append(j)  # 合并IP和端口存到列表
            # http
            res = requests.get("http://www.nimadaili.com/http/{}/".format(str(i)), headers=headers,
                               timeout=5).text.replace('\n', '').replace(' ', '').replace('\t', '')
            time.sleep(1)
            ip_all = re.findall('<tbody>(.*?)</tbody>', res)[0]
            ip_ip = re.findall('<tr><td>(.*?)</td>', ip_all)  # 提取所有IP
            for j in ip_ip:
                j = j.split(':')
                all_ip_port.append(j)  # 合并IP和端口存到列表
            # https
            res = requests.get("http://www.nimadaili.com/https/{}/".format(str(i)), headers=headers,
                               timeout=5).text.replace('\n', '').replace(' ', '').replace('\t', '')
            time.sleep(1)
            ip_all = re.findall('<tbody>(.*?)</tbody>', res)[0]
            ip_ip = re.findall('<tr><td>(.*?)</td>', ip_all)  # 提取所有IP
            for j in ip_ip:
                j = j.split(':')
                all_ip_port.append(j)  # 合并IP和端口存到列表
        except:
            pass
    bar.finish()
    print('【泥马代理】爬取完成！爬取IP 【' + str(len(all_ip_port)) + '】 个')
    return all_ip_port
