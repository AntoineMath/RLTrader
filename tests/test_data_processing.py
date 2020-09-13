import unittest
from ddt import ddt, data, unpack
from rl_trader.data_processing import klines_to_ohcl, datetime
from .data.chart1 import KLINES1
from .data.chart2 import KLINES2


@ddt
class TestDataProcessing(unittest.TestCase):
    @unpack
    @data({"klines_list": KLINES1}, {"klines_list": KLINES2})
    def test_klines_to_ohcl(self, klines_list):
        ohcl_dict = klines_to_ohcl(klines_list)

        self.assertTrue(all(isinstance(value, list) for value in ohcl_dict.values()))

        # test if all o, h, c, l lists have the same length
        len_dict = len(ohcl_dict["t"])
        self.assertTrue(all(len(value) == len_dict for value in ohcl_dict.values()))

        self.assertTrue(
            all(isinstance(value, datetime.datetime) for value in ohcl_dict["t"])
        )
