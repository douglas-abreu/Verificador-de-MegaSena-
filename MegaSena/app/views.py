"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .forms import megaForm
import pandas as pd
from .module import getIndex, getValues

def home(request):
    """Home page

    Home page for number verification
    """

    context={
                'title':'Home Page',
                'year':datetime.now().year,
             }
    return render(
        request, 'app/index.html', context)

def result(request, num1, num2, num3, num4, num5, num6):
    """Result page

    Page to show results to the user
    """

    dataMega= pd.read_csv('app/megasena.csv', encoding='UTF-8');
    column1= dataMega.Coluna_1
    column2= dataMega.Coluna_2
    column3= dataMega.Coluna_3
    column4= dataMega.Coluna_4
    column5= dataMega.Coluna_5
    column6= dataMega.Coluna_6

    indexColumn1= getIndex(column1, num1, num2, num3, num4, num5, num6)
    indexColumn2= getIndex(column2, num1, num2, num3, num4, num5, num6)
    indexColumn3= getIndex(column3, num1, num2, num3, num4, num5, num6)
    indexColumn4= getIndex(column4, num1, num2, num3, num4, num5, num6)
    indexColumn5= getIndex(column5, num1, num2, num3, num4, num5, num6)
    indexColumn6= getIndex(column6, num1, num2, num3, num4, num5, num6)

    allGames=[]
    for index1 in indexColumn1:
        for index2 in indexColumn2:
            if index1 == index2:
                allGames.append(index1)                                
                                
    for index1 in indexColumn1:
        for index3 in indexColumn3:
            if index1 == index3:
                allGames.append(index1)

    for index1 in indexColumn1:
        for index4 in indexColumn4:
            if index1 == index4:
                allGames.append(index1)

    for index1 in indexColumn1:
        for index5 in indexColumn5:
            if index1 == index5:
                allGames.append(index1)

    for index1 in indexColumn1:
        for index6 in indexColumn6:
            if index1 == index6:
                allGames.append(index1)

    # ===========================                             
                                
    for index1 in indexColumn2:
        for index3 in indexColumn3:
            if index1 == index3:
                allGames.append(index1)

    for index1 in indexColumn2:
        for index4 in indexColumn4:
            if index1 == index4:
                allGames.append(index1)

    for index1 in indexColumn2:
        for index5 in indexColumn5:
            if index1 == index5:
                allGames.append(index1)

    for index1 in indexColumn2:
        for index6 in indexColumn6:
            if index1 == index6:
                allGames.append(index1)

# ===========================                             

    for index1 in indexColumn3:
        for index4 in indexColumn4:
            if index1 == index4:
                allGames.append(index1)

    for index1 in indexColumn3:
        for index5 in indexColumn5:
            if index1 == index5:
                allGames.append(index1)

    for index1 in indexColumn3:
        for index6 in indexColumn6:
            if index1 == index6:
                allGames.append(index1)                    
# ===========================                             

    for index1 in indexColumn4:
        for index5 in indexColumn5:
            if index1 == index5:
                allGames.append(index1)

    for index1 in indexColumn4:
        for index6 in indexColumn6:
            if index1 == index6:
                allGames.append(index1)                    
# ===========================                             

    for index1 in indexColumn5:
        for index6 in indexColumn6:
            if index1 == index6:
                allGames.append(index1) 
    
    apresentation=[]
    for line in allGames:
        apresentation.append([dataMega.loc[[line]].Coluna_1,
                              dataMega.loc[[line]].Coluna_2,
                              dataMega.loc[[line]].Coluna_3,
                              dataMega.loc[[line]].Coluna_4,
                              dataMega.loc[[line]].Coluna_5,
                              dataMega.loc[[line]].Coluna_6])
        
    userNumbers=[num1, num2, num3, num4, num5, num6]
    
    acertos = 0
    listGameFour = []
    listGameFive = []
    listGameSix = []

    for listIndexResults in apresentation:
        acertos=0
        for numbers in userNumbers:
            if(int(listIndexResults[0].to_list()[0]) == int(numbers) or
               int(listIndexResults[1].to_list()[0]) == int(numbers) or
               int(listIndexResults[2].to_list()[0]) == int(numbers) or
               int(listIndexResults[3].to_list()[0]) == int(numbers) or
               int(listIndexResults[4].to_list()[0]) == int(numbers) or
               int(listIndexResults[5].to_list()[0]) == int(numbers)):
                    acertos = acertos + 1
                    if(acertos==4):
                        if not listIndexResults[0].index.to_list()[0] in listGameFour:
                            listGameFour.append(listIndexResults[0].index.to_list()[0])
                    elif(acertos==5):
                        if not listIndexResults[0].index.to_list()[0] in listGameFive:
                            listGameFive.append(listIndexResults[0].index.to_list()[0]) 
                    elif(acertos==6):
                        if not listIndexResults[0].index.to_list()[0] in listGameSix:
                            listGameSix.append(listIndexResults[0].index.to_list()[0]) 
                    else:
                        print('Errou tudo')

    listResultsGameFour= getValues(listGameFour, dataMega)
    listResultsGameFive= getValues(listGameFive, dataMega)
    listResultsGameSix= getValues(listGameSix, dataMega)
        
    
    context={'listGameFour':listResultsGameFour,
             'listGameFive':listResultsGameFive,
             'listGameSix':listResultsGameSix
             }

    return render(
        request, 'app/result.html', context)
