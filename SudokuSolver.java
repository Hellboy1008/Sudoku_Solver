
//龍ONE

import java.util.Scanner;
import java.util.ArrayList;

public class SudokuSolver { //cannot solve the world's hardest sudoku

    static int sudokuBoard[][] = new int[9][9];
    static int solution[][] = new int[9][9];
    static ArrayList[][] pencilMarks = new ArrayList[9][9];

    public static void main(String[] args) {
        boolean correctBoard = false;
        Scanner scanInput = new Scanner(System.in);

        while (correctBoard == false) {
            System.out.println("Input Sudoku Board from top to bottom row by row");
            System.out.println("Represent Blanks with the number 0 and don't use spaces");

            // Retrieve Board
            for (int row = 0; row < sudokuBoard.length; row++) {
                int wholeRow = scanInput.nextInt();
                for (int column = sudokuBoard[0].length - 1; column >= 0; column--) {
                    sudokuBoard[row][column] = wholeRow % 10;
                    wholeRow = wholeRow / 10;
                }
                scanInput.nextLine();
            }

            // Print Board
            for (int row = 0; row < sudokuBoard.length; row++) {
                for (int column = 0; column < sudokuBoard[0].length; column++) {
                    System.out.print(sudokuBoard[row][column] + " ");
                }
                System.out.println();
            }

            System.out.println("Does this Sudoku Board match your inputted board? (yes or no)");
            String answer = scanInput.next();
            if (answer.equalsIgnoreCase("Yes")) {
                correctBoard = true;
            }
        }
        scanInput.close();

        // Solve Sudoku (calculate time taken)
        double startTime = System.nanoTime();
        solveBoard();
        double finishTime = System.nanoTime();
        double timeTaken = finishTime - startTime;

        // Print Answer
        System.out.println("The solution to your sudoku is:");
        for (int row = 0; row < solution.length; row++) {
            for (int column = 0; column < solution[0].length; column++) {
                System.out.print(solution[row][column] + " ");
            }
            System.out.println();
        }
        System.out.println("Time Taken:" + timeTaken / 1000000000 + " seconds");
    }

