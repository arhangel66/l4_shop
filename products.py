import json
from typing import List, Optional


def get_products() -> List[dict]:
    with open("products.json") as f:
        data = json.loads(f.read())
    return data


def _get_products_dict_by_slug() -> dict:
    products = get_products()
    products_dict = {}
    for product in products:
        products_dict[product["slug"]] = product
    return products_dict


def get_product_by_slug(slug: str) -> Optional[dict]:
    products = _get_products_dict_by_slug()
    return products.get(slug)
