# menggunakan rekursif
def hitung_pangkat(bilangan, pangkat):
  if pangkat > 1:
    return bilangan * hitung_pangkat(bilangan, pangkat - 1)
  return bilangan

print(hitung_pangkat(3, 2))