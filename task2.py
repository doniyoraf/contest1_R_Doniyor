def typeBasedTransformer(**argumentlar):
    ozgartirdim = {}
    
    for kalit, qiymat in argumentlar.items():
        if isinstance(qiymat, bool):
            ozgartirdim[kalit] = not qiymat
        elif isinstance(qiymat, str):
            ozgartirdim[kalit] = qiymat[::-1]
        elif isinstance(qiymat, (int, float)):
            ozgartirdim[kalit] = value ** 2
        elif isinstance(qiymat, (list, tuple)):
            ozgartirdim[kalit] = qiymat[::-1]
        elif isinstance(qiymat, dict) and len(set(qiymat.values())) == len(qiymat.values()):
            ozgartirdim[kalit] = {v: k for k, v in qiymat.items()}
        else:
            ozgartirdim[kalit] = qiymat
            
    return ozgartirdim
