# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from wordpress_xmlrpc import WordPressPost
from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts,media
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import taxonomies

from urllib.request import urlopen

import urllib
import shutil

import unittest, time, re
import os
import re
import yaml
import sys
import time


book_url = sys.argv[1]
book_number = sys.argv[2]

home = os.getenv("HOME")

fte_yaml = yaml.load(open(home + '/.config/fte-login.yaml'))

fte_username = fte_yaml['username']
fte_password = fte_yaml['password']


print("Getting Book Info")
book_info = yaml.load(urlopen(book_url.replace('details','download') + '/book-info.yaml'))


book_title = book_info['book_title']
print(book_title)

book_title_in_english = book_info['book_title_in_english'].replace(" ","-")
author = book_info['author']
print(author)
category  = book_info['category']
print(category)
if book_info['author_mail']:
    author_mail = book_info['author_mail']
else:
    author_mail = " "

cover_image = book_info['cover_image']


if book_info['artist']:
    artist = book_info['artist']
else:
    artist = ""

if book_info['artist_email']:
    artist_email = book_info['artist_email']
else:
    artist_email = ""

if book_info['translator']:
    translator = book_info['translator']
else:
    translator = ""

if book_info['translator_email']:
    translator_email = book_info['translator_email']
else:
    translator_email = ""



ebook_maker = book_info['ebook_maker']
ebook_maker_email = book_info['ebook_maker_email']
license = book_info['license']




epub_url = book_url.replace('details','download') + "/" +  book_title_in_english + ".epub"
mobi_url = book_url.replace('details','download') + "/" +  book_title_in_english + ".mobi"
a4_pdf_url  = book_url.replace('details','download') + "/" +  book_title_in_english + ".pdf"
six_inch_pdf_url = book_url.replace('details','download') + "/" +  book_title_in_english + "-6-inch.pdf"
cover_url = book_url.replace('details','download') + "/" +  cover_image



print("Logging in to FreeTamilEbooks.com")
driver = webdriver.Firefox(executable_path=r'./geckodriver')
driver.implicitly_wait(5)
driver.maximize_window()
base_url = "http://freetamilebooks.com"
verificationErrors = []
accept_next_alert = True





driver.get("http://freetamilebooks.com/wp-login.php?redirect_to=http%3A%2F%2Ffreetamilebooks.com%2Fwp-admin%2Fpost-new.php%3Fpost_type%3Ddlm_download&reauth=1&jetpack-sso-show-default-form=1")
driver.implicitly_wait(5)
       # driver.find_element_by_link_text("Log in with username and password").click()
driver.find_element_by_id("user_pass").clear()
driver.find_element_by_id("user_pass").send_keys(fte_password)
driver.find_element_by_id("user_login").clear()
driver.find_element_by_id("user_login").send_keys(fte_username)
driver.find_element_by_id("wp-submit").click()
      #  driver.find_element_by_link_text("Download").click()
driver.implicitly_wait(5)




def add_download(filename,file_url):
    driver.get("http://freetamilebooks.com/wp-admin/post-new.php?post_type=dlm_download")
    driver.find_element_by_id("title").clear()
    driver.find_element_by_id("title").send_keys(filename)
    driver.find_element_by_xpath(".//*[@class='button plus add_file']").click()
#    driver.implicitly_wait(30)
    time.sleep(20)
      #  driver.find_element_by_xpath(".//*[@class='downloadable_file_urls']").click()
    driver.find_element_by_xpath(".//*[@class='downloadable_file_urls']").send_keys(file_url)
#    driver.implicitly_wait(30)
    time.sleep(20)
    publish_button = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.XPATH,  ".//*[@id='publish']"))
    )
    publish_button.click()
#    driver.find_element_by_xpath(".//*[@id='publish']").click()
#    driver.implicitly_wait(30)
    time.sleep(20)
 
 
    dl_text  = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.ID,  "dlm-info-id"))
    )
    dl_id  = dl_text.get_attribute('value')
 
   # dl_id = driver.find_element_by_id('dlm-info-id').get_attribute('value')
#    driver.implicitly_wait(30)
    time.sleep(20)
    dl_url = driver.find_element_by_id('dlm-info-url').get_attribute('value')
    print(dl_id)
    return(dl_id,dl_url)

    
    
