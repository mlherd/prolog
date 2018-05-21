from pyswip import Prolog
prolog = Prolog()
prolog.consult("db.pl")

q = list(prolog.query('father(michael,X)'))
	
print q
for i in q:
    for key, value in i.iteritems():
		print value