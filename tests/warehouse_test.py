import pytest
from ecommerce_tcc.domain.product import Product
from unittest.mock import Mock
from ecommerce_tcc.services.warehouse import Warehouse
from ecommerce_tcc.domain.exceptions import InvalidProductException, ProductDoesNotExistExcpetion

# TODO: CONSERTAR TESTES QUEBRADOS

def test_add_new_product_to_warehouse():
  #arrange 
  product = Product(sku="fake_name", desc="fake_desc", photo="fake_photo", available_qty=25, price="255.5")
  fake_repo = Mock()
  fake_repo.get.return_value = product
  warehouse = Warehouse(fake_repo)
  
  #act
  warehouse.add_new_product(product)
  
  #assert
  assert warehouse.get_product("fake_name") == product


def test_add_new_product_when_qty_negative_raise_exception():
  #arrange
  fake_repo = Mock()
  warehouse = Warehouse(fake_repo)
  product = Product("fake_name", "fake_desc", "fake_photo", -10, price="255.5")
  
  #act/assert
  with pytest.raises(InvalidProductException):
    warehouse.add_new_product(product)
    

def test_delete_product_from_warehouse():
  # arrange
  fake_repo = Mock()
  warehouse = Warehouse(fake_repo)
  product = Product("fake_name", "fake_desc", "fake_photo", 25, price="256.6")

  # act
  warehouse.add_new_product(product)
  warehouse.delete_product(product)
  
  # assert
  with pytest.raises(ProductDoesNotExistExcpetion):
    fake_repo.get.return_value = None
    warehouse.get_product("fake_name")
    
  
def test_get_all_products_from_warehouse():
  #arrange
  product = Product("fake_name", "fake_desc", "fake_photo", 25, price="256.6")
  product2 = Product("fake_name", "fake_desc", "fake_photo", 50, price="253.6")
  fake_repo = Mock()
  fake_repo.list.return_value = [product, product2]
  warehouse = Warehouse(fake_repo)
 
  #act
  warehouse.add_new_product(product)
  warehouse.add_new_product(product2)
  all_products = warehouse.get_all_products()
    
  #assert
  assert all_products == [product, product2]
    