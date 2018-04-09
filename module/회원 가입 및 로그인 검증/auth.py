class sign(object):
	def signin(self, memid, mempw):
		f = open("memberlist.txt", 'r')
		while True:	
			line = f.readline()
			if not line:
				break
			line = line[:-1]
			line = line.split(' ')
			print(line)
			if (line[0] == memid) and (line[1] == mempw):
				f.close()
				return True
			else:
				f.close()
				return False
		return False

	def signup(self, memid, mempw):
		f = open("memberlist.txt", 'a')
		info = memid+' '+mempw+'\n'
		f.write(info)
		f.close()

	def valid_sn(self, sn):
		f = open("sn.txt", 'r')
		serial = f.readline()
		serial = serial[:-1]
		print(serial)
		f.close()
		if serial == sn:
			return True
		else:
			return False

	def split_string(self, info):	
		info = info.split(':::')
		return info

s = sign()
string = "ABC:::1234:::1234567890"
info = s.split_string(string)
ID = info[0]
PW = info[1]
SN = info[2]
print(info)
s.signup(ID, PW)
if s.valid_sn('1234567890'):
	s.signup(ID, PW)
	print("yout info is registerd!")
else:
	print("serial num is wrong!")
	

if s.signin(ID, PW):
	print("login succeed")
else:
	print("login failed")

