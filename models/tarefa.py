from dataclasses import dataclass

@dataclass

class Tarefa:    
        id: int
        descricao: str
        empregador: str
        endereco: str
        valor: float
        data: str
        status: str