    public static void solveBoard() {
        boolean solved = false;
        int check = 0;
        int expertSolverIndexOne = 0;
        int expertSolverIndexTwo = 0;
        int expertSolverIndexThree = 0;
        int expertSolverIndexFour = 0;
        long startedSolving = System.nanoTime();
        int[][] tempSolution = new int[9][9];
        ArrayList[][] tempPencilMarks = new ArrayList[9][9];
        for (int row = 0; row < sudokuBoard.length; row++){
            for (int column = 0; column < sudokuBoard[0].length; column++){
                solution[row][column] = sudokuBoard[row][column];
            }
        }
        createPencilMarks();

        while (solved == false) {

            //Used to solve Easy Level Sudokus
            for (int row = 0; row < pencilMarks.length; row++) {
                for (int column = 0; column < pencilMarks[0].length; column++) {
                    if (pencilMarks[row][column].size() == 1) {
                        solution[row][column] = (int) (pencilMarks[row][column].get(0));
                        createPencilMarks();
                    }
                }
            }

            //Used to solve Medium Level Sudokus
            mediumSolver();

            //Used to solve Expert Level Sudokus
            if (System.nanoTime() - startedSolving > 50000000 && expertSolverIndexOne == 0) {
                for (int row = 0; row < solution.length; row++){
                    for (int column = 0; column < solution[0].length; column++){
                        tempSolution[row][column] = solution[row][column];
                    }
                }
                for (int row = 0; row < pencilMarks.length; row++){
                    for (int column = 0; column < pencilMarks[0].length; column++){
                        tempPencilMarks[row][column] = pencilMarks[row][column];
                    }
                }
                int replaced = 0;
                int index = 0;
                for (int origRow = 0; origRow < pencilMarks.length; origRow++) {
                    for (int origColumn = 0; origColumn < pencilMarks[0].length; origColumn++) {
                        if (pencilMarks[origRow][origColumn].size() == 2) {
                            solution[origRow][origColumn] = (int) (pencilMarks[origRow][origColumn].get(index));
                            createPencilMarks();
                            replaced++;
                        }
                        if (replaced == 2) {
                            break;
                        }
                    }
                    if (replaced == 2) {
                        break;
                    }
                }
                expertSolverIndexOne++;
            } else if (System.nanoTime() - startedSolving > 60000000 && expertSolverIndexTwo == 0) {
                for (int row = 0; row < tempSolution.length; row++){
                    for (int column = 0; column < tempSolution[0].length; column++){
                        solution[row][column] = tempSolution[row][column];
                    }
                }
                for (int row = 0; row < tempPencilMarks.length; row++){
                    for (int column = 0; column < tempPencilMarks[0].length; column++){
                        pencilMarks[row][column] = tempPencilMarks[row][column];
                    }
                }
                int replaced = 0;
                int index = 0;
                for (int origRow = 0; origRow < pencilMarks.length; origRow++) {
                    for (int origColumn = 0; origColumn < pencilMarks[0].length; origColumn++) {
                        if (pencilMarks[origRow][origColumn].size() == 2) {
                            solution[origRow][origColumn] = (int) (pencilMarks[origRow][origColumn].get(index));
                            createPencilMarks();
                            replaced++;
                            index++;
                        }
                        if (replaced == 2) {
                            break;
                        }
                    }
                    if (replaced == 2) {
                        break;
                    }
                }
                expertSolverIndexTwo++;
            } else if (System.nanoTime() - startedSolving > 70000000 && expertSolverIndexThree == 0) {
                for (int row = 0; row < tempSolution.length; row++){
                    for (int column = 0; column < tempSolution[0].length; column++){
                        solution[row][column] = tempSolution[row][column];
                    }
                }
                for (int row = 0; row < tempPencilMarks.length; row++){
                    for (int column = 0; column < tempPencilMarks[0].length; column++){
                        pencilMarks[row][column] = tempPencilMarks[row][column];
                    }
                }
                int replaced = 0;
                int index = 1;
                for (int origRow = 0; origRow < pencilMarks.length; origRow++) {
                    for (int origColumn = 0; origColumn < pencilMarks[0].length; origColumn++) {
                        if (pencilMarks[origRow][origColumn].size() == 2) {
                            solution[origRow][origColumn] = (int) (pencilMarks[origRow][origColumn].get(index));
                            createPencilMarks();
                            replaced++;
                        }
                        if (replaced == 2) {
                            break;
                        }
                    }
                    if (replaced == 2) {
                        break;
                    }
                }
                expertSolverIndexThree++;
            } else if (System.nanoTime() - startedSolving > 80000000 && expertSolverIndexFour == 0) {
                for (int row = 0; row < tempSolution.length; row++){
                    for (int column = 0; column < tempSolution[0].length; column++){
                        solution[row][column] = tempSolution[row][column];
                    }
                }
                for (int row = 0; row < tempPencilMarks.length; row++){
                    for (int column = 0; column < tempPencilMarks[0].length; column++){
                        pencilMarks[row][column] = tempPencilMarks[row][column];
                    }
                }
                int replaced = 0;
                int index = 1;
                for (int origRow = 0; origRow < pencilMarks.length; origRow++) {
                    for (int origColumn = 0; origColumn < pencilMarks[0].length; origColumn++) {
                        if (pencilMarks[origRow][origColumn].size() == 2) {
                            solution[origRow][origColumn] = (int) (pencilMarks[origRow][origColumn].get(index));
                            createPencilMarks();
                            replaced++;
                            index--;
                        }
                        if (replaced == 2) {
                            break;
                        }
                    }
                    if (replaced == 2) {
                        break;
                    }
                }
                expertSolverIndexFour++;
            }

            //Check whether or not sudoku board is solved
            for (int row = 0; row < solution.length; row++) {
                for (int column = 0; column < solution[0].length; column++) {
                    if (solution[row][column] == 0) {
                        check++;
                    }
                }
            }
            if (check == 0) {
                solved = true;
            } else {
                check = 0;
            }
        }
    }

