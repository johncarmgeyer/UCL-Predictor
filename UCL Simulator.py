# Based on data from FiveThirtyEight 
import random as rnd

A = {'Atletico':[81,47,22,10,5], 'Dortmund':[57,21,8,3,1], 'Brugge':[36,10,3,1, 1], 'Monaco':[27, 7, 2, 1, 1]}; a = A.keys()
B = {'Barcelona':[87,66,45,28,15], 'Tottenham':[58,32,16,7,3], 'Inter':[37,17,7,3,1], 'PSV':[18,6,2,1,1]}; b = B.keys()
C = {'Liverpool':[77,51,30,16,8], 'PSG':[69,41,23,11,6], 'Napoli':[45,22,9,4,2], 'Red Star':[9,2,1,1,1]}; c = C.keys()
D = {'Porto':[70,27,9,3,1], 'Schalke':[55,16,4,1,1], 'Galatasaray':[52,15,4,1,1], 'Lokomotiv':[24,4,1,1,1]}; d = D.keys()
E = {'Bayern':[91,66,43,26,14], 'Ajax':[46,18,7,3,1], 'Benfica':[44,16,5,2,1], 'AEK Athens':[19,4,1,1,1]}; e = E.keys()
F = {'Man City':[91,66,42,25,13], 'Lyon':[42,15,5,2,1], 'Shakhtar':[39,13,5,2,1], 'Hoffenheim':[28,9,2,1,1]}; f = F.keys()
G = {'Real Madrid':[94,68,44,26,14], 'Roma':[62,25,9,3,1], 'CSKA':[33,9,3,1,1], 'Viktoria Plzen':[12,2,1,1,1]}; g = G.keys()
H = {'Juventus':[78,50,28,15,7], 'Man United':[50,23,10,4,2], 'Valencia':[43,19,7,2,1], 'Young Boys':[30,11,3,1,1]}; h = H.keys()
groups = [A, B, C, D, E, F, G, H]
teams = [a, b, c, d, e, f, g, h]
stages = {'group':  0  , '16':  1  , 'quarters':  2  , 'semis':  3  , 'final':  4  }

A1 = {'Atletico':[81,47,22,10,5], 'Dortmund':[57,21,8,3,1], 'Brugge':[36,10,3,1, 1], 'Monaco':[27, 7, 2, 1, 1]}
B1 = {'Barcelona':[87,66,45,28,15], 'Tottenham':[58,32,16,7,3], 'Inter':[37,17,7,3,1], 'PSV':[18,6,2,1,1]}
C1 = {'Liverpool':[77,51,30,16,8], 'PSG':[69,41,23,11,6], 'Napoli':[45,22,9,4,2], 'Red Star':[9,2,1,1,1]}
D1 = {'Porto':[70,27,9,3,1], 'Schalke':[55,16,4,1,1], 'Galatasaray':[52,15,4,1,1], 'Lokomotiv':[24,4,1,1,1]}
E1 = {'Bayern':[91,66,43,26,14], 'Ajax':[46,18,7,3,1], 'Benfica':[44,16,5,2,1], 'AEK Athens':[19,4,1,1,1]}
F1 = {'Man City':[91,66,42,25,13], 'Lyon':[42,15,5,2,1], 'Shakhtar':[39,13,5,2,1], 'Hoffenheim':[28,9,2,1,1]}
G1 = {'Real Madrid':[94,68,44,26,14], 'Roma':[62,25,9,3,1], 'CSKA':[33,9,3,1,1], 'Viktoria Plzen':[12,2,1,1,1]}
H1 = {'Juventus':[78,50,28,15,7], 'Man United':[50,23,10,4,2], 'Valencia':[43,19,7,2,1], 'Young Boys':[30,11,3,1,1]}
groups1 = [A1, B1, C1, D1, E1, F1, G1, H1]

def findTeam(t):
    c = 0
    for i in teams:
        for j in i:
            if(t == j):
                return groups[c][j]
        c+=1
    raise Exception('Team not found.')

