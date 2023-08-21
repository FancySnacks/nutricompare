from dataclasses import dataclass, field


@dataclass(order=True)
class Product:
    name: str
    price: float
    weight: float
    protein_per_hundred: float
    cost_per_protein: float = field(init=False)

    def __post_init__(self):
        self.set_cost_per_protein()

    def total_protein(self) -> float:
        return (self.weight / 100) * self.protein_per_hundred

    def product_per_protein(self) -> float:
        return self.weight / self.total_protein()

    def product_cost_per_gram(self) -> float:
        return self.price / self.weight

    def set_cost_per_protein(self):
        self.cost_per_protein = self.product_cost_per_gram() * self.product_per_protein()
