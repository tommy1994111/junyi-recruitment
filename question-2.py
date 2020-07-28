'''
請寫一個程式，Input 是一個數字，Output 是從 1 到這個數字，扣除掉所有 3 的
倍數以及 5 的倍數，但是需要保留同時是 3 和 5 的倍數的總數字數。
'''

def transformNumberListToString(numberList):
    '''將元素為 int 的 list 轉換成以 `, ` 分隔的字串'''
    return ', '.join([str(num) for num in numberList])

def numberListFilter(inputNumber):
    '''想法: 先列出所有數字，要排除3和5的倍數，但要保留同時是3跟5的倍數(即15的倍數)
            所以如果要在一個迴圈內判斷完的話，要先找出15的倍數，其次找出3或5的倍數
    '''
    allNumberList = list(range(1, inputNumber + 1))
    print('所有的數字是：', transformNumberListToString(allNumberList))

    fifteenMultiple = []
    threeMultiple = []
    fiveMultiple = []
    filterList = []

    for num in allNumberList:
        if (num % 15 == 0):
            fifteenMultiple.append(num)
            filterList.append(num)
        elif (num % 3 == 0):
            threeMultiple.append(num)
        elif (num % 5 == 0):
            fiveMultiple.append(num)
        else:
            filterList.append(num)

    print(f'其中 {transformNumberListToString(threeMultiple)} 被剔除；{transformNumberListToString(fiveMultiple)} 被剔除；但是 {transformNumberListToString(fifteenMultiple)} 被保留')
    print(f'所以剩下來的數字是 {transformNumberListToString(filterList)}，因此')
    return len(filterList)

if __name__ == "__main__":
    try:
        inputNumber = int(input('Input：'))
        if (inputNumber < 1):
            print('Error: 請輸入大於1的正整數')
        else:
            result = numberListFilter(inputNumber)
            print('Output：', result)
    except ValueError:
        print('Error: 請輸入正整數')