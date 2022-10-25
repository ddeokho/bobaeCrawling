#보배드림 국내 커뮤니티 게시판의 내용을 가져오는 크롤링 파일입니다.

from lib2to3.pgen2 import driver
from urllib import response
import urllib.parse
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

from bs4 import BeautifulSoup



url = "https://www.bobaedream.co.kr/"
lenth = 70
pages = 20

lists_col = {
	'제목':[],
	'조회수':[],
	'날짜':[],
	'링크':[]
	}


if __name__ == "__main__" :

	#search = input("검색어를 입력하세요")
	search = urllib.parse.quote_plus('기아')

	driver = webdriver.Chrome()
	driver.implicitly_wait(4)

	for page in range(pages) :
		
		page=page+1

		print("")
		print(str(page)+"페이지 작업 시작")
		
		try :
			#driver.get(f"https://www.bobaedream.co.kr/cyber/CyberCar.php?sel_m_gubun={cate}&page={page}&order=S11&view_size")
			driver.get(f"https://www.bobaedream.co.kr/list?code=national&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale={lenth}&info3=&noticeShow=&s_select=Body&s_key={search}&level_no=&vdate=&type=list&page={page}")
			html = driver.page_source
			soup = BeautifulSoup(html, 'html.parser')
			driver.implicitly_wait(3)
		
		except :
			print("페이지 오류")



		try :
			datas = soup.select('#boardlist > tbody > tr > td')

			#제목
			for data in datas :
				
				chk_none = data.select_one('a.bsubject')
				
				if chk_none is not None :
					lists_col['제목'].append(chk_none.text)
					url_detail = url+str(chk_none['href'])
					lists_col['링크'].append(url_detail)
		
		except :
			print("제목 문제")
			lists_col['제목'].append("error")
			lists_col['링크'].append("error")


		try :
			#조회수
			datas2 = soup.select('#boardlist > tbody > tr > td.count')
			for data in datas2 :
				lists_col['조회수'].append(int(data.text))

		except :
			print("조회수 문제")
			lists_col['조회수'].append("error")



		try :
			#날짜
			datas3 = soup.select('#boardlist > tbody > tr > td.date')
			for data in datas3 :
				lists_col['날짜'].append(data.text)

		except :
			print("날짜문제")
			lists_col['날짜'].append("error")
		

		time.sleep(1)
		#driver.implicitly_wait(5)
		


	print("크롤링 완료")
	df=pd.DataFrame(lists_col)
	df=df.loc[6:]
	print(df.head())
	df2=df.sort_values(by='조회수', ascending=False) #ascending=True

	print(df2)
	df2.to_csv('kia.csv', encoding='cp949')

	print("완료")

	driver.quit()
