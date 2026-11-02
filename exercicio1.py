dias = int(input("Digite sua idade em dias: "))

anos = dias // 365
resto = dias % 365

meses = resto // 30
dias_restantes = resto % 30

print("\nSua idade é:")
print(f"{anos} anos, {meses} meses e {dias_restantes} dias.")
