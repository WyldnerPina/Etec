from dataclasses import dataclass

from enum_op import EnumOp


@dataclass(frozen=True)
class Entrevistado:
    id: int
    nome: str
    idade: int
    opiniao: EnumOp