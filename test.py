def name_game(word):
    return "{0},{0} bo-b{1},\nBonana-fanana fo-f{1}\nFee fi mo-m{1}\n{0}!".format(
        word,
        word[1:],
    )


print(name_game("Caleb"))
