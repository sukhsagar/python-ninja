# sentence = input("Enter the sentence")
sentence = "Hi. I study Python at Webcooks"


for i in sentence:
	if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
		continue
	print(i, end='')