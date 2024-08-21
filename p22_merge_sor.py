def merge_sort(arr: List[int])->List[int]:
    pass

def insertion_sort(unsorted: List[int]) -> List[int]:
    sorted_list = []
    for i in range(len(unsorted)):
        j = 0
        while j < len(sorted_list) and sorted_list[j] < unsorted[i]:
            j += 1
        sorted_list.insert(j, unsorted[i])
    return sorted_list


if __nam__ == "__main__":
