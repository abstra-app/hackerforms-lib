# Hackerforms Postgres

A Client API for connecting with Postgres Databases and provide ready-to-use pages for CRUD use cases.

#### 1. Creating a Postgres Client Instance

```
>>> import hackerforms.crud.postgres as hpc
>>> db = hpc.Client(database=os.getenv('database'),user=os.getenv('user'),password=os.getenv('password'),host=os.getenv('host'))
```

##### Example: Create a insert form

Suppose a database in which there are three tables `products`, `suppliers` and `categories`. The table `products` has a reference to the tables `suppliers` and `categories` through the foreign key columns `category_id` and `category_id`, respectively.

In order to create a new product, we have to choose its category and supplier, so we are going to define two dropdowns for choosing them.

```
categories = db.dropdown(table="categories", column="category_name", primary_key='category_id') # [{'label': 'category_name', 'value': 'category_id'}]

```

```
suppliers = db.dropdown(table="suppliers", column="company_name", primary_key='supplier_id')
```

`suppliers` and `categories` has the dropdown options in the format expected by `read_dropdown` options. Its labels are the columns passed as parameter to the dropdown method and its values are the respective primary_keys.

Now, for creating the form:

```
page = (
    db.RowPage(table="products")
    .read_dropdown("category", options=categories, column="category_id")
    .read_dropdown("supplier", options=suppliers, column="supplier_id")
    .read("product name", key="product_name", column="product_name")
    .read_number("quantity per unit", column="quantity_per_unit")
    .read_currency("unit price", column="unit_price")
    .read_number("units in stock", column="units_in_stock")
    .read_number("units in order", column="units_on_order")
    .read_number("discontinued", column="discontinued")
    .insert(context={"product_id": 821, })
)
```

Notice that you have to provide the column linked to each widget. Besides that, we use the `suppliers` and `categories` variables as options to `read_dropdown` widgets. We finish our RowPage builder invoking the method insert(), which means it's a `create` form page. The parameter context is rather important. It's a dict with table column names as keys and its values are going to be persisted in row besides the values inserted in the form. Be aware that if you a column name in the form and in context object, the latter will override the value inserted in the form by the user.

##### Example: Search rows in a table

Now, imagine you wish to provide a page for your users search for rows in a table.
In our database example, we would like to allow the users to search for products by its name, display a table of results and update it dinamically while (s)he types, after all UX is crucial!

See below how to achieve it:

```
product = (
    db.SearchPage(table="products")
    .read("Product Name", column="product_name")
    .search(
        display_columns=["product_id", "product_name", "unit_price"]
    )
)
```

A page will be displayed with a `read` widget as input filter and a table will be updated while the user types, in realtime.
