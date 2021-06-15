import socket,os,base64
from multiprocessing import Process
from time import sleep

os.system("clear")
host="127.0.0.1"
port=4164
nick = str(input("your nick > "))
rnick = ""

def showMsg(min):
	global rnick
	_hide = False
	while True:
		res = c.recv(1024)
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
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print(f"socket {port} nolu porta baglandi")
s.listen(5)

while True:
	c,addr = s.accept()
	print(f"yeni baglanti >> {addr}")
	p.start()
	sleep(0.1)
	c.send(f"--nick {nick}".encode('utf-8'))
	c.send(f"--nick {nick} --hidden".encode('utf-8'))
	while c:
		gonderMsg = ""
		gonderMsg = str(input(f"{nick} >> "))
		if(gonderMsg == "exitSocket"):
			break
		elif("--nick" in gonderMsg):
			_nck = gonderMsg.split(" ")
			nick = _nck[1]
			c.send(gonderMsg.encode('utf-8'))
		elif("--join" in gonderMsg):
			c.send(f"--nick {nick} --hidden".encode('utf-8'))
		elif("--enc" in gonderMsg):
			gonderMsg = base64.b64encode(bytes(gonderMsg,'utf-8')).decode('utf-8')
			c.send(gonderMsg.encode('utf-8'))
		else:
			c.send(gonderMsg.encode('utf-8'))
	c.close()
s.close()
