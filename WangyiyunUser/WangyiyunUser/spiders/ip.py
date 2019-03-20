#!/usr/bin/python
# -*- coding: UTF-8 -*-
# print("Hello, World!");
# python动态抓取代理IP：代理获取的相关代码，目前抓取了快代理、代理66、有代理、西刺代理、guobanjia这个五个网站的免费代理
# author:zjcjava@163.com 2016-11-02
import urllib.parse
import urllib.request
import time
from lxml import etree


# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print("Name: ", name);
    print("Age ", age);
    return;


# 调用printinfo函数
printinfo(age=50, name="miki");

global url_path
url_path = [3]


def get_url(url):  # 国内高匿代理的链接
    url_path[0] = url
    url_list = []
    if "xici" in url:
        for i in range(1, 1000):
            url_new = url + str(i)
            url_list.append(url_new)
    if "66" in url:
        for i in range(1, 2):
            url_new = url + str(i) + ".html"
            url_list.append(url_new)
    print(url_new)
    return url_list


def get_content(url):  # 获取网页内容
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    content = res.read()
    return content  # .decode('utf-8')


def get_info(content, url):  # 提取网页信息 / ip 端口
    print("111111111111111111");
    print("sss:" + url)
    if "xici" in url:
        datas_ip = etree.HTML(content).xpath('//table[contains(@id,"ip_list")]/tr/td[2]/text()')
        datas_port = etree.HTML(content).xpath('//table[contains(@id,"ip_list")]/tr/td[3]/text()')
    if "66" in url:
        print(66);
        datas_ip = etree.HTML(content).xpath(
            '//div[contains(@id,"main")]/div/div[1]/table/tr[position()>1]/td[1]/text()')
        datas_port = etree.HTML(content).xpath(
            '//div[contains(@id,"main")]/div/div[1]/table/tr[position()>1]/td[2]/text()')
        # print('%s : %s'%(datas_ip,datas_port))

    with open("temp.txt", "w") as fd:
        for i in range(0, len(datas_ip)):
            out = u""
            out += u"" + datas_ip[i]
            out += u":" + datas_port[i]
            fd.write(out + u"\n")  # 所有ip和端口号写入data文件


def verif_ip(ip, port):  # 验证ip有效性
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    proxy = {'http': 'http://%s:%s' % (ip, port)}
    print(proxy)

    proxy_handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    test_url = "https://www.baidu.com/"
    req = urllib.request.Request(url=test_url, headers=headers)
    time.sleep(6)
    try:
        res = urllib.request.urlopen(req)
        time.sleep(3)
        content = res.read()
        if content:
            print('that is ok')
            with open("G:/1.txt", "a") as fd:  # 有效ip保存到data2文件夹
                fd.write(ip + u":" + port)
                # fd.write("\n")
        else:
            print('its not ok')
    except urllib.request.URLError as e:
        print(e.reason)


# url_list =get_url(url="http://www.xicidaili.com/nn/");
# for i in url_list:
#         print(i)
# url = 'http://www.xicidaili.com/nn/'
if __name__ == "__main__":
    #global url_path
    url = 'http://www.66ip.cn/'
    url_list = get_url(url)
    for i in url_list:
        print(i)
        content = get_content(i)
        time.sleep(3)
        get_info(content, url);

file = open("G:/temp.txt")
while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for data in lines:
        print(data.split(u":")[0])
        # out=data.split(u":");
        # print('%s : %s'%(data.split(u":")[0],data.split(u":")[0]))
        verif_ip(data.split(u":")[0], data.split(u":")[1])

