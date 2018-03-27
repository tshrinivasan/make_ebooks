import yaml
import os

import sys


book_info = yaml.load(open('book-info.yaml'))

book_title = book_info['book_title']
book_title_in_english = book_info['book_title_in_english']
author = book_info['author']

if book_info['author_mail']:
    author_mail = book_info['author_mail']
else:
    author_mail = " "

cover_image = book_info['cover_image']


if book_info['artist']:
    artist = book_info['artist']
else:
    artist = " " 

if book_info['artist_email']:
    artist_email = book_info['artist_email']
else:
    artist_email = " " 


ebook_maker = book_info['ebook_maker']
ebook_maker_email = book_info['ebook_maker_email']
license = book_info['license']

print(book_title)



a4_pan = open('a4_pan.sh','w')
a4_pan_content = '#!/bin/bash \npandoc --latex-engine=xelatex -H forpdf.tex -V classoption=book -V "geometry:vmargin=2.5cm" -V "geometry:hmargin=2.5cm" -V mainfont="Vijaya" -V fontsize="12pt" -V linestretch="1.5" -N -o ' + book_title_in_english +'.pdf a4_cover.md title.md toc.md content.md   \n'
a4_pan.write(a4_pan_content)
a4_pan.close()


a4_cover = open('a4_cover.md','w')
a4_cover_text = r"""\newgeometry{left=0.0cm, right=0.0cm, bottom=0.0cm, top=0.0cm}
\thispagestyle{empty}
\begin{center}
  \makebox[\textwidth]{\includegraphics[width=0.85\paperwidth]{""" + cover_image + r"""}}
\end{center}
\newpage
"""
a4_cover.write(a4_cover_text)
a4_cover.close()


toc = open("toc.md","w")
toc_text = r"""\restoregeometry

\begin{center}

\color{black}\tableofcontents

\end{center}

\newpage
"""
toc.write(toc_text)
toc.close()




title = open("title.md","w")
title_text = r"""\restoregeometry

\begin{center}

        \vspace*{0.2cm}



        \vspace{0.5cm}

       {\LARGE\mytitle{""" + book_title + r"""}}

       \vspace{0.5cm}

       {\LARGE\chapterheading{""" + author + r"""}}
       \vspace{0.5cm}

       {\LARGE\chapterheading{""" + author_mail + r"""}}

        \vspace{1.5cm}


        \LARGE\textbf{மின்னூல் வெளியீடு : FreeTamilEbooks.com}

        \vspace{1.0cm}

        \Large\mani{உரிமை - """ + license + r""" கிரியேட்டிவ் காமன்ஸ். எல்லாரும் படிக்கலாம், பகிரலாம்.}

        \vspace{1.0cm}

        \Large\mani{பதிவிறக்கம் செய்ய - http://FreeTamilEbooks.com/ebooks/""" + book_title_in_english + r"""}

        \vspace{1.0cm}
  
        \Large\mani{மின்னூலாக்கம் - """ + ebook_maker + """ - """ + ebook_maker_email+ r"""}

        \vfill

        \vspace{1.0cm}

        \Large\mani{ This Book was produced using LaTeX + Pandoc}



     \end{center}
    \thispagestyle{empty}
\newpage
\thispagestyle{empty}
\mbox{}

"""

title.write(title_text)
title.close()






print("Making a4 PDF")
os.system("/bin/bash a4_pan.sh")
print("Done")



#sys.exit()

six_inch_pan = open('6_inch_pan.sh','w')
six_inch_pan_content = '#!/bin/bash \npandoc --latex-engine=xelatex -H forpdf.tex -V classoption=book -V "geometry:paperwidth=4in" -V "geometry:paperheight=5in" -V "geometry:tmargin=0.5cm" -V "geometry:bmargin=1.5cm" -V "geometry:lmargin=0.5cm" -V "geometry:rmargin=0.5cm" -V mainfont="Vijaya" -V fontsize="10pt" -V linestretch="1.5" -N -o ' + book_title_in_english + '_6_inch.pdf cover6.md title.md toc.md content.md    \n'
six_inch_pan.write(six_inch_pan_content)
six_inch_pan.close()



six_inch_cover = open('cover6.md','w')
six_inch_cover_text = r"""\newgeometry{left=0.0cm, right=0.0cm, bottom=0.0cm, top=0.0cm}
\thispagestyle{empty}
\begin{center}
  \makebox[\textwidth]{\includegraphics[width=0.80\paperwidth]{""" + cover_image + r"""}}
\end{center}
\newpage
"""
six_inch_cover.write(six_inch_cover_text)
six_inch_cover.close()


print("Making 6 inch PDF")
os.system("/bin/bash 6_inch_pan.sh")
print("Done")



epub_title = open('epub_title.txt','w')
epub_title_text = r"""---
title: """ + book_title + """
author: """ + author + """
publisher : FreeTamilEbooks.com
rights: """ + license + """
language: ta
...
"""
epub_title.write(epub_title_text)
epub_title.close()




epub_front = open("epub_front.md","w")
epub_front_text = r"""


""" + book_title + """

&nbsp;

""" + author + """


&nbsp;

""" +author_mail + """

&nbsp;

மின்னூல் வெளியீடு : FreeTamilEbooks.com

&nbsp;

உரிமை :   """ +license + """
கிரியேட்டிவ் காமன்ஸ். எல்லாரும் படிக்கலாம், பகிரலாம்.

&nbsp;


மின்னூலாக்கம் - """ + ebook_maker + """ - """ + ebook_maker_email + """


&nbsp;

This book was produced using [pandoc](pandoc.org)

&nbsp;

பதிவிறக்கம் செய்ய - http://FreeTamilEbooks.com/ebooks/""" + book_title_in_english + """}

"""

epub_front.write(epub_front_text)
epub_front.close()





epub_pan = open('epub_pan.sh','w')
epub_pan_text = "pandoc -f markdown -t epub --epub-cover-image=" + cover_image +"  -o " + book_title_in_english+ ".epub --smart --toc epub_title.txt epub_front.md content.md "
epub_pan.write(epub_pan_text)
epub_pan.close()



print("Making epub")
os.system("/bin/bash epub_pan.sh")
print("Done")


print("Making mobi")
os.system("ebook-convert " + book_title_in_english+".epub " + book_title_in_english+".mobi")
print("Done")



os.system("rm -rf " + book_title_in_english + "-upload")
os.mkdir(book_title_in_english + "-upload")
os.system("mv *.pdf *.epub *.mobi *.jpg *.png " + book_title_in_english + "-upload")
os.system("Moved files to upload directory")


os.system("rm -rf " + book_title_in_english + "-tex")
os.mkdir(book_title_in_english + "-tex")
os.system("mv *.md *.sh *.txt *.sty *.tex " +  book_title_in_english + "-tex")
os.system("Moved temp files to tex directory")



