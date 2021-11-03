#在文件中写入代码，打印 1 到 100 之间（包含 1 和 100），不是 7 的倍数、且不含 7 的数字，每行打印一个数字

a = 0

while a < 100:
	a += 1
	string = str(a)
	result = '7' in string
	#print(string)
	#print(result)
	if a % 7 == 0 or result == 1:
	        continue
	else:
		print(a)

#a % 7 == 0 or a % 10 == 7 or a // 10 == 7
# 除7整除(7的倍数)   除10取余(末位为7)   除10取商(十位为7)
