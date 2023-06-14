from outcome import capture
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
from webdriver_manager.chrome import ChromeDriverManager
import os

# 에러나는 부분이 있어서 추가
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 터미널에 에러 메시지 나와서 설정
options.add_experimental_option("detach", True)  # 브라우저 자동꺼짐 방지  (생략가능)
driver = webdriver.Chrome(options=options)
options.add_argument("window-size=1200x600")
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
driver.find_element_by_css_selector(".QS5gu.sy4vM").click()
query = "강동원"
elem = driver.find_element(By.NAME, "q")
elem.send_keys(query)
time.sleep(2)
elem.send_keys(Keys.RETURN)
# 스크롤 다운
SCROLL_PAUSE_TIME = 3

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height
time.sleep(3)

for i in range(1, 30):
   
    try:
 
      # XPath of each image
        img = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img')
        img.screenshot(query + ' (' + str(i) + ').png')
        time.sleep(0.2)
 
    except:
         
        # if we can't find the XPath of an image,
        # we skip to the next image
        continue
 
# Finally, we close the driver
driver.close()
# 이미지 다운
# images = []
# images.append(driver.find_elements_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img"))
# time.sleep(10)
# opener=urllib.request.build_opener()
# opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
# print(len(images))

# count = 1
# images[0].click()
# time.sleep(3)
# imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
# print(imgUrl)

# for image in images:

#     # 아래 에러 나는 부분이 있어서 try except문 추가
#     try:
#         image.click()
#         time.sleep(3)
#         # imgUrl = driver.find_element(By.CLASS_NAME, "n3VNCb").get_attribute("src")
#         imgUrl = driver.find_element(
#             By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img").get_attribute("src")
#         #          /html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img
#         # 에러발생경우: 주소가 그림파일주소가 아닌 경우 > 리다이렉트되어 다른 주소로 이동하는 경우등
#         print("image accessed")
#         urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
#         print("image downloaded")
#     except:
#         pass
#     count = count + 1

