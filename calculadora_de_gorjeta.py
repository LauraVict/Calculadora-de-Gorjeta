def calculadora_de_gorjeta():
    total_conta = float(input("Qual é o total da conta? $"))
    percentual_gorjeta = int(input("Qual percentual de gorjeta você gostaria de dar? 10, 12 ou 15? "))
    gorjeta = total_conta * (percentual_gorjeta / 100)
    total_pagar = total_conta + gorjeta
    print(f"\nGorjeta: ${gorjeta:.2f}")
    print(f"Total a pagar: ${total_pagar:.2f}")

if __name__ == "__main__":
    calculadora_de_gorjeta()
202