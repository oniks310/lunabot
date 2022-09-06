import requests
from bs4 import BeautifulSoup
from datetime import date

today = date.today().strftime('%d.%m.%Y')
#print('Сегодня:', today)

url = 'https://www.life-moon.pp.ru/'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
table = soup.find('table', class_='moon-events-table pure-table pure-table-bordered')
lunday = ''
td = table.find_all('td')

for i in td:
    lunday += str(i.text)
#print(lunday)




url_hol = 'https://astrosfera.ru/bez-rubriki/luna-bez-kursa-2022.html'
page_hol = requests.get(url_hol)
soup_hol = BeautifulSoup(page_hol.text, "html.parser")
info_hol = soup_hol.find_all('td', "column-1")
#print(info_hol)
#print(len(info_hol))
list_hol = []
for item in info_hol:
    list_hol.append(item.text.strip())

# info_hol = info_hol.text
# print(info_hol)
#print(len(list_hol))
# print(list_hol)
f = False
for i in list_hol:
    #print('i=', i)
    s = i.split('\n')
    for j in s:
        #print('j=',j)
        if today in j:
            hol = 'Луна холостая' + j
            f = True
            break
        else:
            f = False
            #print('Луна не холостая')
    if f == True: break
if f == False: hol = 'Луна не холостая'

#Общий вывод инфы:
info = lunday + '\n' + hol
