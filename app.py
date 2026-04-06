import argparse
import sys


class AquaCli:
    def __init__(self, goal=2000):
        self.goal = goal
        self.total_water = 0

    def add_water(self, amount):
        if amount <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        self.total_water += amount
        return self.total_water

    def check_status(self):
        if self.total_water >= self.goal:
            return "Parabéns! Você atingiu sua meta diária!"
        falta = self.goal - self.total_water
        return f"Você bebeu {self.total_water}ml. Faltam {falta}ml."


def main():
    parser = argparse.ArgumentParser(
        description="AquaCli - Monitor de Hidratação"
    )
    parser.add_argument(
        '--add', type=int, help="Adiciona água em ml (ex: --add 500)"
    )
    args = parser.parse_args()

    tracker = AquaCli()

    if args.add:
        try:
            tracker.add_water(args.add)
            print(f"Sucesso! {args.add}ml adicionados.")
            print(tracker.check_status())
        except ValueError as e:
            print(f"Erro: {e}")
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
    
