def haha(tiles):
    if len(tiles) == 1:
        return True
    elif tiles[0] == 0:
        return False
    else:
        for j in range(1, tiles[0] + 1):
            if j < len(tiles):
                if haha(tiles[j:]):
                    return True
        return False

tiles = list(map(int, input().split()))
print(haha(tiles))

