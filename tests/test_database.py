from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestDatabase:
    def test_available_buns(self):
        database = Database()
        available_buns = database.available_buns()
        assert available_buns[1].get_name() == "white bun" and available_buns[1].get_price() == 200

    def test_available_ingredients(self):
        database = Database()
        available_ingredients = database.available_ingredients()
        assert (
            available_ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE and
            available_ingredients[0].get_name() == "hot sauce" and
            available_ingredients[0].get_price() == 100
        )





