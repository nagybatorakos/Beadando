import string

def felhasznalo(n):
    if "@" in n:
        k=n.find("@")
        fh=n[:k]
        a=string.ascii_letters + string.digits
        if len(fh)>1:
            if (fh[0] in a) and (fh[-1] in a):
                a+="-"+"_"+"."
                for i in range(len(fh)):
                    if (fh[i]=="." and (fh[i+1]=="." or fh[i-1]==".")) or (fh[i] not in a):
                        return False
    return True

def kiszolgalo(n):
    if "@" in n and "." in n:
        k=n.find("@")
        sz=n[:-3].rfind(".")
        ksz=n[k+1:sz]
        a=string.ascii_letters + string.digits
        if len(ksz)>1:
            if (ksz[0] in a) and (ksz[-1] in a):
                a+="-"+"."
                for i in range(len(ksz)):
                    if (ksz[i]=="." and (ksz[i+1]=="." or ksz[i-1]==".")) or (ksz[i] not in a):
                        return False
            return True
    return False

def tld(n):
    if "." in n:
        l=n[:-3].rfind(".")
        t=n[l+1:]
        a=string.ascii_letters+"."
        for i in range(len(t)):
            if (t[i] not in a) or (t[len(t)-1])==".":
                return False
            elif t[i]==".":
                a=string.ascii_letters
        return True
    return False

def email(n):
    if felhasznalo(n) and kiszolgalo(n) and tld(n):
        return "Helyes"
    return "Hibás"

n=input("Adja meg az e-mail címet: ")
while n != "0":
    print(email(n))
    n=input("Adja meg az e-mail címet: ")