    public static void createPencilMarks() {
        for (int row = 0; row < solution.length; row++) {
            for (int column = 0; column < solution[0].length; column++) {
                if (solution[row][column] == 0) {
                    pencilMarks[row][column] = checkConditions(row, column);
                } else {
                    pencilMarks[row][column] = new ArrayList<Integer>();
                }
            }
        }
        //Used to solve Hard Level Sudokus
        hardSolver();
    }

    public static ArrayList checkConditions(int rowNumber, int columnNumber) {
        ArrayList<Integer> possibleNumbers = new ArrayList<Integer>();
        for (int numb = 1; numb < 10; numb++) {
            possibleNumbers.add(numb);
        }

        // Check Row
        for (int column = 0; column < solution[0].length; column++) {
            if (possibleNumbers.contains(solution[rowNumber][column])) {
                possibleNumbers.remove((Object) (solution[rowNumber][column]));
            }
        }
        // Check Column
        for (int row = 0; row < solution.length; row++) {
            if (possibleNumbers.contains(solution[row][columnNumber])) {
                possibleNumbers.remove((Object) (solution[row][columnNumber]));
            }
        }
        // Check Box
        int boxRow = (rowNumber / 3) * 3;
        int boxColumn = (columnNumber / 3) * 3;
        for (int row = boxRow; row < boxRow + 3; row++) {
            for (int column = boxColumn; column < boxColumn + 3; column++) {
                if (possibleNumbers.contains(solution[row][column])) {
                    possibleNumbers.remove((Object) (solution[row][column]));
                }
            }
        }
        return possibleNumbers;
    }

    public static void mediumSolver() {
        //Check row
        for (int origRow = 0; origRow < pencilMarks.length; origRow++) {
            for (int origColumn = 0; origColumn < pencilMarks[0].length; origColumn++) {
                for (int index = 0; index < pencilMarks[origRow][origColumn].size(); index++) {
                    int check = (int) (pencilMarks[origRow][origColumn].get(index));
                    boolean unique = true;
                    for (int newColumn = 0; newColumn < pencilMarks[0].length; newColumn++) {
                        if (newColumn == origColumn) {
                            continue;
                        } else if (pencilMarks[origRow][newColumn].contains(check)) {
                            unique = false;
                            break;
                        }
                    }
                    if (unique == true) {
                        solution[origRow][origColumn] = check;
                        createPencilMarks();
                    }
                }
            }
        }

        //Check column
        for (int origColumn = 0; origColumn < pencilMarks[0].length; origColumn++) {
            for (int origRow = 0; origRow < pencilMarks.length; origRow++) {
                for (int index = 0; index < pencilMarks[origRow][origColumn].size(); index++) {
                    int check = (int) (pencilMarks[origRow][origColumn].get(index));
                    boolean unique = true;
                    for (int newRow = 0; newRow < pencilMarks.length; newRow++) {
                        if (newRow == origRow) {
                            continue;
                        } else if (pencilMarks[newRow][origColumn].contains(check)) {
                            unique = false;
                            break;
                        }
                    }
                    if (unique == true) {
                        solution[origRow][origColumn] = check;
                        createPencilMarks();
                    }
                }
            }
        }

        //Check box
        for (int origRow = 0; origRow < pencilMarks.length; origRow++) {
            for (int origColumn = 0; origColumn < pencilMarks[0].length; origColumn++) {
                for (int index = 0; index < pencilMarks[origRow][origColumn].size(); index++) {
                    int check = (int) (pencilMarks[origRow][origColumn].get(index));
                    int boxRow = (origRow / 3) * 3;
                    int boxColumn = (origColumn / 3) * 3;
                    boolean unique = true;
                    for (int newRow = boxRow; newRow < boxRow + 3; newRow++) {
                        for (int newColumn = boxColumn; newColumn < boxColumn + 3; newColumn++) {
                            if (newRow == origRow && newColumn == origColumn) {
                                continue;
                            } else if (pencilMarks[newRow][newColumn].contains(check)) {
                                unique = false;
                                break;
                            }
                        }
                    }
                    if (unique == true) {
                        solution[origRow][origColumn] = check;
                        createPencilMarks();
                    }
                }
            }
        }
    }

