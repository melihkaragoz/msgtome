import socket,os
from multiprocessing import Process
s=socket.socket()
os.system("clear")
host = "127.0.0.1"
port = 4164
nick = str(input("your nick > "))
rnick = " "
nickCount=0

def showMsg(min):
	global rnick,nickCount
	while True:
		res = s.recv(1024)
		res = res.decode('utf-8')
		if("-nick" in res):
			_rnck = res.split(" ")
			try:
				rnick = _rnck[1]
				if(nickCount>0):
					#print(f"\n  -!!- karsi taraf nick degistirdi, yeni nick : {rnick}  -!!-")
					continue
				nickCount+=1
			except:
				pass
		else:
			print(f"\n{rnick} >> {res}")

p = Process(target=showMsg,args=('5'))
try:
	s.connect((host,port))
	res = s.recv(1024)
	s.send(f"-nick {nick}".encode('utf-8'))
except:
	print("sunucu aktif degil")
p.start()

while True:
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
		s.send(gonderMsg.encode('utf-8'))

s.close()
