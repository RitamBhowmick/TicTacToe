#include <bits/stdc++.h>
using namespace std;

char board[3][3] = { {'1','2','3'},
                     {'4','5','6'},
                     {'7','8','9'} };

char currentMarker;
int currentPlayer;

void drawBoard() {
    cout << "\n";
    cout << " " << board[0][0] << " | " << board[0][1] << " | " << board[0][2] << "\n";
    cout << "---|---|---\n";
    cout << " " << board[1][0] << " | " << board[1][1] << " | " << board[1][2] << "\n";
    cout << "---|---|---\n";
    cout << " " << board[2][0] << " | " << board[2][1] << " | " << board[2][2] << "\n\n";
}

bool placeMarker(int slot) {
    int row = (slot - 1) / 3;
    int col = (slot - 1) % 3;

    if (board[row][col] != 'X' && board[row][col] != 'O') {
        board[row][col] = currentMarker;
        return true;
    } else {
        return false;
    }
}

int checkWinner() {
    // Rows, Columns, Diagonals
    for (int i = 0; i < 3; i++) {
        // Rows
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2])
            return currentPlayer;
        // Columns
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i])
            return currentPlayer;
    }
    // Diagonals
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2])
        return currentPlayer;
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0])
        return currentPlayer;

    return 0;
}

void swapPlayerAndMarker() {
    if (currentMarker == 'X') {
        currentMarker = 'O';
        currentPlayer = 2;
    } else {
        currentMarker = 'X';
        currentPlayer = 1;
    }
}

int main() {
    cout << "TIC TAC TOE GAME\n";
    cout << "Player 1, choose your marker (X or O): ";
    cin >> currentMarker;
    currentPlayer = 1;

    int winner = 0;
    int moves = 0;

    drawBoard();

    while (winner == 0 && moves < 9) {
        int slot;
        cout << "Player " << currentPlayer << " [" << currentMarker << "], enter your move (1-9): ";
        cin >> slot;

        if (slot < 1 || slot > 9) {
            cout << "Invalid slot. Try again.\n";
            continue;
        }

        if (!placeMarker(slot)) {
            cout << "Slot already taken. Try again.\n";
            continue;
        }

        drawBoard();
        winner = checkWinner();
        swapPlayerAndMarker();
        moves++;
    }

    if (winner != 0)
        cout << "Player " << winner << " wins!\n";
    else
        cout << "It's a draw!\n";

    return 0;
}
