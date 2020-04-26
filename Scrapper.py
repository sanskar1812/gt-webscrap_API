from bs4 import BeautifulSoup
import requests 
import pandas as pd

list1=[]
list11=[]
list2=[]
list22=[]
list3=[]
list33=[]
list4=[]
list44=[]
list5=[]
npo={}


list55=[]
url = "https://www.programmableweb.com/category/tools/api"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data,'html.parser')

one = soup.find_all('tr',{'class':'odd'})
for i in one:
    follow_tags = i.find('td',{'class':'views-field views-field-count'})
    follow = i.find('td',{'class':'views-field views-field-count'}).text if(follow_tags) else "N/a"
    #print(follow,end=' ')
    list1.append(follow)
    
    vers_tags = i.find('td',{'class':'views-field views-field-pw-version-links'})
    vers = i.find('td',{'class':'views-field views-field-pw-version-links'}).text if(vers_tags) else "N/a"
    #print(vers,end='')
    list2.append(vers)
    
    cate_tags=i.find('td',{'class':'views-field views-field-field-article-primary-category'})
    cate = i.find('td',{'class':'views-field views-field-field-article-primary-category'}).text if(cate_tags) else "N/a"
    
    name_tags=i.find('td',{'class':'views-field views-field-title'})
    name = i.find('td',{'class':'views-field views-field-title'}).text if(name_tags) else "N/a"
    #print(name,end=' ')
    list4.append(name)
    
    x=i.find('a')
    #print(cate,end=' ')
    list3.append(cate)
    
    zz='https://www.programmableweb.com/category/tools/'+x.get('href')
    list5.append(zz)
    
    npo[i] = [name, cate, vers, follow, zz]
    
one = soup.find_all('tr',{'class':'even'})
for i in one:
    #jobs = soup.find_all('tr',{'class':'odd views-row-first'})
    follow_tags = i.find('td',{'class':'views-field views-field-count'})
    follow = i.find('td',{'class':'views-field views-field-count'}).text if(follow_tags) else "N/a"
    #print(follow,end=' ')
    list11.append(follow)
    
    vers_tags = i.find('td',{'class':'views-field views-field-pw-version-links'})
    vers = i.find('td',{'class':'views-field views-field-pw-version-links'}).text if(vers_tags) else "N/a"
    #print(vers,end='')
    list22.append(vers)
    
    cate_tags=i.find('td',{'class':'views-field views-field-field-article-primary-category'})
    cate = i.find('td',{'class':'views-field views-field-field-article-primary-category'}).text if(cate_tags) else "N/a"
    
    
    
    name_tags=i.find('td',{'class':'views-field views-field-title'})
    name = i.find('td',{'class':'views-field views-field-title'}).text if(name_tags) else "N/a"
    #print(name,end=' ')
    list44.append(name)
    
    x=i.find('a')
    #cate1=x.get('href') 
    #print(cate,end=' ')
    list33.append(cate)
    
    zz='https://www.programmableweb.com/category/tools/'+x.get('href')
    list55.append(zz)

    
print(' -------------------------------------------------------')
print(" | API-Names         | Category  | Followers | Versions|")
print(' -------------------------------------------------------')

for i in range(0,len(list4)-1):
    print(list4[i],end='  ')
        
    print(list3[i],end='      ')
    
    print(list1[i],end='        ')
    
    print(list2[i],end='    ')
    
    print()
    print(" ",list5[i])
    
    print(list44[i],end=' ')
    print(list33[i],end=' ')
    print(list11[i],end=' ')
    print(list22[i])
    
    print(" ",list55[i])

print("----------------------------")

