def alternate_glasses(glasses):
    n = len(glasses) // 2  # Number of pairs
    filled = []
    empty = []

    for i, glass in enumerate(glasses):
        if glass == "filled":
            filled.append(i)
        else:
            empty.append(i)

    result = [None] * len(glasses)
    for i in range(0, len(glasses), 2):
        result[i] = "filled"
    for i in range(1, len(glasses), 2):
        result[i] = "empty"

    moves = 0
    for i in range(n):
        x = filled[i]
        y = empty[i]

        while y > x:
            result[y], result[y - 2] = result[y - 2], result[y]
            y -= 2
            moves += 1

        while y < x:
            result[y], result[y + 2] = result[y + 2], result[y]
            y += 2
            moves += 1

    return result, moves

def get_glasses_input():
    n = int(input("Enter the number of glasses (n): "))
    glasses = ["filled"] * n + ["empty"] * n
    return glasses

def main():
    glasses = get_glasses_input()
    result, moves = alternate_glasses(glasses)
    print("Initial state:", glasses)
    print("Final state:", result)
    print("Number of moves:", moves)

if __name__ == "__main__":
    main()
