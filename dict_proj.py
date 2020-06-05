from textblob import TextBlob


f = open("words.txt", "r")

num_words = int(input("Number of Words -> "))

operation = str(input("select operation from (+) or (-) or (*) -> "))

words = []

for i in range(num_words):
	words.append(str(input("Word no.{} - ".format(i + 1))).lower())


if operation == "+":
	res_len = max(len(i) for i in words)
elif operation == "-":
	res_len = min(len(i) for i in words)
elif operation == "*" :
	res_len = sum(len(i) for i in words) // len(words)	

print("Please Wait . . .")

candi = []
	
for i in f: 
	if operation == "+" :
		if len(i) ==(res_len + 1) or len(i) == res_len:
			curr = TextBlob(i)
			if curr.tags[0][1][0] == "V" :
				candi.append(i.replace("\n", ""))

	elif operation == "-" :
		if len(i) == (res_len - 1) or len(i) == res_len:
			curr = TextBlob(i)
			if curr.tags[0][1][0] == "V" :
				candi.append(i.replace("\n", ""))

	elif operation == "*" :
		if len(i) in [j for j in range(res_len,2*res_len + 1)]:
			curr = TextBlob(i)
			if curr.tags[0][1][0] == "V" :
				candi.append(i.replace("\n", ""))
					



# template
template = ""

if operation == "+":
	for i in (words) :
		template += i
		template += " + "
	template = template[:len(template) - 2]	

	
elif operation == "-":
	for i in (words) :
		template += i
		template += " - "
	template = template[:len(template) - 2]	

elif operation == "*" :
	for i in (words) :
		template += i
		template += " * "
	template = template[:len(template) - 2]	


#for saving results in .txt file

r = open("Puzzles.txt","w+")


count = 1

for i in candi :
	print("")
	print("Puzzle Number {} ".format(count))
	print(template, " = ", i)
	r.write(" {}) ".format(count)+str(template)+" = "+str(i)+"\n")
	r.write("\n")
	count += 1

r.close()




print("")
print("Completed ! ")
print("total {} results".format(len(candi)))
print("")



