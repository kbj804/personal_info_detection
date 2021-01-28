# List를 활용한 Stack 구현
class Stack(list):
    def __init__(self):
        self.stack = []
 
    def PUSH(self, data):
        self.stack.insert(0, data)
 
    def POP(self):
        if self.is_empty():
            return -1
        return self.stack.pop(0)
 
    def PEEK(self):
        return self.stack[0]
 
    def is_empty(self):
        if len(self.stack) == 0:
            print("Stack Empty")
            return True
        return False
    
    def upRotate(self, num):
        if len(self.stack) < num:
            print("로테이션 횟수가 Stack보다 많습니다. 현재 Stack 수: {}개".format(len(self.stack)))
        else:
            for i in range(num-1):
                temp = self.stack[-1]
                self.stack.pop(-1)
                self.stack.insert(0, temp)
    
    def downRotate(self, num):
        if len(self.stack) < num:
            print("로테이션 횟수가 Stack보다 많습니다. 현재 Stack 수: {}개".format(len(self.stack)))
        else:
            for i in range(num-1):
                temp = self.stack[0]
                self.stack.pop(0)
                self.stack.append(temp)

    def PRINT(self):
        print(''.join(self.stack))



def user_input():
    txts = input()
    return txts.split(' ')
 
def work(input_list):
    f_name = input_list[0]

    if len(input_list) == 2:
        f_arg = input_list[1]

        if f_name == "PUSH":
            s.PUSH(f_arg)

        elif f_name == "UpR":
            s.upRotate(int(f_arg))
        
        elif f_name == "DownR":
            s.downRotate(int(f_arg))
        
        else:
            print("유효하지 않은 함수입니다.[ POP, PUSH , PEEK, DUP, UpR, DownR, PRINT ]")

    elif len(input_list) == 1:

        if f_name == "POP":
            s.POP()

        elif f_name == "DUP":
            temp = s.POP()
            s.PUSH(temp)
            s.PUSH(temp)

        elif f_name =="PEEK":
            print(s.PEEK())

        elif f_name == "PRINT":
            s.PRINT()

        else:
            print("유효하지 않은 함수입니다.[ POP, PUSH , PEEK, DUP, UpR, DownR, PRINT ]")

    else:
        print("잘못 입력하셨습니다. [ POP, PUSH , PEEK, DUP, UpR, DownR, PRINT ]")

def check(msg):
    num = 0
    for i in list(msg):
        if i in ('(','{','['):
            s.PUSH(i)
            num += 1
        elif i in (')','}',']'):
            if s.POP() == 
            num += 1




    if len(s.stack) == 0:
        print("Ok_{}".format(num))
    else:
        print("Wrong_{}".format(num))
        

if __name__=="__main__":
    s = Stack()
    while 1:
        # work(user_input())
        check(input())
        
        