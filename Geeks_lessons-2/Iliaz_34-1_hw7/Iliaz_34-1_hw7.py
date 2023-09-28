import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE if not exists products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL,
    price numeric(10, 2) DEFAULT 0.0 NOT NULL,
    quantity INTEGER DEFAULT 0 NOT NULL)''')

conn.commit()
conn.close()


def add_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    products = [
        ("Жидкое мыло с запахом ванили", 5.99, 50),
        ("Мыло детское", 3.49, 100),
        ("Шампунь", 7.99, 30),
        ("Зубная паста", 2.99, 75),
        ("Молоко 1 литр", 1.99, 60),
        ("Яйца (10 штук)", 2.49, 80),
        ("Хлеб белый", 1.29, 120),
        ("Сахар (1 кг)", 1.79, 40),
        ("Кофе молотый", 8.99, 25),
        ("Гречка (500 г)", 1.49, 90),
        ("Яблоки (кг)", 0.99, 150),
        ("Картофель (кг)", 0.79, 200),
        ("Молокошоколад", 4.29, 35),
        ("Пельмени (1 упаковка)", 6.99, 15),
        ("Сок апельсиновый (1 литр)", 2.49, 50),
    ]

    cursor.executemany('insert into products (product_title, price, quantity) values (?,?,?)', products)

    conn.commit()
    conn.close()


def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('update products set quantity = ? where id = ?', (new_quantity, product_id))
    print(f'Количество товара с id {product_id} было изменено\n')
    conn.commit()
    conn.close()


def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('update products set price = ? where id = ?', (new_price, product_id))
    print(f'Ценник на товар с id {product_id} был изменен\n')
    conn.commit()
    conn.close()


def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('delete from products where id = ?', (product_id,))
    print(f'Продукт с id{product_id} был удален\n')
    conn.commit()
    conn.close()


def select_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('select * from products')
    products = cursor.fetchall()
    print("Все продукты")
    for product in products:
        print(product)

    conn.close()


def select_cheap_and_abundant_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('select * from products where price < 100.00 and quantity > 5')
    products = cursor.fetchall()
    print("\nТовары чей ценник ниже 100 и количество больше 5ти")

    for product in products:
        print(product)
    conn.close()


def search_products_by_title(word):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('select * from products where product_title like ?', ('%' + word + '%',))
    products = cursor.fetchall()
    for product in products:
        print("\nНайденный товар:", product)

    conn.close()


add_products()
update_quantity(14, 90)
update_price(15, 100.0)
delete_product(13)
select_all_products()
select_cheap_and_abundant_products()
search_products_by_title("мыло")