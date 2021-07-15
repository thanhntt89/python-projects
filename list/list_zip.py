class listZip():
    def ZipList(self,list1, list2):
        return zip(list1, list2)

    def sort(self,list, sorted_position: int):
        return sorted(list, key= lambda el: el[sorted_position])

    def sort(self,list,element_name:str):
        return sorted(list, key= lambda el: el[element_name])

def main():
    _zip = listZip()   
    list_dict =[{'city':'Ha Noi', 'popular': 8},{'city':'HCM', 'popular': 20},{'city':'Da Nang', 'popular': 4}]
    print(f'Sorted by element')
    print(f'Before sorted:{list_dict}')
    list_dict = _zip.sort(list_dict,'city')   
    print(f'After sorted:{list_dict}')

    list_sorted =["nguyen","tat","thanh","miyatsu","2020"]

    print(f'Sorted by Index')
    print(f'Before sorted:{list_sorted}')
    list_sorted = _zip.sort(list_sorted, 2)
    print(f'After sorted:{list_sorted}')

    list1 = ["Ha Noi", "Da Nang", "HCM"]
    list2 = ["8","4","20"]
   
    val = _zip.ZipList(list1, list2)
  
    for city, popular in val:
        print(f'City: {city}\nPopular: {popular} Milion')

if __name__ =="__main__":
    main()