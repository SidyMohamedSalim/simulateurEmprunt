from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    # TOOD: return all pret created
    return []


@app.get("/pret/")
def get_one_pret(item_id: int, q: Union[str, None] = None):
    # TOOD: get one pret by id
    # Example of pret
    return {
        "pret_id": 1,
        "capital": 1000,
        "taux": 0.1,
        "duree": 12,
        "type_remboursement": "annuite",
    }
    # return {"item_id": item_id, "q": q}

@app.post("/pret/")
def create_pret(pret: dict):
    # TOOD: create a new pret

    # Example of pret
    # return {
    #     "pret_id": 1,
    #     "capital": 1000,
    #     "taux": 0.1,
    #     "duree": 12,
    #     "type_remboursement": ["annuite"],
    # }
    return {}
