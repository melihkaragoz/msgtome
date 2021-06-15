import socket,os,sys,base64
from multiprocessing import Process
s=socket.socket()
os.system("clear")
host=str(input("host > "))
port=int(input("port > "))
nick = str(input("your nick > "))
_help = """
			Sunucuya hosgeldiniz...

** nick degistirmek icin -nick yazıp yanına yeni nickinizi belirtin. **
örnek: -nick asus

** gönderilen mesajı şifreleyip göndermek için --enc parametresini kullanın. **
örnek: çok gizli mesaj --enc

** bu menüyü görüntülemek için --help yazın. **

** iletişim: melihkkaragoz@hotmail.com **\n\n
"""
print(_help)
rnick = " "

def showMsg(min):
	global rnick
	while True:
		res = s.recv(1024)
		res = res.decode('utf-8')
		if("--hidden" in res):
			_hide = True
		else:
			_hide = False
		if("--nick" in res):
			_rnck = res.split(" ")
			try:
				rnick = _rnck[1]
				if(not _hide):
					print(f"\n  -!!- karsi taraf nick degistirdi, yeni nick : {rnick}  -!!-")
				else:
					print(f"{rnick} baglandi.")
			except:
				pass
		else:
			if(not _hide):
				print(f"\n{rnick} >> {res}")

p = Process(target=showMsg,args=('5'))
try:
	s.connect((host,port))
	res = s.recv(1024)
	s.send(f"--nick {nick} --hidden".encode('utf-8'))
except:
	print("sunucu aktif degil")
p.start()

while True:
	gonderMsg = str(input(f"{nick} >> "))
	if(gonderMsg == "exitSocket"):
		break
	elif("--nick" in gonderMsg):
		_nck = gonderMsg.split(" ")
		try:
			nick = _nck[1]
			s.send(gonderMsg.encode('utf-8'))
		except:
			print("nick degistirilemedi")
	elif("--help" in gonderMsg):
		print(_help)
	elif("--enc" in gonderMsg):
		gonderMsg = base64.b64encode(bytes(gonderMsg,'utf-8')).decode("utf-8")
		s.send(gonderMsg.encode('utf-8'))
	else:
		s.send(gonderMsg.encode('utf-8'))

s.close()
