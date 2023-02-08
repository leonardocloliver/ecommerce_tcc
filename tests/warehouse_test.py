import pytest
from ecommerce_tcc.domain.warehouse import Warehouse
from ecommerce_tcc.domain.product import Product
from ecommerce_tcc.domain.exceptions import InvalidProductException, ProductDoesNotExistExcpetion


def test_add_new_product_to_warehouse():
  #arrange 
  warehouse = Warehouse()
  product = Product("fake_id","fake_name", "fake_desc", "fake_photo", 25, price="255.5")
    
  #act
  warehouse.add_new_product(product)
    
  #assert
  assert warehouse.get_product("fake_id") == product
  
  
def test_add_new_product_when_qty_negative_raise_exception():
  #arrange
  warehouse = Warehouse()
  product = Product("fake_id", "fake_name", "fake_desc", "fake_photo", -10, price="255.5")
  
  #act/assert
  with pytest.raises(InvalidProductException):
    warehouse.add_new_product(product)

  
def test_update_product_in_warehouse():
  # arrange
  warehouse = Warehouse()
  product = Product("fake_id", "fake_name", "fake_desc", "fake_photo", 25, price="256.6")
  new_product = Product("fake_id", "fake_name", "fake_desc", "fake_photo", 50, price="256.6")
  
  # act
  warehouse.add_new_product(product)
  warehouse.update_product(new_product)

  # assert
  assert warehouse.get_product("fake_id").available_qty == 50
  
def test_update_product_invalid_in_warehouse():
  #arrange
  warehouse = Warehouse()
  product = Product("fake_id", "fake_name", "fake_desc", "fake_photo", 24, price="240")
  
  #act/assert
  with pytest.raises(ProductDoesNotExistExcpetion):
    warehouse.update_product(product)
    

def test_delete_product_from_warehouse():
  # arrange
  warehouse = Warehouse()
  product = Product("fake_id", "fake_name", "fake_desc", "fake_photo", 25, price="256.6")

  # act
  warehouse.add_new_product(product)
  warehouse.delete_product(product)

  # assert
  with pytest.raises(ProductDoesNotExistExcpetion):
    warehouse.get_product("fake_id")
    
  
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
    