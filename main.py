class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Словарь для хранения товаров и их цен

    # Метод для добавления товара в ассортимент
    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}")

    # Метод для удаления товара из ассортимента
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален")
        else:
            print(f"Товар '{item_name}' не найден")

    # Метод для получения цены товара
    def get_price(self, item_name):
        return self.items.get(item_name, None)

    # Метод для обновления цены товара
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}")
        else:
            print(f"Товар '{item_name}' не найден для обновления")

# Создание объектов магазинов
store1 = Store("Магазин №1", "ул. Ленина, 1")
store2 = Store("Магазин №2", "ул. Победы, 5")
store3 = Store("Магазин №3", "ул. Мира, 10")

# Добавление товаров в магазины
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2.add_item("апельсины", 1.0)
store2.add_item("груши", 0.6)

store3.add_item("виноград", 1.2)
store3.add_item("ананасы", 1.5)

# Тестирование методов на одном из магазинов
print("\nТестирование методов магазина №1")
store1.add_item("вишня", 0.9)          # Добавление товара
store1.update_price("бананы", 0.8)     # Обновление цены товара
store1.remove_item("яблоки")           # Удаление товара
banana_price = store1.get_price("бананы")  # Получение цены товара
print(f"Цена бананов: {banana_price}")
