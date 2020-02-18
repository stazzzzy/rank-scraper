from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import winsound

def grab():
    print("Scraping...")
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(firefox_options=options)
    link = "http://na.op.gg/summoner/spectator/userName=tactical+muff1n&"
    driver.get(link)
    soup = BeautifulSoup(driver.page_source,"html.parser")
    driver.quit()
    new = []
    ranks = []
    try:
        for i in range(10):
            sums = soup.select('a[class="SummonerName"]')[i].text.strip()
            rank = soup.select('div[class="TierRank"]')[i].text.strip()
            new.append(sums)
            ranks.append(rank)
    except:
        print("Currently not in game!")
        return False
    o = open("output.txt",'w+',encoding='utf-8')
    o.seek(0)
    o.truncate()
    for i in range(10):
        o.write(new[i] + " // RANK: " + ranks[i] + "\n")
    o.close()
    print("Finish. Written to " + str(o))
    winsound.PlaySound('done.mp3', winsound.SND_FILENAME)
    return True
        
#flag = grab()
#if not flag:
#    print("Exit")
#input("Finish\n")
