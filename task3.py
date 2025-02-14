import time

def decorator_1(funks):
    def doniyor(*argumentlar, **kalit_argumentlar):
        boshlanish_vaqti = time.time()
        natija = funks(*argumentlar, **kalit_argumentlar)
        tugash_vaqti = time.time()
        print(f"{func.__name__} call executed in {tugash_vaqti - boshlanish_vaqti:.6f} sec")
        return natija
    return doniyor
