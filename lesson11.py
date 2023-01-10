from csv import DictReader, DictWriter

from pydantic import BaseModel, Field


class Product(BaseModel):
    article: str = Field(min_length=1)
    title: str = Field(min_length=1)
    description: str = Field(default=None)
    price: float = Field(gt=0)


def load_products(filename: str) -> list[dict]:
    with open(filename, "r", encoding="utf-8") as file:
        reader = DictReader(file)
        return list(reader)


def validate_products(products: list[dict]) -> tuple[list[Product], list[dict]]:
    invalid_products = []
    valid_products = []
    for product in products:
        try:
            product = Product(**product)
        except ValueError:
            invalid_products.append(product)
        else:
            valid_products.append(product)
    return valid_products, invalid_products


def save_products(
    products: list[dict] | list[Product], filename: str, mode: str = "w"
) -> None:
    if isinstance(products[0], Product):
        products = list(map(lambda x: x.dict(), products))
    with open(filename, mode, encoding="utf-8") as file:
        writer = DictWriter(
            file, fieldnames=("article", "title", "description", "price")
        )
        if mode == "w":
            writer.writeheader()
        writer.writerows(products)


if __name__ == "__main__":
    filename = "products.csv"
    valid_products, invalid_products = validate_products(load_products(filename))
    save_products(invalid_products, "file.csv", "w")
