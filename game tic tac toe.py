papan = [' ' for _ in range(9)]

def cetak_papan():
    row1 = '| {} | {} | {} |'.format(papan[0], papan[1], papan[2])
    row2 = '| {} | {} | {} |'.format(papan[3], papan[4], papan[5])
    row3 = '| {} | {} | {} |'.format(papan[6], papan[7], papan[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def main():
    current_player = 'X'
    while True:
        cetak_papan()
        move = input("Masukkan posisi (1-9): ")
        if papan[int(move) - 1] == ' ':
            papan[int(move) - 1] = current_player
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
        else:
            print("Posisi sudah terisi!")

main()
