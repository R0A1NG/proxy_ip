import IPy
from tomorrow import threads
from progress.bar import Bar


@threads(100)
def main(ipport, ipcn, bar):
    for i in ipcn:
        if ipport.split(':')[0] in IPy.IP(i):
            x = open('res/cn.txt', 'a+')
            x.write(ipport + '\n')
            x.close()
            bar.next()
            return 0
    bar.next()
    x = open('res/no_cn.txt', 'a+')
    x.write(ipport + '\n')
    x.close()


if __name__ == '__main__':
    x = open('res/cn.txt', 'w')
    x.write('')
    x.close()
    x = open('res/no_cn.txt', 'w')
    x.write('')
    x.close()
    cnip = open('res/cn_ip.txt', 'r').readlines()
    ipcn = []
    for i in cnip:
        ipcn.append(i.replace('\n', ''))
    f = open('res/success.txt', 'r').readlines()
    sip = []
    for i in f:
        sip.append(i.replace('\n', ''))
    bar = Bar('【IP检测】', max=len(sip), fill='#', suffix='%(percent)d%%')  # 进度条
    for j in sip:
        main(j, ipcn, bar)
    bar.finish()