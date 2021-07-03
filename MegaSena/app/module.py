def getIndex(column, n1, n2, n3, n4, n5, n6):
    resultColumn=[]
    for index, value in enumerate(column):
        if  (str(value) == n1 or
            str(value) == n2 or
            str(value) == n3 or 
            str(value) == n4 or
            str(value) == n5 or
            str(value) == n6):
            resultColumn.append(index)
    return resultColumn

def getValues(list, dataMega):
    listResults=[]
    for i in list:
        listResults.append([dataMega.iloc[[i]].Concurso.to_list()[0],
                            dataMega.iloc[[i]].Data_do_sorteio.to_list()[0],
                            dataMega.iloc[[i]].Coluna_1.to_list()[0],
                            dataMega.iloc[[i]].Coluna_2.to_list()[0],
                            dataMega.iloc[[i]].Coluna_3.to_list()[0],
                            dataMega.iloc[[i]].Coluna_4.to_list()[0],
                            dataMega.iloc[[i]].Coluna_5.to_list()[0],
                            dataMega.iloc[[i]].Coluna_6.to_list()[0]])

    return listResults