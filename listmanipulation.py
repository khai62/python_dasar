
nilai = [1,2,3,4,5,6,7,8,9,10]

# mengakses elemen 
print(nilai[0])
print(nilai[-2])

# mengakses sub list  
print(nilai[2:4])
print(nilai[:9])
print(nilai[::3])

# menambah element 
nilai.append(5)
print(nilai)

nilai.insert(2, 25)
print(nilai)

nilai.extend([12, 13, 14])
print(nilai)


# menghapus element 
nilai.remove(25)
print(nilai)

hapusI = nilai.pop(10)
print(hapusI)
print(nilai)

# nilai.clear()
# print(nilai)

# membalikkan list 
nilai.reverse()
print(nilai)


# Urutkan secara ascending 
nilai.sort()
print(nilai)

# Urutkan secara descending 
nilai.sort(reverse=True)
print(nilai)

# copy list 
nilai_baru = nilai.copy()
print(nilai_baru) 


# membuat list dengan logika 
tes = [x for x in range(10) if x % 2 == 0]
print(tes)

# list 2 dimensi 
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[2][1])