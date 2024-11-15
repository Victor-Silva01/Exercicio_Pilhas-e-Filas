class Armazem:
    def __init__(self):
        self.pilha_caixas = []

    def adicionar_caixa(self, caixa):
        self.pilha_caixas.append(caixa)
        print(f"✅ Caixa '{caixa}' adicionada ao topo do armazém.")

    def remover_caixa(self):
        if self.pilha_caixas:
            caixa_removida = self.pilha_caixas.pop()
            print(f"✅ Caixa '{caixa_removida}' removida do topo do armazém.")
        else:
            print("⚠️ Nenhuma caixa para remover. O armazém está vazio.")

    def exibir_caixas(self):
        if self.pilha_caixas:
            print("\n📦 Caixas no armazém (da base para o topo):")
            for i, caixa in enumerate(self.pilha_caixas, start=1):
                print(f"  {i}. {caixa}")
        else:
            print("📭 O armazém está vazio.")


if __name__ == "__main__":
    armazem = Armazem()
    armazem.adicionar_caixa("Caixa A")
    armazem.adicionar_caixa("Caixa B")
    armazem.adicionar_caixa("Caixa C")
    armazem.exibir_caixas()
    armazem.remover_caixa()
    armazem.exibir_caixas()
