alpha='abcdefghijklmnopqrstuvwxyz'
n='dev'

n1=''
i=0
n1=n1+(alpha[(((alpha.index(n[i]))+1)%26)])
n1=n1+(alpha[(((alpha.index(n[i+1]))+1)%26)])
n1=n1+(alpha[(((alpha.index(n[i+2]))+1)%26)])
print(n1)                       