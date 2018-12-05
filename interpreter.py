def isInt(x):
    if (x[0]=='-'):
        if(x[1:].isdigit):
            return True
        else:
            return False
    else:
        return x.isdigit()

def validInt(x,l):
    if(isBound(x,l)):
        return(isInt(value(x,l)))
    return isInt(x)

def validString(x,l):
    if(isBound(x,l)):
        return(isString(value(x,l)))
    return isString(x)

def validBool(x,l):
    if(isBound(x,l)):
        return(isBool(value(x,l)))
    return isBool(x)

def isString(x):
    return (x[0:3]=='str')

def isName(x):
    return (x[0:3]=='nam')

def isBool(x):
    return (x[0:2]==':t' or x[0:2]==':f')

def toBool(x):
    if(x[0:2]==':t'):
        return True
    else:
        return False

def isBound(x,l):
    return (x in l[0])

def value(x,l):
    if(isName(x)):
        if(isBound(x,l)):
            return (l[1][l[0].index(x)])
    return x

def func(inList, outList, bindList, listBindList, letList, funList, cLet, finaloutList, finalbindList, fn, arg, x, boolVal):
    for line in inList:
            print('outList')
            print(outList)
            if(line[0:6]=='return'):
                if(outList[-1][0:7]==':error:'):
                    finaloutList.append(fn)
                    finaloutList.append(arg)
                #if(boolVal):
                    #finalbindList[1][finalbindList[0].index('nam' + str(x) + '\n')] = outList[-1]
                finaloutList.append(value(outList[-1],bindList))
            if len(line)>=2:
                if(line[0:2] == 'or'):
                    if(len(outList)>=2):
                        if(validBool(outList[-1],bindList) and validBool(outList[-1],bindList)):
                            a = value(outList.pop(),bindList)
                            b = value(outList.pop(),bindList)
                            temp = (toBool(a) or  toBool(b))
                            if(temp):
                                outList.append(':true:')
                            else:
                                outList.append(':false:')
                        else:
                            outList.append(':error:')
                    else:
                        outList.append(':error:')

                if(line[0:2] == 'if'):
                    if(len(outList)>=3):
                        if(validBool(outList[-3],bindList)):
                            a = (outList.pop())
                            b = (outList.pop())
                            c = value(outList.pop(),bindList)
                            temp = (toBool(c))
                            if(temp):
                                outList.append(b)
                            else:
                                outList.append(a)
                        else:
                            outList.append(':error:lk')
                    else:
                        outList.append(':error:')

            if len(line)>=3:

                if(line[0:3] == 'pop'):
                    if(len(outList)>0):
                        outList.pop()
                    else:
                        outList.append(':error:')

                if(line[0:3] == 'add'):
                    if(len(outList)>=2):
                        if(validInt(outList[-1],bindList) and validInt(outList[-2],bindList)):
                            temp = str(int(value(outList.pop(),bindList)) + int(value(outList.pop(),bindList)))
                            outList.append(temp)
                        else:
                            outList.append(':error:')
                    else:
                        outList.append(':error:')

                if(line[0:3] == 'sub'):
                    if(len(outList)>=2):
                        if(validInt(outList[-1],bindList) and validInt(outList[-2],bindList)):
                            temp = str(-(int(value(outList.pop(),bindList))) + int(value(outList.pop(),bindList)))
                            outList.append(temp)
                        else:
                            outList.append(':error:')
                    else:
                        outList.append(':error:')

                if(line[0:3] == 'mul'):
                    if(len(outList)>=2):
                        if(validInt(outList[-1],bindList) and validInt(outList[-2],bindList)):
                            temp = str((int(value(outList.pop(),bindList))) * int(value(outList.pop(),bindList)))
                            outList.append(temp)
                        else:
                            outList.append(':error:')
                    else:
                        outList.append(':error:')

                if(line[0:3] == 'div'):
                    if(len(outList)>=2):
                        if(validInt(outList[-1],bindList) and validInt(outList[-2],bindList)):
                            if(int(value(outList[-1],bindList))==0):
                                outList.append(':error:')
                            else:
                                b = (int(value(outList.pop(),bindList)))
                                a = (int(value(outList.pop(),bindList)))
                                temp = str(int(a/b))
                                outList.append(temp)
                        else:
                            outList.append(':error:')
                    else:
                        outList.append(':error:')

                if(line[0:3] == 'rem'):
                    if(len(outList)>=2):
                        if(validInt(outList[-1],bindList) and validInt(outList[-2],bindList)):
                            if(int(value(outList[-1],bindList))==0):
                                outList.append(':error:')
                            else:
                                b = (int(value(outList.pop(),bindList)))
                                a = (int(value(outList.pop(),bindList)))
                                temp = str(int(a%b))
                                outList.append(temp)
                        else:
                            outList.append(':error:')
                    else:
                        outList.append(':error:')

                if(line[0:3] == 'neg'):
                    if(len(outList)>=1):
                        if(validInt(outList[-1],bindList)):
                           temp = str(-(int(value(outList.pop(),bindList))))
                           outList.append(temp)
                        else:
                            outList.append(':error:')
                    else: outList.append(':error:')

                if(line[0:3] == 'cat'):
                    if(len(outList)>=2):
                        if(validString(outList[-1],bindList) and validString(outList[-2],bindList)):
                            a = value(outList.pop(),bindList)
                            b = value(outList.pop(),bindList)
                            temp = 'str' + b[3:] + a[3:]
                            outList.append(temp)
                        else:
                            outList.append(':error:')
                    else:
                        outList.append(':error:')

                if(line[0:3] == 'and'):
                    if(len(outList)>=2):
                        if(validBool(outList[-1],bindList) and validBool(outList[-2],bindList)):
                            a = value(outList.pop(),bindList)
                            b = value(outList.pop(),bindList)
                            temp = (toBool(a) and  toBool(b))
                            if(temp):
                                outList.append(':true:')
                            else:
                                outList.append(':false:')
                        else:
                            outList.append(':error:')
                    else:
                        outList.append(':error:')

                if(line[0:3] == 'not'):
                    if(len(outList)>=1):
                        if(validBool(outList[-1],bindList)):
                            a = value(outList.pop(),bindList)
                            temp = (not (toBool(a)))
                            if(temp):
                                outList.append(':true:')
                            else:
                                outList.append(':false:')
                        else:
                            outList.append(':error:')
                    else:
                        outList.append(':error:')

                if(line[0:3] == 'let'):
                    letList[0].append(list(outList))
                    letList[1].append(list(bindList[0]))
                    letList[2].append(list(bindList[1]))
                    letList[3].append(copy.deepcopy(funList))

                    cLet +=1

                if(line[0:3] == 'end'):
                    cLet -=1
                    letList[0][cLet].append(outList.pop())
                    outList = list(letList[0].pop())
                    bindList[0] = list(letList[1][-1])
                    del letList[1][-1]
                    bindList[1] = list(letList[2][-1])
                    del letList[2][-1]
                    funList = copy.deepcopy(letList[3].pop())

                #if(line[0:3] == 'fun'):



            if len(line)>= 5:
                if(line[0:5] == 'equal'):
                    if(len(outList)>=2):
                        if(validInt(outList[-1],bindList) and validInt(outList[-2],bindList)):
                            temp = (int(value(outList.pop(),bindList)) == int(value(outList.pop(),bindList)))
                            if(temp):
                                outList.append(':true:')
                            else:
                                outList.append(':false:')
                        else:
                            outList.append(':error:')
                    else:
                        outList.append(':error:')


            if len(line)>= 8:
                if(line[0:8] == 'lessThan'):
                    if(len(outList)>=2):
                        if(validInt(outList[-1],bindList) and validInt(outList[-2],bindList)):
                            temp = (int(value(outList.pop(),bindList)) > int(value(outList.pop(),bindList)))
                            if(temp):
                                outList.append(':true:')
                            else:
                                outList.append(':false:')
                        else:
                            outList.append(':error:')
                    else:
                        outList.append(':error:')

            if len(line)>= 4:
                        if(line[0:4] == 'call'):

                            argName = outList[-1]
                            if(argName[0:7]==':error:'):
                                outList.append(':error:\n')
                            else:
                                arg = str(value(outList[-1],bindList))
                                fn = str(value(outList[-2],bindList))[3:-1]
                                print(fn)
                                if(not str(fn) in funList[0]):
                                    outList.append(':error:\n')
                                    print (funList)
                                    print('ERRRRRRRR')
                                else:
                                    outList.pop()
                                    outList.pop()
                                    index = funList[0].index(fn)
                                    x = funList[2][index] 
                                    #print (x)
                                    #print (arg)
                                    counter = 0
                                    tempoutList = []
                                    tempbindList = listBindList[index]
                                    templetList = [[],[],[]]
                                    tempfunList = [[],[[]]]
                                    tempcLet = 0
                                    tempbindList[0].append('nam' + str(x) + '\n')
                                    tempbindList[1].append(arg)
                                    print ('list:')
                                    print (tempbindList)
                                    print (x)
                                    '''for elem in funList[1][index]:
                                        elem = elem.replace(x,arg)
                                        funList[1][index][counter] = elem
                                        counter+=1'''
                                    func(funList[1][index], tempoutList, tempbindList, listBindList, listBindList ,templetList, tempcLet, outList, bindList, fn, arg, argName, funList[3][index]) 
                                    print(funList[3][index])
                                    print(funList[1][index][-1][0:6])
                                    if(funList[3][index]):
                                        #print('YYYYYYYY')
                                        if(str('nam' + (x) + '\n') in tempbindList[0]):
                                            #print('XXXXXXXXXX')
                                            print (argName)
                                            print (tempoutList[-1])
                                            bindList[1][bindList[0].index(argName)] = tempbindList[1][tempbindList[0].index(str('nam' + x + '\n'))]
                                            print (bindList)
                                            print (tempbindList)



            if len(line)>= 4:
                if(line[0:4] == 'bind'):
                    if(len(outList)>=2):
                        if(isName(outList[-2])):
                            if(isName(outList[-1])):
                                if(outList[-1] in bindList[0]):
                                    b = (outList.pop())
                                    a = (outList.pop())
                                    b = bindList[1][bindList[0].index(b)]
                                    if(a in bindList[0]):
                                        bindList[1][bindList[0].index(a)] = b
                                    else:
                                        bindList[0].append(a)
                                        bindList[1].append(b)
                                    outList.append(':unit:')

                                else:
                                    outList.append(':error:')

                            else:
                                b = (outList.pop())
                                a = (outList.pop())
                                if(a in bindList[0]):
                                    bindList[1][bindList[0].index(a)] = b
                                else:
                                    bindList[0].append(a)
                                    bindList[1].append(b)
                                outList.append(':unit:')
                        else:
                            outList.append(':error:')
                    else:
                       outList.append(':error:')

                if(line[0:4] == 'swap'):
                    if(len(outList)>=2):
                        b = (outList.pop())
                        a = (outList.pop())
                        outList.append(b)
                        outList.append(a)
                    else:
                       outList.append(':error:')

                if(line[0:4] == 'push'):
                    if(line[5]=='-'):
                        if(line[6]=='0'):
                            outList.append('0')
                        elif(line[6:-1].isdigit()):
                            if(line[-1:]=='\n'):
                                outList.append(line[5:-1])
                            else:
                                outList.append(line[5:])
                        else:
                            outList.append(':error:')

                    elif(line[5]=='0'):
                            outList.append('0')

                    elif(line[5:-1].isdigit()):
                        if(line[-1:]=='\n'):
                            outList.append(line[5:-1])
                        else:
                            outList.append(line[5:])

                    elif(line[5] == '"'):
                        if (line[6:].find('"')!= -1):
                            if(line[-1:]=='\n'):
                                outList.append('str' + line[6:-2])
                            else:
                                outList.append('str' + line[6:-1])
                        else:
                            outList.append(':error:')


                    elif(line[5:-1]==':true:' or line[5:-1]==':false:'):
                        outList.append(line[5:])


                    elif(line[5].isalpha() and line[5:].isalnum):
                        outList.append('nam' + line[5:])

                    elif(line[5:-1]==':unit:'):
                        outList.append(':unit:')

                    else:
                        outList.append(':error:')

    
