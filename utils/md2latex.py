"""
************************************************************
Author: Tao Li
Email:  eroicacmcs@gmail.com
Date:   Sept. 25, 2014
Usage:  This script converts markdown files to LaTeX format
************************************************************
"""
import os
from load import *
from convert import *

def insert(row,col):
	"""
	insert into tex source code
	"""
	cards_per_page=row*col
	tex_name = "../src/content/cards.tex"
	save_path1 = "../src/content/words/" # for main script
	save_path2 = "./content/words/" # for cards.tex

	files = os.listdir(save_path1)
	words = list(set( [i.split("_")[0] for i in files if i.split("_")[0][0] != "."] )) # to avoid file like: .fuse****
	os.system("echo > %s" % tex_name) # refresh
	page_num = len(words) / cards_per_page

	for i in range(0, page_num): # skip left words at the end
		words_group = words[i*cards_per_page : (i+1)*cards_per_page]
		# this allocation algorithm is valid only if cards_per_page is six
		new_words_group=[]
		for row_index in range(row):
			new_row=[]
			for col_index in range(col):
				new_row.insert(0,words_group[row_index*col+col_index])
			new_words_group.extend(new_row)
		order_list = words_group + new_words_group
		for j in range(0, 2*cards_per_page):
			if j>=len(order_list):
				break
			word = order_list[j]
			attach = "_1.tex}" if j <= cards_per_page-1 else "_2.tex}"
			input_str = "\\input{" + save_path2 + word + attach
			cmd = "echo '%s' >> %s" % (input_str, tex_name)
			# debug module
			# cmd = "cat %s >> %s" % (save_path1+word+attach[:-1], tex_name)
			os.system(cmd)
	return

def main():
	## predefinition
	source_path = "../data/"
	save_path = "../src/content/words/"
	tex_path = "../src/content/"

	words = load(source_path)
	convert(words, save_path)
	insert(3,3)
	return 

if __name__ == "__main__":
	main()
