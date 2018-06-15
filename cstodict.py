def cstodict(cs):
    d={}
    for i in cs.split(";"):
     k,v=i.split("=")
     d[k]=v
    return d
cs="a=b;c=d;e=f;g=j"
print (cstodict(cs))
