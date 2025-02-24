import pandas as pd
import numpy as np

# city 딕트딕셔너리구조를  시리즈화

student1 = pd.Series({
    'kor': 80,
    'eng': 50,
    'mat': 90,
})

print(student1)
student2 = pd.Series({
    'kor': np.nan,
    'com': 90,
    'mat': 90,
})
# print(student2)

# plus = student1 + student2
# min = student1 - student2
# mul = student1 * student2
# div = student1 / student2
plus = student1.add(student2, fill_value=0)
sub = student1.sub(student2, fill_value=0)
mul = student1.mul(student2, fill_value=0)
div = student1.div(student2, fill_value=0)

# print(plus, min, mul, div)
df = pd.DataFrame([plus, sub, mul, div], index=['더함', '빼기', '곱함', '나눔'])
print(df)

print()
print()
