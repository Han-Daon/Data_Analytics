#시각화를 위해 사용할 라이브러리  metplotlib
import matplotlib.pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
GDP = [67.0, 80.0, 257.0, 1886.0, 6506, 11865.3, 22105,3]

#y축 x축 색깔 마커모양 
plt.plot(years, GDP, color = 'green', marker = 'o', linestyle='solid')
#제목 설정
plt.title("GDP per capita")
#y축 레이블 붙이기
plt.ylable("dollars")
#이미지로 데이터 저장
plt.savefig("GDP_per_capita.png", dpi = 600)
plt.show()

#하나의 차트에 여러개의 라인을 같이 그리려면
x = [x for x in rage(20)]
y =  [x**2 for x in range(20) ]#0에서 20 까지 정수 x에 대해 x 제곱값을 생성
z = [x**3 for x in range(20)]
#각 선에 대한 레이블
plt.plot(x, x, lable ='liner')
plt.plot(x, y, lable = 'quadratic')
plt.plot(x, y, lable='qubic')

plt.xlabel ('x lable')
plt.ylable('y lable')
plt.title("three plot")
plt.legend() # 디폴트 위치에 범례를 표시한다
plt.show()

#막대형 차트 그리기
from matplotlib import pyplot as plt

plt.bar(range(len(years)), GDP)

plt.title("GDP per capita")
plt.ylable("dollars")

#y축에 틱을 붙인다.
plt.xtricks(range(len(years)), years)
plt.show()

#데이터를 산포도로! scatter 사용
import numpy as np

xData = np.arange(20,50)
yData = xData + 2*np.random.randn(30) #xData에 randn()함수로 잡음을 섞는다.-> 정규분포로 만들어 진다.

plt.scatter(xData, yData)
plt.title('Real Age vs Physical Age')
plt.xlabel('Real Age')
plt.ylabel('Physical Age')

plt.savefig("age.png", dpi = 600) 
plt.show()


#파이차트
times = [8, 14, 2]
timelables = ["Sleep", "Study", "Play"]
plt.pie(times, labels = timelables, autopct = "%.2f")
plt.show()

#히스토그램으로 자료의 분포를한눈에 보아요~
books = [1, 6, 2, 3, 1, 2, 0, 2]

#잘료가 6개니 6개의 빈을 이용해야함!
plt.hist(books, bin = 6)

plt.xlabel("books")
plt.ylabel("frequency")
plt.show()

#그럼 이제 다중히스토그램으로 만들어보자
n_bins = 10
x = np.random.randn(1000)
y = np.random.randn(1000)

plt.hist(x, n_bins, histtype = 'bar', color = 'red')
plt.hist(y, n_bins, histtype = 'bar', color = 'blue', alpha = 0.3) #alpha는 투명도
plt.show()

#상자차트 : 최대,최소,중간값,사분위수
random_data = np.random.randn(100)

plt.boxplot(random_data)
plt.show()

#상자 : 중앙깂을 기준 상위 하위 25%깂이 모 여 있는 구간
#범위 밖 데이터는 이상치

#여러개 데이터 박스
data1 = [1,2,3,4,5]
data2 = [2,3,4,5,6]

plt.boxplot([data1,data2 ])
plt.boxplot(np.array[data1,data2 ]) # 박스를 따로 만들기 위해서


