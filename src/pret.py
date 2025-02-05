

class Pret:

    def __init__(self, capital, taux, duree, type_remboursement:list[str]):
        self.capital = capital
        self.taux = taux
        self.duree = duree
        self.type_renboursement = "amortissement"

    
    def calcul_interet(self) -> list[float]:
        #  TOOD: implementer le calcul de l'interet
        interets = []

        new_capital = self.capital

    
    def calcul_amortissement(self) -> list[float]:
        #  TOOD: implementer le calcul de l'amortissement
        ...
    
    def calcul_annuite(self) -> list[float]:
        #  TOOD: implementer le calcul de l'annuite
        ...
    
    def get_net_value(self) -> list[float]:
        #  TOOD: implementer le calcul de la valeur nette
        ...



    