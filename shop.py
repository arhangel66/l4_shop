from flask import Flask, render_template, abort

from products import get_products, get_product_by_slug

app = Flask(__name__)


@app.route('/')
def home() -> str:
    response = render_template("home.html", products=get_products())
    return response


@app.route("/about/")
def about() -> str:
    response = render_template("about.html")
    return response


@app.route("/product/<string:slug>/")
def product_detail(slug) -> str:
    product = get_product_by_slug(slug)
    if not product:
        abort(404)

    response = render_template("details.html", product=product)
    return response
