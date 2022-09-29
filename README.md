# 보배드림 PYTHON 크롤러

[보배드림](https://www.bobaedream.co.kr/cyber/CyberCar.php?sel_m_gubun=ALL
) 중고자동차 상세 내역을 가져오는 크롤러 입니다.


#### 환경설정

1. 설치 모듈 설치
 - numpy
 - pandas
 - requests
 - BeautifulSoup4
 - selenium
 - matplotlib

```
pip install 모듈명
```

2. chromedriver 설치 및 설정
- chrome버전 확인
![image](https://user-images.githubusercontent.com/20199818/192540395-b8bdfe7f-dc36-4b8f-8d4c-24abd4e5d633.png)

- 동일한 버전의 chromedriver 설치: [chromedriver.exe](https://chromedriver.chromium.org/downloads) 다운

- 다운받은 chromedriver.exe는 python 파일과 같은 폴더 내에 위치
- 아나콘다 터미널에서 파이썬 파일 접근: cd 해당 python파일의 경로까지 작성

3. 파이썬 파일 실행
```
(base)PS C:\user\경로>python bobaeDream.py
```


4. anaconda 가상환경
- 가상환경 만들기

```
conda create -n 이름 python=버전
ex) conda create -n <span style="color:red">py36</span> python=<span style="color:red">3.6</span>
```
- 가상환경 리스트 확인
```
conda env list
```
- 가상환경 활성화
```
conda activate 이름
ex)
(base)PS C:\user\경로>conda activate <span style="color:red">py36</span>
(py36)PS C:\user\경로>
```
