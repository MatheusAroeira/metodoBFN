class newton_raphson:
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

    def newton_raphson_consumo(tipo_imovel, quartos, andares, dias_mes, consumo_desejado, tol=1e-6, max_iter=1000):
        """
        Aplica o método de Newton-Raphson para encontrar o valor de consumo por pessoa que satisfaça
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
            return newton_raphson.consumo_total_litros_mes(tipo_imovel, quartos, consumo_por_pessoa, andares, dias_mes) - consumo_desejado

        # Derivada numérica da função f em relação ao consumo por pessoa
        def f_derivada(consumo_por_pessoa, h=1e-6):
            return (f(consumo_por_pessoa + h) - f(consumo_por_pessoa)) / h

        # Valor inicial de chute
        consumo_por_pessoa = 150  # Chute inicial (em litros)

        i = 0
        
        for _ in range(max_iter):
            # Valor da função e sua derivada
            f_val = f(consumo_por_pessoa)
            f_deriv_val = f_derivada(consumo_por_pessoa)

            # Atualização do valor pelo método de Newton-Raphson
            if abs(f_deriv_val) < tol:
                raise ValueError("Derivada muito pequena. Método pode não convergir.")

            consumo_por_pessoa_novo = consumo_por_pessoa - f_val / f_deriv_val
            
            print('i = ' + i + ' | x = ' + consumo_por_pessoa_novo)

            # Verificação da convergência
            if abs(consumo_por_pessoa_novo - consumo_por_pessoa) < tol:
                return consumo_por_pessoa_novo

            consumo_por_pessoa = consumo_por_pessoa_novo
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

        # Encontrar o consumo por pessoa usando Newton-Raphson
        try:
            consumo_por_pessoa_ideal = newton_raphson.newton_raphson_consumo(tipo_imovel, quartos, andares, dias_mes, consumo_desejado)
            print(f"O consumo ideal por pessoa é: {consumo_por_pessoa_ideal:.2f} litros")
        except ValueError as e:
            print(e)
