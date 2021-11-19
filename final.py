import requests
import csv
from bs4 import BeautifulSoup
import shutil # to save it locally    
from urllib.request import Request, urlopen
import re
import wget

def saving_image(url):

    image_url = url
    filename = image_url.split("/")[-1]

    r = requests.get(image_url, stream = True)

    if r.status_code == 200:

        r.raw.decode_content = True

        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')
        
        

    


    


import requests
import csv
from bs4 import BeautifulSoup
import shutil 
from urllib.request import Request, urlopen
import re


def scrape_image_link(link):
    
    tags = []
    
    final_tags = []
    
    try:
        
        new = link.split('/')
        
        with open('images.csv', 'a') as f: # append image into images.csv
            writer = csv.writer(f)

            html = requests.get(link).text # getting html from page

            soup = BeautifulSoup(html, 'html.parser') # creating bs4 instance

            images = soup.find(class_='PreviewGallery__leftColumn--1ut9H').find_all('img') # getting all the images from the side column

            for image in images: # looping through images from side column
                image = image.get('src') # getting images links
                if 'raf,' in image: # raf, is the identifier I told you about
                                        
                    out = str(soup.title).split('>')
                    out1 = out[1].split('|')
                    final = out1[0].split(' T-shirt by ')
            
                    result = soup.find_all("div", class_="styles__box--2Ufmy styles__marginBottom-m--2W0L- styles__marginRight-xs--13bZk")

                    for i in result:
                        aa = str(i.find_all('a')).split('<')
                        new = str(aa[2]).split('>')
                        tags.append(new[1])
                    
                    for i in tags:
                        final_tags.append(i.split(" ")[0])
                    
                    data = [final[0].strip('"'), image, final[1], final_tags]
                    writer.writerow(data)
                    
                    print(image)
                    #wget_func(image)
                    
            print()
    except:
        return()


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

with open('images.csv', 'a') as f: # append image into images.csv
    writer = csv.writer(f)
            
    header = ['Design_Name', 'Desin_Link', 'Author', 'Tags']
            
    writer.writerow(header)

b = 1102
for i in range(1195):
    a = "https://www.redbubble.com/shop/*?gender=gender-men&iaCode=u-tees&page="
    a = a + str(b)
    x = '&sortOrder=trending'
    a = a + x
    print(a)
    b = b + 1
    req = Request(a)

    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))
    
    count=0
    
    for i in links[20:220]:
        #print(i)
        if i == None:
            break
        count=count+1
        #print(count)
        scrape_image_link(i)
     
        
        
    import pandas as pd
    pd.set_option('display.max_rows', None)
    employee =  pd.read_csv("images.csv")
    dept_emp_num =  employee.groupby('Author')['Author'].count()

    #print(dept_emp_num)

    import csv

    with open('authors.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
   
        writer.writerow(employee.Author)
        #data = [employee.Author, dept_emp_num]
    
        writer.writerow(dept_emp_num)
    
    print("An author report has also been generated")
