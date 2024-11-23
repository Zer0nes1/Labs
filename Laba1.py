# 1. Продукт
class Product:
    def __init__(self, id, name, description, price, category):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category.to_json()
        }

    def from_json(js):
        id = js['id']
        name = js['name']
        description = js['description']
        price = js['price']
        category = Category.from_json(js['category'])
        return Product(id, name, description, price, category)

    def to_xml(self):
        product_elem = ET.Element("Product")
        ET.SubElement(product_elem, "Id").text = str(self.id)
        ET.SubElement(product_elem, "Name").text = self.name
        ET.SubElement(product_elem, "Description").text = self.description
        ET.SubElement(product_elem, "Price").text = str(self.price)
        product_elem.append(self.category.to_xml())
        return product_elem

    def from_xml(elem):
        id = int(elem.find("Id").text)
        name = elem.find("Name").text
        description = elem.find("Description").text
        price = float(elem.find("Price").text)
        category_elem = elem.find("Category")
        category = Category.from_xml(category_elem)
        return Product(id, name, description, price, category)