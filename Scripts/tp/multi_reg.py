import re
import time
import pandas as pd
import numpy as np

start = time.time()

accountRegex1 = re.compile(r'''(
    (\d{3})
    -
    (\d{5})
    -
    (\d{3})
)''', re.VERBOSE)

accountRegex2 = re.compile(r'''(
    (\d{3})
    -
    (\d{6})
    -
    (\d{5})
)''', re.VERBOSE)

accountRegex3 = re.compile(r'''(
    (\d{3})
    -
    (\d{2})
    -
    (\d{5})
    -
    (\d{1})
)''', re.VERBOSE)

accountRegex4 = re.compile(r'''(
    (\d{3})
    -
    (\d{4})
    -
    (\d{4})
    -
    (\d{3})
)''', re.VERBOSE)


# 위 정규식 통합 Dictionary
dic_reg = {
    'aR1' : accountRegex1,
    'aR2' : accountRegex2,
    'aR3' : accountRegex3,
    'aR4' : accountRegex4
}

# Dictionary로 KEY List 생성
reg_list = list(dic_reg.keys())

def extract_all(text):
    for i in range(0, len(reg_list)):
        for regex in dic_reg[reg_list[i]].findall(text):
            # print(reg_list[i] + ' : ' + str(regex))
            reg_list[i] + ' : ' + str(regex)

re1 = r'\s?\d{3}[-]\d{5}[-]\d{3}'
re2 = r'\s?\d{3}[-]\d{6}[-]\d{5}'
re3 = r'\s?\d{3}[-]\d{2}[-]\d{5}[-]\d{1}'
re4 = r'\s?\d{3}[-]\d{4}[-]\d{4}[-]\d{3}'
 

print("Start Time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

with open('test.txt', 'r') as f:
    # 파일 한줄 씩 읽는거. 성능안좋아서 안쓸듯
    # while True:
    #     line = f.readline()
    #     if not line: break
    #     print(line)

    data = f.read()
    
    # re_list = re.compile("(%s|%s|%s|%s)" % (re1, re2, re3, re4)).findall(data)
    # print(re_list)

    # for r in re_list:
    #     extract_all(r)


    # group을 사용하면 or 연산중 하나라도 찾을 경우에 다음 뒷 문자열을 전부 버려버림... group은 한 정규식에서 원하는부분만 추출할 경우에 사용해야 함
    '''
    generic_re = re.compile("(?P<func>%s)|(%s)|(%s)|(%s)" % ((re1), (re2), (re3), (re4)))
    generic_re = re.compile("(?P<func>\s?\d{3}[-]\d{5}[-]\d{3})|(?P<fc2>\d{3}[-]\d{6}[-]\d{5})|(\s?\d{3}[-]\d{2}[-]\d{5}[-]\d{1})|(\d{3}[-]\d{4}[-]\d{4}[-]\d{3})")
    m = generic_re.search("333-55555-333 333-22-55555-1 333-666666-555")
    print(m)
    print(m.group('func'))
    print(m.group('fc2'))
    print(m.group(2))
    print(m.group(3))
    print(m.group(4))
    '''

    colums_list = ['re1','re2','re3','re4']

    # for_csv = re.compile("(%s)|(%s)|(%s)|(%s)"%(re1,re2,re3,re4)).sub(r'\1,\2,\3,\4\n',data)
    # print(for_csv)
    
    
    # list1 = for_csv.split('\n')
    # list1 = [line.split(',') for line in list1]
    # df = pd.DataFrame(list1, columns=colums_list)

    # df['re1'] = df['re1'].replace(" ",np.NaN)
    
    # print(df['re1'].head(20))
    # print(len(df['re1'][2]))
    # print(df['re1'][2])

    # print(df['re1'].dropna())


    
    # CSV로 뽑
    # with open("extract.csv", "w") as file:
    #     file.write("re1,re2,re3,re4\n"+for_csv)
    #     file.close()

    df = pd.read_csv("extract.csv")
    # print(df.head(10))


    # NULL값 제거하고 shift
    df1 = df['re1'].dropna(axis=0).reset_index(drop=True)
    df2 = df['re2'].dropna(axis=0).reset_index(drop=True)
    df3 = df['re3'].dropna(axis=0).reset_index(drop=True)
    df4 = df['re4'].dropna(axis=0).reset_index(drop=True)

    condf = pd.concat([df1, df2, df3, df4], axis=1, ignore_index=True)
    condf.columns = colums_list
    print(condf)

    # print(df['re1'].head(5))

    # 문자열 한줄씩 읽어서 처리하는건 너무 오래 걸림
    '''
    resub = re.compile("(%s)|(%s)|(%s)|(%s)" %(re1, re2, re3, re4)).sub(r're1:\1, re2:\2, re3:\3, re4:\4\n', data)

    re1_list = []
    re2_list = []
    re3_list = []
    re4_list = []

    for i in resub.splitlines():
        if 're1:' in i:
            re1_list.append(re.findall(re1,i))
        elif 're2:' in i:
            re2_list.append(re.findall(re2,i))
        elif 're3:' in i:
            re3_list.append(re.findall(re3,i))
        elif 're4:' in i:
            re2_list.append(re.findall(re4,i))
        else:
            pass
    
    sum(re1_list,[])
    '''



    # extract_all(data)


print("End Time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간



