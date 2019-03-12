
//龍ONE

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class SudokuSolver {

    private static int solution[][] = new int[9][9];
    private static ArrayList[][] pencilMarks = new ArrayList[9][9];
    private static ArrayList[][] tempPencilMarks = new ArrayList[9][9];
    private static int[][] pencilMarkIndex = new int[9][9];
    private static final int[] DIGITS = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    private static final int BOX_LENGTH = 3;

    public static void main(String[] args) {
        boolean correctBoard = false;
        int sudokuBoard[][] = new int[9][9];
        Scanner scanInput = new Scanner(System.in);

        // get user input for the sudoku board
        while (correctBoard == false) {
            System.out.println("Input Sudoku Board from top to bottom row by row");
            System.out.println("Represent Blanks with the number 0, don't use spaces");

            // retrieve board
            for (int row = 0; row < sudokuBoard.length; row++) {
                String wholeRow = scanInput.next();
                for (int col = 0; col < sudokuBoard[row].length; col++) {
                    sudokuBoard[row][col] = Character.getNumericValue(wholeRow.charAt(col));
                }
                scanInput.nextLine();
            }

            // print board
            for (int row = 0; row < sudokuBoard.length; row++) {
                for (int col = 0; col < sudokuBoard[0].length; col++) {
                    System.out.print(sudokuBoard[row][col] + " ");
                }
                System.out.println();
            }

            // check if user input matches the sudoku board they desire
            System.out.println("Does this Sudoku Board match your inputted board? (yes or no)");
            String answer = scanInput.next();
            if (answer.equalsIgnoreCase("Yes")) {
                correctBoard = true;
            }
        }
        scanInput.close();

        // solve sudoku and calculate the time taken
        double startTime = System.nanoTime();
        solveBoard(sudokuBoard);
        double timeTaken = System.nanoTime() - startTime;

        // print solution to sudoku
        System.out.println("The solution to your sudoku is:");
        for (int row = 0; row < solution.length; row++) {
            for (int col = 0; col < solution[row].length; col++) {
                System.out.print(solution[row][col] + " ");
            }
            System.out.println();
        }
        System.out.println("Time Taken:" + timeTaken / 1000000000 + " seconds");
    }

    // solves the sudoku board
    private static void solveBoard(int[][] unsolvedBoard) {
        boolean solved = false;

        // populate solution array with known values
        for (int row = 0; row < unsolvedBoard.length; row++) {
            for (int col = 0; col < unsolvedBoard[row].length; col++) {
                if (unsolvedBoard[row][col] != 0) {
                    solution[row][col] = unsolvedBoard[row][col];
                }
            }
        }

        // create pencil marks
        int counter = 0;
        while (counter < 15) {
            createPencilMarks();
            counter++;
        }
        /*
         * Tester: System.out.println(Arrays.toString(pencilMarks[0]));
         * System.out.println(Arrays.toString(pencilMarks[1]));
         * System.out.println(Arrays.toString(pencilMarks[2]));
         * System.out.println(Arrays.toString(pencilMarks[3]));
         * System.out.println(Arrays.toString(pencilMarks[4]));
         * System.out.println(Arrays.toString(pencilMarks[5]));
         * System.out.println(Arrays.toString(pencilMarks[6]));
         * System.out.println(Arrays.toString(pencilMarks[7]));
         * System.out.println(Arrays.toString(pencilMarks[8]));
         */
        // solve the sudoku board or check if it is already solved
        while (solved == false) {

            // check if the sudoku is solved
            solved = true;
            for (int row = 0; row < solution.length; row++) {
                for (int col = 0; col < solution[0].length; col++) {
                    if (solution[row][col] == 0) {
                        solved = false;
                    }
                }
            }

            // brute force algorithm
            boolean violation = false;
        }
    }

    // creating possible values for each empty cell
    public static void createPencilMarks() {
        // create pencil marks
        for (int row = 0; row < solution.length; row++) {
            for (int col = 0; col < solution[row].length; col++) {
                if (solution[row][col] == 0) {
                    pencilMarks[row][col] = checkConditions(row, col);
                }
            }
        }

        // update solution set
        for (int row = 0; row < pencilMarks.length; row++) {
            for (int col = 0; col < pencilMarks[row].length; col++) {
                if (pencilMarks[row][col] == null) {
                    continue;
                }
                if (pencilMarks[row][col].size() == 1) {
                    solution[row][col] = (int) pencilMarks[row][col].get(0);
                    pencilMarks[row][col] = null;
                }
            }
        }
    }

    // check the three main conditions (row,col,box)
    public static ArrayList<Integer> checkConditions(int itemRow, int itemCol) {
        // initialise the pencil marks
        ArrayList<Integer> possibleNumbers = new ArrayList<Integer>();
        for (int index = 0; index < DIGITS.length; index++) {
            possibleNumbers.add(DIGITS[index]);
        }

        // Check Row
        for (int col = 0; col < solution[itemRow].length; col++) {
            if (possibleNumbers.contains(solution[itemRow][col])) {
                possibleNumbers.remove((Integer) (solution[itemRow][col]));
            }
        }

        // Check Column
        for (int row = 0; row < solution.length; row++) {
            if (possibleNumbers.contains(solution[row][itemCol])) {
                possibleNumbers.remove((Integer) (solution[row][itemCol]));
            }
        }

        // Check Box
        int boxRow = (itemRow / BOX_LENGTH) * BOX_LENGTH;
        int boxColumn = (itemCol / BOX_LENGTH) * BOX_LENGTH;
        for (int row = boxRow; row < boxRow + BOX_LENGTH; row++) {
            for (int col = boxColumn; col < boxColumn + BOX_LENGTH; col++) {
                if (possibleNumbers.contains(solution[row][col])) {
                    possibleNumbers.remove((Integer) (solution[row][col]));
                }
            }
        }
        return possibleNumbers;
    }
}