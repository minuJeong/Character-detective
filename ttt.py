import codecs
file_to_open = "strings.xml"

table = []
with codecs.open(file_to_open, "r", encoding="utf8") as ff:
	strings = ff.read()
	for i in range(len(strings)):
		if not strings[i] in table:
			table.append (strings[i])

sss = ""
for char in table:
	sss += char.encode ("utf-8")


print sss