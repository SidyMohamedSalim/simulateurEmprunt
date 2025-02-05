from pret import Pret


def compare_pret(first_preteur:Pret, second_preteur:Pret) -> str:
    """
    Compare two preteurs
    """
    ...


def get_all_prets() -> list[Pret]:
    """
    Get all prets
    """
    ...

def get_one_pret(pret_id:int) -> Pret:
    """
    Get one pret by id
    """
    ...


def create_pret(pret:dict) -> Pret:
    """
    Create a new pret
    """
    ...

def load_json(file:str) -> dict:
    """
    Load a json file
    """
    ...