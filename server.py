import socket,os
from multiprocessing import Process

os.system("clear")
host="127.0.0.1"
port=4164
nick = str(input("your nick > "))
rnick = ""
nickCount=0

def showMsg(min):
	global rnick,nickCount
	while True:
		res = c.recv(1024)
		res = res.decode('utf-8')
		if("-nick" in res):
			_rnck = res.split(" ")
		try:
			rnick = _rnck[1]
		except:
			pass
		else:
			print(f"\n{rnick} >> {res}")

p = Process(target=showMsg,args=('5'))
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print(f"socket {port} nolu porta baglandi")
s.listen(5)

while True:
	c,addr = s.accept()
	print(f"yeni baglanti >> {addr}")
	msg = "rosnet sunucularina hosgeldiniz"
	c.send(msg.encode('utf-8'))
	p.start()
	c.send(f"-nick {nick}".encode('utf-8'))
	while c:
		gonderMsg = ""
		gonderMsg = str(input(f"{nick} >> "))
		if(gonderMsg == "exitSocket"):
			break
		elif("-nick" in gonderMsg):
			_nck = gonderMsg.split(" ")
			try:
				nick = _nck[1]
				s.send(gonderMsg.encode('utf-8'))
			except:
				print("nick degistirilemedi")
		else:
			c.send(gonderMsg.encode('utf-8'))
	c.close()
s.close()
