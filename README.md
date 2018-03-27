# make_ebooks

This is a project to make ebooks for FreeTamilEbooks.com using pandoc.
This gives the ebooks in 4 formats. A4 PDF, 6 inch PDF, epub and mobi

# config.yaml

Fill the following details in the file config.yaml

book_title : 
book_title_in_english : 
author : 
author_mail : 
cover_image : 
artist : 
artist_email : 
ebook_maker : 
ebook_maker_email : 
license :  
content : content.md



example :

book_title : தசாவதாரம்
book_title_in_english : dasavatharam
author : அறிஞர் அண்ணா
author_mail : 
cover_image : dasavatharam.jpg
artist : த. சீனிவாசன்
artist_email : tshrinivasan@gmail.com
ebook_maker : த. சீனிவாசன்
ebook_maker_email : tshrinivasan@gmail.com
license : Public Domain - CC0 
content : content.md



always keep the book content as markdown format in the name called content.md

Keep the cover image in the same parent folder.


# Installation

It needs a ubuntu linux computer.


run the below commands

```
sudo apt-get install python3 python3-pip pandoc texlive-base texlive-xetex calibre texlive-lang-indic texlive-latex-recommended 
sudp pip3 install internetarchive
```


Note that this will download nearly 1 GB of data.
Make sure that you have enough bandwidth on your internet connection.




open the "fonts" directory.
Click every font.
Install all the fonts.


# How to Execute?

In the file content.md, make sure each chapters have # as first charector.

The, run 

```
python3 make-ebook.py
```


This will make the ebooks and store in a new folder as "ebookname"-upload




