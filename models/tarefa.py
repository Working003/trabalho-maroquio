from dataclasses import dataclass

@dataclass
class Tarefa:    
        id: int
        descricao: str
        empregador: int
        freelancer: int
        endereco: str
        valor: float
        data: str
        avaliacao: float
        status: str