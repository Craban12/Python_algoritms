num_company = int(input("Введите число предприятий:"))
company = {}
sum_com = {}
for i in range(num_company):
    profit = [int(input('Введите по очереди прибыль за кварталы:')) for z in range(4)]
    company.setdefault(f'company{i+1}', profit)
    print(f'company{i+1}')
#print(company['company1'])

sum_year = 0
for com in company.keys():
    sum_num = 0
    for pr in company[com]:
        sum_num += pr
    sum_year += sum_num
    company[com] = sum_num
av_am = sum_year / num_company
print("Средняя за год:", av_am)

for com in company.keys():
    if company[com] < av_am:
        print(f"Прибыль компании {com} меньшее средней за год")
        print(f'Прибыль:{company[com]}')
    elif company[com] > av_am:
        print(f"Прибыль компании {com} больше средней за год")
        print(f'Прибыль:{company[com]}')
    else:
        print(f"Прибыль компании {com} равна средней за год")
        print(f'Прибыль:{company[com]}')
