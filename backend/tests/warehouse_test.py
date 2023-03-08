import pytest
from unittest.mock import Mock
from ecommerce_tcc.services.warehouse import Warehouse
from ecommerce_tcc.domain.exceptions import InvalidProductException, ProductDoesNotExistExcpetion
    
      
def test_add_new_product_to_warehouse():
  #arrange 
  new_product = {"sku":"fake_name", "desc":"fake_desc", "photo":"fake_photo", "available_qty":25, "price":"255.5"}
  fake_repo = Mock()
  warehouse = Warehouse(fake_repo)
  
  #act
  product_id = warehouse.add_new_product(new_product)
  
  #assert
  assert product_id


def test_add_new_product_when_qty_negative_raise_exception():
  #arrange
  fake_repo = Mock()
  warehouse = Warehouse(fake_repo)
  new_product = {"sku":"fake_name", "desc":"fake_desc", "photo":"fake_photo", "available_qty":-25, "price":"255.5"}
 
  #act/assert
  with pytest.raises(InvalidProductException):
    warehouse.add_new_product(new_product)
    

def test_delete_product_from_warehouse():
  # arrange
  fake_repo = Mock()
  warehouse = Warehouse(fake_repo)
  new_product = {"sku":"fake_name", "desc":"fake_desc", "photo":"fake_photo", "available_qty":25, "price":"255.5"}

  # act
  product_id = warehouse.add_new_product(new_product)
  warehouse.delete_product(product_id)
  
  # assert
  with pytest.raises(ProductDoesNotExistExcpetion):
    fake_repo.get.return_value = None
    warehouse.get_product("fake_name")
    
  
def test_get_all_products_from_warehouse():
  #arrange
  new_product_1 = {"sku":"fake_name", "desc":"fake_desc", "photo":"fake_photo", "available_qty":25, "price":"255.5"}
  new_product_2 = {"sku":"fake_name", "desc":"fake_desc", "photo":"fake_photo", "available_qty":25, "price":"253.5"}
  fake_repo = Mock()
  fake_repo.list.return_value = [new_product_1, new_product_2]
  warehouse = Warehouse(fake_repo)
 
  #act
  warehouse.add_new_product(new_product_1)
  warehouse.add_new_product(new_product_2)
  all_products = warehouse.get_all_products()
    
  #assert
  assert all_products == [new_product_1, new_product_2]
    