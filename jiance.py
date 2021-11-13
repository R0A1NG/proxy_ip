#!/usr/bin/python3
import telnetlib
from tomorrow import threads
from progress.bar import Bar


@threads(100)
def jiance(bar, i):
    global aaa
    global bbb
    try:
        telnetlib.Telnet(i[0], i[1], timeout=5)
        qq = open('res/success.txt', 'a+')
        qq.write(i[0] + ':' + str(i[1]) + '\n')
        qq.close()
        bar.next()
    except:
        bar.next()


if __name__ == '__main__':
    f = open('res/ip.txt', 'r').readlines()
    bar = Bar('【IP检测】', max=len(f), fill='#', suffix='%(percent)d%%')  # 进度条
    q = open('res/success.txt', 'w')
    q.write('')
    q.close()
    for i in f:
        i = i.replace('\n', '')
        i = i.split(':')
        jiance(bar, i)
    bar.finish()
