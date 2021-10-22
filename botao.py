class Botao:
    '''
    Botões de seleção de personagens
    Propriedades:
        label,
        dim_botao,
        posicao_botao,
        cores (cor_principal, cor_secundaria),
        label,
       
    '''
    
    def __init__(self, label, dim_botao, posicao_botao, cores, posicao_seta): #construtor
        self.__label = label
        self.__dim_botao = dim_botao
        self.__posicao_botao = posicao_botao
        self.__cor_principal = cores[0]
        self.__cor_secundaria = cores[1]
        self.__posicao_seta = posicao_seta

    @property #comentário que pode ser lido pelo interpretador
    def label(self):
        return self.__label

    @property #comentário que pode ser lido pelo interpretador
    def dim_botao(self):
        return self.__dim_botao

    @property #comentário que pode ser lido pelo interpretador
    def posicao_botao(self):
        return self.__posicao_botao

    @property #comentário que pode ser lido pelo interpretador
    def cor_principal(self):
        return self.__cor_principal

    @property #comentário que pode ser lido pelo interpretador
    def cor_secundaria(self):
        return self.__cor_secundaria

    @property #comentário que pode ser lido pelo interpretador
    def posicao_seta(self):
        return self.__posicao_seta

    @property
    def rect(self): #retorna a posição e o tamanho do próprio botão
        x0, y0 = self.posicao_botao #posição do botão
        dx, dy = self.dim_botao #tamanho do botão

        return [x0, y0, dx, dy] #retorna a posição e o tamanho do botão

    def __contains__(self, point): #verifica se o cursor está no botão
        x0, y0 = self.posicao_botao #posição do botão
        dx, dy = self.dim_botao #tamanho do botão
        px, py = point #ponto em que o cursor está

        contem_x = x0 <= px <= x0 + dx #true se o cursor estiver em x do botão
        contem_y = y0 <= py <= y0 + dy #true se o cursor estiver em y do botão

        return contem_x and contem_y #retorna true se o cursor estiver com x e y no botão