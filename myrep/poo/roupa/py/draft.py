class Roupa:
    def __init__(self):
        self.__tamanho: str = ""
    
    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, tamanho: str):
        if tamanho != "PP" \
            and tamanho != "P" \
            and tamanho != "M" \
            and tamanho != "G" \
            and tamanho != "GG" \
            and tamanho != "XG":
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return
        
        self.__tamanho = tamanho

    def __str__(self) -> str:
        return f"size: ({self.getTamanho()})"

roupa = Roupa()

while True:
    command = input()
    print("$" + command)
    args = command.split()

    if args[0] == "end":
        break
    elif args[0] == "show":
        print(roupa)
    elif args[0] == "size":
        