import os.path

try:
    fname = './dumy.txt'
    save_path = os.path.abspath(fname)
    if not os.path.exists(save_path):
        print('No fileName ... \n파일데이터가 없습니다 ')
    else:
        with open(fname , 'r', encoding='utf-8') as myfile:
            data = myfile.readlines()
        print(data)
except Exception as e:
    print(f'파일의 경로 및 파일 이름을 다시 한번 체크해주세요 {e}')