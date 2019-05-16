from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html

def find_matched_tag(areas, tag, find_text, a_class=None):
    for area in areas:
        if a_class:
            results = area.find_all(tag, {"class": a_class})
        else:
            results = area.find_all(tag)

        for result in results:
            if result and result.text == find_text:
                return area

def day_to_str(month, day):
    return str(month) + "/" + str(day)

def get_menulist_areas(URL, restaurant_name):
    #URL = "http://www.korea.ac.kr/user/restaurantMenuAllList.do?siteId=university&id=university_050402000000"
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')


    haksik_areas = soup.find("div", {"class": "ku_restaurant mb60"}).find_all("li")
    haksik_area = find_matched_tag(haksik_areas, "strong", restaurant_name)
    menulist_areas = haksik_area.find_all("ol")
    return menulist_areas

menulist_areas = get_menulist_areas(
    "http://www.korea.ac.kr/user/restaurantMenuAllList.do?siteId=university&id=university_050402000000",
    "교우회관 학생식당"
)

def get_menu(day=0):
    target_date = datetime.today() + timedelta(days=day)
    target = day_to_str(target_date.month, target_date.day)
    menulist_area = find_matched_tag(menulist_areas, "span", target, "date")
    menulist = menulist_area.find_all("p")
    menu = ""

    for _menu in menulist:
        menu = menu + _menu.text + '\n'
    
    return menu

def print_today_menu():
    print("오늘 날짜 : {}".format(datetime.today()))
    print(get_menu())




