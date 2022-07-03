from math import cos, sin, pi
ANGLECONST = pi / 180

def scaling(scaling_factor):

    # scaling(2) = [[2.0, 0.0], [0.0, 2.0]]
    scaling_factor = float(scaling_factor)
    return [[scaling_factor * int(x == y) for x in range(2)] for y in range(2)]

def rotation(angle):
    # rotation(90) = [[0.0, -1.0], [1.0, 0.0]]
    angle = angle * ANGLECONST # radian to degree
    c, s = cos(angle), sin(angle)
    s = round(s, 6)
    c = round(c, 6)
    return [[c, -s], [s, c]]

def projection(angle):
    # projection(90)  = [[0.0, 0.0], [0.0, 1.0]] projection of y-axis
    # projection(360) = [[1.0, 0.0], [0.0, 0.0]] projection of x-axis
    angle = angle * ANGLECONST  # radian to degree
    c, s = cos(angle), sin(angle)
    s = round(s, 6)
    c = round(c, 6)
    cs = c * s
    return [[c * c, cs], [cs, s * s]]

def reflection(angle):
    # refletion(90)   = [[-1.0, 0.0], [0.0, 1.0]] reflection of y-axis
    # reflection(360) = [[-1.0, 0.0], [0.0, 1.0]] reflection of x-axis
    angle = angle * ANGLECONST  # radian to degree
    c, s = cos(angle), sin(angle)
    s = round(s, 6)
    c = round(c, 6)
    cs = c * s
    return [[2 * c - 1, 2 * cs], [2 * cs, 2 * s - 1]]

def main():
    print(scaling(5))
    print(rotation(90))
    print(projection(90))
    print(projection(360))
    print(reflection(90))
    print(reflection(360))
    
if __name__ == "__main__":
    main()