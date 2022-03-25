# // ----- Funções----- // #

def entrada(texto):
    return input(texto)


def converterBinario():
    print("Insira sua numeração binária:")
    dado = entrada("\nSelecione:")
    binarioInd = list(dado)
    dadosSoma = []
    contador = len(binarioInd) - 1
    for element in binarioInd:
        calculoExpoente = 2 ** contador
        inteiro = int(element)
        calculo = inteiro * calculoExpoente
        if contador >= 0:
            contador = contador - 1
            dadosSoma.append(calculo)
            soma = sum(dadosSoma)
    print("\nO número decimal do binário " +
          str(dado) + " é " + str(soma) + "!\n")


def converterDecimal():
    def condicaoDecimal(calculo, modulo):
        if calculo != 1 and modulo == 1 or calculo != 1 and modulo == 0:
            binario.insert(0, modulo)
            calculoDecimal(int(calculo))
        if calculo == 1 and modulo == 0:
            binario.insert(0, modulo)
            binario.insert(0, 1)
            numero_final = "".join([str(_) for _ in binario])
            print("\nO número binário do decimal " +
                  dado + " é " + numero_final + "!\n")

    def calculoDecimal(element):
        valor = int(element)
        calculo = valor / 2
        modulo = valor % 2
        condicaoDecimal(calculo, modulo)

    print("\nInsira sua numeração decimal:")
    dado = entrada("\nSelecione:")
    binario = []
    calculoDecimal(dado)


def condicao(a):
    if a == "1":
        converterBinario()
    if a == "2":
        converterDecimal()


def escolherFuncao():
    print("\nConversor Binário-Decimal\n")

    print("Que converter qual numeração?\n")

    print("1.Binário")
    print("2.Decimal")

    dado = entrada("\nSelecione:")
    condicao(dado)

# // ----- Programa ----- //


escolherFuncao()
