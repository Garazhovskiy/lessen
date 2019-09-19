import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    art = soup.find('article', class_="conversion-essense")
    uah = art.find_all('span', class_="pretty-sum")[1].next
    uah = uah.replace(',', '.')
    return (uah)

def get_html_pln(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse_pln(html):
    soup = BeautifulSoup(html, 'html.parser')
    art = soup.find('article', class_="conversion-essense")
    pln = art.find_all('span', class_="pretty-sum")[1].next
    pln = pln.replace(',', '.')
    return (pln)

course_doll = float(parse(get_html('https://pokur.su/usd/pln/1/')))
course_pln = float(parse_pln(get_html_pln('https://pokur.su/uah/pln/1/')))

time_work_day = float(input("Сколько часов вы будете работать в день?: "))
amount_of_payment = float(input("Сколько вы будете зарабатывать в час?(сумма): "))
how_many_working = float(input("Сколько дней в месяц будешь работать?: "))


def get_cesh_dey(summ):
    rout = summ * time_work_day                                                                #дневная зарплата
    return rout

def get_cesh_mount(summ):
    tuut = amaunt_of_dey * how_many_working                                                    #Месячная зарплата
    return tuut

amaunt_of_dey_pln = get_cesh_dey(amount_of_payment)                                                #дневная зарплата_pln
amaunt_of_mount_pln = get_cesh_dey(amount_of_payment) * how_many_working                           #Месячная зарплата_pln
amaunt_of_dey_usd = amaunt_of_dey_pln / course_doll                                                #Долларов в день_usd
amaunt_of_mount_usd = amaunt_of_mount_pln / course_doll                                            #Долларов в месяц_usd
amaunt_of_dey_uah = amaunt_of_dey_pln / course_pln
amaunt_of_mount_uah = amaunt_of_mount_pln / course_pln

print('Ваша зарплата: ')
print("{} PLN/ДЕНЬ".format(round(amaunt_of_dey_pln,2)))
print("{} PLN/МЕСЯЦ".format(round(amaunt_of_mount_pln,2)))
print("{} USD/ДЕНЬ".format(round(amaunt_of_dey_usd,2)))
print("{} USD/МЕСЯЦ".format(round(amaunt_of_mount_usd,2)))
print("{} ГРН/ДЕНЬ".format(round(amaunt_of_dey_uah,2)))
print("{} ГРН/МЕСЯЦ".format(round(amaunt_of_mount_uah,2)))


