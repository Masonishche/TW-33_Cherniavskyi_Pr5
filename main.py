from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from algorithm import SimpleGeneticAlgorithm
from db import save_result

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
    allow_credentials=True,
)

class GeneticAlgorithmRequest(BaseModel):
    problem_size: int
    population_size: int
    num_iterations: int

@app.post("/run_genetic_algorithm/")
def run_genetic_algorithm(request: GeneticAlgorithmRequest):
    problem_size = request.problem_size
    population_size = request.population_size
    num_iterations = request.num_iterations

    genetic_algorithm = SimpleGeneticAlgorithm(problem_size, population_size, num_iterations)
    best_solution = genetic_algorithm.run()

    save_result(problem_size, population_size, num_iterations, best_solution.genes, best_solution.fitness)

    return {"best_solution_genes": best_solution.genes, "fitness": best_solution.fitness}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
