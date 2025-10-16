print("Menghitung Konversi Suhu Celsius ke Fahrenheit dan Celsius ke Reamur \n")

celsiusFahrenheit = lambda celsius : (9/5) * celsius + 32
celsiusReamur = lambda celsius : (4/5) * celsius

celsius = float(input("Masukkan Suhu dalam Celsius: "))

print("Hasil Konversi Celsius ke Fahrenheit adalah:", celsiusFahrenheit(celsius))
print("Hasil Konversi Celsius ke Reamur adalah:", celsiusReamur(celsius))