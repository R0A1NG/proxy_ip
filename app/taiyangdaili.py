import requests
import re
import time
from progress.bar import Bar


def taiyangdaili_main():
    headers = {
        'User-Agent': 'User-Agent,Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'
    }
    all_ip_port = []
    print('正在爬取 【太阳代理】')
    bar = Bar('【太阳代理】', max=30, fill='#', suffix='%(percent)d%%')       # 进度条
    for i in range(1, 31):              # 爬取10页
        try:
            bar.next()
            res = requests.get("http://http.taiyangruanjian.com/free/page{}/".format(str(i)), headers=headers,
                               timeout=5)
            res.encoding = 'utf-8'
            res = res.text.replace('\r\n', '').replace(' ', '').replace('\t', '').replace('\n', '')
            time.sleep(1)
            ip_all = re.findall('<divclass="list"id="ip_list">(.*?)</div><divclass="free_page"', res)[0]
            ip_ip = re.findall('<divclass="trip_tr"><divclass="tdtd-4">(.*?)</div>', ip_all)     # 提取所有IP
            for j in ip_ip:
                ip_port = re.findall(j + '</div><divclass="tdtd-2">(.*?)</div>', ip_all)[0]     # 提取所有端口
                all_ip_port.append([j, ip_port])         # 合并IP和端口存到列表
        except:
            pass
    bar.finish()
    print('【太阳代理】爬取完成！爬取IP 【' + str(len(all_ip_port)) + '】 个')
    return all_ip_port
