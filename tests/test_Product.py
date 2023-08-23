import pytest

from nutricompare.Product import Product
from nutricompare.const import TEST_PRODUCTS


TEST_PRODUCTS = [Product(**kw) for kw in TEST_PRODUCTS]


def test_product_created():
    prod = Product(name="Test", price=2.54, weight=100.0, macro_per_hundred=12.0)
    assert prod


@pytest.mark.parametrize("values, expected", [
    ({"name": "Skyr", "price": 2.54, "weight": 150.0, "macro_per_hundred": 12.0}, "0.141"),
    ({"name": "Quark", "price": 3.99, "weight": 250.0, "macro_per_hundred": 18.0}, "0.089"),
    ({"name": "Super Skyr", "price": 5.99, "weight": 450.0, "macro_per_hundred": 12.0}, "0.111"),
    ({"name": "Tuna", "price": 8.59, "weight": 120.0, "macro_per_hundred": 28.0}, "0.256"),
    ({"name": "Milk Boost", "price": 3.49, "weight": 250.0, "macro_per_hundred": 10.0}, "0.140"),
    ({"name": "Cocktail", "price": 3.99, "weight": 250.0, "macro_per_hundred": 10.5}, "0.152"),
    ({"name": "Oats", "price": 4.99, "weight": 200.0, "macro_per_hundred": 9.5}, "0.263"),
    ({"name": "Protein Wafer", "price": 3.49, "weight": 46.0, "macro_per_hundred": 30.0}, "0.253"),
    ({"name": "Giant Yoghurt", "price": 9.99, "weight": 1000.0, "macro_per_hundred": 7.9}, "0.126")
])
def test_product_macro_efficiency_is_correctly_calculated(values, expected):
    prod = Product(**values)
    efficiency = f"{prod.cost_per_macro:.3f}"
    assert efficiency == expected
