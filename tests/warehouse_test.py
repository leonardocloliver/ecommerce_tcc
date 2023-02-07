from ecommerce_tcc.warehouse import Warehouse
from ecommerce_tcc.product import Product

def test_add_new_product_to_warehouse():
  #arrange 
  warehouse = Warehouse()
  product = Product("fake_id","fake_name", "fake_desc", "fake_photo", 25, "255.5")
    
  #act
  warehouse.add_new_product(product)
    
  #assert
  assert warehouse.get_product("fake_id") == product


def test_update_product_in_warehouse():
  # arrange
  warehouse = Warehouse()
  product = Product("fake_id", "fake_name", "fake_desc", "fake_photo", 25, "256.6")
  new_product = Product("fake_id", "fake_name", "fake_desc", "fake_photo", 50, "256.6")
  
  # act
  warehouse.add_new_product(product)
  warehouse.update_product(new_product)

  # assert
  assert warehouse.get_product("fake_id").available_qty == 50
  

def test_delete_product_from_warehouse():
  # arrange
  warehouse = Warehouse()
  product = Product("fake_id", "fake_name", "fake_desc", "fake_photo", 25, "256.6")

  # act
  warehouse.add_new_product(product)
  warehouse.delete_product(product)

  # assert
  assert not warehouse.get_product("fake_id")
  

def test_get_all_products_from_warehouse():
  #arrange
  warehouse = Warehouse()
  product = Product("fake_id", "fake_name", "fake_desc", "fake_photo", 25, price="256.6")
  product2 = Product("fake_id1", "fake_name", "fake_desc", "fake_photo", 50, price="253.6")
    
  #act
  warehouse.add_new_product(product)
  warehouse.add_new_product(product2)
  all_products = warehouse.get_all_products()
    
  #assert
  assert all_products == [product, product2]
    