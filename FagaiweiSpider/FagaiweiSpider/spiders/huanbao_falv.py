# -*- coding: utf-8 -*-
import scrapy
from FagaiweiSpider.items import FagaiweispiderItem
import re
import time
from lxml import etree


class HuanbaofalvSpider(scrapy.Spider):
    name = "huanbao_falv"
    #allowed_domains = ["zhb.gov.cn"]

    start_list = [
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/fl/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/fl/index_2.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/fl/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/fg/xzfg/index.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/fg/xzfg/index_3.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/fg/xzfg/index_2.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/fg/xzfg/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/fg/gwyfbdgfxwj/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/fg/gwyfbdgfxwj/index_16.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/gz/bmgz/gjhjbhbmgz/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/gz/bmgz/gjhjbhbmgz/index_6.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/gz/bmgz/gjhjbhbmgz/index_5.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/gz/bmgz/gjhjbhbmgz/index_4.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/gz/bmgz/gjhjbhbmgz/index_3.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/gz/bmgz/gjhjbhbmgz/index_2.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/gz/bmgz/gjhjbhbmgz/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/gz/bmgz/gwybmyggz/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/gz/bmgz/gwybmyggz/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/gz/bmfbdgfxwj/bfbdgfxwj/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/gz/bmfbdgfxwj/bfbdgfxwj/index_17.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/gz/bmfbdgfxwj/gwyfbdgfxwj/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/gz/bmfbdgfxwj/gwyfbdgfxwj/index_13.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/hjxyzd/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/hbzhmljyy/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/hbzhmljyy/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/hjczzc/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/hjczzc/index_6.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/hjczzc/index_5.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/hjczzc/index_4.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/hjczzc/index_3.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/hjczzc/index_2.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/hjczzc/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/lssfzc/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/lssfzc/index_4.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/lssfzc/index_3.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/lssfzc/index_2.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/lssfzc/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/lsxdzc/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/lsxdzc/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/hjwrzrbxzc/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/lszqzc/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/lsjgzc/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/lsjgzc/index_3.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/lsjgzc/index_2.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/lsjgzc/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/lscgzc/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/stbczc/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/stbczc/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/pwqjyzc/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzcx/qtjjzc/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/hbzhmljyy1/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/hjxyzd1/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/hjczzc1/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/hjczzc1/index_4.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/hjczzc1/index_3.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/hjczzc1/index_2.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/hjczzc1/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/lssfzc/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/lssfzc/index_2.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/lssfzc/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/lsxdzc1/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/hjwrzrbxzc1/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/hjwrzrbxzc1/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/lszqzc1/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/lsjgzc1/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/lsjgzc1/index_2.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/lsjgzc1/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/hjmyzc1/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/lscgzc1/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/stbczc1/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/stbczc1/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/pwqjyzc/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/pwqjyzc/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/qtjjzc/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/qtjjzc/index_3.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/qtjjzc/index_2.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/hjjzc/gjfbdjjzc/qtjjzc/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/zcfgjd/",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/zcfgjd/index_5.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/zcfgjd/index_4.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/zcfgjd/index_3.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/zcfgjd/index_2.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/zcfg/zcfgjd/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/hjtj/hjtjnb/",
        "http://www.zhb.gov.cn/gzfw_13107/hjtj/hjtjnb/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/hjtj/qghjtjgb/",
        "http://www.zhb.gov.cn/gzfw_13107/hjtj/qghjtjgb/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/ghjh/wngh/",
        "http://www.zhb.gov.cn/gzfw_13107/ghjh/zxgh/",
        "http://www.zhb.gov.cn/gzfw_13107/ghjh/zxgh/index_2.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/ghjh/zxgh/index_1.shtml",
        "http://www.zhb.gov.cn/gzfw_13107/ghjh/xdjh/",
        "http://www.zhb.gov.cn/home/rdq/gjhz/gjgy/",
        "http://www.zhb.gov.cn/home/rdq/gjhz/lydt/",
        "http://www.zhb.gov.cn/home/rdq/gjhz/lydt/index_6.shtml",
        "http://www.zhb.gov.cn/home/rdq/gjhz/lydt/index_5.shtml",
        "http://www.zhb.gov.cn/home/rdq/gjhz/lydt/index_4.shtml",
        "http://www.zhb.gov.cn/home/rdq/gjhz/lydt/index_3.shtml",
        "http://www.zhb.gov.cn/home/rdq/gjhz/lydt/index_2.shtml",
        "http://www.zhb.gov.cn/home/rdq/gjhz/lydt/index_1.shtml",
        # 科技
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/shjbh/",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/shjbh/index_20.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/dqhjbh/",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/dqhjbh/index_16.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/wlhj/",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/wlhj/index_1.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/trhj/",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/trhj/index_3.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/trhj/index_2.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/gthw/",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/gthw/index_6.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/gthw/index_5.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/gthw/index_4.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/gthw/index_3.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/gthw/index_2.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/gthw/index_1.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/hxxhj/",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/hxxhj/index_4.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/hxxhj/index_3.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/hxxhj/index_2.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/hxxhj/index_1.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/stzl/",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/stzl/index_2.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/stzl/index_1.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/hp/",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/hp/index_3.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/hp/index_2.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/hp/index_1.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/other/",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/other/index_28.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/wrfzjszc/",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/wrfzjszc/index_2.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/wrfzjszc/index_1.shtml",
        "http://kjs.mep.gov.cn/hjbhbz/bzwb/kxxjszn/",
        # 环境评估
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/ghhjyxpj/xgwj/",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/ghhjyxpj/xgwj/index_1.shtml",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/ghhjyxpj/flfg/",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/ghhjyxpj/jsdz/",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpj/xmslqk/",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpj/xmslqk/index_31.shtml",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpj/nscxmgs/",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpj/nscxmgs/index_24.shtml",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpj/ypzxmgg/",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpj/ypzxmgg/index_33.shtml",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmjghjbh/ysxmslgs/",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmjghjbh/ysxmslgs/index_20.shtml",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmjghjbh/npzysxmgs/",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmjghjbh/npzysxmgs/index_5.shtml",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmjghjbh/npzysxmgs/index_4.shtml",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmjghjbh/npzysxmgs/index_3.shtml",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmjghjbh/npzysxmgs/index_2.shtml",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmjghjbh/npzysxmgs/index_1.shtml",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmjghjbh/ysxmgg/",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmjghjbh/ysxmgg/index_8.shtml",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpjzz/slgs/",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpjzz/slgs/index_10.shtml",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpjzz/scgs/",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpjzz/scgs/index_6.shtml",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpjzz/spgg/",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpjzz/spgg/index_7.shtml",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpjzz/hpjg/",
        "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpjzz/hpjg/index_1.shtml",
    ]
    i = 1
    while i < 16:
        url = "http://www.zhb.gov.cn/gzfw_13107/zcfg/fg/gwyfbdgfxwj/index_%s.shtml" %str(i)
        start_list.append(url)
        i += 1
    i = 1
    while i < 17:
        url = "http://www.zhb.gov.cn/gzfw_13107/zcfg/gz/bmfbdgfxwj/bfbdgfxwj/index_%s.shtml" %str(i)
        start_list.append(url)
        i += 1
    i = 1
    while i < 13:
        url = "http://www.zhb.gov.cn/gzfw_13107/zcfg/gz/bmfbdgfxwj/gwyfbdgfxwj/index_%s.shtml" %str(i)
        start_list.append(url)
        i += 1
    i = 1
    while i < 20:
        url = "http://kjs.mep.gov.cn/hjbhbz/bzwb/shjbh/index_%s.shtml" %str(i)
        start_list.append(url)
        i += 1
    i = 1
    while i < 16:
        url = "http://kjs.mep.gov.cn/hjbhbz/bzwb/dqhjbh/index_%s.shtml" %str(i)
        start_list.append(url)
        i += 1
    i = 1
    while i < 28:
        url = "http://kjs.mep.gov.cn/hjbhbz/bzwb/other/index_%s.shtml" %str(i)
        start_list.append(url)
        i += 1
    i = 1
    while i < 31:
        url = "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpj/xmslqk/index_%s.shtml" %str(i)
        start_list.append(url)
        i += 1
    i = 1
    while i < 24:
        url = "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpj/nscxmgs/index_%s.shtml" %str(i)
        start_list.append(url)
        i += 1
    i = 1
    while i < 33:
        url = "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpj/ypzxmgg/index_%s.shtml" %str(i)
        start_list.append(url)
        i += 1
    i = 1
    while i < 20:
        url = "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmjghjbh/ysxmslgs/index_%s.shtml" %str(i)
        start_list.append(url)
        i += 1
    i = 1
    while i < 8:
        url = "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmjghjbh/ysxmgg/index_%s.shtml" %str(i)
        start_list.append(url)
        i += 1
    i = 1
    while i < 10:
        url = "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpjzz/slgs/index_%s.shtml" %str(i)
        start_list.append(url)
        i += 1
    i = 1
    while i < 6:
        url = "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpjzz/scgs/index_%s.shtml" %str(i)
        start_list.append(url)
        i += 1
    i = 1
    while i < 7:
        url = "http://www.zhb.gov.cn/home/rdq/hjyxpj/jsxmhjyxpjzz/spgg/index_%s.shtml" %str(i)
        start_list.append(url)
        i += 1

    start_urls = start_list
    # start_urls = ["http://www.zhb.gov.cn/gzfw_13107/zcfg/fl/",
    #               "http://www.zhb.gov.cn/gzfw_13107/zcfg/fl/index_2.shtml",
    #               "http://www.zhb.gov.cn/gzfw_13107/zcfg/fl/index_1.shtml",
    #               ]

    def parse(self, response):
        title_list = response.xpath("//div[@class='main_rt_list']/ul/li/a|//div[@class='bgleft']/a").extract()
        uptime_list = response.xpath("//div[@class='main_rt_list']/ul/li/span/text()|//div[@class='bgleft']/span/text()").extract()
        sun_url_list = response.xpath("//div[@class='main_rt_list']/ul/li/a/@href|//div[@class='bgleft']/a/@href").extract()

        if sun_url_list != []:
            for i in range(len(sun_url_list)):
                item = FagaiweispiderItem()
                item["title"] = etree.HTML(title_list[i]).xpath("//a/text()")[0]
                item["uptime"] = uptime_list[i]
                item["myproject"] = "环保部"
                item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                sun_url = sun_url_list[i]

                if sun_url.startswith("./"):
                    new_sun_url = re.match(r".+/", response.url).group() + sun_url[2:]
                    item["source"] = new_sun_url

                    if sun_url.endswith("htm") or sun_url.endswith("shtml"):
                        item["f_file"] = ""
                        yield scrapy.Request(url=item["source"], callback=self.next_parse, meta={"item": item})
                    else:
                        item["num"] = 1
                        item["attachment0"] = new_sun_url
                        item['source'] = new_sun_url
                        file_path = sun_url.split("/")[-1]
                        item["f_file"] = "index/images/" + "zhb" + "/" + file_path
                        item["pdf_name0"] = file_path
                        item["content"] = ""
                        item["content_text"] = ""
                        yield item

                elif sun_url.startswith("../../"):
                    new_sun_url = "http://www.zhb.gov.cn/" + sun_url.lstrip("../")
                    item["source"] = new_sun_url
                    item["f_file"] = ""
                    yield scrapy.Request(url=item["source"], callback=self.next_parse, meta={"item": item})

                elif sun_url.startswith("http"):
                    item["source"] = sun_url
                    if sun_url.endswith("htm") or sun_url.endswith("shtml"):
                        item["f_file"] = ""
                        yield scrapy.Request(url=item["source"], callback=self.next_parse, meta={"item": item})
                    else:
                        item["num"] = 1
                        item["attachment0"] = new_sun_url
                        item['source'] = new_sun_url
                        file_path = sun_url.split("/")[-1]
                        item["f_file"] = "index/images/" + "zhb" + "/" + file_path
                        item["pdf_name0"] = file_path
                        item["content"] = ""
                        item["content_text"] = ""
                        yield item
    def next_parse(self, response):
        item = response.meta["item"]
        content = response.xpath("""//div[@class='TRS_Editor']|//div[@class='wzxq_neirong2']|\
        //div[@class='main']""").extract()[0]

        url_list = response.xpath("""//p[@align='center']/a/@href|\
        //div[@class='Custom_UnionStyle']/p/a/@href|//div[@class='content']/p/a/@href|\
        //p[@align='center']/span/a/@href|//p/a[@oldsrc]/@href""").extract()

        content_text = re.sub(r'<div[^>]*class="lujing">[\s\S]+?</div>', "", content)
        content_text = re.sub(r"<script[^>]*?>.*?</script>","",content_text)
        content_text = re.sub(r'<style[^>]*?>[\s\S]*?</style>',"",content_text).strip()
        content_text = re.sub(r"<[^>]*>","",content_text).strip()
        item["content_text"] = re.sub(r"&", "", content_text)
        item["myproject"] = "环保部"
        item["crawl_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        if url_list != []:
            new_pdf_url_content = content
            for i in range(len(url_list)):
                attachment_url = url_list[i]
                item["num"] = len(url_list)
                if attachment_url.startswith("./"):

                    pdf_source_url = re.match(r".+/", response.url).group() + attachment_url[2:]
                    pdf_name = "pdf_name%s" % str(i)
                    # 保存附件文件名
                    file_path = attachment_url.split("/")[-1]
                    item[pdf_name] = file_path
                    attachment_name = "attachment%s" % str(i)
                    item[attachment_name] = pdf_source_url

                    # 更换附件地址为本地的相对地址
                    load_pdf_url = "index/images/" + "zhb" + "/" + file_path

                    new_pdf_url_content = re.sub(attachment_url, load_pdf_url, new_pdf_url_content)
                    new_pdf_url_content = re.sub(
                        r'<span[^>]*?class="wzxq2_lianjie">.*?</span>',"",new_pdf_url_content
                    )
                    new_pdf_url_content = re.sub(
                        r'<table[^>]*?class="dth14l22">[\s\S]*?</table>','',new_pdf_url_content
                    )
                    new_pdf_url_content = re.sub(
                        r'<div[^>]*class="lujing">[\s\S]+?</div>', "", new_pdf_url_content
                    )
                    item["content"] = new_pdf_url_content

                else:
                    pdf_name = "pdf_name%s" % str(i)
                    # 保存附件文件名
                    item[pdf_name] = attachment_url.split("/")[-1]
                    attachment_name = "attachment%s" % str(i)
                    item[attachment_name] = attachment_url

        else:
            content = re.sub(r'<span[^>]*?class="wzxq2_lianjie">.*?</span>',"",content)
            content = re.sub(r'<table[^>]*?class="dth14l22">[\s\S]*?</table>','',content)
            content = re.sub(r'<div[^>]*class="lujing">[\s\S]+?</div>', "", content)
            item["content"] = content

        yield item

