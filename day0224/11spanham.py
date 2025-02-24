import pandas as pd
import numpy as np
import re
'''
첫번째 순서[1] spam.data 파일 열기 
순서 [2] 리스트 컴프리헨젼 이용해서 spam 1, ham 0 
권장 리스트
데이터 프레임 사용여부 권장
시각화 적용 안함
출력 결과는 리스트나 문자열 추출 가능 

'''
path = './data/spam_data.csv'
df = pd.read_csv(path, encoding='euc-kr', header=None)


class create_csv():

    print(df)
    passList = []
    for i, v in enumerate(df[0]):
        if v == 'ham': passList.append(1)
        else: passList.append(0)
    is_spam = ['고려' if x == 0 else '안심' for x in passList]
    df[3] = passList
    df[4] = is_spam


def extract_korean(text):
    return re.sub(r'[^가-힣\s]', '', text)


df[1] = df[1].apply(extract_korean)
copyData1 = pd.DataFrame(df)
copyData = pd.Series([df])
content = list(map(lambda x: {x.replace(' ', '')}, df[1]))
print(content)
print()

if __name__ == '__main__':
    csv = create_csv()
