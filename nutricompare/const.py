import pathlib
import json

from nutricompare.Product import Product

DEFAULT_PATH = pathlib.Path.cwd().parent

TEST_PRODUCT_PATH = pathlib.Path(DEFAULT_PATH).joinpath("./tests/example_products.json")


def load_test_products() -> list[Product]:
    with open(TEST_PRODUCT_PATH, "r") as f:
        products: dict = json.load(f)
    return products['products']


TEST_PRODUCTS = load_test_products()
