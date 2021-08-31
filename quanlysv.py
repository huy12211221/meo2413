
from sys import excepthook, implementation

# def question(func,text):
#      while True:
#         func
#         que=input(text)
#         if que == "Y":
#             continue
#         elif que == "N":
#             break

def enter_mhv(text):
    while True:
        x=input(text)  
        if len(x)==9:
            break
        else:
            continue
    return x

def enter_gioi_tinh():
    x=""
    number=input("""Chọn giới tính:
    (1)Nếu là nữ
    (2)Nếu là nam
    (3)Nếu chưa rõ giới tính
    Chọn: """) 
    if number == "1":
        x = "Nu"
    elif number == "2":
        x = "Nam"
    elif number == "3":
        x = "none"
    return x

def add_hv():
    file_object= open('data.txt',mode='r+')
    data = file_object.read()
    f=exists(0,"Nhập mã học viên mới(Gồm 9 số): ")
    mhv = f[2]
    name=input("Nhập tên học viên: ")
    gioi_tinh=enter_gioi_tinh()
    score_theoly=input("Nhập điểm thi lý thuyết: ")
    score_practice=input("Nhập điểm thi thực hành: ")
    file_object.write("\n"+mhv+","+name+","+gioi_tinh+","+score_theoly+","+score_practice)
    file_object.close()
    print("Bạn đã thêm thành công!!")

def exists(num,text):
    while True:
        file_object= open('data.txt',mode='r+')
        data = file_object.read()
        list_data = data.split("\n")
        mhv=enter_mhv(text)
        for i in range (0,len(list_data)):
            c = list_data[i]
            if c == '':
                num+=2
                continue
            if c[0:9]==mhv:
                break
            else:
                num += len(c)+2
        if c[0:9]!=mhv:
            break
        else:
            print("Mã học viên đã tồn tại!")
            num=0
    return num,c,mhv #num là vị trí con trỏ chuột, c là str thông tin học viên

def not_exists(num,text):
    while True:
        file_object= open('data.txt',mode='r+')
        data = file_object.read()
        list_data = data.split("\n")
        mhv=enter_mhv(text)
        for i in range (0,len(list_data)):
            c = list_data[i]
            if c == '':
                num+=2
                continue
            if c[0:9]==mhv:
                # print(c)
                break
            else:
                num += len(c)+2
        if c[0:9]==mhv:
            break
        else:
            print("Mã học viên không tồn tại!")
            num=0
    m = c.split(",") # list thông tin của học viên
    return num,c,m #num là vị trí con trỏ chuột, c là str thông tin học viên
        
def delete_hv(num,c):
    file_object= open('data.txt',mode='r+')
    file_object.seek(num)
    file_object.write(" "*len(c))
    file_object.close()

def check_score(text):
    file_object = open('data.txt',mode='r+')
    data = file_object.read()
    list_data = data.split("\n")
    for i in range (0,len(list_data)):
        c = list_data[i]
        if c[0]==" ":
            continue
        d = c.split(",")
        if text == "up":
            if ((int(d[3])+int(d[4]))/2) >= 75:
                print(d[0],d[1])  
        elif text == "down":
            if ((int(d[3])+int(d[4]))/2) < 75:
                print(d[0],d[1]) 
def update2_hv(num,c,z,m):
    l=""
    n=0
    delete_hv(num,c) #num là vị trí con trỏ chuột, c là số kí tự cần xóa
    if z == "0":
        f=exists(0,"Nhập mã học viên mới(Gồm 9 số): ")
        mhv = f[2]
        m[0]=mhv
    elif z== "1":
        name=input("Nhập tên mới: ")
        m[1]=name
    elif z == "2":
        gioi_tinh = enter_gioi_tinh()
        m[2]=gioi_tinh
    elif z == "3":
        score_theoly = input("Nhập điểm thi lý thuyết: ")
        m[3]=score_theoly
    elif z == "4":
        score_practice = input("Nhập điểm thi thực hành: ")
        m[3]=score_practice
    file_object= open('data.txt',mode='r+')
    file_object.seek(num)
    for i in range (0,len(m)):
        l+=m[i]
        if n<len(m)-1:
            l+=","
        n+=1
    file_object.write(l)
#main
print("""Chọn chế độ:
(1)Để thêm học viên.
(2)Xóa thông tin học viên.
(3)Hiển thị danh sách học viên.
(4)Cập nhật thông tin học viên.
(5)Hiển thị danh sách học viên thi đỗ.
(6)Hiển thị danh sách học viên thi trượt.""")
mode = input("Chọn: ")

if mode == "1":
    text = """Bạn có muốn thêm nữa không?(Nhập Y để tiếp tục, nhập "N" thoát)
        -->"""
    while True:
        add_hv()
        que=input(text)
        if que == "Y":
            continue
        elif que == "N":
            break
elif mode == "2":
    text = """Bạn có muốn xóa thêm không?(Nhập Y để tiếp tục, nhập "N" để thoát)
            -->"""
    x = not_exists(0,"Nhập mã học viên cần xóa thông tin(gồm 9 số): ")
    while True:
        delete_hv(x[0],x[1])
        print("Đã xóa thành công")
        que=input(text)
        if que == "Y":
            continue
        elif que == "N":
            break
elif mode == "3":
    file_object= open('data.txt',mode='r+')
    data = file_object.read()
    list_data = data.split("\n")
    for i in range (0,len(list_data)):
        c = list_data[i]
        if c[0]==" ":
            continue
        d = c.split(",")
        print(d[0],d[1])
    file_object.close()
elif mode == "4":
    while True:
        x = not_exists(0,"Nhập mã học viên cần cập nhật(gồm 9 số): ")
        while True:
            z = input("""Bạn cần cập nhật thông tin gì?
            (0)Mã học viên
            (1)Họ và tên
            (2)Giới tính
            (3)Điểm thi lý thuyết
            (4)Điểm thi thục hành
            Chọn: """)
            update2_hv(x[0],x[1],z,x[2])
            que = input("""Bạn muốn cập nhật thông tin khác không?
            (Chọn Y để tiếp tục cập nhật thông tin khác, N để cập nhật học viên khác)
            -->""")
            if que == "Y":
                continue
            elif que == "N":
                break
        que = input("""Bạn có muốn cập nhật học viên khác không?
        (Chọn Y để tiếp tục, N để thoát)
        -->""")
        if que == "Y":
                continue
        elif que == "N":
            break
elif mode == "5":
    check_score("up")
elif mode == "6":
    check_score("down")