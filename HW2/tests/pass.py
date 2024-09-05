from src.hw2_debugging import mergeSort


def test_single_element_array():
    arr = [1]
    sorted_array = mergeSort(arr)
    assert sorted_array == arr

def test_normal_array():
    arr = [2,5,3,8,9,6]
    sort_array = mergeSort(arr)
    assert sort_array == [2,3,5,6,8,9]