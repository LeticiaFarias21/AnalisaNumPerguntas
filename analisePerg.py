# funcina de jan ate dez, independe do ano
# analizaPerg(arquivo txt, nome1, nome2)
# nome do aruivo em Str assim, ele deve esta no msm diretorio do Script
# nome da pesssoas deve ser de acordo com o nome delas no arquivo de txt
# usa como base conversa exportada do wpp
# não funciona p/ grupos.

def analisePerg(nomeArquivo, nome1, nome2):
    
    conversa = open(nomeArquivo, encoding="utf8" )

    perguntas = []
    perguntasNome1 = []
    perguntasNome2 = []

    PerguntasPorMes = [12]

    DIAS = 213

    for mgs in conversa:
        for letra in mgs:
            if letra == '?' :
                perguntas.append(mgs)
                break
                
    for mgs in perguntas:

        texto = mgs.split(" ")
        
        for p in texto:
            if p == nome2:
                perguntasNome2.append(mgs)
                break
            if p == nome1:
                perguntasNome1.append(mgs)
                break

    # Separar por quem fez a pergunta
    #Por mes
    #analisar a data e separar o texto
    #Parametro 1 ate 12

    jan, fev, mar, abr, mai, jun, jul, ago, setm, out, nov, dez = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    for msg in perguntasNome2:
        texto = msg.split("/")

        if texto[1] == "01":
            jan += 1
        elif texto[1] == "02":
            fev += 1
        elif texto[1] == "03":
            mar += 1
        elif texto[1] == "04":
            abr += 1
        elif texto[1] == "05":
            mai += 1
        elif texto[1] == "06":
            jun += 1
        elif texto[1] == "07":
            jul += 1
        elif texto[1] == "08":
            ago += 1
        elif texto[1] == "09":
            setm += 1
        elif texto[1] == "10":
            out += 1
        elif texto[1] == "11":
            nov += 1
        elif texto[1] == "12":
            dez += 1
         

    perguntasPorMesNome2 = [ jan, fev, mar, abr, mai, jun, jul, ago, setm, out, nov, dez]    

    ljan, lfev, lmar, labr, lmai, ljun, ljul, lago, lset, lout, lnov, ldez = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    for msg in perguntasNome1:
        
        texto = msg.split("/")

        if texto[1] == "01":
            ljan += 1
        elif texto[1] == "02":
            lfev += 1
        elif texto[1] == "03":
            lmar += 1
        elif texto[1] == "04":
            labr += 1
        elif texto[1] == "05":
            lmai += 1
        elif texto[1] == "06":
            ljun += 1
        elif texto[1] == "07":
            ljul += 1
        elif texto[1] == "08":
            lago +=1
        elif texto[1] == "09":
            lsetm += 1
        elif texto[1] == "10":
            lout += 1
        elif texto[1] == "11":
            lnov += 1
        elif texto[1] == "12":
            ldez += 1

    perguntasPorMesNome1 = [ljan, lfev, lmar, labr, lmai, ljun, ljul, lago, lset, lout, lnov, ldez]

    print("Numero total de perguntas = ", len(perguntas))
    print("Numero total de ", nome2, " = ", len(perguntasNome2))
    print("Numero por dia de", nome2, "= ", len(perguntasNome2) / DIAS)
    print("Numero por mes de", nome2 ,"= ", perguntasPorMesNome2)
    print("Numero total de ", nome1, " = ", len(perguntasNome1))
    print("Numero por dia de ", nome1,"  = ", len(perguntasNome1) / DIAS)
    print("Numero por mes de ", nome1," = ", perguntasPorMesNome1)
