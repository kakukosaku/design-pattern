import unittest

from design_pattern.creational.strategy import StrategyContainerBase, StrategyConfig, StrategyFactory, \
    strategy_factory_register


class Validator:

    def __init__(self, data):
        self.data = data


class License:
    MARSCO = "MARSCO"
    USTS = "USTS"
    TBNZ = "TBNZ"


class Clearing:
    MARSCO = "MARSCO"
    IB = "IB"


class Category:
    INDIVIDUAL = "Individual"
    RIA = "RIA"


class TestStrategyContainer(unittest.TestCase):

    def test_no_default_impl_cls(self):
        with self.assertRaises(ValueError):
            class Container(StrategyContainerBase):
                class T(Validator):
                    _strategy = {
                        "license": License.MARSCO,
                        "clearing": Clearing.IB,
                        # "default": True,
                    }

            test_data = {
                "license": License.MARSCO,
                "clearing": Clearing.IB,
            }
            Container(test_data)

    def test_multiple_default_impl_cls(self):
        with self.assertRaises(ValueError):
            class Container(StrategyContainerBase):
                class T1(Validator):
                    _strategy = {
                        "license": License.MARSCO,
                        "clearing": Clearing.IB,
                        "default": True,
                    }

                class T2(Validator):
                    _strategy = {
                        "license": License.MARSCO,
                        "clearing": Clearing.IB,
                        "default": True,
                    }

            test_data = {
                "license": License.MARSCO,
                "clearing": Clearing.IB,
            }
            Container(test_data)

    def test_correctly_choice_impl_cls(self):
        class Container(StrategyContainerBase):
            class T1(Validator):
                _strategy = {
                    "license": License.USTS,
                    "clearing": Clearing.IB,
                    "default": True,
                }

            class T2(Validator):
                _strategy = {
                    "license": License.MARSCO,
                    "clearing": Clearing.IB,
                    "default": False,
                }

            class T3(Validator):
                _strategy = {
                    "license": License.MARSCO,
                    "clearing": Clearing.MARSCO,
                    "default": False,
                }

        test_data1 = {
            "license": License.USTS,
            "clearing": Clearing.IB,
        }
        c1 = Container(test_data1)
        self.assertIsInstance(c1, Container.T1)

        test_data2 = {
            "license": License.MARSCO,
            "clearing": Clearing.IB,
        }
        c2 = Container(test_data2)
        self.assertIsInstance(c2, Container.T2)

        test_data3 = {
            "license": License.MARSCO,
            "clearing": Clearing.MARSCO,
        }
        c3 = Container(test_data3)
        self.assertIsInstance(c3, Container.T3)

        # switch to default cls
        test_data4 = {
            "license": License.MARSCO,
            # "clearing": Clearing.MARSCO,
        }
        c4 = Container(test_data4)
        self.assertIsInstance(c4, Container.T1)


class TestStrategyInterface(unittest.TestCase):

    def test_general_impl(self):
        s0 = StrategyConfig(category=Category.INDIVIDUAL,
                            license=License.TBNZ, clearing=Clearing.IB)

        s1 = StrategyConfig(category=Category.INDIVIDUAL,
                            license=License.TBNZ, clearing=Clearing.IB)
        s2 = StrategyConfig(category=Category.INDIVIDUAL,
                            license=License.MARSCO, clearing=Clearing.MARSCO)
        s3 = StrategyConfig(category=Category.RIA,
                            license=License.MARSCO, clearing=Clearing.IB)

        strategy_config = {
            "category": Category.INDIVIDUAL,
            "license": License.TBNZ,
            "clearing": Clearing.IB,
        }
        self.assertTrue(strategy_config == s0.get_strategy_config())
        strategy_map = {
            s1: 1,
            s2: 2,
            s3: 3,
        }
        self.assertTrue(s0 == s0)
        self.assertTrue(s0 == s1)
        self.assertTrue(s1 != s2)
        self.assertTrue(s2 != s3)

        self.assertTrue(1 == strategy_map[s0])
        self.assertTrue(1 == strategy_map[s1])
        self.assertTrue(2 == strategy_map[s2])
        self.assertTrue(
            3 == strategy_map[StrategyConfig(
                category=Category.RIA, license=License.MARSCO, clearing=Clearing.IB)]
        )


class TestStrategyRegister(unittest.TestCase):

    def test_register(self):
        class JobInfoValidator(StrategyFactory):
            pass

        @strategy_factory_register(JobInfoValidator, default=True, license="Marsco", clearing="ib")
        class MarscoIB(object):

            def __init__(self, data):
                self.data = data

        @strategy_factory_register(JobInfoValidator, default=False, license="Marsco", clearing="marsco")
        @strategy_factory_register(JobInfoValidator, default=False, license="re-register", clearing="re-register")
        class MarscoMarsco(object):

            def __init__(self, data):
                self.data = data

        c1 = JobInfoValidator(
            {
                "license": "Marsco",
                "clearing": "ib"
            }
        )
        self.assertIsInstance(c1, MarscoIB)

        c2 = JobInfoValidator(
            {
                "license": "Marsco",
                "clearing": "marsco"
            }
        )
        self.assertIsInstance(c2, MarscoMarsco)

        c3 = JobInfoValidator(
            {
                "license": "re-register",
                "clearing": "re-register"
            }
        )
        self.assertIsInstance(c3, MarscoMarsco)

        c4 = JobInfoValidator(
            {
                "license": "mismatch",
                # "clearing": "lack_key"
            }
        )
        self.assertIsInstance(c4, MarscoIB)
