# workdictlist.py

score_dict = {'kim':[100,60],'lee':[90,77],'goo':[82,34]}
guk,eng = 0,0
for i,v in score_dict.items():
    guk += v[0]
    eng += v[1]
print(f'국어 점수 총합은 = {guk}\n영어 점수 총합은 = {eng}')

guk_avg = guk // len(score_dict.keys())
eng_avg = eng // len(score_dict.keys())


print(f'국어 평균 점수는 {guk_avg} \n영어 평균 점수는 {eng_avg}')