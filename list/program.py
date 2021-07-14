from list_utils import listUtils

class program():
    def main():
        
        string_array=['nguyen','tat','thanh']
        print(f'original data: {string_array}')
        val = listUtils.joinStringArrayByChar(string_array)
        print(f'Join array:{val}')
        print(f'Split: {listUtils.convertStringToArray(val)}')
        print(f'Check exist char a in string:{listUtils.checkCharInString(val,"a")}')

        char_val = "a"     

        print(f'Char {char_val} counts:{listUtils.countCharInString(val,char_val)}')
        startIndex = input("startIndex:").strip()
        endIndex = input("endIndex:").strip()
        rst = listUtils.getSubString(val,int(startIndex),int(endIndex))
        print(f"substring position {startIndex} - {endIndex}:{rst}\n")
        print(f'revese string:{listUtils.reverseString(val)}')

        startIndex = input("take data postion index:").strip()
        print(f'data in position{startIndex}:{listUtils.takeEveryPosition(val,int(startIndex))}')
    
    if __name__ =="__main__":
        main()
