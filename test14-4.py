import xml.etree.ElementTree as et
#tạo class chứa các thông tin của 1 người
class People:
    #override lại init khởi tạo:
    def __init__(self, ID, createAt, name, age):
        self.__id = ID
        self.__createAt = createAt
        self.__name = name
        self.__age = age
    #override lại str để in các đối tượng từ class ra
    def __init__(self):
        return f'people[ID={self.__id}, createAt= {self.__createAt}, name={self.__name}, age={self.__age},' 
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age  
    @property
    def ID(self):
        return self.__id  
    @property
    def createAt(self):
        return self.__createAt 
    #tạo hàm bóc tách dữ liệu xml:
    def parse_xml(file_name):
     tree = et.parse(file_name)
     root = tree.getroot()
     danhsach  = []
     for item in root:
         ID = item[0].text
         createAt = item[1].text
         name = item[2].text
         age = item[3].text

         danhsach.append(People(ID, createAt, name,age))
     return danhsach 

    def show_danhsach(danhsach):
     for item in danhsach:
         print(item)


    if __name__ == '__main__'  :
        file = 'baitap14-4.xml' 
        peopleList = parse_xml(file)
        print('Danh sach: ')
        show_danhsach(danhsach)
  