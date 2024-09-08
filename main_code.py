# Definindo a função para calcular as porcentagens
def calcular_porcentagens(renda_mensal):

    # Valores das porcentagens
    valor_necessidade = 50
    valor_gastos = 30
    valor_economias = 20

    # Obtendo as porcentagens
    obter_50_percent = (valor_necessidade / 100) * renda_mensal
    obter_30_percent = (valor_gastos / 100) * renda_mensal
    obter_20_percent = (valor_economias / 100) * renda_mensal

    # Retornando resultados
    return obter_50_percent, obter_30_percent, obter_20_percent

# Função principal para executar o código
def main():

    # Entrada do usário
    renda_mensal = float(input("Informe o valor da sua renda mensal: "))

    # Chamar função para calcular porcentagens
    necessidades, gastos, economias = calcular_porcentagens(renda_mensal)

    # Exibindo resultados
        
    print("R${:,.2f}".format(necessidades))
    print("R${:,.2f}".format(gastos))
    print("R${:,.2f}".format(economias))

# Chamando a função principal
main()