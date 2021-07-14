class listUtils():   

    #join lists
    @staticmethod
    def addList(source1,source2):
        source1.extend(source2)
        return source1

    #removed last item in list
    @staticmethod
    def popList(source,position = -1):
        if position == -1:
            source.pop()
        else:
            source.pop(position)

    #Delete item in list
    @staticmethod
    def deleteItem(source,position):
        del source[position]
        return source

    #sorted list
    @staticmethod
    def sorted(souce, desc = False):       
        souce.sort(reverse = desc)
        return souce

    #reversed list
    @staticmethod
    def reversedList(source):
        source.reverse()
        return source

    #sum list
    @staticmethod
    def sumList(source):
        return sum(source)

def main():
    list1 =[3,2,5]
    list2 =[9,7,8]
    print(f'List1:{list1} list2:{list2}')    
    val = listUtils.addList(list1, list2)
    print(f'List add:{val}')    
    
    #Maximum 
    print(f'Max value: {max(val)}')
    print(f'Min value: {min(val)}')
    #reversed list
    listUtils.reversedList(val)
    print(f'Reversed1:{val}')
    listUtils.reverseString(val)
    print(f'Reversed2:{val}')

    SUM = listUtils.sumList(val)
    print(f'Sum:{SUM}')

    #List sort
    listUtils.sorted(val, True)
    print(f'List sorted desc:{val}')
    listUtils.sorted(val)
    print(f'List sorted asc:{val}')

    listUtils.popList(val)
    print(f'Removed last item in list:{val}')
    listUtils.deleteItem(val,2)
    print(f'Delete item in position 2:{val}')

if __name__ =="__main__":
    main()