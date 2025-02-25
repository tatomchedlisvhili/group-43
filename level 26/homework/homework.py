# 2) for ციკლის საშვალებით გამოიტანეთ ლუწი რიცხვები 20-იდან 40-მდე. შეასრულეთ იგივე while ციკლით

for i in range(20,40,2):
    print(i)

m = 20

while m < 40:
    print(m)
    m += 2


# 3) შექმენით 1 ცვლადი, შემდეგ for ციკლის საშვალებით გაიგეთ ყველა რიცხვი 15-მდე და ყველა ეს რიცხვი დაამატეთ პირველად შექმნილ ცვლადში, საბოლოოდ დაბეჭდეთ ჯამი. შეასრულეთ იგივე while ციკლით

sum = 0 

for i in range(0,15):
    sum = sum + i

print(sum)


sum2 = 0
q = 0

while q < 15:
    sum2 = sum2 + q
    q += 1

print(sum2)



# 4) მომხმარებელს შემოატანინეთ 2 რიცხვი, შემდეგ კი ამ ორ რიცხვს შორის არსებული ყველა რიცხვის ჯამი გაიგეთ for ციკლის გამოყენებით უმციერსიდან უდიდესამდე. საბოლოოდ დაბეჭდეთ ეს ჯამი

a = int(input("sheiyvanet ricxvi: "))
b = int(input("sheiyvanet ricxvi: "))
sum3 = 0
for i in range(a,b):
    sum3 = sum3 + i

print(sum3)



# 5) შექმენით პაროლის ცვლადი და შეინახეთ თქვენთვის სასურველი სიტყვა, შემდეგ მომხმარებელს შეეკითხეთ პაროლი და შეინახეთ ცვლადში, იქამდე შეეკითხეთ სანამ სწორად არ ჩაწერს while ციკლით გამოყენებით, საბოლოოდ კი დაუბეჭდეთ "Logged in successsfuly" ასევე ის თუ რამდენი ცდა დასჭირდა, ამისთვის ცალკე ცვლადი შექმენით და ყოველ ციკლის გამეორებაზე გაზარდეთ 1-ით


password = "tato123"
momxmarebeli = input("sheiyvanet paroli: ")
counter = 0

while momxmarebeli != password:
    print("try again")
    momxmarebeli = input("sheiyvanet paroli: ")
    counter +=1

print("done")
print(counter)


    