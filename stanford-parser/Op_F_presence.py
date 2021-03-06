OPfilein = open("opi_words.txt")

Ffilein = open("fact_list.txt")

opinion_synonyms_raw_data =OPfilein.readlines()

fact_synonyms_raw_data = Ffilein.readlines()

opinion_synonyms = []

for line in opinion_synonyms_raw_data:
	opinion_synonyms += line.replace("\n","").lower().split()[2:]

fact_synonyms = []

for line in fact_synonyms_raw_data:
	fact_synonyms += line.replace("\n","").lower().split()[1:]

Ffilein.close()

OPfilein.close()


def check_presence_of_synonyms(string=""):
	temp = set(string.replace("\n","").lower().split())

	global opinion_synonyms
	op = 0
	if len(set(opinion_synonyms).intersection(temp)) > 0:
		op = 1
	global fact_synonyms
	fact = 0
	if len(set(fact_synonyms).intersection(temp)) > 0:
		fact = 1

	ret = []
	ret.append(op)
	ret.append(fact)
	return ret

#print check_presence_of_synonyms("bleakness test")

filein = open("idioms.txt")
fileout = open("synonyms_presence.txt","w")

data = filein.readlines()

for line in data:
	ret = check_presence_of_synonyms(line.replace("\n",""))
	fileout.write(str(ret[0])+","+str(ret[1])+","+"\n")
