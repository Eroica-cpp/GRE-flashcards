
template_font = r"""
\begin{frame}
\begin{center}
\begin{turn}{180}
{\fontsize{1.7cm}{1em}\selectfont %s}
\end{turn}
\vspace{1em}\par  
\hrule
\vspace{1em}\par  
{\fontsize{1.7cm}{1em}\selectfont %s}
\end{center}
\end{frame}
"""

template_back = r"""
\begin{frame}
{\huge %s}
\begin{center}
\begin{enumerate}\Large
%s
\end{enumerate}
\end{center}
\end{frame}
"""

def form_explanations(dic):
	"""
	form explanations of the word in LaTeX formats
	"""
	num_exp = len(dic.keys())
	inserts = []
	for i in range(1, num_exp+1):
		exp = dic[i]
		if len(exp) <= 1:
			inserts.append(r"  \item \textbf{%s}" % exp[0])
		else:
			inserts.append(r"  \item \textbf{%s}" % exp[0])
			inserts.append(r"  \begin{itemize}")
			inserts += [ r"    \item \em{\Large{%s}}" % j for j in exp[1:] ]
			inserts.append(r"  \end{itemize}")

	return "\n".join(inserts)

def convert_one(word, dic, save_path):
	# save font side
	open(save_path+word+"_1.tex", "w").write(template_font % (word,word))
	
	# save back side 
	explanations = form_explanations(dic)
	open(save_path+word+"_2.tex", "w").write(template_back % (word, explanations))
	print template_back % (word, explanations) # debug
	print 
	return

def convert(words, save_path):
	print template_font
	for word in words.keys():
		dic = words[word]
		convert_one(word, dic, save_path)
	return