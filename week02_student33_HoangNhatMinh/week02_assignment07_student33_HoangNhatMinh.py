# tận dụng mã ASCII để mã hóa thay vì dùng dictionary 
# chuyển đổi từ ký tự --> ASCII:    ord('A')    #65
# chuyển đổi ASCII --> ký tự:       chr(65)     #A
# [A-B] ASCII range: [65-91)
# [a-b] ASCII range: [97-123)



# thực hiện việc trả lại giá trị ASCII đếm lùi về phía sau một đoạn n
# thực hiện khi n từ [0, 26] trả về -1 với những giá trị n còn lại 
def moveBackward(n : int, ASCII : int) :
    CHAR = list(range(65,91))
    char = list(range(97,123))
    if 0 <= n <= 26 :
        if ASCII in range(65,91) :
            return CHAR[ASCII - 65 - n]
        elif ASCII in range(97,123) :
            return char[ASCII - 97 - n]
    else: raise IndexError("index out of range 26")

  
def ROTn(code: str, n : int = 13, isDecryption : bool = False):
    result = ''

    n = n % 26
    if isDecryption : 
        pass
    else : n = 26 - n

    for rotnIter in range(len(code)):
        ASCII = ord(code[rotnIter])
        result = result + chr(moveBackward(n, ASCII))

    return result

def testROTn() :
    print("Encode test: ")
    print('___n = 1:')
    for i in range(65, 91):
        tmp = chr(i)
        print(tmp, '-->' ,ROTn(tmp,  1, isDecryption = False), end="   ")
    print('\n___n = 27:')
    for i in range(97, 123):
        tmp = chr(i)
        print(tmp, '-->' ,ROTn(tmp, 27, isDecryption = False), end="   ")
    print('\n___n = -1')
    for i in range(65, 91):
        tmp = chr(i)
        print(tmp, '-->' ,ROTn(tmp, -1, isDecryption = False), end="   ")
    print("\nDecryption test: ")
    print('___n = 1')
    for i in range(65, 91):
        tmp = chr(i)
        print(tmp, '-->' ,ROTn(tmp, 1, isDecryption = True), end="   ")
    print("\nEncode/Decryption test:")
    tmp = ROTn('Python', 19, isDecryption = False)
    print("Encode for 'Python' with ROT-19: ", tmp)
    print("Decryption: ", ROTn(tmp, 19, isDecryption = True))

testROTn()