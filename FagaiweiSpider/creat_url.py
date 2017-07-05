#coding=utf-8

'''
发改委网站url情况较多，专门用一个脚本文件生成，存放到fagaiwei_url.txt文件中，
提取到scrapy里做start_urls.
'''

#这个是发改委网站start_urls
f = open("fagaiwei_url.txt","a")

i = 1
#首页>发展改革工作>发展规划>综合情况  24页
f.write("http://www.ndrc.gov.cn/fzgggz/fzgh/zhdt/\n")
while i<24:
    url = "http://www.ndrc.gov.cn/fzgggz/fzgh/zhdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>发展规划>规划文本>国家总体规划 2
f.write("http://www.ndrc.gov.cn/fzgggz/fzgh/ghwb/gjjh/\n")
f.write("http://www.ndrc.gov.cn/fzgggz/fzgh/ghwb/gjjh/index_1.html\n")

#首页>发展改革工作>发展规划>规划文本>主体功能区规划 2
f.write("http://www.ndrc.gov.cn/fzgggz/fzgh/ghwb/ztgngh/\n")
f.write("http://www.ndrc.gov.cn/fzgggz/fzgh/ghwb/ztgngh/index_1.html\n")

#首页>发展改革工作>发展规划>规划文本>国家级专项规划 15
f.write("http://www.ndrc.gov.cn/fzgggz/fzgh/ghwb/gjjgh/\n")
i = 1
while i<15:
    url = "http://www.ndrc.gov.cn/fzgggz/fzgh/ghwb/gjjgh/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>发展规划>规划文本>地方总体规划 3
f.write("http://www.ndrc.gov.cn/fzgggz/fzgh/ghwb/dfztgh/\n")
f.write("http://www.ndrc.gov.cn/fzgggz/fzgh/ghwb/dfztgh/index_1.html\n")
f.write("http://www.ndrc.gov.cn/fzgggz/fzgh/ghwb/dfztgh/index_2.html\n")

#首页>发展改革工作>发展规划>政策法规 3
f.write("http://www.ndrc.gov.cn/fzgggz/fzgh/zcfg/\n")
f.write("http://www.ndrc.gov.cn/fzgggz/fzgh/zcfg/index_1.html\n")
f.write("http://www.ndrc.gov.cn/fzgggz/fzgh/zcfg/index_2.html\n")

