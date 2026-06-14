import argparse
import sys
import requests
from database import supabase


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


def buscar_temperatura_local(cidade, api_key):
    """Faz uma requisição HTTP GET para a OpenWeather API."""
    url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={cidade}&appid={api_key}&units=metric"
    )
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        dados = response.json()
        return dados['main']['temp']
    except requests.RequestException:
        print("Aviso: Não foi possível obter o clima. Usando meta padrão.")
        return None


def ajustar_meta_agua(temperatura):
    """Se a temperatura for igual ou superior a 30°C, adiciona 500ml."""
    meta_padrao = 2000
    if temperatura is not None and temperatura >= 30.0:
        print(f"Está calor ({temperatura}°C)! Sua meta aumentou para 2500ml.")
        return meta_padrao + 500
    return meta_padrao


def salvar_agua(quantidade_ml):
    dados = {"quantidade": quantidade_ml}
    supabase.table("registro_agua").insert(dados).execute()
    print(f" 💧 {quantidade_ml}ml salvos no banco de dados!")


def main():
    parser = argparse.ArgumentParser(
        description="AquaCli - Monitor de Hidratação"
    )
    parser.add_argument(
        '--add', type=int, help="Adiciona água em ml (ex: --add 500)"
    )
    args = parser.parse_args()

    # Informações fixas da API (Cidade e Key)
    api_key = "ea36329ff03bc14ec48c68b5698edca6"
    cidade = "Brasilia"

    # Busca a temperatura e define a nova meta antes de iniciar o app
    temperatura_atual = buscar_temperatura_local(cidade, api_key)
    meta_dinamica = ajustar_meta_agua(temperatura_atual)

    # Inicia o tracker já com a meta dinâmica aplicada
    tracker = AquaCli(goal=meta_dinamica)

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