# draw chance is the lowest ranked team's pct
def h2h(t1, t2, stage):
    i = findTeam(t1); ii = findTeam(t2)
    s = [i, ii]; s1 = [t1, t2]
    p = []
    for i in range(0, 2):
        for j in range(0, s[i][stage]):
            p.append(s1[i])
    for i in range(0, min(s)[stage]):
        p.append('Draw')
    w = p[rnd.randint(0, len(p)-1)]
    return w

def group():
    table = groups1
    for i in range(0, 8):
        for j in range(0, 4):
            table[i][teams[i][j]] = 0
    c = 0
    for i in teams:
        for j in range(1, 4):
            m = h2h(i[0], i[j], 0)
            if(m == 'Draw'): 
                table[c][i[0]]+=1
                table[c][i[j]]+=1
            else:
                table[c][m] += 3
        for j in range(2, 4):
            m = h2h(i[1], i[j], 0)
            if(m == 'Draw'): 
                table[c][i[1]]+=1
                table[c][i[j]]+=1
            else:
                table[c][m] += 3
        m = h2h(i[2], i[3], 0)
        if(m == 'Draw'): 
            table[c][i[2]]+=1
            table[c][i[3]]+=1
        else:
            table[c][m] += 3
        for j in range(1, 4):
            m = h2h(i[0], i[j], 0)
            if(m == 'Draw'): 
                table[c][i[0]]+=1
                table[c][i[j]]+=1
            else:
                table[c][m] += 3
        for j in range(2, 4):
            m = h2h(i[1], i[j], 0)
            if(m == 'Draw'): 
                table[c][i[1]]+=1
                table[c][i[j]]+=1
            else:
                table[c][m] += 3
        m = h2h(i[2], i[3], 0)
        if(m == 'Draw'): 
            table[c][i[2]]+=1
            table[c][i[3]]+=1
        else:
            table[c][m] += 3      
        c+=1
        first = []
        second = []
    c1 = 0
    ls = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    print '\n-------------- GROUP STAGE --------------'
    for i in table:
        s = [(k, i[k]) for k in sorted(i, key=i.get, reverse=True)]
        first.append(s[0][0])
        second.append(s[1][0])
        print '\n                Group '+ls[c1]
        c1+=1
        c = 1
        for i in s:
            print str(c)+'.   '+str(i[0])+',  '+str(i[1])+' pts.'
            c+=1
    return first, second
    
def knockout():
    g = group()
    f = g[0]
    s = g[1]
    # haven't included same-nation r16 rule yet, fuck it
    ms = []
    ns = range(0, 8)
    print '\n-------------- ROUND OF 16 --------------\n'
    for i in f:
        r = rnd.randint(0, 8)
        while r not in ns:
            r = rnd.randint(0, 8)
        h = h2h(i, s[r], 1)
        while h is 'Draw':
            h = h2h(i, s[r], 1)
        print i + ' v ' + s[r]+' -----> ' + h
        ms.append(h)
        ns.pop(ns.index(r))
    ls = []
    for i in f+s:
        if i not in ms:
            ls.append(i)
    print '\n-------------- QUARTERFINALS --------------\n'
    qs = []
    for i in range(0, 4):
        h = h2h(ms[i], ms[i+4], 2)
        while h is 'Draw':
            h = h2h(ms[i], ms[i+4], 2)
        print ms[i] + ' v ' + ms[i+4]+' -----> ' + h  
        qs.append(h)
    print '\n-------------- SEMIFINALS --------------\n' 
    ss = []
    for i in range(0, 2):
        h = h2h(qs[i], qs[i+2], 3)
        while h is 'Draw':
            h = h2h(qs[i], qs[i+2], 3)
        print qs[i] + ' v ' + qs[i+2]+' -----> ' + h  
        ss.append(h)
    
    print '\n-------------- FINAL --------------\n' 
    h = h2h(ss[0], ss[1], 4)
    while h is 'Draw':
        h = h2h(ss[0], ss[1], 4)
    print ss[0] + ' v ' + ss[1]+' -----> ' + h +' win the Champions League!' 
knockout()