from src.hw2_debugging import mergeSort


def test_single_element_array():
    arr = [1]
    sorted_array = mergeSort(arr)
    assert sorted_array == arr
