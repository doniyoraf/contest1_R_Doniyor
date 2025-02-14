def typeBasedTransformer(**kwargs):
    ozgargan = {}
    
    for kalit, qiymat in kwargs.items():
        if isinstance(qiymat, bool):
            transformed[kalit] = not qiymat
        elif isinstance(qiymat, str):
            transformed[kalit] = qiymat[::-1]
        elif isinstance(qiymat, (int, float)):
            transformed[kalit] = value ** 2
        elif isinstance(qiymat, (list, tuple)):
            transformed[kalit] = qiymat[::-1]
        elif isinstance(qiymat, dict) and len(set(qiymat.values())) == len(qiymat.values()):
            ozgargan[kalit] = {v: k for k, v in qiymat.items()}
        else:
            ozgargan[kalit] = qiymat
            
    return ozgargan
