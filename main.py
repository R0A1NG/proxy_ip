#!/usr/bin/python3
# coding=utf-8
from app import ihuan, kuaidaili, kxdaili, ip89, taiyangdaili, yundaili, nimadaili, zdaye
import itertools
import time
import threading

alippert = []
bar = threading.Barrier(7)


def kx():
    global alippert
    alippert.extend(kxdaili.kxdaili_main())
    bar.wait()


def kuai():
    global alippert
    alippert.extend(kuaidaili.kuaidaili_main())
    bar.wait()


def yun():
    global alippert
    alippert.extend(yundaili.yundaili_main())
    bar.wait()


def wai():
    global alippert
    alippert.extend(taiyangdaili.taiyangdaili_main())
    bar.wait()


def ip8():
    global alippert
    alippert.extend(ip89.ip89_main())
    bar.wait()


def ih():
    global alippert
    alippert.extend(ihuan.ihuan_main())
    bar.wait()


def nima():
    global alippert
    alippert.extend(nimadaili.nimadaili_main())
    bar.wait()
    main()


def zdy():
    global alippert
    alippert.extend(zdaye.zdaye_main())
    bar.wait()


def main():
    # 合并去重
    global alippert
    print('正在进行合并去重！')
    alippert.sort()
    l = []
    it = itertools.groupby(alippert)
    for k, g in it:
        l.append(k)
    f = open('res/ip.txt', 'w')
    for i in l:
        f.write(str(i[0]) + ':' + str(i[1]) + '\n')
    f.close()
    time.sleep(1)
    print('合并去重完成！ 共 【' + str(len(l)) + '】 条代理，已保存到ip.txt')


if __name__ == "__main__":
    print('IP爬取开始！')
    threading.Thread(target=kx).start()
    threading.Thread(target=kuai).start()
    threading.Thread(target=yun).start()
    threading.Thread(target=wai).start()
    threading.Thread(target=ip8).start()
    threading.Thread(target=ih).start()
    threading.Thread(target=zdy).start()
    threading.Thread(target=nima).start()
