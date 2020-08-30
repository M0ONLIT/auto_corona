#1인당 소요시간 7~8초

from selenium import webdriver
import time

'''
hour,min=8,0
print('%d시 %d분에 설문조사를 시작합니다.'%(hour,min))

while 1:
    now=time.localtime()
    if now.tm_hour==hour and now.tm_min==min:
        break
    print('현재 시간은 %d시 %d분 입니다.'%(now.tm_hour,now.tm_min))
    time.sleep(10)
'''

driver=webdriver.Chrome()#'chromedriver.exe'
driver.implicitly_wait(3)

for i in open('class.txt',encoding='UTF-8'):
    if i.strip()=='break':
        break
    while True:
        try:
            school,name,birth=i.strip().split()
            driver.get('https://eduro.pen.go.kr/stv_cvd_co00_002.do')
            driver.find_element_by_class_name('btn_sm.btn_gray').click()

            driver.switch_to.window(driver.window_handles[1])
            driver.find_element_by_xpath("//input[@id='schulNm']").clear()
            driver.find_element_by_xpath("//input[@id='schulNm']").send_keys(school)
            driver.find_element_by_class_name('btn_sm.btn_gray').click()
            driver.find_elements_by_xpath("//a[@href='#']")[0].click()

            driver.switch_to.window(driver.window_handles[0])
            driver.find_elements_by_class_name('common_input_text')[1].send_keys(name)
            driver.find_elements_by_class_name('common_input_text')[2].send_keys(birth)

            driver.find_element_by_xpath("//*[@id='btnConfirm']").click()

            for j in ['011','02','070','080','090']:
                driver.find_element_by_xpath("//input[@id='rspns%s']"%j).click()

            driver.find_element_by_class_name('btn_blue.btn_block.search_btn').click()
            print(i.strip(),'완료')
            break
        except:
            print(i.strip(),'오류')
            driver.close()
            driver=webdriver.Chrome()
            driver.implicitly_wait(3)
driver.close()


'''
import os
os.system('shutdown /s /t 30')
print('30초안에 종료됩니다. 취소하고 싶으시면 엔터를 눌러주세요')
input()
os.system('shutdown /a')
'''
exit()
