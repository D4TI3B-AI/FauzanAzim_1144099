import time
start_time = time.time()
print("Menghitung ( nilai1 * nilai2) + (nilai3 / nilai4)") 
a = input("Masukan Nilai 1 : ")
b = input("Masukan Nilai 2 : ")
c = input("Masukan Nilai 3 : ")
d = input("Masukan Nilai 4 : ")

if a == 'satu'    : a=1
if a == 'dua'     : a=2
if a == 'tiga'    : a=3
if a == 'empat'   : a=4
if a == 'lima'    : a=5
if a == 'enam'    : a=6
if a == 'tujuh'   : a=7
if a == 'delapan' : a=8
if a == 'sembilan': a=9
if a == 'nol'     : a=0

if b == 'satu'    : b=1
if b == 'dua'     : b=2
if b == 'tiga'    : b=3
if b == 'empat'   : b=4
if b == 'lima'    : b=5
if b == 'enam'    : b=6
if b == 'tujuh'   : b=7
if b == 'delapan' : b=8
if b == 'sembilan': b=9
if b == 'nol'     : b=0

if c == 'satu'    : c=1
if c == 'dua'     : c=2
if c == 'tiga'    : c=3
if c == 'empat'   : c=4
if c == 'lima'    : c=5
if c == 'enam'    : c=6
if c == 'tujuh'   : c=7
if c == 'delapan' : c=8
if c == 'sembilan': c=9
if c == 'nol'     : c=0

if d == 'satu'    : d=1
if d == 'dua'     : d=2
if d == 'tiga'    : d=3
if d == 'empat'   : d=4
if d == 'lima'    : d=5
if d == 'enam'    : d=6
if d == 'tujuh'   : d=7
if d == 'delapan' : d=8
if d == 'sembilan': d=9
if d == 'nol'     : d=0

jumlah = (a * b) / (d - c)
print ("hasil" ,jumlah)
print("Waktu Eksekusi : %s detik " % (time.time() - start_time))
