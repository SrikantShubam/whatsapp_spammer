
#import selenium and selenium keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
#threading optional
import threading


driver = webdriver.Firefox(executable_path="C:\\WebDriver\\bin\\geckodriver.exe") #Enter Location of Firefox driver. To change the browser just use webdriver.(name_of_the_preffered_browser)
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
sleep(20)
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").click() #using x_path
# driver.find_element_by_class_name("_13NKt copyable-text selectable-text").click() #using class_name
path2="html.js.serviceworker.adownload.cssanimations.csstransitions.webp.webp-alpha.webp-animation.webp-lossless body.web.dark div#app div._1ADa8._3Nsgw.app-wrapper-web.os-win div._1XkO3.two div.ldL67._3sh5K div#main._1fqrG footer._2cYbV div._2BU3P.tm2tP.copyable-area div._1SEwr span div._6h3Ps div._2lMWa div.p3_M1 div._1UWac._1LbR4 div._13NKt.copyable-text.selectable-text"
driver.find_element_by_css_selector(path2).click()


# sleep(40)

def send():
    for i in range(200):
                word="any message"
                driver.find_element_by_css_selector(path2).send_keys(word)
                driver.find_element_by_css_selector(path2).send_keys(Keys.ENTER)
                sleep(0.45)
t1=threading.Thread(target=send)
t1.start()



fileLocation= "E:\\code\\2nd sem\\script.txt"  #Enter location of movie script file
def send_movie():
    with open(fileLocation,"r") as file:
        for line in file:
            for word in line.split(" "):
                driver.find_element_by_css_selector(path2).send_keys(word)
                driver.find_element_by_css_selector(path2).send_keys(Keys.ENTER)
                sleep(0.45)
t2=threading.Thread(target=send_movie)

t2.start()