from nutricompare.Product import Product


def main(argv: list[str] = None):
    total_g = float(input("Enter total amount of product (g):"))
    protein_per_hundred = float(input("Enter amount of protein in 100g:"))
    price = float(input("Enter price of product:"))

    a = Product(name='', weight=total_g, protein_per_hundred=protein_per_hundred, price=price)

    print(f"{a.cost_per_macro:2f} zł per 1g protein")


if __name__ == '__main__':
    main()
