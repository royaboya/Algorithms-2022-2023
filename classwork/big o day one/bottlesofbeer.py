def BottlesOfBeer(n):
    for i in range(n, 1, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down, pass it around, {i-1} bottles of beer on the wall")
    print(f"0 bottles of beer on the wall, 0 bottles of beer.")
    print(f"Go to the store and buy some more, n bottles of beer on the wall.")


BottlesOfBeer(100)
