

#pangkat ** pow
# sisa %
# bagi /  bagi dengan mencetak nilai bulangan bulat //


# Number
a = 5
b = 3
c = 4.0


# penjumlahan
d = a + b
print("penjumlahan a + b", d)

# String Python
# ada dua cara untung mengasi tanda kutip pada String
# yang pertama dengan \
# yang kedua dengan ""


text = 'gue belajar python'
text1 = 'gue membuat program dengan pthony'
text3 = 'gue mencoba membuat program dengan tanda kutip\'t'
text4 = "gue belajar pda hari jum'at"

# multi line
text5 = """
    gue: lu mau kmana bro?
    dia : Lu siapa sok kenal
    gue : sombong amat!
"""

# raw String
# kasih r pada depan stringnya

text6 = r'c:\thaie'

# print text dengan cepat sama kayak lorem di html
# jumlah text * text print(10*"tahie")
print(10*"Thaie")


# mengambil text yang di ingginkan
text7 = 'cahya mau men game'
a = text7[0]


print(text, text1, text3, text4)


print(text5)

print(text6)

# ingin mengambil string yng sesusai yang di inggin kan
b = text7[0:6]
print(a)
print(b)


# list/Array Python
Data = [1, 4, 9, 16, 24]
Subdata = Data[0]

# menambah list
Data1 = [100, 200, 300, 400, 500, 600]
data2 = Data + Data1

print(data2)


print(Data)
print(Subdata)


# mengcopy data dari list
# fungsi dari titik dua agar tidak merubah datanya
v = Data[:]
v[3] = 199

print(v)


Data.append(Data1)

print(Data)
