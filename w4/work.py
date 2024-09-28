a = input('어서옵쇼~ 어떤 과일을 찾으세요? ')
fruits = {
    '사과' : 1000,
    '바나나' : 2000,
    '딸기' : 3000,
    '포도' : 4000
}
if a in fruits:
    print(f'아! {a}는 {fruits[a]}원입죠~ ')
else:
    print(f'아이고 {a}는 매장에 없네요.')