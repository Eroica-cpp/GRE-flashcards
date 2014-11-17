import os
import re

def load(source_path):
	"""
	load raw files and then convert them into dictionary format
	"""
	files = os.listdir(source_path)
	doc = ""
	for f in files:
		doc += open(source_path+f).read().strip().replace(r"&", r"\&")

	dic = {}
	raw_words = doc.split("#### ")
	for raw_word in raw_words:
		tmp = raw_word.split("\n")
		word = tmp[0].strip()
		tmp_dic = {}
		for i in tmp:
			if len(i) > 0 and i[0].isdigit():
				number = int(i.split(".")[0])
				tmp_dic[number] = [ re.split(r"\d.", i)[1].strip() ]
			if i.find("*") >= 0:
				tmp_dic[number].append(i.split("*")[1].strip())
		if word != "": dic[word] = tmp_dic
	return dic