word=input('Enter a word: ')
w=word.split()
w=word.lower()
wf={}
for i in w:
    if i not in wf:
        wf[i]=1
    else:
        wf[i]+=1
print("word frequencies: ",wf)