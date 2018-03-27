import yaml
import os
import time
import sys


book_info = yaml.load(open('book-info.yaml'))

book_title_in_english = book_info['book_title_in_english']
cover_image = book_info['cover_image']
timestamp = time.strftime('%Y-%m-%d-%H-%M-%S')

ia_identifier = book_title_in_english + "-" + timestamp

content_dir = book_title_in_english + "-upload/"

tar = "tar czf " + book_title_in_english + ".tar.gz " + book_title_in_english + "-tex"
os.system(tar)


ia_upload = "ia upload " + ia_identifier + " -m collection:opensource -m mediatype:texts -m sponsor:FreeTamilEbooks -m language:ta " +  content_dir + book_title_in_english + ".epub " + content_dir + book_title_in_english + ".mobi " + content_dir + book_title_in_english + ".pdf " + content_dir + book_title_in_english + "_6_inch.pdf " +  content_dir + cover_image + " "  + book_title_in_english + ".tar.gz"

print("Uploading to Internet Archive")

os.system(ia_upload)

os.system("rm " + book_title_in_english + ".tar.gz ")

print("Uploaded to https://archive.org/details/" + ia_identifier)


