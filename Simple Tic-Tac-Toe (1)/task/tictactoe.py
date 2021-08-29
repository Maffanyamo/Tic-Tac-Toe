m = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
i = 1
char = "Y"

def main():
    print_grid(m)
    while i <= 9:
      coordinates()
    if i == 10:
      print("Draw")

def x_or_o(i, char):
  if i % 2 == 1:
    char = "X"
  else:
    char = "O"
  return char

def coordinates():

    x, y = input("Enter the coordinates: ").split()
    global i, char
    if x.isdigit() == False or y.isdigit() == False:
     print("You should enter numbers!")
     return coordinates()

    x = int(x)
    y = int(y)
    if x > 3 or y > 3 or x < 1 or y < 1:
        print("Coordinates should be from 1 to 3")
        coordinates()
    elif m[x - 1][y - 1] == " ":
        # x_or_o(i, char)
        if i % 2 == 1:
            char = "X"
        else:
            char = "O"
        m[x - 1][y - 1] = char
        print_grid(m)
        i += 1
        if i > 2 and (m[x - 1] == [char, char, char] or [m[0][y -1], m[1][y - 1], m[2][y - 1]] == [char, char, char] or [m[0][0], m[1][1], m[2][2]] == [char, char, char] or [m[0][2], m[1][1], m[2][0]] == [char, char, char]):
            print(char + " wins")
            i = 100
        return m, i
    else:
        print("This cell is occupied! Choose another one!")
        coordinates()


def print_grid(m):
    grid = [" ".join(m[0]), " ".join(m[1]), " ".join(m[2])]
    print("-" * 9)
    print("|", " |\n| ".join(grid), "|")
    print("-" * 9)


main()

