from textblob import TextBlob
f = open("words.txt", "r")
num_words = int(input("Number of Words -> "))



operations = []

for _ in range(num_words - 1):
	operations.append(str(input("enter operation no {} -> ".format(_+1))))



num_of_operations = num_words - 1


words = []

for _ in range(num_words):
	words.append(str(input("word no {} - ".format(_+1))))

print("Please Wait . . . ")

# The function for getting words length is still under work
# for now using arbit length 
res_length = 9 

candi = []

for i in f: 
	if len(i) == res_length :
		curr = TextBlob(i)
		if curr.tags[0][1][0] == "V" :
			candi.append(i.replace("\n", "")) 


# below logic works for single operations

	# if operations[i] == "+" :
	# 	if len(f[i]) == res_len + 1 or res_len:
	# 		curr = TextBlob(i)
	# 		if curr.tags[0][1][0] == "V" :
	# 			candi.append(i.replace("\n", ""))

	# elif operations[i] == "-" :
	# 	if len(i) == res_len - 1 or res_len:
	# 		curr = TextBlob(i)
	# 		if curr.tags[0][1][0] == "V" :
	# 			candi.append(i.replace("\n", ""))

	# elif operations[i] == "*" :
	# 	if len(i) in [j for j in range(res_len,2*res_len + 1)]:
	# 		curr = TextBlob(i)
	# 		if curr.tags[0][1][0] == "V" :
	# 			candi.append(i.replace("\n", ""))




template = ""

for _ in range(len(words)):
	template += " "
	template += words[_]
	template += " "
	if _ < len(words) - 1 :
		template += operations[_]
template.strip()

count = 1

r = open("Puzzles_multiple_operations.txt","w+")


for i in candi :
	# print(template + " " + "=" +" "+str(i))
	r.write(" {}) ".format(count)+str(template)+" = "+str(i)+"\n")
	r.write("\n")
	count += 1

r.close()

print("")
print("Completed ! ")
print("total {} results".format(len(candi)))
print("")



	