#首页>发展改革工作>宏观经济 25
f.write("http://www.ndrc.gov.cn/fzgggz/hgjj/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/hgjj/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>经济运行>综合情况 25
f.write("http://www.ndrc.gov.cn/fzgggz/jjyx/zhdt/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/jjyx/zhdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>经济运行>宏观经济运行 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/jjyx/gjyx/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/jjyx/gjyx/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>经济运行>煤电油气运 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/jjyx/mtzhgl/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/jjyx/mtzhgl/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>经济运行>电力需求侧管理 10
""
f.write("http://www.ndrc.gov.cn/fzgggz/jjyx/dzxqcgl/\n")
i= 1
while i<10:
    url = "http://www.ndrc.gov.cn/fzgggz/jjyx/dzxqcgl/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>经济运行>现代物流 15
""
f.write("http://www.ndrc.gov.cn/fzgggz/jjyx/xdwl/\n")
i= 1
while i<15:
    url = "http://www.ndrc.gov.cn/fzgggz/jjyx/xdwl/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>经济运行>应急管理 14
""
f.write("http://www.ndrc.gov.cn/fzgggz/jjyx/yjxt/\n")
i= 1
while i<14:
    url = "http://www.ndrc.gov.cn/fzgggz/jjyx/yjxt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>体制改革>综合情况 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/tzgg/zhdt/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/tzgg/zhdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>体制改革>改革快讯 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/hgjj/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/hgjj/index_%s.html\n" % str(i)
    f.write(url)
    i+=1


#首页>发展改革工作>固定资产投资>投资工作 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/gdzctz/tzgz/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/gdzctz/tzgz/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>固定资产投资>投资法规 8
""
f.write("http://www.ndrc.gov.cn/fzgggz/gdzctz/tzfg/\n")
i= 1
while i<8:
    url = "http://www.ndrc.gov.cn/fzgggz/gdzctz/tzfg/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>外资利用>综合情况 23
""
f.write("http://www.ndrc.gov.cn/fzgggz/wzly/zhdt/\n")
i= 1
while i<23:
    url = "http://www.ndrc.gov.cn/fzgggz/wzly/zhdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>外资利用>境外投资>发展情况 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/wzly/jwtz/jwtzgk/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/wzly/jwtz/jwtzgk/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>外资利用>境外投资>国别资料 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/wzly/jwtz/jwtzzl/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/wzly/jwtz/jwtzzl/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>外资利用>外商投资>外商投资情况 10
""
f.write("http://www.ndrc.gov.cn/fzgggz/wzly/wstz/wstzgk/\n")
i= 1
while i<10:
    url = "http://www.ndrc.gov.cn/fzgggz/wzly/wstz/wstzgk/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>外资利用>外商投资>开发区情况 8
""
f.write("http://www.ndrc.gov.cn/fzgggz/wzly/wstz/wstzqk/\n")
i= 1
while i<8:
    url = "http://www.ndrc.gov.cn/fzgggz/wzly/wstz/wstzqk/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>外资利用>外债管理 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/wzly/wzgl/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/wzly/wzgl/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>外资利用>政策法规 10
""
f.write("http://www.ndrc.gov.cn/fzgggz/wzly/zcfg/\n")
i= 1
while i<10:
    url = "http://www.ndrc.gov.cn/fzgggz/wzly/zcfg/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>地区经济>综合情况 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/dqjj/zhdt/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/dqjj/zhdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>地区经济>区域规划和区域政策 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/dqjj/qygh/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/dqjj/qygh/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>地区经济>扶贫开发 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/dqjj/fpkf/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/dqjj/fpkf/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>地区经济>对口支援 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/dqjj/dkzy/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/dqjj/dkzy/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 工作动态 25
""
f.write("http://xbkfs.ndrc.gov.cn/gzdt/\n")
i= 1
while i<25:
    url = "http://xbkfs.ndrc.gov.cn/gzdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 最近更新 25
""
f.write("http://xbkfs.ndrc.gov.cn/zjgx/\n")
i= 1
while i<25:
    url = "http://xbkfs.ndrc.gov.cn/zjgx/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 最近更新 25
""
f.write("http://dbzxs.ndrc.gov.cn/xglj/\n")
i= 1
while i<25:
    url = "http://dbzxs.ndrc.gov.cn/xglj/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 工作动态 18
""
f.write("http://dbzxs.ndrc.gov.cn/gzdt/\n")
i= 1
while i<18:
    url = "http://dbzxs.ndrc.gov.cn/gzdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 振兴简报 25
""
f.write("http://dbzxs.ndrc.gov.cn/zxjb/\n")
i= 1
while i<25:
    url = "http://dbzxs.ndrc.gov.cn/zxjb/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 重要文件 7
""
f.write("http://dbzxs.ndrc.gov.cn/zywj/\n")
i= 1
while i<7:
    url = "http://dbzxs.ndrc.gov.cn/zywj/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 东北振兴 7
""
f.write("http://dbzxs.ndrc.gov.cn/dbzx/\n")
i= 1
while i<7:
    url = "http://dbzxs.ndrc.gov.cn/dbzx/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 全国老工业基地调整改造 12
""

f.write("http://dbzxs.ndrc.gov.cn/qglgyjd/\n")
i= 1
while i<12:
    url = "http://dbzxs.ndrc.gov.cn/qglgyjd/index_%s.html\n" % str(i)
    f.write(url)
    i+=1
#首页 > 全国资源型城市可持续发展 25
""
f.write("http://dbzxs.ndrc.gov.cn/zycszx/\n")
i= 1
while i<25:
    url = "http://dbzxs.ndrc.gov.cn/zycszx/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 重点领域改革 2
""
f.write("http://dbzxs.ndrc.gov.cn/zdwtyj/\n")
i= 1
while i<2:
    url = "http://dbzxs.ndrc.gov.cn/zdwtyj/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>基础产业>综合情况 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/nyjt/zhdt/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/nyjt/zhdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>基础产业>政策规划 5
""
f.write("http://www.ndrc.gov.cn/fzgggz/nyjt/fzgh/\n")
i= 1
while i<5:
    url = "http://www.ndrc.gov.cn/fzgggz/nyjt/fzgh/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>基础产业>重大工程 18
""
f.write("http://www.ndrc.gov.cn/fzgggz/nyjt/zdxm/\n")
i= 1
while i<18:
    url = "http://www.ndrc.gov.cn/fzgggz/nyjt/zdxm/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>产业发展>工业发展 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/gyfz/gyfz/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/gyfz/gyfz/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 高技术工作 25
""
f.write("http://gjss.ndrc.gov.cn/gjsgz/\n")
i= 1
while i<25:
    url = "http://gjss.ndrc.gov.cn/gjsgz/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 发展动态 25
""
f.write("http://gjss.ndrc.gov.cn/gzdtx/hgjj/\n")
i= 1
while i<25:
    url = "http://gjss.ndrc.gov.cn/gzdtx/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 政策发布 25
""
f.write("http://gjss.ndrc.gov.cn/ghzc/\n")
i= 1
while i<25:
    url = "http://gjss.ndrc.gov.cn/ghzc/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>环境与资源>综合情况 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/hjbh/hjzhdt/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/hjbh/hjzhdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>环境与资源>生态文明建设 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/hjbh/hjjsjyxsh/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/hjbh/hjjsjyxsh/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>环境与资源>节能节水 16
""
f.write("http://www.ndrc.gov.cn/fzgggz/hjbh/jnjs/\n")
i= 1
while i<16:
    url = "http://www.ndrc.gov.cn/fzgggz/hjbh/jnjs/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>环境与资源>环境保护 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/hjbh/huanjing/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/hjbh/huanjing/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#环境保护司 3
""
f.write("http://hzs.ndrc.gov.cn/newfzxhjj/zcfg/\n")
i= 1
while i<3:
    url = "http://hzs.ndrc.gov.cn/newfzxhjj/zcfg/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#4ye
""
f.write("http://hzs.ndrc.gov.cn/newfzxhjj/xfxd/\n")
i= 1
while i<4:
    url = "http://hzs.ndrc.gov.cn/newfzxhjj/xfxd/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#19ye
""
f.write("http://hzs.ndrc.gov.cn/newfzxhjj/dtxx/\n")
i= 1
while i<19:
    url = "http://hzs.ndrc.gov.cn/newfzxhjj/dtxx/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 工作动态 25
""
f.write("http://qhs.ndrc.gov.cn/gzdt/\n")
i= 1
while i<25:
    url = "http://qhs.ndrc.gov.cn/gzdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 国际谈判与合作 12
""
f.write("http://qhs.ndrc.gov.cn/gwdt/\n")
i= 1
while i<12:
    url = "http://qhs.ndrc.gov.cn/gwdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 低碳发展 6
""
f.write("http://qhs.ndrc.gov.cn/dtjj/\n")
i= 1
while i<6:
    url = "http://qhs.ndrc.gov.cn/dtjj/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 政策法规 4
""
f.write("http://qhs.ndrc.gov.cn/zcfg/\n")
i= 1
while i<4:
    url = "http://qhs.ndrc.gov.cn/zcfg/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 适应气候变化 2
""
f.write("http://qhs.ndrc.gov.cn/syqhbh/\n")
i= 1
while i<2:
    url = "http://qhs.ndrc.gov.cn/syqhbh/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 碳市场建设 25
""
f.write("http://qhs.ndrc.gov.cn/qjfzjz/\n")
i= 1
while i<25:
    url = "http://qhs.ndrc.gov.cn/qjfzjz/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 气候变化南南合作
""
f.write("http://qhs.ndrc.gov.cn/qhbhnnhz/\n")


#首页 > 社会发展工作 25
""
f.write("http://shs.ndrc.gov.cn/gzdt/\n")
i= 1
while i<25:
    url = "http://shs.ndrc.gov.cn/gzdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 社会发展动态 25
""
f.write("http://shs.ndrc.gov.cn/shfzdt/\n")
i= 1
while i<25:
    url = "http://shs.ndrc.gov.cn/shfzdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 社会发展规划、政策与研究 23
""
f.write("http://shs.ndrc.gov.cn/zcyj/\n")
i= 1
while i<23:
    url = "http://shs.ndrc.gov.cn/zcyj/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>经济贸易>综合情况 22
""
f.write("http://www.ndrc.gov.cn/fzgggz/jjmy/zhdt/\n")
i= 1
while i<22:
    url = "http://www.ndrc.gov.cn/fzgggz/jjmy/zhdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>经济贸易>粮油政策 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/jjmy/lyzc/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/jjmy/lyzc/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>经济贸易>棉花食糖产业发展  25
""
f.write("http://www.ndrc.gov.cn/fzgggz/jjmy/mhstfz/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/jjmy/mhstfz/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>经济贸易>流通业发展 21
""
f.write("http://www.ndrc.gov.cn/fzgggz/jjmy/ltyfz/\n")
i= 1
while i<21:
    url = "http://www.ndrc.gov.cn/fzgggz/jjmy/ltyfz/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>经济贸易>对外经贸合作 21
""
f.write("http://www.ndrc.gov.cn/fzgggz/jjmy/dwjmhz/\n")
i= 1
while i<21:
    url = "http://www.ndrc.gov.cn/fzgggz/jjmy/dwjmhz/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>价格管理>综合情况 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/jggl/zhdt/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/jggl/zhdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>价格管理>政策法规 25
""
f.write("http://www.ndrc.gov.cn/fzgggz/jggl/zcfg/\n")
i= 1
while i<25:
    url = "http://www.ndrc.gov.cn/fzgggz/jggl/zcfg/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 监测信息 > 国内外市场价格监测情况周报 2
""
f.write("http://jgjc.ndrc.gov.cn/list.aspx?clmId=695&page=0\n")
f.write("http://jgjc.ndrc.gov.cn/list.aspx?clmId=695&page=1\n")


#首页 > 监测信息 > 主要粮油副食品日报 33
""
f.write("http://jgjc.ndrc.gov.cn/list.aspx?clmId=703&page=0\n")
i= 1
while i<33:
    url = "http://jgjc.ndrc.gov.cn/list.aspx?clmId=703&page=%s\n" % str(i)
    f.write(url)
    i+=1

#首页 > 监测信息 > 生猪出厂价与玉米价格周报 7
""
f.write("http://jgjc.ndrc.gov.cn/list.aspx?clmId=704&page=0\n")
i= 1
while i<7:
    url = "http://jgjc.ndrc.gov.cn/list.aspx?clmId=704&page=%s\n" % str(i)
    f.write(url)
    i+=1

#首页 > 监测信息 > 国际市场石油价格每日动态 31
""
f.write("http://jgjc.ndrc.gov.cn/list.aspx?clmId=705&page=0\n")
i= 1
while i<31:
    url = "http://jgjc.ndrc.gov.cn/list.aspx?clmId=705&page=%s\n" % str(i)
    f.write(url)
    i+=1

#首页 > 监测信息 > 监测周期价格动态 12
""
f.write("http://jgjc.ndrc.gov.cn/list.aspx?clmId=706&page=0\n")
i= 1
while i<12:
    url = "http://jgjc.ndrc.gov.cn/list.aspx?clmId=706&page=%s\n" % str(i)
    f.write(url)
    i+=1

#首页 > 监测信息 > 月度监测行情表 15
""
f.write("http://jgjc.ndrc.gov.cn/list.aspx?clmId=707&page=0\n")
i= 1
while i<15:
    url = "http://jgjc.ndrc.gov.cn/list.aspx?clmId=707&page=0%s\n" % str(i)
    f.write(url)
    i+=1

#首页 > 监测信息 > 猪料、鸡料、蛋料比价 7
""
f.write("http://jgjc.ndrc.gov.cn/list.aspx?clmId=708&page=0\n")
i= 1
while i<7:
    url = "http://jgjc.ndrc.gov.cn/list.aspx?clmId=708&page=%s\n" % str(i)
    f.write(url)
    i+=1

#首页 > 监测信息 > 全国钢材批发市场价格周报 7
""
f.write("http://jgjc.ndrc.gov.cn/list.aspx?clmId=739&page=0\n")
i= 1
while i<7:
    url = "http://jgjc.ndrc.gov.cn/list.aspx?clmId=739&page=%s\n" % str(i)
    f.write(url)
    i+=1

#首页 > 监测信息 > 全国成品油批发市场价格周报 6
""
f.write("http://jgjc.ndrc.gov.cn/list.aspx?clmId=740&page=0\n")
i= 1
while i<6:
    url = "http://jgjc.ndrc.gov.cn/list.aspx?clmId=740&page=%s\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>价格监督与反垄断>综合情况 13
""
f.write("http://www.ndrc.gov.cn/fzgggz/jgjdyfld/jjszhdt/\n")
i= 1
while i<13:
    url = "http://www.ndrc.gov.cn/fzgggz/jgjdyfld/jjszhdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>价格监督与反垄断>反垄断 6
""
f.write("http://www.ndrc.gov.cn/fzgggz/jgjdyfld/fjgld/\n")
i= 1
while i<6:
    url = "http://www.ndrc.gov.cn/fzgggz/jgjdyfld/fjgld/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>价格监督与反垄断>市场监管 7
""
f.write("http://www.ndrc.gov.cn/fzgggz/jgjdyfld/scjg/\n")
i= 1
while i<7:
    url = "http://www.ndrc.gov.cn/fzgggz/jgjdyfld/scjg/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>法治建设>工作动态 11
""
f.write("http://www.ndrc.gov.cn/fzgggz/flfg/gzdtn/\n")
i= 1
while i<11:
    url = "http://www.ndrc.gov.cn/fzgggz/flfg/gzdtn/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>法治建设>法规规章 8
""
f.write("http://www.ndrc.gov.cn/fzgggz/flfg/flgz/\n")
i= 1
while i<8:
    url = "http://www.ndrc.gov.cn/fzgggz/flfg/flgz/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>法治建设>地方动态 16
""
f.write("http://www.ndrc.gov.cn/fzgggz/flfg/dfdtn/\n")
i= 1
while i<16:
    url = "http://www.ndrc.gov.cn/fzgggz/flfg/dfdtn/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页>发展改革工作>重大项目稽察 11
""
f.write("http://www.ndrc.gov.cn/fzgggz/zdxmjc/\n")
i= 1
while i<11:
    url = "http://www.ndrc.gov.cn/fzgggz/zdxmjc/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 工作动态 24
""
f.write("http://cbj.ndrc.gov.cn/gzdt/\n")
i= 1
while i<24:
    url = "http://cbj.ndrc.gov.cn/gzdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 图片新闻 11
""
f.write("http://cbj.ndrc.gov.cn/cbjtpxw/\n")
i= 1
while i<11:
    url = "http://cbj.ndrc.gov.cn/cbjtpxw/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 下属单位动态 25
""
f.write("http://cbj.ndrc.gov.cn/xsdwdt/\n")
i= 1
while i<25:
    url = "http://cbj.ndrc.gov.cn/xsdwdt/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

#首页 > 人事任免 5
""
f.write("http://cbj.ndrc.gov.cn/rsrm/\n")
i= 1
while i<5:
    url = "http://cbj.ndrc.gov.cn/rsrm/index_%s.html\n" % str(i)
    f.write(url)
    i+=1

f.close()
print("结束了！")

