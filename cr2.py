#первый код
with open('iii.txt', 'r+') as f:
    f.seek(0)
    symbols = f.read
    print(symbols)
      
    
    
#второй код    
s = 'самое длинное слово'.split()
n = list(map(lambda e: len(e),s))
for i in range(len(n)):
    if len(s[i]) == max(n):
        print('самое длинное')
    
    
    
    
    
    
