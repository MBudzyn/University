def superciag(g1, g2):
    if len(g1) == 0:
        return g2
    if len(g2) == 0:
        return g1
    if g1[0] == g2[0]:
        return [g1[0]] + superciag(g1[1:], g2[1:])
    else:

        pom1 = [g1[0]] + superciag(g1[1:], g2)
        pom2 = [g2[0]] + superciag(g1, g2[1:])

        if len(pom1) > len(pom2):
            return pom2
        else:
            return pom1


print(superciag([1,2,3,4,7,1,2],[5,4,8,1,3,1]))