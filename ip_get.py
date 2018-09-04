# -*- coding: utf-8 -*-  
import requests
import sys

def ip_parsing(ip):
    payload = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    link = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip
    r = requests.get(link,params = payload)
    country = r.json()['data']['country']
    area = r.json()['data']['area']
    region = r.json()['data']['region']
    city = r.json()['data']['city']
    isp = r.json()['data']['isp']
    #country_id = r.json()['data']['country_id']
    
    return country,area,region,city,isp
country,area,region,city,isp = ip_parsing(sys.argv[1])
print '\t'.join([sys.argv[1],country,area,region,city,isp])
