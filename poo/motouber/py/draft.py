class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def get_nome(self):
        return self.__nome

    def get_dinheiro(self):
        return self.__dinheiro

    def pagar(self, valor: int):
        if valor > self.__dinheiro:
            pago = self.__dinheiro
            self.__dinheiro = 0
            return pago
        else:
            self.__dinheiro -= valor
            return valor

    def receber(self, valor: int):
        self.__dinheiro += valor

    def __str__(self):
        return f"{self.__nome}:{self.__dinheiro}"


class Moto:
    def __init__(self):
        self.__custo = 0
        self.__motorista = None
        self.__passageiro = None

    def set_driver(self, nome: str, dinheiro: int):
        self.__motorista = Pessoa(nome, dinheiro)

    def set_pass(self, nome: str, dinheiro: int):
        self.__passageiro = Pessoa(nome, dinheiro)

    def drive(self, distancia: int):
        if self.__motorista is None or self.__passageiro is None:
            print("fail: missing driver or passenger")
            return
        self.__custo += distancia

    def leave_pass(self):
        if self.__passageiro is None:
            print("fail: no passenger")
            return

        valor_pago = self.__passageiro.pagar(self.__custo)

        if valor_pago < self.__custo:
            print("fail: Passenger does not have enough money")

        print(f"{self.__passageiro.get_nome()}:{self.__passageiro.get_dinheiro()} left")


        self.__motorista.receber(self.__custo)


        self.__passageiro = None
        self.__custo = 0

    def show(self):
        driver_str = str(self.__motorista) if self.__motorista else "None"
        pass_str = str(self.__passageiro) if self.__passageiro else "None"
        print(f"Cost: {self.__custo}, Driver: {driver_str}, Passenger: {pass_str}")


def main():
    moto = Moto()
    while True:
        try:
            line = input()
            parts = line.strip().split()
            if len(parts) == 0:
                continue
            cmd = parts[0]

            print(f"${line}")

            if cmd == "end":
                break
            elif cmd == "show":
                moto.show()
            elif cmd == "setDriver":
                moto.set_driver(parts[1], int(parts[2]))
            elif cmd == "setPass":
                moto.set_pass(parts[1], int(parts[2]))
            elif cmd == "drive":
                moto.drive(int(parts[1]))
            elif cmd == "leavePass":
                moto.leave_pass()
        except EOFError:
            break


if __name__ == "__main__":
    main()