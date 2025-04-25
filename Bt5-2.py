import math
import random
from os import lstat


def menu():
    print("-------------MENU---------------")
    print("1. In ra danh sách vừa tạo.")
    print("2. In đảo ngược danh sách.")
    print("3. Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).")
    print("4. tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.")
    print("5. đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.")
    print("6. In ra vị trí các phần tử là số nguyên tố.")
    print("7. tìm các số duy nhất (không trùng lặp) trong danh sách.")
    print("8. liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.")
    print("9. In ra các đoạn con trong danh sách giảm liên tiếp.")
    print("10. Thoát")
def sinhmang(n):
    lst = list()
    for i in range(n):
        x = random.randint(1, 100)
        lst.append(x)
    return lst
def in_mang(mang):
    print(mang)
def biggest_index(mang):
    mang_coppy = mang.copy()
    mang_coppy.sort()
    max_value = mang_coppy[-1]
    print(f"Số lớn nhất trong danh sách: {max_value}")
    for i in range(len(mang)-1,-1,-1):
        if max_value == mang[i]:
            print(f"số lớn nhất ở vị trí {i+1}")
            return i
def songuyento(mang):
    mang_coppy = mang.copy()
    mang_coppy.sort()
    for num in mang_coppy:
        if num < 2:
            continue
        is_prime = True
        for i in range (2, int(math.sqrt(num)+1) ):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{num} là so nguyen to")
def num_only(mang):
    mang_coppy = mang.copy()
    mang_coppy.sort()
    ketqua = []
    for num in mang_coppy:
        if mang_coppy.count(num) == 1:
            ketqua.append(num)
    print(ketqua)
def count_num(mang):
    mang_coppy = mang.copy()
    mang_coppy.sort()
    for num in set(mang_coppy):
        c= mang_coppy.count(num)
        print(f"Số {num} xuất hiện {c} lần")


def doan_giam(mang_chinh):
    mang_coppy = mang_chinh.copy()
    ket_qua = []
    mang_tam = [mang_coppy[0]]  # Chỉnh lại mang_tam là danh sách
    for i in range(1, len(mang_coppy)):
        if mang_coppy[i] < mang_coppy[i - 1]:
            mang_tam.append(mang_coppy[i])  # Tiếp tục thêm vào mang_tam nếu giảm
        else:
            if len(mang_tam) >= 2:
                ket_qua.append(mang_tam)  # Lưu đoạn giảm dần vào ket_qua
            mang_tam = [mang_coppy[i]]  # Bắt đầu đoạn mới với phần tử hiện tại
    if len(mang_tam) >= 2:
        ket_qua.append(mang_tam)  # Đảm bảo thêm đoạn cuối cùng nếu nó có đủ phần tử

    for mang in ket_qua:
        print(mang)

if __name__ == '__main__':
    n = int(input("Mời bạn nhập số phần tử của list :"))
    mang_chinh = sinhmang(n)
    new_mang = mang_chinh.copy()
    while True:
        menu()
        chon = int(input("Mời bạn chọn số:"))
        if chon == 1:
            in_mang(mang_chinh)
        if chon == 2:
            new_mang.reverse()
            in_mang(new_mang)
        if chon == 3:
            sort_mang = sorted(mang_chinh)
            in_mang(sort_mang)
        if chon == 4:
            biggest_index(mang_chinh)
        if chon == 5:
            count = 0
            vi_tri = []
            index = int(input("Mời bạn nhập số: "))
            for i in range(len(mang_chinh)):
                if mang_chinh[i] == index:
                    count +=1
                    vi_tri.append(i+1)
            print(f"So luong index: {count}")
            print(f"Cac vi tri trong mang: {vi_tri}")
        if chon == 6:
            songuyento(mang_chinh)
        if chon == 7:
            num_only(mang_chinh)
        if chon == 8:
            count_num(mang_chinh)
        if chon == 9:
            doan_giam(mang_chinh)
        if chon == 10:
            break
