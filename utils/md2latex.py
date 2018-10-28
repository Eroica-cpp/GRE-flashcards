# coding=utf-8
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

def insert(cards_per_page):
	"""
	insert into tex source code
	"""
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
		order_list = words_group + [words_group[1], words_group[0], words_group[3], words_group[2], words_group[5], words_group[4]]

		for j in range(0, 2*cards_per_page):
			word = order_list[j]
			attach = "_1.tex}" if j <= 5 else "_2.tex}"
			input_str = "\\input{" + save_path2 + word + attach
			cmd = "echo '%s' >> %s" % (input_str, tex_name)
			# debug module
			# cmd = "cat %s >> %s" % (save_path1+word+attach[:-1], tex_name)
			os.system(cmd)
	return

def main():
	## predefinition
	print("本工具可以自定义行列数，根据给定的行列生成A4大小 R x M 的单词卡片")
	row = input("输入行数：")
	col = input("输入列数：")
	source_path = "../data/"
	save_path = "../src/content/words/"
	tex_path = "../src/content/"
	cards_per_page = 6

	words = load(source_path)
	convert(words, save_path)
	insert(row,col)
	return 

if __name__ == "__main__":
	main()