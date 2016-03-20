def savetxt(fname, s=""):
    with open(fname,"w") as f:
        f.write(s);
def readtxt(fname):
    with open(fname,"r") as f:
        s = f.read();
    return s;
def take(d,l):
    return {i:d[i] for i in l};
