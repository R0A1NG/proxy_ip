import requests
import re
import time
from progress.bar import Bar


def ihuan_main():
    headers = {
        'User-Agent': 'User-Agent,Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'
    }
    all_ip_port = []
    print('正在爬取 【小幻代理】')
    bar = Bar('【小幻代理】', max=500, fill='#', suffix='%(percent)d%%')       # 进度条
    page = ['b97827cc', '4ce63706', '5crfe930', 'f3k1d581', 'ce1d45977', '881aaf7b5', 'eas7a436', '981o917f5', '2d28bd81a', 'a42g5985d', 'came0299', 'e92k59727', '242r0e7b5', 'bc265a560', '622b6a5d3', 'ae3g7e7aa', 'b01j07395', '68141a2df', '904545743', '0134c4568', '885t249e8', 'ed442164b', '806fe4987', '0558da7f4', '3734334de', '636g6d8ca', '3252d86d1', 'd67sbb99f', '0e1q9e209', '078e9d9eb', '476p30758', '9520ab2cf', 'cd7772718', '669i449ed', '7c7l8a702', '637sa470e', '645pdd5b9', 'e25uc357c', 'c19of28a3', '5fa0ad8bb', 'eabh0997c', '026i27546', '859ddf7d1', '33b0f488f', '602q622b1', '75bge08a1', '562ud6274', '943073281', 'dec88f8ec', 'bdauca7c9', '8dcoec821', 'fa84ca5bd', 'add876865', '6f8e22532', 'b9aae0682', 'fb8o3e5cd', '4b5bc0336', '603k8b2a7', 'a2b2f866b', '26b8f4637', 'bd5n983f4', '63fg528fe', '79bqb16f8', '08i02e9d3', '00g8248be', 'f4iiae93c', '8169ed33f', '4cakf257b', '87f3457a0', '996i1938c', 'd4jv8c9ff', '6ak8529d5', '06i8ce823', '23bibc5c7', 'a3io5a8c9', '49j0cd869', 'cej864824', 'e6lued95f', 'e9jo398df', '02k0f7814', 'b6k8d385b', 'c5cq0b56a', 'ffkof18b6', '7258c32a2', '77nt98997', '9cde835f9', '03j19d790', '6cm0e5833', '438b90367', '9eb8f74ae', 'a52r9e103', 'd1ec56579', '7beh95563', '9fngf8829', 'f5bs0b4d4', '02o02a8fe', '3dr9e69d5', '1erief906', 'bdff2e56e', 'e1p093843', 'f5sd2798e', '99sm7b997', '606e0b2d9', '3fmoc8715', 'cc6ib92cd', '92qga68c9', '98gn5c54d', '27gsd05ee', '38r8e08c2', '4d3e3d146', '8a6u1c281', '0bag803b6', '96ajeb36a', 'db3i0017b', '1fso3884c', '29pc1e7b5', '8910t059cb', 'a73maa145', '89ma67642', '3eu0d3885', 'aau8578a5', '6fj2b35df', '59uo5b84b', 'b1r4f17ed', 'f41355f969', '84nk0c6a8', 'd313nb899e', 'bac0c63c0', 'd610848894', '19ka7c570', '84slab7b0', '5e888d27d', 'a9kp6a50e', '26p40a6bb', 'a1cl2231c', '03120c68f8', 'bc16h8c9e9', 'ecpsa56b1', '5a173d19b6', '90uk43716', '30qeaf6cd', 'f9m669593', 'camb9852a', 'a8r093620', '2a148e6858', '3amq3150f', '78ic484d9', '3c1506784d', 'a3158a18a4', 'bae225396', 'c5njdb571', 'e41ao959da', '7esma46f3', 'fc11m39706', '7916o718d1', '94124d07ed', 'b79qfe283', '6atkf3644', '2112pd07e0', '9fu06a661', 'f5u6326b9', '4ck813462', '40uib86b8', '5a190838eb', '5dpp955a7', '2afib73ab', 'fb5740106', '2avg3b6fe', '771fh4299d', '98156d37ae', 'd6qnb4501', '7a15k1f7d6', 'ce1b88282c', '7a10kb460c', '7bls3e4cf', '651hgf19e3', 'd7rl6b5e0', '79m8ee46c', '87mc944bc', 'a111o24697', '601d8ac845', 'f11dg65874', '2f1819b78c', '45bg7a2c4', '5d1k10795a', '2ft282571', '0c1kj8692a', '76tc59575', '94th7f567', '6319i547ef', '1113q876b8', '9f608315d', 'be146ef6e0', 'f5ua685e2', '5b14i5a64f', '7214od468c', 'd8ok1c4c8', '68154d462d', '57osef42c', '8e1o8fe93c', '34ir4c3ca', 'e4p81147c', '0d1p3c5999', '3a1j0a68a0', '201pl30905', '9fja2b3f8', 'f7cud02d7', 'd3170b4665', 'a4176126a5', 'e3d49e215', '7c1rba19a2', '5a1ec59752', '801199f57b', '2a1eq837fa', 'a91sfa8995', '5e1m09389c', '0ddi3b269', 'b81ta5a9bd', '7e1ft70795', 'e91tsa8985', '9419e41689', 'ac19kea603', '381gp6a72f', '0e1h0f176d', 'c31o8458be', 'c013aa4508', '46l978307', '8elc4635a', '827509118', '3becf42cc', '5e143a3539', '0d1bg7362d', 'ba21h0991c', '9d1qg2380e', '327bad19b', '6d1c84568f', 'e37d12103', 'cc1565d56e', '507fb71a9', '8d23g9b941', '5b1s8f58e3', '5b24237900', '621l56b7ac', 'c216448544', '541dub566a', '0c2562a959', '5f25fb29d1', '7cfg2a2d2', 'e81emb561a', '1cfk93225', '141mtb3709', 'c71f8896b0', 'e41nb667bb', 'c11ni0578b', '6b1vob28c9', '8c200678f9', '42208688a1', '0e82411ee', 'a41ola77a7', '8318k3f507', 'c91gu006e3', '6b29me5921', '5110s1c4dd', '24220e18cf', '342ah89995', '5222g6f862', '342b3c493b', '7411g7e41f', '601ie646de', '3a2bu6995d', '09pdb936d', '32pg99368', 'e824886831', '8524g0d87d', '24h64327a', '3a2501a8d0', 'fc258208e6', '3b1k4c6637', 'aa25o528a4', '371bo075c7', '832f1a09f6', '89hkd02b9', '721l2bb630', '762700b853', '8a1lefb622', '2b1ui277d8', '311crb75d2', 'ca280c4837', 'b5144af405', '6428g898a2', 'b21df105d4', 'a41vsa1742', '43954f195', 'f9ica4229', 'a129of58a4', 'a82a0518ca', '7f1ed2f5c1', '602ag1d8b6', 'b62k35b9b3', '4d1es20530', '782klac9b9', '9e9ed51e4', '27229f27c1', '1b2lge890a', 'a02c8c4858', '571pc95657', '1716c494cc', 'f61g4e4563', '752mt249e1', 'a01q4fe696', 'df1gj4a537', 'b41go3a58b', '3524f1470b', '5btec33da', 'a41h764559', '172osf999f', '989ta61ea', '342fg33835', 'e717s8c4f5', '172q0cf924', '05267ed702', '07a2f31a7', '3d1sid06b1', 'c72h0c4851', '7d18k6d4c9', 'a61iu9a527', '521ta3263c', 'fe27o2675e', '20ki39263', 'bc2ig8084e', '9akmd9255', 'f228k067ce', 'ce2tlf79a2', 'd72jg678b0', '892jo4d88d', 'e4l09d2d3', '422up81988', '251a83a4cc', '911vif963f', '802l0ac839', '012vtfc933', 'ddam5d1c2', '6f30fa79a0', '8d20ga660e', 'e02m86489f', '122bmc97f1', '3f2btc0738', 'e0218c264c', '0521ec16e7', '981mmd45d1', '9532n429da', '38330b793b', '952d7387ba', '2c1c821479', 'd41cc1b495', '70m845278', '622p84c84e', 'a61nuda540', '372eh2d7ce', '44358d9993', '47b9051bf', '522f6a57ce', 'c9242216a6', 'c5248c86d2', '0e1p1145c8', 'e6be921a3', '4f24q396ca', 'fa2gg4f7f6', '092560262c', '582sg068f3', 'd32so488fa', 'a62t0928d3', '122t85a84a', '801qe4956f', '7c2to3a8af', 'ea2i8e078b', '0c2u8cd8e6', 'b71f845489', 'e51r7ef546', '7b27833683', '2d27ef5635', 'd72vg2d839', '9b27q6e65b', '822807b650', '1e308a482c', 'ed3cib39ea', '5c1gc69431', 'd7310ad86d', 'ef2l3557d5', '3c1su42526', '25c7ee174', '493202982a', '3014ree30e', '8a32g9187b', '232md2a78e', '8d330798fc', 'aa3fld994f', 'a52ak23638', '683g7db9dc', 'b72ng2c79f', '051i4eb437', 'a3p44e243', '322bi8a657', '6f350dc88a', '1d2bu4665d', '7b1ioab4d7', 'a035oda80c', '932cgb86fa', 'e51vte15de', '052pmfd79e', 'c82ptc2747', 'a72d8846d5', '432deca6d2', 'c7ps132a1', '4837o7a8a1', '0d1k08c447', 'b3388e68d0', 'a338gf7803', '0f179853fd', '7d2eo49643', '273md5b956', '9b39g8085c', 'ef39of08a8', 'cd3n8f0911', '5a3a8308fa', '59qk84213', '252td9f7f2', 'cb1lgbb416', 'e7187f63da', '8e3bg89840', 'd5qu18258', '793c0c9878', '762h6a7658', '4f23q3e5fd', '913co5787e', '3b3d030888', '2d3d8df883', '732vq7a7ab', '953rfa6925', '4b24o2757c', '8430f7c7bf', '6130mcf745', '1930td7758', 'deds411a6', 'afrq52211', 'e231ib7796', '8f25rc45cf', 'e426057532', '933g811865', '8a3gge9877', '5826f95562', '3e26k7e540', '673h85984f', '533vmea975', 'ba1os7c41e', '773i03f8c8', '553i84388e', 'ab3ig73897', 'd01b1e03cb', '4127s24526', 'd52meae67a', '0deeb11e5', '923jo25812', 'b63k04d83c', 'c5t2752ce', '184322592f', 'cf28v4f577', '8f1qgb949d', '0c3l82b842', '963lg53878', '4e1qs134dc', 'd044oa193c', '193m80f8cc', 'd33mg2e8d3', '5aerd610b', '37esd810a', '071cn743bc', 'cb38idc7ef', 'ce3noca81d', 'b4u07229b', 'be2b57654b', 'f43og0b875', 'ee47r97970', 'cd4842798b', 'd13p8be860', '941di9d35a', 'ae2c329542', '3e3ao5373f', 'b41t4074bb', '3d3b6177ae', 'dffb861f6', 'f1fcc4141', '933r82788a', '563c2557ca', '724b77d926', '6b2t043644', '321ejae3fc', '192tc8c6b7', '3f4cb0b967', '2e3dc2373a']
    for i in page:              # 爬取10页
        try:
            bar.next()
            res = requests.get("https://ip.ihuan.me/?page={}".format(i), headers=headers,
                               timeout=5).text.replace('\n', '').replace(' ', '')
            time.sleep(1)
            ip_all = re.findall('<tbody>(.*?)</tbody>', res)[0]
            ip_ip = re.findall('<ahref="/check.html\?proxy=.*?"target="_blank"><imgsrc=".*?">(.*?)</a>', ip_all)     # 提取所有IP
            for l in ip_ip:
                ip_port = re.findall(l + '</a></td><td>(.*?)</td>', ip_all)[0]     # 提取所有端口
                all_ip_port.append([l, ip_port])        # 合并IP和端口存到列表
        except:
            pass
    bar.finish()
    print('【小幻代理】爬取完成！爬取IP 【' + str(len(all_ip_port)) + '】 个')
    return all_ip_port

