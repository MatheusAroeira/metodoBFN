
class newtonRaphson:
    def derivada_consumo(tipo_imovel, quartos, andares, dias_mes=30):
        """
        Calcula a derivada do consumo total de água em relação ao número de andares.
        
        Args:
            tipo_imovel (str): Tipo de imóvel ('apartamento' ou 'casa').
            quartos (int): Número de quartos no imóvel.
            andares (int): Número de andares.
            dias_mes (int): Número de dias no mês (padrão = 30).
        
        Returns:
            float: Derivada do consumo total em m³ por andar.
        """
        if tipo_imovel == 'apartamento':
            consumo_por_pessoa = 150
            pessoas = (2 * quartos) + 2
        elif tipo_imovel == 'casa':
            consumo_por_pessoa = 200
            pessoas = 2 * quartos
        else:
            raise ValueError("Tipo de imóvel inválido. Escolha 'apartamento' ou 'casa'.")

    
        consumo_diario_com_reserva = 1.2 * pessoas * consumo_por_pessoa

    
        derivada = consumo_diario_com_reserva * dias_mes / 1000  # Derivada em m³
        
        return derivada


    def calcular(func, deriv_func, limite, quartos, tipo_imovel, dias_mes=30, tol=1e-5, max_iter=100):
        """
        Método de Newton-Raphson para encontrar o número de andares necessário para atingir o limite de consumo.
        
        Args:
            func (function): Função que calcula o consumo total (função objetivo).
            deriv_func (function): Função que calcula a derivada do consumo total.
            limite (float): Limite de consumo em m³.
            quartos (int): Número de quartos no imóvel.
            tipo_imovel (str): Tipo de imóvel ('apartamento' ou 'casa').
            dias_mes (int): Número de dias no mês (padrão = 30).
            tol (float): Tolerância para o erro da aproximação.
            max_iter (int): Número máximo de iterações.
        
        Returns:
            float: Aproximação do número de andares para atingir o limite de consumo.
        """

        andares = 10
        iteracoes = 0

        while iteracoes < max_iter:
        
            consumo_atual = func(tipo_imovel, quartos, andares, dias_mes) - limite
            derivada_atual = deriv_func(tipo_imovel, quartos, andares, dias_mes)

        
            if derivada_atual == 0:
                print("Derivada zero encontrada, o método não pode continuar.")
                return None

        
            andares_novo = andares - (consumo_atual / derivada_atual)

        
            if abs(andares_novo - andares) < tol:
                return andares_novo

            andares = andares_novo
            iteracoes += 1

    
        return andares