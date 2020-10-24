#正方向搜索，确定搜索区间
def s_dis(f):
    t = 0
    h = 0.1
    a = 2
    judge = True
    if f(t)>f(t+h):#此时正向搜索
        while judge:        
            t0 = t
            t1 = t0+h
            if f(t0)<f(t1):
                try:
                    s = [t_ready,t1]
                except:
                    s = [0,t1]
                judge = False
            else:
                t_ready = t
                t = t1
                h = a*h   
        return s
    else:#反向搜索
        h = -h
        while judge:        
            t0 = t
            t1 = t0+h
            if f(t0)<f(t1):
                try:
                    s = [t_ready,t1]
                except:
                    s = [0,t1]
                judge = False
            else:
                t_ready = t
                t = t1
                h = a*h   
        return [s[1],s[0]]
    
#黄金分割法
def goldcut(t,f):
    a,b = t[0],t[1]
    while abs(b-a)>=0.000001:
        t2 = a + 0.618*(b-a)
        t1 = a + 0.382*(b-a)
        if f(t1)<f(t2):
            b = t2
        else:
            a = t1
    v = (a+b)/2
    return v