# Problem
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
# Score: 20

#------------------------------------------------
# Solution 1: (Terminated due to timeout)

# def climbingLeaderboard(ranked, player):
    # pos = []
    # rank = sorted(set(ranked), reverse=True)
    # print(rank)
    # for p in player:
        # if p < min(rank):
            # pos.append(len(rank) + 1)
        # elif p > max(rank):
            # pos.append(1)
        # else:
            # cont = 1
            # for r in rank[::-1]:
                # if p >= r:
                    # pos.append(rank.index(r))
                    # print(rank.index(r))
                    # break
                # cont += 1

# Solution 2:
def climbingLeaderboard(ranked, player):
    rank = sorted(list(set(ranked)))
    pos = []
    i = 0
    length = len(rank)
    for p in player:
        while length > i and p >= rank[i]:
            i += 1
        pos.append(length + 1 - i)

    return pos

#------------------------------------------------
# Input

ranked = [100, 100, 50, 40, 40, 20, 10]
players = [5, 25, 50, 120]
print(climbingLeaderboard(ranked, players))
ranked = [100, 90, 90, 80, 75, 60]
players = [50, 65, 77, 90, 102]
print(climbingLeaderboard(ranked, players))

