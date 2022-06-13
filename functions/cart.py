

#structure:
# -- id: int
# -- title: str
# -- images: arr
#    -- title: str
#    -- desctiption: str
#    -- image: file
# -- size: arr 
#    -- weight: int
#    -- metrics: str
# -- price: arr
# -- price_discount: arr
# -- currency: str
# -- in_stock: bool(True/False/None), specifing none means not to display


cart_positions = [
	{
		"id": 1,
		"title": 'Tomato',
		"images": [
			{
				"title": 'Tomato 1',
				"description": None,
				"image_url": 'url to file'
			},
			{
				"title": 'Tomato 2',
				"description": None,
				"image_url": 'url to file'
			},
		],
		"sizes": [
			{
				"weight": 100,
				"metrics": 'grams'
				"price": 100,
				"discount_percent": 10
			},
			{
				"weight": 500,
				"metrics": 'grams',
				"price": 150,
				"discount_percent": None, 
			}
		],
		"currency": 'UAH',
		"in_stock": True
	}
]

class Cart():
	def __init__(self, cart_positions):
		self.cart_positions = cart_positions
	
	def get(self):
		return cart_json

	def clear(self):
		#clear_cart
		return 0

	def insert(self, cart_object):
		#insert object
		return 0
	def remove(self, cart_object_id):
		#remove element by id
		return 0

	def increase_by_id(self, cart_object_id):
		#increase cart object quantity  by id
		return 0

	def decrease_by_id(self, cart_object_id):
		#decrease cart object quantity by id
		return 0


for item in Cart(cart_positions).cart_positions:
	print(item)