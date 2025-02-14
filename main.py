import random
from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import decorator_1

print("Vazifa 1 Natijasi:")
print(kwargsAcceptFun(ism="Doniyor", yosh=21, mamlakat="O‘zbekiston"))

print("\nVazifa 2 Natijasi:")
print(typeBasedTransformer(
    son=7, 
    matn="Salom", 
    mantiqiy=True, 
    royxat=[10, 20, 30], 
    lugat={"a": 1, "b": 2}
))


@decorator_1
def funksiya():
    print("Men ishga tayyorman")
    natija = 0
    n = random.randint(10, 751)
    for i in range(n):
        natija += (i**2)


@decorator_1
def boshqa_funksiya(n=2, m=5):
    print("Men jiddiy ish qilishga tayyorman")
    eng_katta = float('-inf')
    n = random.randint(10, 751)
    natijalar = [pow(i, 2) for i in range(n)]
    for qiymat in natijalar:
        if qiymat > eng_katta:
            eng_katta = qiymat


if __name__ == "__main__":
    funksiya()
    boshqa_funksiya()
    funksiya()
    boshqa_funksiya()
    funksiya()
