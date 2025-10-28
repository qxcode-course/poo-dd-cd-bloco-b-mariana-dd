class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def get_carga(self):
        return self.__carga

    def get_capacidade(self):
        return self.__capacidade

    def descarregar(self, tempo: int):
        gasto = min(self.__carga, tempo)
        self.__carga -= gasto
        return gasto

    def carregar(self, tempo: int):
        self.__carga = min(self.__capacidade, self.__carga + tempo)

    def esta_vazia(self):
        return self.__carga == 0

    def mostrar(self):
        print(f"({self.__carga}/{self.__capacidade})")

    def __str__(self):
        return f"({self.__carga}/{self.__capacidade})"


class Carregador:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def get_potencia(self):
        return self.__potencia

    def mostrar(self):
        print(f"(Potência {self.__potencia})")

    def __str__(self):
        return f"(Potência {self.__potencia})"


class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__bateria = None
        self.__carregador = None

    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria

    def rmBateria(self):
        if self.__bateria is not None:
            print("bateria removida")
            b = self.__bateria
            self.__bateria = None
            return b
        print("fail: sem bateria para remover")
        return None

    def setCarregador(self, carregador: Carregador):
        self.__carregador = carregador

    def ligar(self):
        if self.__ligado:
            print("notebook já está ligado")
            return

        if (self.__bateria and not self.__bateria.esta_vazia()) or self.__carregador:
            self.__ligado = True
            print("notebook ligado")
        else:
            print("não foi possível ligar")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("notebook desligado")
        else:
            print("notebook já está desligado")

    def usar(self, tempo: int):
        if not self.__ligado:
            print("notebook desligado")
            return

        if self.__bateria is None and self.__carregador is None:
            print("fail: sem energia")
            self.__ligado = False
            return

        if self.__bateria and not self.__bateria.esta_vazia():
            # usa bateria
            descarregado = self.__bateria.descarregar(tempo)
            tempo_restante = tempo - descarregado

            # se tiver carregador, ele carrega durante o uso
            if self.__carregador:
                self.__bateria.carregar(self.__carregador.get_potencia() * tempo)

            if self.__bateria.esta_vazia():
                print(f"Usando por {descarregado} minutos, notebook descarregou")
                self.__ligado = False
            else:
                print(f"Usando por {tempo} minutos")

        elif self.__bateria and self.__carregador:
            # estava descarregada, mas tem carregador
            self.__bateria.carregar(self.__carregador.get_potencia() * tempo)
            print("Notebook utilizado com sucesso")

        elif self.__carregador and not self.__bateria:
            # sem bateria, mas ligado ao carregador
            print("Notebook utilizado com sucesso")

        else:
            print("fail: sem energia")
            self.__ligado = False

    def mostrar(self):
        status = "Ligado" if self.__ligado else "Desligado"
        bateria_str = str(self.__bateria) if self.__bateria else "Nenhuma"
        carregador_str = str(self.__carregador) if self.__carregador else "Desconectado"
        print(f"Status: {status}, Bateria: {bateria_str}, Carregador: {carregador_str}")
