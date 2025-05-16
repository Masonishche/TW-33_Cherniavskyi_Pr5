from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///genetic_algorithm_results.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class GeneticResult(Base):
    __tablename__ = "genetic_results"

    id = Column(Integer, primary_key=True, index=True)
    problem_size = Column(Integer)
    population_size = Column(Integer)
    num_iterations = Column(Integer)
    best_solution_genes = Column(String)
    fitness = Column(Float)

Base.metadata.create_all(bind=engine)

def save_result(problem_size, population_size, num_iterations, best_solution_genes, fitness):
    db = SessionLocal()
    result = GeneticResult(
        problem_size=problem_size,
        population_size=population_size,
        num_iterations=num_iterations,
        best_solution_genes=','.join(map(str, best_solution_genes)),
        fitness=fitness
    )
    db.add(result)
    db.commit()
    db.close()
