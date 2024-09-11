
class FalsaPosicao:

    def calcular(func, limite, quartos, tipo_imovel, dias_mes=30, tol=1e-5, max_iter=100):
        """
        Método da Falsa Posição para encontrar o número de andares necessário para atingir o limite de consumo.
        
        Args:
            func (function): Função que calcula o consumo total (função objetivo).
            limite (float): Limite de consumo em m³.
            quartos (int): Número de quartos no imóvel.
            tipo_imovel (str): Tipo de imóvel ('apartamento' ou 'casa').
            dias_mes (int): Número de dias no mês (padrão = 30).
            tol (float): Tolerância para o erro da aproximação.
            max_iter (int): Número máximo de iterações.
        
        Returns:
            float: Aproximação do número de andares para atingir o limite de consumo.
        """
    
        a, b = 1, 100
        iteracoes = 0

    
        consumo_a = func(tipo_imovel, quartos, andares=a, dias_mes=dias_mes) - limite
        consumo_b = func(tipo_imovel, quartos, andares=b, dias_mes=dias_mes) - limite

        if consumo_a * consumo_b > 0:
            raise ValueError("Não há raiz no intervalo fornecido.")

        while iteracoes < max_iter:
        
            c = (a * consumo_b - b * consumo_a) / (consumo_b - consumo_a)
            consumo_c = func(tipo_imovel, quartos, andares=int(c), dias_mes=dias_mes) - limite

        
            if abs(consumo_c) < tol:
                return c

            
            if consumo_c * consumo_a < 0:
                b = c
                consumo_b = consumo_c
            else:
                a = c
                consumo_a = consumo_c

            iteracoes += 1

    
        return c


