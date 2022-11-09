if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = list(arr)
    l = [arr1[i] for i in range(len(arr1)) if max(arr1) - arr1[i] != 0]
    print(max(l))
