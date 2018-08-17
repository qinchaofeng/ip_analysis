import os
import sys

from ipip import IP
from ipip import IPX

IPX.load(os.path.abspath("17monipdb.datx"))
reload(sys)
sys.setdefaultencoding( "utf-8" )
print sys.argv[1]+" "+IPX.find(sys.argv[1])
