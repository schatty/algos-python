def sift_down(heap, idx):
    left = 2 * idx
    right = 2 * idx + 1

    if len(heap) - 1 < left:
        return idx

    if right <= len(heap) - 1 and heap[left] < heap[right]:
        idx_largest = right
    else:
        idx_largest = left

    if heap[idx]  < heap[idx_largest]:
        heap[idx], heap[idx_largest]= heap[idx_largest], heap[idx]
        return sift_down(heap, idx_largest)
    return idx
           

def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5



