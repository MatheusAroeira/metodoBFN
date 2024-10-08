class falsa_posicao:
    
    def consumo_total_litros_mes(tipo_imovel, quartos, consumo_por_pessoa, andares=1, dias_mes=30):
        """
        Calcula o consumo total de água em um mês para um apartamento ou casa.

        Args:
            tipo_imovel (str): Tipo de imóvel ('apartamento' ou 'casa').
            quartos (int): Número de quartos no imóvel.
            consumo_por_pessoa (float): Consumo diário de água por pessoa (em litros).
            andares (int): Número de andares (para apartamentos, por padrão é 1 para casas).
            dias_mes (int): Número de dias no mês (padrão = 30).

        Returns:
            float: Consumo total de água em m³ por mês.
        """
        if tipo_imovel == 'apartamento':
            pessoas = (2 * quartos) + 2  
        elif tipo_imovel == 'casa':
            pessoas = 2 * quartos  
        else:
            raise ValueError("Tipo de imóvel inválido. Escolha 'apartamento' ou 'casa'.")

        consumo_diario = pessoas * consumo_por_pessoa
        consumo_diario_com_reserva = 1.2 * consumo_diario
        consumo_total_dia = consumo_diario_com_reserva * andares
        consumo_total_mes = consumo_total_dia * dias_mes
        consumo_total_m3_mes = consumo_total_mes / 1000

        return consumo_total_m3_mes

    def falsa_posicao_consumo(tipo_imovel, quartos, andares, dias_mes, consumo_desejado, tol=1e-6, max_iter=1000):
        """
        Aplica o método da Falsa Posição para encontrar o valor de consumo por pessoa que satisfaça
        o consumo total desejado.

        Args:
            tipo_imovel (str): Tipo de imóvel ('apartamento' ou 'casa').
            quartos (int): Número de quartos no imóvel.
            andares (int): Número de andares no imóvel.
            dias_mes (int): Número de dias no mês.
            consumo_desejado (float): Consumo total desejado em m³.
            tol (float): Tolerância para o erro do método.
            max_iter (int): Número máximo de iterações.

        Returns:
            float: Valor de consumo por pessoa que resulta no consumo total desejado.
        """
        # Função f(x) = consumo_total_litros_mes - consumo_desejado
        def f(consumo_por_pessoa):
            return falsa_posicao.consumo_total_litros_mes(tipo_imovel, quartos, consumo_por_pessoa, andares, dias_mes) - consumo_desejado

        # Limites iniciais para o consumo por pessoa (em litros)
        a = 50   # Limite inferior do consumo por pessoa (chute inicial)
        b = 300  # Limite superior do consumo por pessoa (chute inicial)

        # Verifica se há mudança de sinal entre os extremos
        if f(a) * f(b) > 0:
            raise ValueError("Não há raiz no intervalo fornecido. Tente outros limites iniciais.")

        i = 0
        for _ in range(max_iter):
            # Ponto de falsa posição (interpolação linear)
            fa = f(a)
            fb = f(b)
            x = (a * fb - b * fa) / (fb - fa)  # Fórmula da falsa posição
            fx = f(x)
            
            print('i = ' + i + ' | x = ' + x)

            # Verifica a convergência
            if abs(fx) < tol:
                return x

            # Atualiza os limites do intervalo com base no sinal de f(x)
            if fa * fx < 0:
                b = x  # A raiz está entre a e x
            else:
                a = x  # A raiz está entre x e b
            i+=1
        raise ValueError("Número máximo de iterações atingido. Método não convergiu.")

    def main():
        tipo_imovel = input("Digite o tipo de imóvel ('apartamento' ou 'casa'): ").lower()
        quartos = int(input("Digite o número de quartos: "))
        if tipo_imovel == 'apartamento':
            andares = int(input("Digite o número de andares: "))
        else:
            andares = 1  # Para casas, por padrão, será 1 andar
        dias_mes = int(input("Digite o número de dias no mês: "))
        consumo_desejado = float(input("Digite o consumo desejado em m³: "))

        # Encontrar o consumo por pessoa usando o método da Falsa Posição
        try:
            consumo_por_pessoa_ideal = falsa_posicao.falsa_posicao_consumo(tipo_imovel, quartos, andares, dias_mes, consumo_desejado)
            print(f"O consumo ideal por pessoa é: {consumo_por_pessoa_ideal:.2f} litros")
        except ValueError as e:
            print(e)
