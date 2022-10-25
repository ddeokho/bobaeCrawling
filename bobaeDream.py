from lib2to3.pgen2 import driver
from urllib import response
import urllib.parse
import requests
import pandas as pd
import os
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

from bs4 import BeautifulSoup



url = "https://www.bobaedream.co.kr/"
cate = "ALL&"#"ALL&search_cat=C3_s0"
lenth = 70
pages = 10
lists = {
	'차량이름' : [],
	'출시가격' : [],
	'엔진형식' : [],
	'실린더 수' : [],
	'배기량(cc)' : [],
	'최고출력(ps/rpm)' : [],
	'최대토크(kg·m/rpm)' : [], 
	'0to100km/h(초)' : [],
	'최고속도(km/h)' : [],
	'구동방식' : [],
	'브레이크(전/후)' : [],
	'서스펜션(전/후)' : [],
	'스티어링' : [],
	'타이어' : [],
	'휠' : [],
	'차체(길이x너비x높이mm)' : [],
	'윤거(전x후mm)' : [],
	'축간거리(mm)' : [],
	'최저지상고(mm)' : [],
	'최소회전반경(ft)' : [],
	'연료' : [],
	'url' : []
}


#lists_col = ['차량이름','출시가격','엔진형식','실린더 수','배기량(cc)','최고출력(ps/rpm)','최대토크(kg·m/rpm)', '0to100km/h(초)','최고속도(km/h)','구동방식','브레이크(전/후)','서스펜션(전/후)','스티어링','타이어','휠','차체(길이x너비x높이mm)','윤거(전x후mm)','축간거리(mm)','최저지상고(mm)','최소회전반경(ft)','연료','url']



if __name__ == "__main__" :

	driver = webdriver.Chrome()
	driver.implicitly_wait(3)

	#search = input("검색어를 입력하세요")
	#search = urllib.parse.quote_plus(search)


	for page in range(pages) :

		page=page+1
		print("")
		print(str(page)+"페이지 작업 시작")
		
		driver.get(f"https://www.bobaedream.co.kr/cyber/CyberCar.php?sel_m_gubun={cate}&page={page}&order=S11&view_size={lenth}")		
		#driver.get(f"https://www.bobaedream.co.kr/cyber/CyberCar.php?sel_m_gubun={cate}&search_txt={search}&page={page}&order=S11&view_size={lenth}")

		html = driver.page_source
		soup = BeautifulSoup(html, 'html.parser')

		driver.implicitly_wait(3)

		'''
		driver.find_element_by_xpath('//*[@id="inp-search"]').send_keys(search)
		driver.find_element_by_xpath('//*[@id="frm_search"]/div[2]/div/div/button').click()
		'''

		#for i in range(lenth) :
		datas=soup.select('p.tit.ellipsis')
		#listCont > div.wrap-thumb-list > ul > li:nth-child(1) > div > div.mode-cell.title > p.tit.ellipsis
		


		i=1#현재 번째
		for data in datas:

			title=data.select_one('a').text
			url_detail=str(url)+data.find('a')['href']

			print("")
			print("======="+str(i)+"번 째 차종 시작=========")
			print(str(i)+". "+title)
			print("-> "+url_detail)
			print("")


			#새창 열기
			driver.execute_script('window.open("'+str(url_detail)+'");')

			#새로 연 탭으로 이동
			last_tab = driver.window_handles[-1]			
			driver.switch_to.window(window_name=last_tab)

			time.sleep(1)
			
			#더보기 클릭
			driver.find_element_by_xpath('//*[@id="bobaeConent"]/div[2]/div[1]/div[3]/div/div[2]/dl/dd[8]/a').click()
			
			time.sleep(1)


			try : 
				#상세페이지 스크래핑
				html2 = driver.page_source
				soup2 = BeautifulSoup(html2, 'html.parser')
				
				infos=soup2.select('tbody > tr > td')


				#터미널 뷰단	
				print("출시가격: "+infos[28].text)		
				print("엔진형식: "+infos[29].text)
				print("실린더 수: "+infos[30].text)
				print("배기량(cc): "+infos[31].text)
				print("최고출력(ps/rpm): "+infos[32].text)
				print("최대토크(kg·m/rpm): "+infos[33].text)
				print("0→100km/h(초): "+infos[34].text)
				print("최고속도(km/h): "+infos[35].text)
				print("구동방식: "+infos[36].text)
				print("브레이크(전/후): "+infos[37].text)
				print("서스펜션(전/후): "+infos[38].text)
				print("스티어링: "+infos[39].text)
				print("타이어: "+infos[40].text)
				print("휠: "+infos[41].text)
				print("차체(길이x너비x높이mm): "+infos[42].text)
				print("윤거(전x후mm): "+infos[43].text)
				print("축간거리(mm): "+infos[44].text)
				print("최저지상고(mm): "+infos[45].text)
				print("최소회전반경(ft): "+infos[46].text)
				print("연료: "+infos[47].text)


				#csv저장	
				lists['차량이름'].append(title)
				lists['출시가격'].append(infos[28].text)
				lists['엔진형식'].append(infos[29].text)
				lists['실린더 수'].append(infos[30].text)
				lists['배기량(cc)'].append(infos[31].text)
				lists['최고출력(ps/rpm)'].append(infos[32].text)
				lists['최대토크(kg·m/rpm)'].append(infos[33].text)
				lists['0to100km/h(초)'].append(infos[34].text)
				lists['최고속도(km/h)'].append(infos[35].text)
				lists['구동방식'].append(infos[36].text)
				lists['브레이크(전/후)'].append(infos[37].text)
				lists['서스펜션(전/후)'].append(infos[38].text)
				lists['스티어링'].append(infos[38].text)
				lists['타이어'].append(infos[40].text)
				lists['휠'].append(infos[41].text)
				lists['차체(길이x너비x높이mm)'].append(infos[42].text)
				lists['윤거(전x후mm)'].append(infos[44].text)
				lists['축간거리(mm)'].append(infos[44].text)
				lists['최저지상고(mm)'].append(infos[45].text)
				lists['최소회전반경(ft)'].append(infos[46].text)
				lists['연료'].append(infos[47].text)
				lists['url'].append(url_detail)


				'''
				#csv저장2
				for j in range(20) :
					lists[lists_col[j+1]].append(infos[j+28].text)
					print(str(lists_col[j+1])+": "+infos[j+28].text)
				'''

			except :


				print("정보없음")
				driver.implicitly_wait(10)
			

			print("======="+str(i)+"번 째 차종 완료=========")
			print("")


			driver.close()  #링크 이동 후 탭 닫기
			first_tab = driver.window_handles[0]
			driver.switch_to.window(window_name=first_tab)

			i=i+1

		print("")
		print("========"+str(page)+" 완료===========")
		print("")
		
		driver.implicitly_wait(2)


	df = pd.DataFrame(lists)
	df.to_csv('bobae.csv', encoding='cp949')
	
	print("bobae.csv 저장 완료")

	driver.quit()
