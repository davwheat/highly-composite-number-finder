print("This starts to get VERY slow at 20 000 or above.")
val = int(input("Enter max num: "))

num = 0
currentBest = {"num": 0, "factors": [0]}
while True:
    if num > val:
        break

    num += 1
    factors = []

    for i in range(1, round((num + 1) / 2)):
        if num % i == 0:
            factors.append(i)
            # If x is a factor of n, n/x will be a factor too
            factors.append(num / i)

    if len(factors) > len(currentBest["factors"]):
        # New best!
        currentBest = {"num": num, "factors": factors}
        print(f"== NEW BEST ==\n  num: {num}\ncount: {len(factors)}")
