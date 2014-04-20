while 2>1:
	try:
		a,b,c,d,e,f = map(float, raw_input().split(" "))
		x=(c*e-b*f)/(e*a-b*d)
		y=(c*d-a*f)/(b*d-e*a)
		print "%.3f %.3f" % (x+0,y+0)#+0 for minus zero!
	except EOFError:
		break
	except ValueError:
		break

#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0004&lang=jp
#ax + by = c(1)
#dx + ey = f(2)
#x=(ce-bf)/(ea-bd)
#sy=(cd-af)/(bd-ea)
