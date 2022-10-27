#보배드림 국내 커뮤니티 게시판의 내용을 가져오는 크롤링 파일입니다.

#from lib2to3.pgen2 import driver #python2 -> python3로 바꾸어주는 모듈 - 필요X
import urllib.parse #input으로 받은 키워드를 url에 맞게 파싱하는 모듈
import selenium #셀레니움 동적 제어 모듈 전체
from selenium import webdriver #셀레니움 동적 제어(드라이버)
from selenium.webdriver.common.keys import Keys #셀레니움 동적 제어(클릭,입력 등등)
import pandas as pd #데이터프레임, 분석
import time #시간 제어 및 체크

from bs4 import BeautifulSoup #정적, 데이터 크롤링



url = "https://www.bobaedream.co.kr/"
#상세페이지 url을 담기 위한 url
lenth = 70
#한 화면에 나오는 게시글 수
pages = 20
#몇 페이지까지 할 것인지 정의

lists_col = {
	'제목':[],
	'조회수':[],
	'날짜':[],
	'링크':[]
	}


if __name__ == "__main__" :

	#search = input("검색어를 입력하세요")
	search = urllib.parse.quote_plus('기아') 
	#키워드를 url로 인지할 수 있게 바꾸어줌.

	driver = webdriver.Chrome()
	driver.implicitly_wait(4)
	#크롬드라이버를 오픈하고 로딩이 끝날 때까지 기다림.
	#활성화한 드라이버를 driver에 담아서 제어함.

	for page in range(pages) :
	#페이지네이션(1,2,3 ... )을 이용해 여러페이지의 데이터를 추출하기 위래 for를 사용함.
	#무한으로 가동시키고 마지막 페이지에서 끝내고 싶으면 while 활용+오류가 뜨는 시점을 try / except 이용.
	#즉, while문을 가동을 중지 시키고 작업한 내용을 csv로 저장하면 완료할 수 있음.
	
		page=page+1

		print("")
		print(str(page)+"페이지 작업 시작")
		
		try :
			#driver.get(f"https://www.bobaedream.co.kr/cyber/CyberCar.php?sel_m_gubun={cate}&page={page}&order=S11&view_size")
			driver.get(f"https://www.bobaedream.co.kr/list?code=national&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale={lenth}&info3=&noticeShow=&s_select=Body&s_key={search}&level_no=&vdate=&type=list&page={page}")
			html = driver.page_source
			soup = BeautifulSoup(html, 'html.parser')
			driver.implicitly_wait(3)
			#드라이버로 원하는 웹화면으로 이동 후 bs를 이용해 html을 긁어옴 -> 이 떄 html형식으로 파싱해 가시화 필수.
		
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
			#select로 가져온 데이터는 리스트로서 여러개의 데이터가 담겨있기 때문에 for를 이용해 하나씩 내보내 줌.
			#td안에는 제목, 링크 등 데이터가 포함되어 있어 한 번에 2개를 보여줄 수 있음.
			#여기 링크를 활용해 상세페이지로 이동할 수 있음.
			#javascript 함수 window.open('url') 이용 / 첫번째 코드 참고
		
			
		except :
			print("제목 문제")
			lists_col['제목'].append("error")
			lists_col['링크'].append("error")


		try :
			#조회수
			datas2 = soup.select('#boardlist > tbody > tr > td.count')
			for data in datas2 :
				lists_col['조회수'].append(int(data.text))
			
			#조회수를 얻어옴, 위와 같음
			#하나 더 생각해 볼 점은 '#boardlist > tbody > tr > td.count' 위와 접근 위치가 같음
			#이에 우리는 for문 하나에 여러개를 넣을 수 있을 것을 예상해 볼 수 있음
			#ex)
			#datas = soup.select('#boardlist > tbody > tr > td')의 위치를 datas = soup.select('#boardlist > tbody > tr') 한 단계 올리고 
			#자식들을 각각 따라간다면
			#chk_none = data.select_one('td > a.bsubject')
			#chk_title = data.select_one('td.count')
			#이러한 형태로 받아올 수 있을 것을 예상해봄

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
	#공지, 이벤트를 제외한 6번째부터 새로이 저장 
	df=df.sort_values(by='조회수', ascending=False) #ascending=True
	#조회수 기반으로 정렬
	
	print(df)
	df.to_csv('kia.csv', encoding='cp949')
	#csv 저장

	print("완료")

	driver.quit()
