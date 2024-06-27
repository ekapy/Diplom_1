from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import DataBurger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun('testkateburger', 199)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(DataBurger.ingredients[0], DataBurger.ingredients[0], DataBurger.ingredients[0])
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(DataBurger.ingredients[1], DataBurger.ingredients[1], DataBurger.ingredients[1])
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_0 = Ingredient(DataBurger.ingredients[0], DataBurger.ingredients[0], DataBurger.ingredients[0])
        burger.add_ingredient(ingredient_0)
        ingredient_1 = Ingredient(DataBurger.ingredients[1], DataBurger.ingredients[1], DataBurger.ingredients[1])
        burger.add_ingredient(ingredient_1)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ingredient_1
        assert burger.ingredients[1] == ingredient_0

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = DataBurger.buns[0][1]
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = DataBurger.ingredients[0][2]
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        expected_price = mock_bun.get_price() * 2 + mock_ingredient.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = DataBurger.buns[1][0]
        mock_bun.get_price.return_value = DataBurger.buns[1][1]
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = DataBurger.ingredients[4][1]
        mock_ingredient.get_price.return_value = DataBurger.ingredients[4][2]
        burger.bun = mock_bun
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        text = f'= {mock_ingredient.get_type().lower()} {mock_ingredient.get_name()} ='
        assert text in receipt






