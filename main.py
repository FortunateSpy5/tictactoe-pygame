import pygame

pygame.init()

size = 450
cell_size = size // 3
screen = pygame.display.set_mode((size, size))
clock = pygame.time.Clock()

board_img = pygame.image.load('board.png')
board_img = pygame.transform.scale(board_img, (size, size))

o_img = pygame.image.load('o.png')
o_img = pygame.transform.scale(
    o_img, (int(cell_size * 0.8), int(cell_size * 0.8)))

x_img = pygame.image.load('x.png')
x_img = pygame.transform.scale(
    x_img, (int(cell_size * 0.8), int(cell_size * 0.8)))

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
player1 = True
count = 0


def reset():
    global board
    global player1
    print("\nGame Reset\n")
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    player1 = True


def draw():
    pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(0, 0, size, size))

    screen.blit(board_img, (0, 0))

    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                screen.blit(
                    x_img, ((i + 0.1) * cell_size, (j + 0.1) * cell_size))
            elif board[i][j] == 2:
                screen.blit(
                    o_img, ((i + 0.1) * cell_size, (j + 0.1) * cell_size))

    pygame.display.update()


while True:
    clock.tick(100)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            pos = [pos[0] // cell_size, pos[1] // cell_size]

            if board[pos[0]][pos[1]] == 0:
                count += 1

                board[pos[0]][pos[1]] = 1 if player1 else 2
                player1 = not player1

                board_set = [set(), set(), set()]
                for i in range(3):
                    for j in range(3):
                        board_set[i].add(board[j][i])
                for i in range(3):
                    board_set.append(set(board[i]))
                board_set.append(set([board[0][0], board[1][1], board[2][2]]))
                board_set.append(set([board[0][2], board[1][1], board[2][0]]))

                # print(board_set)

                if {1} in board_set:
                    print("Player 1 won")
                    reset()

                if {2} in board_set:
                    print("Player 2 won")
                    reset()
                
                if count == 9:
                    print("Draw")
                    reset()
