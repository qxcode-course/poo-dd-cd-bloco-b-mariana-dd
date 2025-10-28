class Battery:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.charge = capacity

    def use(self, time: int):
        self.charge -= time
        if self.charge < 0:
            self.charge = 0

    def charge_up(self, amount: int):
        self.charge += amount
        if self.charge > self.capacity:
            self.charge = self.capacity

    def __str__(self):
        return f"Bateria {self.charge}/{self.capacity}"


class Charger:
    def __init__(self, power: int):
        self.power = power

    def __str__(self):
        return f"Carregador {self.power}W"


class Notebook:
    def __init__(self):
        self.on = False
        self.time_on = 0
        self.battery = None
        self.charger = None

    # ----------------- COMPONENTES -----------------
    def set_battery(self, capacity: int):
        if self.battery is not None:
            print("fail: bateria já conectada")
            return
        self.battery = Battery(capacity)

    def rm_battery(self):
        if self.battery is None:
            print("fail: Sem bateria")
            return
        print(f"Removido {self.battery.charge}/{self.battery.capacity}")
        self.battery = None
        self.on = False

    def set_charger(self, power: int):
        if self.charger is not None:
            print("fail: carregador já conectado")
            return
        self.charger = Charger(power)

    def rm_charger(self):
        if self.charger is None:
            print("fail: Sem carregador")
            return
        print(f"Removido {self.charger.power}W")
        self.charger = None
        if self.battery is None:
            self.on = False

    # ----------------- CONTROLE -----------------
    def turn_on(self):
        if self.on:
            return
        if (self.battery and self.battery.charge > 0) or self.charger:
            self.on = True
        else:
            print("fail: não foi possível ligar")

    def turn_off(self):
        self.on = False

    def use(self, time: int):
        if not self.on:
            print("fail: desligado")
            return

        # --- só bateria ---
        if self.battery and not self.charger:
            if self.battery.charge < time:
                # só usa o que resta da bateria
                self.time_on += self.battery.charge
                self.battery.use(self.battery.charge)
                self.on = False
                print("fail: descarregou")
                return
            else:
                self.battery.use(time)
                self.time_on += time
                return

        # --- bateria + carregador ---
        if self.battery and self.charger:
            self.battery.charge_up(self.charger.power * time)
            self.time_on += time
            return

        # --- só carregador ---
        if self.charger:
            self.time_on += time
            return

    # ----------------- STATUS -----------------
    def __str__(self):
        parts = []
        if self.on:
            parts.append(f"Notebook: ligado por {self.time_on} min")
        else:
            parts.append("Notebook: desligado")
        if self.charger:
            parts.append(str(self.charger))
        if self.battery:
            parts.append(str(self.battery))
        return ", ".join(parts)


# ----------------- SHELL -----------------
def main():
    note = Notebook()

    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if not line:
            continue

        print(f"${line}")  # imprime o comando, conforme QxCode espera
        cmd = line.split()

        if cmd[0] == "end":
            break
        elif cmd[0] == "show":
            print(note)
        elif cmd[0] == "set_battery":
            note.set_battery(int(cmd[1]))
        elif cmd[0] == "rm_battery":
            note.rm_battery()
        elif cmd[0] == "set_charger":
            note.set_charger(int(cmd[1]))
        elif cmd[0] == "rm_charger":
            note.rm_charger()
        elif cmd[0] == "turn_on":
            note.turn_on()
        elif cmd[0] == "turn_off":
            note.turn_off()
        elif cmd[0] == "use":
            note.use(int(cmd[1]))
        else:
            print("fail: comando inválido")


if __name__ == "__main__":
    main()