def Appmove_sort(liste):
	new_list = []
	for i in range(len(liste)):
		Min = min(liste)
		new_list.append(Min)
		liste.remove(Min)
	return new_list



liste = [19,44,65,26,54,22,59,11,3,323,77,854,23,2123,5,767,997,11]

print("Unsorted list {}".format(liste))
print("sorted list {}\t".format(Appmove_sort(liste)))
