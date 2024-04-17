import pykakasi
text = input()
kks = pykakasi.kakasi()

result = kks.convert(text)
print(result[0]["hepburn"])
