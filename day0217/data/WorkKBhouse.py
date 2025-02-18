# workKBhouse.py


class KBHouse:

    def __init__(self, *p):
        self.p = p

    def print_list(self, *p):
        for i in p:
            print(i)


house1 = KBHouse("제주", "아파트", "매매", "2억", "2025년")
house2 = KBHouse("독도", "오피스텔", "전세", "1억", "2025년")
house3 = KBHouse("서울", "단독빌라", "월세", "500/30", "2025년")
kb = KBHouse()
kb.print_list(house1)
""""
work시리즈] kBhouse클래스 연습 workhouse.py 클래스이름 KBHouse
house1 = KBHouse("제주", "아파트", "매매", "2억", "2025년")
house2 = KBHouse("독도", "오피스텔", "전세", "1억", "2025년")
house3 = KBHouse("서울", "단독빌라", "월세", "500/30", "2025년")

'''
3건 부동산거래가 있습니다
제주 아파트 매매 2억 2025년
독도 오피스텔 전세 1억 2025년
서울 단독빌라 월세 500/30 2025년
'''
힌트 리스트 항목 추가하면 편합니다 
"""
