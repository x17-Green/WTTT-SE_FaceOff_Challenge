// style.js
let currentPlayer = 'X';
let gameActive = true;
const statusDisplay = document.getElementById('status');
const winningCombos = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
    [0, 4, 8], [2, 4, 6]             // Diagonals
];
let board = ['', '', '', '', '', '', '', '', ''];

statusDisplay.textContent = `Player ${currentPlayer}'s turn`;

document.getElementById('play-btn').addEventListener('click', () => {
    document.querySelector('.banner').style.display = 'none';
    document.querySelector('.game-board').style.display = 'block';
});

function makeMove(cell) {
    const index = cell.getAttribute('data-index');
    if (board[index] === '' && gameActive) {
        board[index] = currentPlayer;
        cell.textContent = currentPlayer;
        cell.classList.add(currentPlayer.toLowerCase());
        
        if (checkWin()) {
            statusDisplay.textContent = `Player ${currentPlayer} wins!`;
            gameActive = false;
            displayGameResults(`Player ${currentPlayer} wins!`);
            return;
        }
        
        if (checkDraw()) {
            statusDisplay.textContent = "It's a draw!";
            gameActive = false;
            displayGameResults("It's a draw!");
            return;
        }
        
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        statusDisplay.textContent = `Player ${currentPlayer}'s turn`;
    }
}

function checkWin() {
    for (let i = 0; i < winningCombos.length; i++) {
        const [a, b, c] = winningCombos[i];
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            markWinningCells(a, b, c, i);
            return true;
        }
    }
    return false;
}

function markWinningCells(a, b, c, comboIndex) {
    const cells = document.querySelectorAll('.cell');
    cells[a].classList.add('winner');
    cells[b].classList.add('winner');
    cells[c].classList.add('winner');

    if (comboIndex < 3) {
        cells[a].classList.add('winner-row');
        cells[b].classList.add('winner-row');
        cells[c].classList.add('winner-row');
    } else if (comboIndex < 6) {
        cells[a].classList.add('winner-col');
        cells[b].classList.add('winner-col');
        cells[c].classList.add('winner-col');
    } else {
        cells[a].classList.add('winner-diag');
        cells[b].classList.add('winner-diag');
        cells[c].classList.add('winner-diag');
        if (comboIndex === 6) {
            cells[a].classList.add('winner-diag-1');
            cells[b].classList.add('winner-diag-1');
            cells[c].classList.add('winner-diag-1');
        } else {
            cells[a].classList.add('winner-diag-2');
            cells[b].classList.add('winner-diag-2');
            cells[c].classList.add('winner-diag-2');
        }
    }
}

function checkDraw() {
    return board.every(cell => cell !== '');
}

function displayGameResults(result) {
    const gameResultsElement = document.getElementById('game-results');
    gameResultsElement.textContent = result;
    gameResultsElement.style.display = 'block';
    gameResultsElement.style.fontSize = '64px';
    gameResultsElement.style.fontWeight = 'bold';
    gameResultsElement.style.textAlign = 'center';
    gameResultsElement.style.animation = 'fadeIn 2s';

    const boardElement = document.querySelector('.board');
    boardElement.style.opacity = 0.5;
    boardElement.style.pointerEvents = 'none';

    const restartButton = document.getElementById('restart-btn');
    restartButton.style.display = 'block';
    restartButton.onclick = function() {
        gameResultsElement.style.display = 'none';
        boardElement.style.opacity = 1;
        boardElement.style.pointerEvents = 'auto';
        restartButton.style.display = 'none';
        restartGame();
    };
}

function restartGame() {
    currentPlayer = 'X';
    gameActive = true;
    board = ['', '', '', '', '', '', '', '', ''];
    statusDisplay.textContent = `Player ${currentPlayer}'s turn`;
    document.querySelectorAll('.cell').forEach(cell => {
        cell.textContent = '';
        cell.classList.remove('x', 'o', 'winner', 'winner-row', 'winner-col', 'winner-diag', 'winner-diag-1', 'winner-diag-2');
    });
    const gameResultsElement = document.getElementById('game-results');
    gameResultsElement.style.display = 'none';
    const boardElement = document.querySelector('.board');
    boardElement.style.opacity = 1;
    boardElement.style.animation = '';
}