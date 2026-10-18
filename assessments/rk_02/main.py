from test_queries import QueryTests
import unittest


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(QueryTests))
    raise SystemExit(0 if result.wasSuccessful() else 1)
