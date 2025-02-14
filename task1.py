def kwargsAcceptFun(**argumentlar):
    for kalit, qiymat in argumentlar.items():
        print(f"{qiymat} == {kalit}")
    return argumentlar
