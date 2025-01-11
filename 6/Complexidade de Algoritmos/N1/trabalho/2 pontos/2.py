def bt(self, m, o, d, a, v, c):
    if d == a:
        return True
    else:
        if not a in v:
            v.append(a)
            l = m.getVizinhos(a)
            for i in l:
                x = self.bt(m,o,d,i,v,c)
                if x:
                    c.append(i)
                    return x
    return False

def busca(self, m, o, d):
    v = list()
    c = list()
    if self.bt(m, o, d, o, v, c):
        print("\nEncontrei: \n")
        c.append(o)
        self.caminho(c)
    else:
        print("Não encontrei o caminho. ")

def caminho(self, c):
    if len(c)>0:
        l = c.pop()
        print(l.getNome())
        self.caminho(c)
