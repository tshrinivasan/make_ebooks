#!/bin/bash
sed '/~/!b;:l;n;/~~/b;n;/~~/b;s/^/==/;bl;' content.md > content-epub.md
sed '/~/!b;:l;n;/~~/b;n;/~~/b;s/^/==/;bl;' content.md > content-pdf.md
awk ' {gsub("~~","")}; Print $0' content-pdf.md > content-pdf1.md
awk ' {gsub("~","\\noindent")}; Print $0' content-pdf1.md > content-pdf2.md
sed '/^-b/ s/$/**/' content-pdf2.md > content-pdf3.md
sed 's/-b/**/g' content-pdf3.md > content-pdf4.md
sed '/^-c/ s/$/\\end{center}/' content-pdf4.md > content-pdf5.md
sed '/^-c/ s//\\begin{center}/' content-pdf5.md > content-pdf6.md
sed '/^-r/ s//\\null\\hfill /' content-pdf6.md > content-pdf7.md
sed 's/$/  /' content-pdf7.md > content_pdf.md
awk '/^==/ {$0=$0" </span>"} 1' content-epub.md > content-epub1.md
sed 's/==/<span class="mw-poem-indented" style="display: inline-block; margin-left: 3em;">/g' content-epub1.md > content-epub2.md
awk ' {gsub("~~","</div>")}; Print $0' content-epub2.md > content-epub3.md
sed 's/~/<div class="poem">/g' content-epub3.md > content-epub4.md
sed '/^-b/ s/$/**/' content-epub4.md > content-epub5.md
sed 's/-b/**/g' content-epub5.md > content-epub6.md
sed '/^-c/ s/$/<\/center>/' content-epub6.md > content-epub7.md
sed '/^-c/ s//<center>/' content-epub7.md > content-epub8.md
sed '/^-r/ s/$/<\/div>/' content-epub8.md > content-epub9.md
sed '/^-r/ s//<div style="text-align: right">/' content-epub9.md > content-epub10.md
sed 's/$/  /' content-epub10.md > content_epub.md
rm content-pdf*.md content-epub*.md
