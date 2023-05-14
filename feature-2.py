def _lis(arr, n, max_ref):
    if n == 1:
        return 1
    max_ending_here = 1
    for i in range(1, n):
        res = _lis(arr, i, max_ref)
        if arr[i-1] < arr[n-1] and res + 1 > max_ending_here:
            max_ending_here = res + 1
    if max_ref[0] < max_ending_here:
        max_ref[0] = max_ending_here
    return max_ending_here

def lis(arr):
    n = len(arr)
    max_ref = [1]
    _lis(arr, n, max_ref)
    return max_ref[0]
