# ip_analysis
根据ipip.net提供的ip地市信息获取IP地市

思路：将你要查询的IP写到文本文件，使用shell循环读取每一行，到IP库中对应地市信息

使用方法:
sh read_ip.sh

单独查询一个IP使用方法：
python ip_jiexi.py '172.17.1.1'
