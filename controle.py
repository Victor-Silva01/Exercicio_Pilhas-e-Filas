from collections import deque

class PatioEstacionamento:
    def __init__(self):
        self.fila_veiculos = deque()

    def entrar_veiculo(self, veiculo):
        self.fila_veiculos.append(veiculo)
        print(f"✅ Veículo '{veiculo}' entrou no pátio e ocupou uma vaga.")

    def sair_veiculo(self):
        if self.fila_veiculos:
            veiculo_saida = self.fila_veiculos.popleft()
            print(f"✅ Veículo '{veiculo_saida}' saiu do pátio.")
        else:
            print("⚠️ Nenhum veículo no pátio para sair.")

    def exibir_veiculos(self):
        if self.fila_veiculos:
            print("\n🚗 Veículos no pátio (ordem de entrada):")
            for i, veiculo in enumerate(self.fila_veiculos, start=1):
                print(f"  {i}. {veiculo}")
        else:
            print("📭 O pátio está vazio.")

if __name__ == "__main__":
    patio = PatioEstacionamento()
    patio.entrar_veiculo("Carro A")
    patio.entrar_veiculo("Carro B")
    patio.entrar_veiculo("Carro C")
    patio.exibir_veiculos()
    patio.sair_veiculo()
    patio.exibir_veiculos()
    patio.sair_veiculo()
    patio.exibir_veiculos()
