#!/bin/bash
sed '/~/!b;:l;n;/~~/b;n;/~~/b;s/^/==/;bl;' content.md > content-epub.md
sed '/~/!b;:l;n;/~~/b;n;/~~/b;s/^/==/;bl;' content.md > content-pdf.md
# find and add '==' to beginiing of all even lines between '~' and '~~' block
sed '/~/!b;:l;n;/~~/b;/~~/b;s/^/1111/;bl;' content-pdf.md > content-pdfa.md
sed '/~/!b;:l;n;/~~/b;/~~/b;s/$/\\par/;bl;' content-pdfa.md > content-pdfb.md
sed '/+/!b;:l;n;/++/b;/++/b;s/^/2222/;bl;' content-pdfb.md > content-pdf1.md
sed 's/~~/\\end{spacing}\\end{myparindent}/' content-pdf1.md > content-pdf1a.md
sed '/+/!b;:l;n;/++/b;/++/b;s/$/\\par/;bl;' content-pdf1a.md > content-pdf1b.md
sed 's/++/\\end{spacing}\\end{myparindent}/' content-pdf1b.md > content-pdf2.md
# replace '~~' with nothing for pdf
sed 's/@@/\\noindent/' content-pdf2.md > content-pdf2x.md
# find '+' and replace \noindent for pdf ('+' noindented poems only)
sed '/^-bc/s/$/}\\end{center}/' content-pdf2x.md > content-pdf2a.md
sed '/^-bc/s//\\begin{center}\\bfseries{/' content-pdf2a.md > content-pdf2b.md
sed '/^-br/s/$/}/' content-pdf2b.md > content-pdf2c.md
sed '/^-br/s//\\null\\hfill\\textbf{/' content-pdf2c.md > content-pdf2d.md
sed '/^-b/s/$/**/' content-pdf2d.md > content-pdf3.md
# find '-b' and add '**' at end of the line for bold 
sed 's/-b/**/g' content-pdf3.md > content-pdf4.md
# find '-b' and replace '**' for bold 
sed '/^-c/s/$/\\end{center}/' content-pdf4.md > content-pdf5.md
# find '-c' and add '\end{center}' at end of the line for centering 
sed '/^-c/s//\\begin{center}/' content-pdf5.md > content-pdf6.md
# find '-c' and replace '\begin{center}' centering 
sed '/^-r/s//\\null\\hfill /' content-pdf6.md > content-pdf7.md
# find '-r' and replace '\null\hfill' for align right 
sed 's/==/\\hspace*{1cm}/' content-pdf7.md > content-pdf8.md
# find '==' and replace '\hspace*{1cm}' for peom's even line indent
sed 's/~/\\begin{myparindent}{3cm}\\begin{spacing}{1.0}/' content-pdf8.md > content-pdf8a.md
sed 's/+/\\begin{myparindent}{3cm}\\begin{spacing}{1.0}/' content-pdf8a.md > content-pdf9.md
sed 's/\\hspace\*{1cm}\\par/\\vspace*{1.5cm}/' content-pdf9.md > content-pdf10.md
sed 's/1111\\par//' content-pdf10.md > content-pdf11.md
sed 's/2222\\par/\\vspace*{0.75cm}/' content-pdf11.md > content-pdf12.md
# find '~' and replace '\noindent' pdf ('+' noindented poems only)
sed 's/1111//' content-pdf12.md > content-pdf13.md
sed 's/2222//' content-pdf13.md > content-pdf14.md
sed 's/$/  /' content-pdf14.md > content_pdf.md
# adding double space at end of the line (for force new line)
sed '/^-bc/s/$/**<\/center>/' content-epub.md > content-epub1.md
sed '/^-bc/s//<center>**/' content-epub1.md > content-epub2.md
sed '/^-br/s/$/**<\/div>/' content-epub2.md > content-epub3.md
sed '/^-br/s//<div style="text-align: right">**/' content-epub3.md > content-epub4.md
sed '/~/!b;:l;n;/~~/b;/~~/b;s/$/<\/span>/;bl;' content-epub4.md > content-epuba.md
sed '/~/!b;:l;n;/~~/b;/~~/b;s/^/%%/;bl;' content-epuba.md > content-epubaa.md
# sed '/+/!b;:l;n;/++/b;/++/b;s/$/<\/span>/;bl;' content-epubaa.md > content-epubx.md
sed 's/-b/xb/g' content-epubaa.md > content-epuby.md
# sed '/+/!b;:l;n;/++/b;/~~/b;s/^/<span class="mw-poem-indented" style="display: inline-block; margin-left: 3em;">/;bl;' content-epuby.md > content-epubab.md
# find '-b' and replace '++b' (-b already in epub code block)
sed 's/%%==/<span class="mw-poem-indented" style="display: inline-block; margin-left: 5em;">/g' content-epuby.md > content-epubb.md
# find '==' and add '</span>' at end of the line
sed 's/%%/<span class="mw-poem-indented" style="display: inline-block; margin-left: 3em;">/g' content-epubb.md > content-epub3.md
# find '==' and replace '<span class="mw-poem-indented" style="display: inline-block; margin-left: 3em;">'
sed 's/~~/<\/div>/g' content-epub3.md > content-epub4.md
sed 's/++/<\/div>/g' content-epub4.md > content-epub4a.md
# find '~~' and replace '</div>' 
sed 's/~/<div class="poem">/g' content-epub4a.md > content-epub5.md
sed 's/+/<div style="margin-left: 3em;">/g' content-epub5.md > content-epub5a.md
# find '~' and replace '<div class="poem">' 
sed '/^xb/s/$/**/' content-epub5a.md > content-epub6.md
# find '++b' and add '**' end of the line for bold
sed 's/xb/**/g' content-epub6.md > content-epub7.md
# find '++b' and replace '**' for bold
sed '/^-c/s/$/<\/center>/' content-epub7.md > content-epub8.md
# find '-c' and add '</center>' end of the line for centering
sed '/^-c/s//<center>/' content-epub8.md > content-epub9.md
# find '-c' and replace '<center>' for centering
sed '/^-r/s/$/<\/div>/' content-epub9.md > content-epub10.md
# find '-r' and add '</div>' end of the line for right alignment
sed '/^-r/s//<div style="text-align: right">/' content-epub10.md > content-epub11.md
# find '-r' and replace '<div style="text-align: right">' for right alignment
sed 's/@@//g' content-epub11.md > content-epub12.md
sed 's/+//g' content-epub12.md > content-epub13.md
sed 's/++//g' content-epub13.md > content-epub14.md
sed 's/<span class="mw-poem-indented" style="display: inline-block; margin-left: 3em;"><\/span>//g' content-epub14.md > content-epub15.md
sed 's/<span class="mw-poem-indented" style="display: inline-block; margin-left: 5em;"><\/span>//g' content-epub15.md > content-epub16.md
# find '+' and replace with nothing
sed 's/$/  /' content-epub16.md > content_epub.md
# adding double space at end of the line (for force new line)
rm content-pdf*.md content-epub*.md 
## remove all files except content_pdf.md and content_epub.md
