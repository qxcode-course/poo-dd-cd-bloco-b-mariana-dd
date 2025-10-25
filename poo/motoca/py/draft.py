class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def getName(self):
        return self.__nome

    def getAge(self):
        return self.__idade

    def __str__(self):
        return f"{self.__nome}:{self.__idade}"


class Moto:
    def __init__(self, potencia: int = 1):
        self.potencia = potencia
        self.tempo = 0
        self.pessoa = None

    def enter(self, pessoa: Pessoa):
        if self.pessoa is not None:
            print("fail: busy motorcycle")
            return
        self.pessoa = pessoa

    def leave(self):
        if self.pessoa is None:
            print("fail: empty motorcycle")
            return
        print(self.pessoa)
        self.pessoa = None

    def buy(self, tempo: int):
        self.tempo += tempo

    def drive(self, tempo: int):
        if self.tempo == 0:
            print("fail: buy time first")
            return
        if self.pessoa is None:
            print("fail: empty motorcycle")
            return
        if self.pessoa.getAge() > 10:
            print("fail: too old to drive")
            return
        if tempo > self.tempo:
            print(f"fail: time finished after {self.tempo} minutes")
            self.tempo = 0
        else:
            self.tempo -= tempo

    def honk(self):
        print("P" + "e" * self.potencia + "m")

    def __str__(self):
        pessoa_str = "(empty)" if self.pessoa is None else f"({self.pessoa})"
        return f"power:{self.potencia}, time:{self.tempo}, person:{pessoa_str}"


def main():
    moto = Moto()
    while True:
        try:
            line = input().strip()
            if not line:
                continue
            print(f"${line}")
            parts = line.split()
            cmd = parts[0]

            if cmd == "end":
                break
            elif cmd == "init":
                moto = Moto(int(parts[1]) if len(parts) > 1 else 1)
            elif cmd == "show":
                print(moto)
            elif cmd == "enter":
                moto.enter(Pessoa(parts[1], int(parts[2])))
            elif cmd == "leave":
                moto.leave()
            elif cmd == "buy":
                moto.buy(int(parts[1]))
            elif cmd == "drive":
                moto.drive(int(parts[1]))
            elif cmd == "honk":
                moto.honk()
        except EOFError:
            break


if __name__ == "__main__":
    main()