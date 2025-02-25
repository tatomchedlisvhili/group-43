# 1) შექმენით ერთი ცვლადი რომელშიც შეინახავთ 0-ს, შემდეგ გამოიყენეთ while ციკლი და დაბეჭდეთ ეს რიცხვი სანამ ის 10-ზე ნაკლებია, თითოეულ ჯერზე რიცხვი გაზარდეთ 1-ით

i = 0

while i < 10:
    print(i)
    i += 1


# 2) ახსენით რა არის while ციკლი, როგორ ვქმნით (ჩამოწერეთ while ციკლის შექმნის ნაბიჯიები), რისთვის შექიძლება გამოვიყენოთ, ახსენით რა არის counter ცვლადი და რომელია ასეთი თქვენს დაწერილ კოდში

# while aris cikli romelic iqamde gameordeba sanam piroba ar shesruldeba
# vqmnit cvlads, shemdeg vwert while loops da pirobas da shemdeg shigtavss
# counter cvladi itvlis iteraciebis raodenobas




# 3) მომხმარებელს შეეკითხეთ სახელი და იქამდე არ შეეშვათ (განმეორებითად ჰკითხეთ) სანამ თქვენს სახელს არ შემოიყვანს
m = input("sheiyvanet saxeli: ")

while m != "tato":
  print("try again")
  m = input("sheiyvanet saxeli: ")

print("done")

