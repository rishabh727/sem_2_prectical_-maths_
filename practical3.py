from itertools import permutations, product

def generate_permutations(Set, repetition):
    if repetition:
        return list(permutations(Set))
    else:
        return list(product(Set, repeat=len(Set)))

if __name__ == "__main__":
    Set = set(map(int, input("Enter all elements of set with space: ").split()))
    with_repetition = generate_permutations(Set, repetition=True)
    without_repetition = generate_permutations(Set, repetition=False)
    print("Permutations with repetition:")
    for perm in with_repetition:
        print(perm)
    print("\nPermutations without repetition:")
    for perm in without_repetition:
        print(perm)
