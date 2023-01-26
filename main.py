try:
    number = int(input("lutfen bir sayı giriniz:"))
    print(number)
except ValueError:
    print("sayı girin yazıyo orda ")
    number = int(input("lutfen bir sayı giriniz:"))
    print(number)
