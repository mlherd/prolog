from pyswip import Prolog
prolog = Prolog()
prolog.consult("db.pl")

print list(prolog.query('father(michael,X)'))
names = list(prolog.query("father(michael,X)"))

for i in range (0, len(names)):
	print str(i+1) + str(names[i])
	
for i in prolog.query("father(X,Y)"):
    print(i["X"], "is the father of", i["Y"])
