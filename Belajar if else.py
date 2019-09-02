nilai = 10
# belajar Kondisian if else
if nilai == 100:
    print('berasil hasilnya 100')

if nilai != 100:
    print('berasil tidak 100')


# if else versi python
if nilai is 100:
    print('sama dengan 100')


if nilai is not 100:
    print('tidak sama dengan 100')


nilai1 = 50
print('===================\n===================')
print(10*'\t=')
if 80 <= nilai <= 100:
    print('nilai Anda A')
elif 70 <= nilai < 80:
    print('nilai Anda B')
elif 60 <= nilai < 70:
    print('nilai Anda C')
elif 50 <= nilai < 60:
    print('Anda Tidak lulus')
else:
    print('kangokan ngulang Lain waktu')

print(100*'#')
# oprator logika untuk list dan string

nama = ['cahya', 'dadi', 'mama', 'kakak']

panggil = 'cah'


if panggil in nama:
    print('pangil gue', panggil)

if not panggil in nama:
    print('tidak ada nama di list array', panggil)

# bisa untung ngecek string

if 'h' in panggil:
    print('ada hurupnya')

else:
    print('tidak ada hurup yang sama di panggil')
