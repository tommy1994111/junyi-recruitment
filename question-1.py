# (A) 請寫一個程式把裡面的字串反過來。
# (B) 請寫一個程式把裡面的字串，每個單字本身做反轉，但是單字的順序不變。

def f(string):
    '''想法：先將整串字串反轉後，以空格分隔後再反轉順序'''
    return ' '.join(string[::-1].split(' ')[::-1])

if __name__ == "__main__":
    print('''f("junyiacademy") == "ymedacaiynuj":''', f("junyiacademy") == "ymedacaiynuj")
    print('''f("flipped class room is important") == "deppilf ssalc moor si tnatropmi":''', f("flipped class room is important") == "deppilf ssalc moor si tnatropmi")