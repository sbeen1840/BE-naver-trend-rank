
from datetime import datetime, timedelta
import requests
import csv
import json


# API 요청 URL
url = "https://openapi.naver.com/v1/datalab/search"


# 요청 헤더 설정
headers = {
    "Content-Type": "application/json",
    "X-Naver-Client-Id": "OuESBKEPczJdpfYICRjF",
    "X-Naver-Client-Secret": "UTK596Iqtz"
}


# 어제, 오늘 날짜 계산
today = datetime.now().strftime('%Y-%m-%d')
yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')


# CSV 파일에서 데이터 읽기
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        groupName = row[0]  # 첫번째 열에 있는 데이터를 groupName으로 사용
        # API 요청 바디 설정
        body = {
            "startDate": yesterday,
            "endDate": today,
            "timeUnit": "date",
            "keywordGroups": [
                {"groupName": groupName, "keywords": [groupName]}
            ]
        }

        # API 요청 보내기
        response = requests.post(url, headers=headers, data=json.dumps(body))

        # 결과 가져오기
        result = json.loads(response.text)

        # 검색량 데이터 출력
        for group in result["results"]:
            print(f"키워드 그룹: {group['title']}")
            for data in group["data"]:
                print(f"날짜: {data['period']}, 검색량: {data['ratio']}")