#####################################################################################################################################    
def interpreter(input, output):
    import copy
    inFile = open(input)
    outFile = open(output, "w")
    inList = []
    outList = []
    bindList = [[],[]]
    letList = [[],[],[],[]]
    funList = [[],[[]],[],[]]
    listBindList = []
    cLet = 0
    cFun = 0
    cIndex = -1
    fnBindCounter = 0
    iterator = 0
    #checkInFun = False
    
    for line in inFile:
        '''if(line[0:6]=='funEnd'):
            cFun -= 1
            inList.append('push :unit:\n')
            
        elif(line[0:3]=='fun'):
            cFun += 1
            cIndex += 1
            funList[1].append([])
            funList[0].append(line[4:line.replace(' ', '_',1).find(' ')])
            funList[2].append(line[line.replace(' ', '_',1).find(' ')+1:-1])
            funList[3].append(False)
            inList.append('makeCopy\n')
        elif(line[0:8]=='inOutFun'):
            cFun += 1
            cIndex += 1
            funList[1].append([])
            funList[0].append(line[9:line.replace(' ', '_',1).find(' ')])
            funList[2].append(line[line.replace(' ', '_',1).find(' ')+1:-1])
            funList[3].append(True)
            inList.append('makeCopy\n')
        else:   
            if(cFun==0):
               inList.append(line)
            else:
               funList[1][cIndex].append(line)
        iterator+=1
    for line in inList:'''

        if(line[0:6]=='funEnd'):
            cFun -= 1
            outList.append(':unit:')
            #checkInFun = False
            
        elif(line[0:3]=='fun'):
            cFun += 1
            cIndex += 1
            funList[1].append([])
            funList[0].append(line[4:line.replace(' ', '_',1).find(' ')])
            funList[2].append(line[line.replace(' ', '_',1).find(' ')+1:-1])
            funList[3].append(False)
            #inList.append('makeCopy\n')
            temp = copy.deepcopy(bindList)
            listBindList.append(temp)
            #checkInFun = True
            
        elif(line[0:8]=='inOutFun'):
            cFun += 1
            cIndex += 1
            funList[1].append([])
            funList[0].append(line[9:line.replace(' ', '_',1).find(' ')])
            funList[2].append(line[line.replace(' ', '_',1).find(' ')+1:-1])
            funList[3].append(True)
            #inList.append('makeCopy\n')
            temp = copy.deepcopy(bindList)
            listBindList.append(temp)
            #checkInFun = True
        
        
        else:
            if(cFun>0):
                funList[1][cIndex].append(line)
                print('xxxx')
                print(funList)
            else:
                if(line == 'quit' or line == 'quit\n'):
                    outList.reverse()
                    
                    for x in outList:
                        if(x[0:3]=='str' or x[0:3]=='nam'):
                            x = x[3:]
                        if(x[-1:]=='\n'):
                            outFile.write(x)
                            print(x)
                        else:
                            outFile.write(x + '\n')
                            print(x+'\n')
                    break

                else:       
                            
                    if len(line)>=2:
                        if(line[0:2] == 'or'):
                            if(len(outList)>=2):
                                if(validBool(outList[-1],bindList) and validBool(outList[-1],bindList)):
                                    a = value(outList.pop(),bindList)
                                    b = value(outList.pop(),bindList)
                                    temp = (toBool(a) or  toBool(b))
                                    if(temp):
                                        outList.append(':true:')
                                    else:
                                        outList.append(':false:')
                                else:
                                    outList.append(':error:')
                            else:
                                outList.append(':error:')

                        if(line[0:2] == 'if'):
                            if(len(outList)>=3):
                                if(validBool(outList[-3],bindList)):
                                    a = (outList.pop())
                                    b = (outList.pop())
                                    c = value(outList.pop(),bindList)
                                    temp = (toBool(c))
                                    if(temp):
                                        outList.append(b)
                                    else:
                                        outList.append(a)
                                else:
                                    outList.append(':error:lk')
                            else:
                                outList.append(':error:')

                    if len(line)>=3:

                        if(line[0:3] == 'pop'):
                            if(len(outList)>0):
                                outList.pop()
                            else:
                                outList.append(':error:')

                        if(line[0:3] == 'add'):
                            if(len(outList)>=2):
                                if(validInt(outList[-1],bindList) and validInt(outList[-2],bindList)):
                                    temp = str(int(value(outList.pop(),bindList)) + int(value(outList.pop(),bindList)))
                                    outList.append(temp)
                                else:
                                    outList.append(':error:')
                            else:
                                outList.append(':error:')

                        if(line[0:3] == 'sub'):
                            if(len(outList)>=2):
                                if(validInt(outList[-1],bindList) and validInt(outList[-2],bindList)):
                                    temp = str(-(int(value(outList.pop(),bindList))) + int(value(outList.pop(),bindList)))
                                    outList.append(temp)
                                else:
                                    outList.append(':error:')
                            else:
                                outList.append(':error:')

                        if(line[0:3] == 'mul'):
                            if(len(outList)>=2):
                                if(validInt(outList[-1],bindList) and validInt(outList[-2],bindList)):
                                    temp = str((int(value(outList.pop(),bindList))) * int(value(outList.pop(),bindList)))
                                    outList.append(temp)
                                else:
                                    outList.append(':error:')
                            else:
                                outList.append(':error:')

                        if(line[0:3] == 'div'):
                            if(len(outList)>=2):
                                if(validInt(outList[-1],bindList) and validInt(outList[-2],bindList)):
                                    if(int(value(outList[-1],bindList))==0):
                                        outList.append(':error:')
                                    else:
                                        b = (int(value(outList.pop(),bindList)))
                                        a = (int(value(outList.pop(),bindList)))
                                        temp = str(int(a/b))
                                        outList.append(temp)
                                else:
                                    outList.append(':error:')
                            else:
                                outList.append(':error:')

                        if(line[0:3] == 'rem'):
                            if(len(outList)>=2):
                                if(validInt(outList[-1],bindList) and validInt(outList[-2],bindList)):
                                    if(int(value(outList[-1],bindList))==0):
                                        outList.append(':error:')
                                    else:
                                        b = (int(value(outList.pop(),bindList)))
                                        a = (int(value(outList.pop(),bindList)))
                                        temp = str(int(a%b))
                                        outList.append(temp)
                                else:
                                    outList.append(':error:')
                            else:
                                outList.append(':error:')

                        if(line[0:3] == 'neg'):
                            if(len(outList)>=1):
                                if(validInt(outList[-1],bindList)):
                                   temp = str(-(int(value(outList.pop(),bindList))))
                                   outList.append(temp)
                                else:
                                    outList.append(':error:')
                            else: outList.append(':error:')

                        if(line[0:3] == 'cat'):
                            if(len(outList)>=2):
                                if(validString(outList[-1],bindList) and validString(outList[-2],bindList)):
                                    a = value(outList.pop(),bindList)
                                    b = value(outList.pop(),bindList)
                                    temp = 'str' + b[3:] + a[3:]
                                    outList.append(temp)
                                else:
                                    outList.append(':error:')
                            else:
                                outList.append(':error:')

                        if(line[0:3] == 'and'):
                            if(len(outList)>=2):
                                if(validBool(outList[-1],bindList) and validBool(outList[-2],bindList)):
                                    a = value(outList.pop(),bindList)
                                    b = value(outList.pop(),bindList)
                                    temp = (toBool(a) and  toBool(b))
                                    if(temp):
                                        outList.append(':true:')
                                    else:
                                        outList.append(':false:')
                                else:
                                    outList.append(':error:')
                            else:
                                outList.append(':error:')

                        if(line[0:3] == 'not'):
                            if(len(outList)>=1):
                                if(validBool(outList[-1],bindList)):
                                    a = value(outList.pop(),bindList)
                                    temp = (not (toBool(a)))
                                    if(temp):
                                        outList.append(':true:')
                                    else:
                                        outList.append(':false:')
                                else:
                                    outList.append(':error:')
                            else:
                                outList.append(':error:')

                        if(line[0:3] == 'let'):
                            letList[0].append(list(outList))
                            letList[1].append(list(bindList[0]))
                            letList[2].append(list(bindList[1]))
                            letList[3].append(copy.deepcopy(funList))

                            cLet +=1

                        if(line[0:3] == 'end'):
                            cLet -=1
                            letList[0][cLet].append(outList.pop())
                            outList = list(letList[0].pop())
                            bindList[0] = list(letList[1][-1])
                            del letList[1][-1]
                            bindList[1] = list(letList[2][-1])
                            del letList[2][-1]
                            funList = copy.deepcopy(letList[3].pop())
                                           



                    if len(line)>= 5:
                        if(line[0:5] == 'equal'):
                            if(len(outList)>=2):
                                if(validInt(outList[-1],bindList) and validInt(outList[-2],bindList)):
                                    temp = (int(value(outList.pop(),bindList)) == int(value(outList.pop(),bindList)))
                                    if(temp):
                                        outList.append(':true:')
                                    else:
                                        outList.append(':false:')
                                else:
                                    outList.append(':error:')
                            else:
                                outList.append(':error:')


                    if len(line)>= 8:
                        if(line[0:8] == 'lessThan'):
                            if(len(outList)>=2):
                                if(validInt(outList[-1],bindList) and validInt(outList[-2],bindList)):
                                    temp = (int(value(outList.pop(),bindList)) > int(value(outList.pop(),bindList)))
                                    if(temp):
                                        outList.append(':true:')
                                    else:
                                        outList.append(':false:')
                                else:
                                    outList.append(':error:')
                            else:
                                outList.append(':error:')


                    if len(line)>= 4:
                        if(line[0:4] == 'call'):

                            argName = outList[-1]
                            if(argName[0:7]==':error:'):
                                outList.append(':error:\n')
                            else:
                                arg = str(value(outList[-1],bindList))
                                fn = str(value(outList[-2][3:-1],bindList))
                                print(fn)
                                if(not str(fn) in funList[0]):
                                    outList.append(':error:\n')
                                else:
                                    outList.pop()
                                    outList.pop()
                                    index = funList[0].index(fn)
                                    x = funList[2][index] 
                                    #print (x)
                                    #print (arg)
                                    counter = 0
                                    tempoutList = []
                                    tempbindList = listBindList[index]
                                    templetList = [[],[],[]]
                                    tempfunList = [[],[[]],[],[]]
                                    tempcLet = 0
                                    tempbindList[0].append('nam' + str(x) + '\n')
                                    tempbindList[1].append(arg)
                                    print ('list:')
                                    print (tempbindList)
                                    print (x)
                                    '''
                                    for elem in funList[1][index]:
                                        elem = elem.replace(x,temparg)
                                        funList[1][index][counter] = elem
                                        counter+=1
                                    '''
                                    func(funList[1][index], tempoutList, tempbindList, listBindList, templetList, funList, tempcLet, outList, bindList, fn, arg, argName, funList[3][index]) 
                                    print(funList[3][index])
                                    print(funList[1][index][-1][0:6])
                                    if(funList[3][index]):
                                        #print('YYYYYYYY')
                                        if(str('nam' + (x) + '\n') in tempbindList[0]):
                                            #print('XXXXXXXXXX')
                                            print (argName)
                                            print (tempoutList[-1])
                                            bindList[1][bindList[0].index(argName)] = tempbindList[1][tempbindList[0].index(str('nam' + x + '\n'))]
                                            print (bindList)
                                            print (tempbindList)




                        if(line[0:4] == 'bind'):
                            if(len(outList)>=2):
                                if(isName(outList[-2])):
                                    if(isName(outList[-1])):
                                        if(outList[-1] in bindList[0]):
                                            b = (outList.pop())
                                            a = (outList.pop())
                                            b = bindList[1][bindList[0].index(b)]
                                            if(a in bindList[0]):
                                                bindList[1][bindList[0].index(a)] = b
                                            else:
                                                bindList[0].append(a)
                                                bindList[1].append(b)
                                            outList.append(':unit:')

                                        else:
                                            outList.append(':error:')

                                    else:
                                        b = (outList.pop())
                                        a = (outList.pop())
                                        if(a in bindList[0]):
                                            bindList[1][bindList[0].index(a)] = b
                                        else:
                                            bindList[0].append(a)
                                            bindList[1].append(b)
                                        outList.append(':unit:')
                                else:
                                    outList.append(':error:')
                            else:
                               outList.append(':error:')

                        if(line[0:4] == 'swap'):
                            if(len(outList)>=2):
                                b = (outList.pop())
                                a = (outList.pop())
                                outList.append(b)
                                outList.append(a)
                            else:
                               outList.append(':error:')

                        if(line[0:4] == 'push'):
                            if(line[5]=='-'):
                                if(line[6]=='0'):
                                    outList.append('0')
                                elif(line[6:-1].isdigit()):
                                    if(line[-1:]=='\n'):
                                        outList.append(line[5:-1])
                                    else:
                                        outList.append(line[5:])
                                else:
                                    outList.append(':error:')

                            elif(line[5]=='0'):
                                    outList.append('0')

                            elif(line[5:-1].isdigit()):
                                if(line[-1:]=='\n'):
                                    outList.append(line[5:-1])
                                else:
                                    outList.append(line[5:])

                            elif(line[5] == '"'):
                                if (line[6:].find('"')!= -1):
                                    if(line[-1:]=='\n'):
                                        outList.append('str' + line[6:-2])
                                    else:
                                        outList.append('str' + line[6:-1])
                                else:
                                    outList.append(':error:')


                            elif(line[5:-1]==':true:' or line[5:-1]==':false:'):
                                outList.append(line[5:])


                            elif(line[5].isalpha() and line[5:].isalnum):
                                outList.append('nam' + line[5:])

                            elif(line[5:-1]==':unit:'):
                                outList.append(':unit:')

                            else:
                                outList.append(':error:')

                    print('out: ')
                    print (outList)
                    print('bind: ')
                    print (bindList)
                    print('let: ')
                    print (letList)
                    print('fun: ')
                    print (funList)
                    print ('inList: ')
                    print (inList)

                    iterator+=1
        
            #outFile.close()
            #inFile.close()
#################################################################################################################
            
                        
############################################################################################################################################



interpreter("input.txt", "output.txt")
