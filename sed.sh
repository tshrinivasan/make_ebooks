#!/bin/bash
sed '/~/!b;:l;n;/~~/b;n;/~~/b;s/^/==/;bl;' content.md > content-epub.md
sed '/~/!b;:l;n;/~~/b;n;/~~/b;s/^/==/;bl;' content.md > content-pdf.md
# find and add '==' to beginiing of all even lines between '~' and '~~' block
sed 's/~~//' content-pdf.md > content-pdf1.md
# replace '~~' with nothing for pdf
sed 's/+/\\noindent/' content-pdf1.md > content-pdf2.md
# find '+' and replace \noindent for pdf ('+' noindented poems only)
sed '/^-bc/s/$/**\\end{center}/' content-pdf2.md > content-pdf2a.md
sed '/^-bc/s//\\begin{center}**/' content-pdf2a.md > content-pdf2b.md
sed '/^-br/s/$/**/' content-pdf2b.md > content-pdf2c.md
sed '/^-br/s//\\null\\hfill**/' content-pdf2c.md > content-pdf2d.md
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
sed 's/~/\\noindent/' content-pdf8.md > content-pdf9.md
# find '~' and replace '\noindent' pdf ('+' noindented poems only)
sed 's/$/  /' content-pdf9.md > content_pdf.md
# adding double space at end of the line (for force new line)
sed '/^==/s/$/<\/span>/' content-epub.md > content-epub1.md
# find '==' and add '</span>' at end of the line
sed '/^-bc/s/$/**<\/center>/' content-epub1.md > content-epub1a.md
sed '/^-bc/s//<center>**/' content-epub1a.md > content-epub1b.md
sed '/^-br/s/$/**<\/div>/' content-epub1b.md > content-epub1c.md
sed '/^-br/s//<div style="text-align: right">**/' content-epub1c.md > content-epub1d.md
sed 's/-b/++b/' content-epub1d.md > content-epub2.md
# find '-b' and replace '++b' (-b already in epub code block)
sed 's/==/<span class="mw-poem-indented" style="display: inline-block; margin-left: 3em;">/g' content-epub2.md > content-epub3.md
# find '==' and replace '<span class="mw-poem-indented" style="display: inline-block; margin-left: 3em;">'
sed 's/~~/<\/div>/' content-epub3.md > content-epub4.md
# find '~~' and replace '</div>' 
sed 's/~/<div class="poem">/g' content-epub4.md > content-epub5.md
# find '~' and replace '<div class="poem">' 
sed '/^++b/s/$/**/' content-epub5.md > content-epub6.md
# find '++b' and add '**' end of the line for bold
sed 's/++b/**/g' content-epub6.md > content-epub7.md
# find '++b' and replace '**' for bold
sed '/^-c/s/$/<\/center>/' content-epub7.md > content-epub8.md
# find '-c' and add '</center>' end of the line for centering
sed '/^-c/s//<center>/' content-epub8.md > content-epub9.md
# find '-c' and replace '<center>' for centering
sed '/^-r/s/$/<\/div>/' content-epub9.md > content-epub10.md
# find '-r' and add '</div>' end of the line for right alignment
sed '/^-r/s//<div style="text-align: right">/' content-epub10.md > content-epub11.md
# find '-r' and replace '<div style="text-align: right">' for right alignment
sed 's/+//g' content-epub11.md > content-epub12.md
# find '+' and replace with nothing
sed 's/$/  /' content-epub12.md > content_epub.md
# adding double space at end of the line (for force new line)
rm content-pdf*.md content-epub*.md 
## remove all files except content_pdf.md and content_epub.md


