str1 = "PANDA"
str2 = "PYTHON"
str1len = len(str1)
str2len = len(str2)
if str2len>str1len :
	print(str1)
	spaces = str2len
	i=0
	while(i<(str2len//2)):
		print(" "*i, str2[i]," "*spaces,str2[(str2len-i)-1], " "*i)
		spaces-=3
		i+=1
