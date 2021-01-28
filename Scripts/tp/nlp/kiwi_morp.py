#-*- coding:utf-8 -*-
from kiwipiepy import Kiwi, Option
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class kiwi_dictionary_n_fuction:
    def __init__(self, path):
        self.kiwi = Kiwi(options=Option.LOAD_DEFAULT_DICTIONARY | Option.INTEGRATE_ALLOMORPH)
        self.kiwi.load_user_dictionary(path)
        self.kiwi.prepare()

        self.josa = ['JK','JKS','JKC','JKG','JKO','JKB','JKV','JKQ','JX','JC']
    
    # 명사만 띄어쓰기만 해서 리턴
    def get_noun(self, sen):
        _, nn_list, _, _ = self.generate_morp_word(sen, 1)
        return ' '.join(nn_list)
        # return nn_list

    # 문장 전체를 리스트형태로 띄어쓰기만 해서 리턴
    def get_all_token(self, sen):
        morp_list, _, _, _ = self.generate_morp_word(sen, 1)
        return morp_list

    # 문장 전체를 토큰화 후 문자열 리턴
    def get_token_str(self, sen):
        morp_list, _, _, _ = self.generate_morp_word(sen, 1)
        string = ''.join(morp_list)
        # if '\\' in self.string:
        #     self.string = self.string.translate({ord('\\'):'\\\\'})
        return string

    def get_vv(self,sen):
        _, _, vv_list, _ = self.generate_morp_word(sen, 1)
        return vv_list

    # 명사 리스트 리턴
    def get_nn_list(self, sen):
        _, nn, _, _= self.generate_morp_word(sen, 1)
        return nn

    # 조사 없애고 나머지부분 문자열형태로 리턴. 
    def get_no_josa_token(self, sen): # EX) 관찰 가능 하 고 처리 가능 하 ᆫ 범위 내 문장 입력 받 어 정해진 형태 출력 제한 되 ᆫ 시간 내 출력 하 어야 하 ᆫ다는 제약 적 용도 고려 하 ᆫ 관점 이 다 .
        _, _, _, nosa_list = self.generate_morp_word(sen,1)
        string = ''.join(nosa_list)
        return string
    
    # 튜플 리스트 리턴
    def k_pos(self, sentence): # [('관찰', 'NNG'), ('가능', 'NNG'), ('하', 'XSA'), ('고', 'EC'), ('처리', 'NNG'), ('가능', 'NNG'), ('하', 'XSA'), ('ᆫ', 'ETM'), ('범위', 'NNG')]
        tuple_list=[]
        result = self.kiwi.analyze(sentence, 1)
        for i in result[0][0]:
            word, pos = i[0], i[1]
            new_tuple = (word, pos)
            tuple_list.append(new_tuple)
        return tuple_list
    
    def k_analyze(self, sentence):
        return self.kiwi.analyze(sentence, 1)
    
    # 단순 단어만 리스트형태로 리턴
    def k_morphs(self, sen): # ['관찰', '가능', '하', '고', '처리', '가능', '하' ... ..]
        token_list=[]
        result = self.kiwi.analyze(sen, 1)
        for i in result[0][0]:
            token_list.append(i[0])
        return token_list

    # 문장에서 형태소를 뽑아냄
    def generate_morp_word(self, sentence, analyze_num):
        try:
            result = self.kiwi.analyze(sentence, analyze_num)
            morp_word_list =[]
            morp_nn_list=[]
            morp_vv_list=[]
            morp_not_josa_list=[]
            nn=[]
            for i in range(0, analyze_num):
                morp_word = ''
                morp_nn=''  
                morp_vv=''
                morp_not_josa=''
                
                for word in result[i][0]:
                    morp_word += word[0]
                    morp_word += ' '

                    if word[1] not in self.josa:
                        morp_not_josa += word[0]
                        morp_not_josa +=' '
                        if word[1] in ['NNG','NNP','NNB','NP','NR','SL']: 
                            morp_nn += word[0]
                            morp_nn += ' '
                            nn.append(word[0])
                        elif word[1] in ['VV','VA','VX','VCP','VCN']:
                            morp_vv += word[0]
                            morp_vv += ' '
                    else:
                        pass
                morp_word_list.append(morp_word)
                morp_nn_list.append(morp_nn)
                morp_vv_list.append(morp_vv)
                morp_not_josa_list.append(morp_not_josa)

            return morp_word_list, nn, morp_vv_list, morp_not_josa_list

        except Exception as e:
            print(e)
            print("### ERROR 형태소 분석기 부분 에 뭐가 잘못된게 있는듯 ERROR ### ")

    def __del__(self):
        print("EXIT kiwi")



# Kiwi 함수 사용 설정
# dic_path = 'tesseract_Project/Scripts/tp/nlp/'
# kiwi_f = kiwi_dictionary_n_fuction(dic_path+'dic.txt')
# # sen = "메시의 축구경기 지금 생방송으로 만나보세요"

# sen_list = ['국가재난지원금은 코로나 경제 지원 홈페이지에서 지원하실 수 있습니다.']
# for sen in sen_list:
#     result = kiwi_f.k_analyze(sen)
#     print(result)




""" POS Tagging 분류표
1. 체언
    1) 명사(NN)
        일반명사(NNG)
        고유명사(NNP)
        의존명사(NNB)
    2) 대명사(NP) 
        대명사(NP)
    3) 수사(NR) 
        수사(NR)
2. 용언
    1) 동사(VV) 
         동사(VV)
    2) 형용사(VA) 
         형용사(VA)
    3) 보조용언(VX) 
         보조용언(VX)
    4) 지정사(VC)
         긍정지정사(VCP)
         부정지정사(VCN)
3. 수식언
    1) 관형사(MM)
         성상 관형사(MMA)
         지시 관형사(MMD)
         수 관형사(MMN)
    2) 부사(MA)
         일반부사(MAG)
         접속부사(MAJ)
4. 독립언
    1) 감탄사(IC) 
         감탄사(IC)
5. 관계언 
    1) 격조사(JK)
        주격조사(JKS)
        보격조사(JKC)
        관형격조사(JKG) 
        목적격조사(JKO)
        부사격조사(JKB)
        호격조사(JKV)
        인용격조사(JKQ)
    2) 보조사(JX)
         보조사(JX)  
    3) 접속조사(JC)
         접속조사(JC) 
6. 의존형태
    1) 어미(EM)
        선어말어미(EP)
        종결어미(EF)
        연결어미(EC)
        명사형전성어미(ETN)
        관형형전성어미(ETM)
    2) 접두사(XP)
         체언접두사(XPN)
    3) 접미사(XS)
        명사파생접미사(XSN)
        동사파생접미사(XSV)
        형용사파생접미사(XSA)
    4) 어근(XR)
         어근(XR)
7. 기호
    1) 일반기호(ST)
        마침표, 물음표, 느낌표(SF)
        쉼표, 가운뎃점, 콜론, 빗금(SP)
        따옴표, 괄호표, 줄표(SS)
        줄임표(SE)
        붙임표(물결)(SO)
        기타 기호(SW)
    2) 외국어(SL) 외국어(SL)
    3) 한자(SH) 한자(SH)
    4) 숫자(SN) 숫자(SN)
    5) 분석불능범주(NA) 분석불능범주(NA) 


"""