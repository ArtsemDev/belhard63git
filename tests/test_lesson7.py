import pytest

from lesson7 import reverse_list


# def test_reverse_list():
#     data = (([1, 2, 34, 4], [4, 3, 2, 1]), ([5, 4, 67, 7], [7, 67, 4, 5]))
#     for i, j in data:
#         # if reverse_list(i) == j:
#         #     print('test passed')
#         # else:
#         #     print('test fail')
#         try:
#             assert reverse_list(i) == j
#         except AssertionError:
#             print('passed failed')
#         else:
#             print('test passed')
#
#
# test_reverse_list()


# class SimpleTestCase(unittest.TestCase):
#
#     def test_reverse_list(self):
#         self.assertEqual(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])
#
#     def test_reverse_list2(self):
#         self.assertEqual(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])


@pytest.mark.skipif(2 == 4, reason="error")
@pytest.mark.parametrize(
    "a, b",
    (
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([2, 3, 2], [2, 3, 2]),
        ([6, 5, 4, 3], [3, 4, 5, 6]),
    )
)
def test_reverse_list(a, b):
    assert reverse_list(a) == b
