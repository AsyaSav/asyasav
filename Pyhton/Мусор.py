def Add(Materialslist,Predmetslist):
	litlelistpredmetov=[]
	Мateriya=input('Введите материал, который хотите добавить')
	if Materialslist.count(Мateriya)<1:
		Materialslist.append(Мateriya)		
		KolvoPredmetov= int(input('Введите количество добавляемых предметов. Только целое число!'))
		for i in range (1, KolvoPredmetov+1):
			predmet=input('Введите предмет, который хотите добавить')
			litlelistpredmetov.append(predmet)
		Predmetslist.append(litlelistpredmetov)
	else:
		numberlistPredmets=Materialslist.index(Мateriya)
		KolvoPredmetov= int(input('Введите количество добавляемых предметов. Только целое число!'))
		for i in range (1, KolvoPredmetov+1):
			predmet=input('Введите предмет, который хотите добавить ')
			litlelistpredmetov.append(predmet)
		Predmetslist[numberlistPredmets].extend(litlelistpredmetov)
def deletematerial(Materialslist,Predmetslist,choice):
	for i in range (0,len(Materialslist)):
		if Materialslist[i]==choice:
			Materialslist.pop(i)
			Predmetslist.pop(i)
Materials=['Дерево', 'Пластик', 'Железо']
Object=[['бумага', 'шкаф'], ['коробка', 'ручка', 'линейка'], ['банка', 'цепь']]
choice=input('Хотите добавить материал или предмет? >>да >>нет  ')
if choice=='да':
	Add(Materials,Object)
choice=input('Хотите удалить материал? >>да >>нет  ')
if choice=='да':
	choice=('Какой материал хотите удалить? ')	
	if Materials.count(choice)>0:
		deletematerial(Materials,Object,choice)
	else: 
		choice=('Такого материала нет, хотите добавить? >>да >>нет ')
		if choice=='да':
			Add(Materials,Object)
for i in range(0,len(Materials)):
	Object[i].sort()
	print(Materials[i],' - ',Object[i])
