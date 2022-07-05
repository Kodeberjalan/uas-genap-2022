a=int(input('Masukkan awal fibonacci data: '))
b=int(input('Masukkan data selanjutnya fibonacci data: '))
c=int(input('Masukkan deret data: '))
fibonacci=[a,b]
for i in range (c): 
    fibonacci.append(fibonacci[i]+fibonacci[i+1]) 
    if fibonacci [i]+fibonacci[i+1]==53:
        break
print(fibonacci)
