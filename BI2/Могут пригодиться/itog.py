from bs4 import BeautifulSoup
import requests
from time import sleep


headers = {"User-Agent": 
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}

def get_url():
  
    url = f"https://russia.superjob.ru/vakansii/analitik-bi.html?utm_source=yandex_sj&utm_medium=cpc&utm_campaign=SJ_candidate_do_RF|type3&utm_content=1233052|%D0%92%D0%B0%D0%BA%D0%B0%D0%BD%D1%81%D0%B8%D0%B8|4|%D0%A1%D1%82%D1%83%D0%BF%D0%B8%D0%BD%D0%BE&utm_term=none&yclid=5541557058299494399"

    response = requests.get(url, headers = headers)
        # lxml парсинг тегов в html
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find_all("span", class_ = "hAGFy _6KjNy jOraY _1U9AF _1MHTr aSJ_Z FbZAB _3I5b8")
    for i in data:
        
        cars_url = "https://russia.superjob.ru" + i.find("a").get("href")
       
        # Вход на страницу
        # Обьект генератор для оптимизации использования памяти
        yield cars_url
        

def array_conv():
    for j in get_url():
        response = requests.get(j, headers = headers)
        sleep(3)
        # lxml парсинг тегов в html
        soup = BeautifulSoup(response.text, "lxml")
        #Наименование вакансии
        name = soup.find("span", class_ = "_1MHTr aSJ_Z FbZAB _1quxI").text
        # Наименование организации
      #  print(name)
       # company = soup.find("span", class_ = "_1MHTr aSJ_Z FbZAB _1quxI").text
        # Опыт работы
       # work_space = soup.find("span", class_ = "FJ_1X aSJ_Z _1quxI").text
        # Зарплата
      #  price = soup.find("span", class_ = "_2eYAG _1MHTr aSJ_Z _1quxI").text
        # Регион 
        #region_push = soup.find_all("span", class_ = "_3CcMp aSJ_Z FbZAB _1quxI")[1]
    
        # Режим работы
       # work_date = soup.find_all("span", class_ = "FJ_1X aSJ_Z _1quxI")
       # for index, span_tag in enumerate(work_date):
        #    itog_work_date = span_tag.text
        # Навыки
        skills = soup.find_all("ul")
        if len(skills) > 1:
            skills = skills[1].text.replace(";", "\n")
        
        # Описание вакансии
        #write = soup.find("li").text.replace(";", "")
        # Дата публикации
        #date_push = soup.find_all("div", class_ = "_3fjMn _1o5Wk")
       # for i in date_push:
       #     date_pushs = i.find("span", class_ = "_3CcMp aSJ_Z _36p94 _1quxI").text
        
        return name
print(array_conv())