print("Adding Downloads")    
epub_data = add_download(book_title + " epub",epub_url )
mobi_data = add_download(book_title + " mobi",mobi_url)
a4_pdf_data = add_download(book_title + " A4 PDF",a4_pdf_url)
six_inch_pdf_data = add_download(book_title + " 6 inch PDF",six_inch_pdf_url)
driver.quit()

#epub_data = (1,"a")
#mobi_data = (1,"a")
#a4_pdf_data = (1,"a")
#six_inch_pdf_data = (1,"a")

#print(book_title_in_english)
 
#For security, consider creating a user just for your script.

wp = Client('http://freetamilebooks.com/xmlrpc.php', fte_username, fte_password)
post = WordPressPost()


taxes = wp.call(taxonomies.GetTaxonomies())
print(taxes)


 
with urllib.request.urlopen(cover_url) as response, open(cover_image, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
print("Downloaded Cover Image")    
    
filename = cover_image


data = {
        'name': filename,
        'type': 'image/jpeg',  # mimetype
}


# read the binary file and let the XMLRPC library encode it into base64
with open(filename, 'rb') as img:
        data['bits'] = xmlrpc_client.Binary(img.read())
        

response = wp.call(media.UploadFile(data))
print(response)

image_url = response["url"]
attachment_id = response['id']

print("Uploaded cover Image")


content = "நூல் : " +  book_title + "\n\n" + "ஆசிரியர் : " + author + "\n\n" + "மின்னஞ்சல் : " + author_mail + "\n" +  "<a href=" + image_url + "><img class='alignright size-medium wp-image-6958' src=" + image_url + "  width='300' height='300' /></a>" + "\n" 


print("Generating Content to Post")


if book_info['artist']:
    content = content + "அட்டைப்படம் : " + artist + "\n"

if book_info['artist_email']:
    content = content + artist_email + "\n"


if book_info['translator']:
    content =  content + "தமிழாக்கம் : " + book_info['translator'] + "\n"

if book_info['translator_email']:
    content = content + book_info['translator_email'] + "\n"
    
content = content + "மின்னூலாக்கம் : " + ebook_maker + "\n"
content = content + "மின்னஞ்சல் : " + ebook_maker_email + "\n"

content = content + "வெளியிடு : FreeTamilEbooks.com" + "\n"
content = content + "உரிமை : " + license + "\n" + "உரிமை – கிரியேட்டிவ் காமன்ஸ். எல்லாரும் படிக்கலாம், பகிரலாம்." + "\n"



extra = '''

&nbsp;

&nbsp;

&nbsp;

<b>பதிவிறக்க*</b>

ஆன்ட்ராய்டு(FBreader), ஆப்பிள், புது நூக் கருவிகளில் படிக்க

[download id=" ''' + str(epub_data[0]) + '''" template="button"]

புது கிண்டில் கருவிகளில் படிக்க

[download id=" ''' + str(mobi_data[0]) + '''" template="button"]

குனூ/லினக்ஸ், விண்டோஸ் கணிணிகளில் படிக்க

[download id=" ''' + str(a4_pdf_data[0]) + '''" template="button"]

பழைய கிண்டில்,நூக் கருவிகளில் படிக்க

[download id=" ''' + str(six_inch_pdf_data[0]) + '''" template="button"]

&nbsp;

&nbsp;

&nbsp;


<a>Send To Kindle Directly</a><a href="http://35.166.185.40/send2kindle?fileurl=''' + str(mobi_data[1]) + '''&amp;filename=''' +book_title_in_english + '''.mobi" target="_blank" rel="noopener"><img class="alignleft wp-image-6127 " src="http://freetamilebooks.com/wp-content/uploads/2017/09/send-to-kindle-logo.jpg" alt="" width="579" height="129" /></a>

&nbsp;

&nbsp;

&nbsp;

பிற வடிவங்களில் படிக்க  – ''' + book_url + '''


புத்தக எண் - ''' + str(book_number) + '''


'''
  
content = content + extra

post.title = book_title + " - " + category + " - " + author
post.slug = book_title_in_english
post.post_type = 'ebooks'

post.content = content

post.thumbnail = attachment_id

post.post_status = 'publish'


post.terms_names = {
  'genres': [category],
  'contributors': [artist, ebook_maker],
  'authors' : [author]
}
wp.call(NewPost(post))

print("Published")
