from dataclasses import dataclass, field


@dataclass(order=True)
class Product:
    name: str
    price: float
    weight: float
    macro_per_hundred: float
    cost_per_macro: float = field(init=False)

    def __post_init__(self):
        self.set_cost_per_macro()

    def total_macro(self) -> float:
        return (self.weight / 100) * self.macro_per_hundred

    def product_per_macro(self) -> float:
        return self.weight / self.total_macro()

    def product_cost_per_gram(self) -> float:
        return self.price / self.weight

    def set_cost_per_macro(self):
        self.cost_per_macro = self.product_cost_per_gram() * self.product_per_macro()
