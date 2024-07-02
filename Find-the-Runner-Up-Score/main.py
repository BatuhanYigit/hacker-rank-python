def find_the_runner_up(n, arr):
    not_duplice = list(set(arr))
    not_duplice.sort(reverse=True)
    runner_up = not_duplice[1]

    return runner_up


if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    result = find_the_runner_up(n, arr)
    print(result)
