自制 GRE 单词卡片
====
受magoosh的flashcard启发，准备GRE的时候自己做了一套打印版的GRE flashcard(词和例句来自于3000)。个人觉得刷flashcard比直接刷书带感，平时带一叠卡片放口袋里上无聊的课、等车啥的时候都可以看一看比较方便；而且根据心理学，刷flashcard属于active learning，比一般看书passive learning记忆效果好。

制作方法
----
* **步骤一：下载pdf文件** [GRE-flashcards-all.pdf](https://github.com/Eroica-cpp/GRE-flashcards/blob/master/download/GRE-flashcards-all.pdf)，

* **步骤二： 打印这个pdf文件。**
打印的时候设置一张A4纸打六页（正反面打印），横向的顺序打印，即：
```
1 | 2
-----
3 | 4
-----
5 | 6
```
上面是一张A4的一面的结构，1-6表示pdf文件里面的页码。顺序都是程序调过的，按照上面的设置，正反面正好可以对上。

* **步骤三：裁剪。** 打印店一般都有专门裁纸的机器，裁开即可。

1700多个单词全部打印下来大概是500+面A4纸，一般打印店的价位是50RMB左右，如果能背好单词还是很值的！

效果图
----
正面单词，背面中英文解释和例句

![](https://github.com/Eroica-cpp/GRE-flashcards/blob/master/image/card1.png)

从3000里面挑的1700个我不太熟悉的词，分成了12叠

![](https://github.com/Eroica-cpp/GRE-flashcards/blob/master/image/card2.png)

背单词的时候认识的放一边，不认识的放另一边

![](https://github.com/Eroica-cpp/GRE-flashcards/blob/master/image/card3.png)

说明
----
* **utils文件夹** 里面是简单的python脚本，把markdown文件转换成LaTeX代码，同时排好序保证正反面相对应。
```Bash
# 转到utils目录，执行:
python md2latex.py
```

* **src 文件夹** 里面是tex文件。LaTeX方面主要用了beamer库，也就是说一个单词的一面对应一个slide。
```Bash
# tex文件用xelatex编译
xelatex flashcards.tex
```

* **data 文件夹** 里面是原始的markdown文件，是我从[《再要你命3000》](https://www.google.com/search?q=%E5%86%8D%E8%A6%81%E4%BD%A0%E5%91%BD3000+pdf&ie=utf-8&oe=utf-8)电子版里面自己整理出来的，总共1700个左右《再要你命3000》里面我不太熟的单词，整理大概花了25-30个小时。

如何拓展？
----
* *修改或增加单词：* 修改`data`文件夹内相应的`md`文件。
* *修改字号和字体：* 修改`src`文件夹下的`tex`文件。

修改完成后，执行如下两步：
```Bash
# 转到utils目录，执行:
python md2latex.py
# 然后转到到src目录，执行:
xelatex flashcards.tex
```

许可证
---
[The MIT License (MIT)](https://mit-license.org/)