    public static void hardSolver() {
        //Check row
        for (int origRow = 0; origRow < pencilMarks.length; origRow++) {
            for (int origColumn = 0; origColumn < pencilMarks[0].length; origColumn++) {
                if (pencilMarks[origRow][origColumn].size() == 2) {
                    for (int newColumn = 0; newColumn < pencilMarks[0].length; newColumn++) {
                        if (newColumn == origColumn) {
                            continue;
                        } else if (pencilMarks[origRow][origColumn].equals(pencilMarks[origRow][newColumn])) {
                            int firstNum = (int) (pencilMarks[origRow][origColumn].get(0));
                            int secondNum = (int) (pencilMarks[origRow][origColumn].get(1));
                            for (int newColumnTwo = 0; newColumnTwo < pencilMarks[0].length; newColumnTwo++) {
                                if (newColumnTwo == origColumn || newColumnTwo == newColumn) {
                                    continue;
                                } else if (pencilMarks[origRow][newColumnTwo].contains(firstNum)) {
                                    pencilMarks[origRow][newColumnTwo].remove((Object) (firstNum));
                                } else if (pencilMarks[origRow][newColumnTwo].contains(secondNum)) {
                                    pencilMarks[origRow][newColumnTwo].remove((Object) (secondNum));
                                }
                            }
                        }
                    }
                }
            }
        }

        //Check column
        for (int origRow = 0; origRow < pencilMarks.length; origRow++) {
            for (int origColumn = 0; origColumn < pencilMarks[0].length; origColumn++) {
                if (pencilMarks[origRow][origColumn].size() == 2) {
                    for (int newRow = 0; newRow < pencilMarks.length; newRow++) {
                        if (newRow == origRow) {
                            continue;
                        } else if (pencilMarks[origRow][origColumn].equals(pencilMarks[newRow][origColumn])) {
                            int firstNum = (int) (pencilMarks[origRow][origColumn].get(0));
                            int secondNum = (int) (pencilMarks[origRow][origColumn].get(1));
                            for (int newRowTwo = 0; newRowTwo < pencilMarks[0].length; newRowTwo++) {
                                if (newRowTwo == origRow || newRowTwo == newRow) {
                                    continue;
                                } else if (pencilMarks[newRowTwo][origColumn].contains(firstNum)) {
                                    pencilMarks[newRowTwo][origColumn].remove((Object) (firstNum));
                                } else if (pencilMarks[newRowTwo][origColumn].contains(secondNum)) {
                                    pencilMarks[newRowTwo][origColumn].remove((Object) (secondNum));
                                }
                            }
                        }
                    }
                }
            }
        }

        //Check box
        for (int origRow = 0; origRow < pencilMarks.length; origRow++) {
            for (int origColumn = 0; origColumn < pencilMarks[0].length; origColumn++) {
                if (pencilMarks[origRow][origColumn].size() == 2) {
                    int boxRow = (origRow / 3) * 3;
                    int boxColumn = (origColumn / 3) * 3;
                    for (int newRow = boxRow; newRow < boxRow + 3; newRow++) {
                        for (int newColumn = boxColumn; newColumn < boxColumn + 3; newColumn++) {
                            if (newRow == origRow && newColumn == origColumn) {
                                continue;
                            } else if (pencilMarks[origRow][origColumn].equals(pencilMarks[newRow][newColumn])) {
                                int firstNum = (int) (pencilMarks[origRow][origColumn].get(0));
                                int secondNum = (int) (pencilMarks[origRow][origColumn].get(1));
                                for (int newRowTwo = boxRow; newRowTwo < boxRow + 3; newRowTwo++) {
                                    for (int newColumnTwo = boxColumn; newColumnTwo < boxColumn + 3; newColumnTwo++) {
                                        if ((newRowTwo == origRow && newColumnTwo == origColumn)
                                                || (newRowTwo == newRow && newColumnTwo == newColumn)) {
                                            continue;
                                        } else if (pencilMarks[newRowTwo][newColumnTwo].contains(firstNum)) {
                                            pencilMarks[newRowTwo][newColumnTwo].remove((Object) (firstNum));
                                        } else if (pencilMarks[newRowTwo][newColumnTwo].contains(secondNum)) {
                                            pencilMarks[newRowTwo][newColumnTwo].remove((Object) (secondNum));
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}