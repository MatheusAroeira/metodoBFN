
class Bisseccao:

    def calular(func, limite, quartos, tipo_imovel, dias_mes=30, tol=1e-5, max_iter=100):
        """
        Método da Bissecção para encontrar o número de andares necessário para atingir o limite de consumo.
        
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
        # Definindo os limites iniciais para o número de andares
        a = 1  # limite inferior (min 1 andar)
        b = 100  # limite superior (suposição máxima de 100 andares)
        
        iteracoes = 0

        while iteracoes < max_iter:
            # Calcula o ponto médio
            c = (a + b) / 2
            
            # Calcula o consumo no ponto médio
            consumo_c = func(tipo_imovel, quartos, c, dias_mes)
            
            # Verifica se estamos próximos o suficiente do limite
            if abs(consumo_c - limite) < tol:
                return c
            
            # Se o consumo for maior que o limite, atualiza o intervalo
            if consumo_c > limite:
                b = c
            else:
                a = c
            
            iteracoes += 1

        # Retorna a melhor aproximação após o número máximo de iterações
        return c


