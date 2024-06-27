import pytest
from praktikum.bun import Bun
from data import DataBurger


class TestBun:
    @pytest.mark.parametrize('buns, price', DataBurger.buns)
    def test_get_name(self, buns, price):
        bun_name = Bun(buns, price)
        assert bun_name.get_name() == buns

    @pytest.mark.parametrize('buns, price', DataBurger.buns)
    def test_get_price(self, buns, price):
        bun_price = Bun(buns, price)
        assert bun_price.get_price() == price
