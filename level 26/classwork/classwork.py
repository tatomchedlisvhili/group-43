# 1) ჯერ for ციკლის საშვალებით გამოიტანეთ რიცხვები 5-იდან 15-მდე. შემდეგ კი while ციკლით, კომენატრებით ახსენით რა განსხვავებაა ამ 2 ციკლს შორის და რომელი ჯობია ამ კონკრეტულ შემთხვევაში
# rodesac vicit ricxvebis raodenoba umjobesia for ciklis gamoyeneba da roca arvici while ciklis, am shemtxvevashi for cikli jobia

# 2) შექმენით პროგრამა, რომელშიც მომხმარებელს შემოატანინებთ ქულას, შემდეგ კი if განხადების საშვალებით გამოუტანთ 2 შესაძლო შედეგს: "You have passed" ან "You failed"



for i in range(5,15):
    print(i)

m = 5

while m < 15:
    print(m)
    m += 1



a = int(input("sheiyvanet qula: "))

if a < 50:
    print("you failed")

else:
    print("you have passed")


