from typing import List
from fastapi import FastAPI
import main

app = FastAPI()

@app.post("/exercicio1")
def exe1(salario_hora: float, horas_trabalhadas: float, n_filhos: int):
    resultado = main.exercicio1(salario_hora, horas_trabalhadas, n_filhos)
    return resultado


@app.post("/exercicio2")
def exe2(n: int, sequencia:List[int]):
    print(type(sequencia))

    resultado = main.exercicio2(n, sequencia)
    return resultado


@app.post("/exercicio3")
def exe3(n:int):
    resultado_a = main.exercicio3_a(n)
    resultado_b = main.exercicio3_b(n)
    return [resultado_a, resultado_b]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)