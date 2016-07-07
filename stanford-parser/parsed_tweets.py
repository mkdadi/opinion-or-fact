import wordsegment as ws

filein = open("idioms_14_4_16tags.txt")

data = filein.readlines()

parsedfile = open("idioms.txt", "w")

parsedData = []

for line in data:
	x = line.replace(".", "").replace("\'","").replace("`","").replace("\"","")
	y = " ".join(ws.segment(x))
	parsedData.append(y)

parsedfile.write(" .\n".join(parsedData))
