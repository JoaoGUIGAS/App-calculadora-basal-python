def calcular_tmb(peso, altura, idade, genero):
    """
    Calcula a Taxa Metabólica Basal usando a equação de Mifflin-St Jeor
    Para gênero não informado, usa uma média entre as fórmulas masculina e feminina
    Referência: Mifflin MD, et al. A new predictive equation for resting energy expenditure in healthy individuals. Am J Clin Nutr. 1990
    """
    if genero.lower() == 'masculino':
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    elif genero.lower() == 'feminino':
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161
    else:  # gênero não informado
        # Calcula a média entre as fórmulas masculina e feminina
        tmb_masc = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
        tmb_fem = (10 * peso) + (6.25 * altura) - (5 * idade) - 161
        tmb = (tmb_masc + tmb_fem) / 2
    
    return tmb

def calcular_gasto_energetico(tmb, nivel_atividade, objetivo):
    """
    Calcula o gasto energético total considerando o nível de atividade e objetivo
    Referência: Journal of the International Society of Sports Nutrition
    """
    # Fatores de atividade (ACSM Guidelines)
    fatores = {
        'sedentario': 1.2,      # Pouco ou nenhum exercício
        'leve': 1.375,          # Exercício leve 1-3x/semana
        'moderado': 1.55,       # Exercício moderado 3-5x/semana
        'ativo': 1.725,         # Exercício intenso 6-7x/semana
        'muito_ativo': 1.9      # Exercício muito intenso, trabalho físico
    }
    
    gasto_total = tmb * fatores[nivel_atividade]
    
    # Ajuste baseado no objetivo
    ajustes = {
        'perder_peso': -500,    # Déficit calórico moderado
        'manter_peso': 0,       # Manutenção
        'ganhar_massa': 500     # Superávit calórico moderado
    }
    
    return gasto_total + ajustes[objetivo]

def calcular_macronutrientes(calorias_diarias, objetivo):
    """
    Calcula a distribuição de macronutrientes baseado no objetivo e pesquisas recentes
    Referências:
    - International Society of Sports Nutrition
    - American College of Sports Medicine
    - Journal of the International Society of Sports Nutrition
    """
    if objetivo == 'perder_peso':
        # Alto teor de proteína para preservar massa magra durante déficit calórico
        proteina_pct = 0.35  # 35% das calorias
        gordura_pct = 0.25   # 25% das calorias
        carb_pct = 0.40      # 40% das calorias
    
    elif objetivo == 'ganhar_massa':
        # Alto teor de carboidratos para suportar treinos intensos e recuperação
        proteina_pct = 0.30  # 30% das calorias
        gordura_pct = 0.20   # 20% das calorias
        carb_pct = 0.50      # 50% das calorias
    
    else:  # manter_peso
        # Distribuição balanceada para manutenção
        proteina_pct = 0.30  # 30% das calorias
        gordura_pct = 0.30   # 30% das calorias
        carb_pct = 0.40      # 40% das calorias

    # Cálculo em gramas
    proteina = (calorias_diarias * proteina_pct) / 4  # 4 calorias/g
    carboidratos = (calorias_diarias * carb_pct) / 4  # 4 calorias/g
    gorduras = (calorias_diarias * gordura_pct) / 9   # 9 calorias/g
    
    return {
        'proteina': round(proteina, 1),
        'carboidratos': round(carboidratos, 1),
        'gorduras': round(gorduras, 1),
        'proteina_pct': int(proteina_pct * 100),
        'carboidratos_pct': int(carb_pct * 100),
        'gorduras_pct': int(gordura_pct * 100)
    }

def main():
    print("=== Calculadora de Calorias e Macronutrientes ===\n")
    
    # Coleta de dados do usuário
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (cm): "))
    idade = int(input("Digite sua idade: "))
    genero = input("Digite seu gênero (masculino/feminino): ")
    
    print("\nNíveis de atividade física:")
    print("1 - Sedentário (pouco ou nenhum exercício)")
    print("2 - Levemente ativo (exercício leve 1-3 dias/semana)")
    print("3 - Moderadamente ativo (exercício moderado 3-5 dias/semana)")
    print("4 - Muito ativo (exercício pesado 6-7 dias/semana)")
    print("5 - Extremamente ativo (exercício muito pesado, trabalho físico)")
    
    opcao = int(input("\nEscolha seu nível de atividade (1-5): "))
    
    niveis_atividade = {
        1: 'sedentario',
        2: 'leve',
        3: 'moderado',
        4: 'ativo',
        5: 'muito_ativo'
    }
    
    nivel_atividade = niveis_atividade[opcao]
    
    # Cálculo das calorias diárias
    calorias_diarias = calcular_tmb(peso, altura, idade, genero)
    
    # Cálculo dos macronutrientes
    macros = calcular_macronutrientes(calorias_diarias, 'manter_peso')
    
    # Apresentação dos resultados
    print("\n=== Resultados ===")
    print(f"\nSuas necessidades calóricas diárias: {round(calorias_diarias)} calorias")
    print("\nDistribuição recomendada de macronutrientes:")
    print(f"Proteínas: {macros['proteina']}g")
    print(f"Carboidratos: {macros['carboidratos']}g")
    print(f"Gorduras: {macros['gorduras']}g")
    
    print("\nObservações:")
    print("- Esta é uma estimativa baseada na fórmula de Mifflin-St Jeor")
    print("- Ajuste os valores conforme sua resposta individual e objetivos")
    print("- Consulte um profissional de saúde para recomendações personalizadas")

if __name__ == "__main__":
    main()
