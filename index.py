listem = ['a','b','c','d','e']
print(type(listem))

word = 'happy'
print(list(word))
print(list('a b c'))

country = ['USA','BRAZIL','UK']
print(country)

text = 'Clarusway'
print(list(text))
print([text])

listem = [1,2,3]
print(len(listem))
print(list(listem))

a= [[1,2,3],['ali','ayse'],[True,False]]
print(len(a))

text="2024's perfect"
print(list(text))
print([text])
#list icine iterebil alir
bos1=[]
print(len(bos1))

numbers= [1,4,7]
numbers.append(9)
print(numbers)
numbers.append('9')
print(numbers)
numbers.append(['a','b','c'])
print(numbers)

listem = ['a','b','c','d']
listem.insert(3,12)

listem = [1,2,3,4,]
listem.insert(4,5)
print(listem)
print(numbers)
numbers.remove(9)
print(numbers)
numbers.remove('9')
print(numbers)
numbers.remove(['a','b','c'])
print(numbers)

listem = [1,2,3,4,2,3,4,3]
listem.remove(2)
print(listem)
listem.pop()
print(listem)
listem.pop(4)
print(listem)
#pop indexe gore remove degere gore siler
listem.clear()
print(listem)

listem = [2,7,3,0,5,7]
listem.sort()
print(listem)

listem.sort(reverse=True)
print(listem)

print(ord('A'))
print(chr(97))
a= ['a',3,'c']
#sort ayni tiptekini siralar yoksa hata

listem = ['veli','ali','ayse','kemal']
print(sorted(listem))
print(listem)
listem = sorted(listem)
print(listem)

listem = ['veli','ali','ayse','kemal']

print(sorted(listem,reverse=True))
#sort kalici degislik yapar sorted kalici degil bu yuzde sorted daha kullanisli

