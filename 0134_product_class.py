class Product:
	def __init__(self, name, price, discountPercent):
		self.name = name
		self.price = price
		self.discountPercent = discountPercent

	def discountAmount(self):
		return self.price * self.discountPercent / 100

	def discountPrice(self):
		return self.price - self.discountAmount()