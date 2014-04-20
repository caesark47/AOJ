def keta_sum(n):
    a = int(n*0.001)
    b = int(n*0.01) % 10
    c = int(n*0.1) % 10
    d = n % 10
    return a+b+c+d
 
while 2>1:
    try:
        n_try = int(raw_input())
        count = 0
        for n in range(10000):
            if n_try == keta_sum(n):
                count += 1
        print count
    except EOFError:
        break
    except ValueError:
        break

#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0008&lang=jp
