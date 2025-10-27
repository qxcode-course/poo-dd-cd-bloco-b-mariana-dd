class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size

    def usagePerSheet(self) -> int:
        if self.hardness == "HB":
            return 1
        elif self.hardness == "2B":
            return 2
        elif self.hardness == "4B":
            return 4
        elif self.hardness == "6B":
            return 6
        return 0

    def __str__(self):
        return f"[{self.thickness:.1f}:{self.hardness}:{self.size}]"


class Pencil:
    def __init__(self, thickness: float):
        self.thickness = thickness
        self.tip = None

    def hasGrafite(self):
        return self.tip is not None

    def insert(self, lead: Lead):
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return
        if lead.thickness != self.thickness:
            print("fail: calibre incompativel")
            return
        self.tip = lead

    def remove(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return
        self.tip = None

    def writePage(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return
        gasto = self.tip.usagePerSheet()
        if self.tip.size <= 10:
            print("fail: tamanho insuficiente")
            return
        if self.tip.size - gasto < 10:
            print("fail: folha incompleta")
            self.tip.size = 10
            return
        self.tip.size -= gasto

    def __str__(self):
        if not self.hasGrafite():
            return f"calibre: {self.thickness:.1f}, grafite: null"
        return f"calibre: {self.thickness:.1f}, grafite: {self.tip}"


def main():
    pencil = None
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
                pencil = Pencil(float(parts[1]))
            elif cmd == "show":
                print(pencil)
            elif cmd == "insert":
                lead = Lead(float(parts[1]), parts[2], int(parts[3]))
                pencil.insert(lead)
            elif cmd == "remove":
                pencil.remove()
            elif cmd == "write":
                pencil.writePage()
        except EOFError:
            break


if __name__ == "__main__":
    main()