def validar_casas_decimais(valor):
    partes = str(valor).split('.')
    if len(partes) == 2 and len(partes[1]) <= 2:
        return True
    return False

def definir_meta():
    print("Bem-vindo à Calculadora de Meta Financeira!")
    nome_meta = input("Por favor, digite um nome ou objetivo para a sua meta: ")
    while True:
        try:
            meta_financeira = float(input(f"Qual é o valor da sua meta financeira '{nome_meta}'? Use '.' (ponto) para separar casas decimais: "))
            if meta_financeira <= 0:
                print("Por favor, insira um valor positivo.")
                continue
            if not validar_casas_decimais(meta_financeira):
                print("Por favor, insira um valor com no máximo duas casas decimais.")
                continue
            break
        except ValueError:
            print("Por favor use '.' (ponto) para separar casas decimais e não ',' (vírgula).")
    return nome_meta, meta_financeira

def definir_economia_mensal():
    while True:
        try:
            economia_mensal = float(input("Quanto você pode economizar por mês? Use '.' (ponto) para separar casas decimais: "))
            if economia_mensal < 0:
                print("Por favor, insira um valor positivo.")
                continue
            if not validar_casas_decimais(economia_mensal):
                print("Por favor, insira um valor com no máximo duas casas decimais.")
                continue
            break
        except ValueError:
            print("Por favor use '.' (ponto) para separar casas decimais e não ',' (vírgula).")
    return economia_mensal

def calcular_tempo(meta, economia_mensal):
    if economia_mensal == 0:
        return float('inf')
    return meta / economia_mensal

def main():
    nome_meta, meta = definir_meta()
    economia_mensal = definir_economia_mensal()

    meses = calcular_tempo(meta, economia_mensal)
    
    if meses == float('inf'):
        print(f"Com uma economia mensal de R$0, você nunca atingirá a sua meta econômica '{nome_meta}'.")
    else:
        print(f"Levará aproximadamente {meses:.2f} meses para atingir a sua meta econômica '{nome_meta}'.")

if __name__ == "__main__":
    main()
