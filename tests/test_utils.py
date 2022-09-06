import unittest
from autom8it import Log
from autom8it import get_class_by_name, HttpRequestTask


class TestMe:

    def get_test_value(self):
        return self.__hash__()


class UtilsTestCase(unittest.TestCase):

    def test_class_by_name(self):
        Log.info(f'Class name is {TestMe.__name__}, {self.__module__}')
        cls = get_class_by_name('test_utils.TestMe', requested_type=TestMe)
        inst_a = cls()
        self.assertEqual(inst_a.__hash__(), inst_a.get_test_value())

    def test_my_order(self):
        self.m_a()
        self.m_c()
        self.m_b()

    def m_a(self):
        Log.debug('Test A')
        self.assertEqual(True, True)

    def m_c(self):
        Log.debug('Test C')
        self.assertEqual(True, True)

    def m_b(self):
        Log.debug('Test B')
        self.assertEqual(True, True)

    def test_http_task(self):
        task_data = {
            HttpRequestTask.HTTP_METHOD: 'get',
            HttpRequestTask.URL: 'http://www.google.com',
            HttpRequestTask.DATA: {"text": "Hello"}
        }
        resp = HttpRequestTask(task_data=task_data).run()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
