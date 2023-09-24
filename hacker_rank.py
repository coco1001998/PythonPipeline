

def hackerRank():
    newStr=""
    if n <= 150 and n >=1:
        for  i in range(1,n+1) :
            newStr=newStr+str(i)

    return newStr    
    
if __name__ == '__main__':
    n = int(input())
    print(hackerRank())