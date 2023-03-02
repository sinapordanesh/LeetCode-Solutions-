package com.sina.leetCode;

import java.sql.Struct;
import java.util.*;
import java.lang.*;
import java.io.*;

/*
 * inputArr, represents the array with inputArr_size (N) elements.
 */
public class Solution
{
    public static void  funcMatrix(int[][] matrix)
    {
        int result = -1;
        // Write your code here
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
               if (checkInRow(matrix, i, j) && checkInColumn(matrix, i, j)){
                   result = matrix[i][j];
               }
            }
        }

        System.out.println(result);
    }

    public static boolean checkInRow(int[][] matrix, int i, int j){
        int target = matrix[i][j];

        for (int k = 0; k < matrix[i].length; k++) {
            if (target < matrix[i][k]) return false;
        }
        return true;
    }

    public static boolean checkInColumn(int[][] matrix, int i, int j){
        int target = matrix[i][j];
        for (int k = 0; k < matrix.length; k++) {
            if (target > matrix[k][j]) return false;
        }
        return true;
    }

    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        // input for matrix
        int matrix_row = in.nextInt();
        int matrix_col = in.nextInt();
        int matrix[][] = new int[matrix_row][matrix_col];
        for(int idx = 0; idx < matrix_row; idx++)
        {
            for(int jdx = 0; jdx < matrix_col; jdx++)
            {
                matrix[idx][jdx] = in.nextInt();
            }
        }


        funcMatrix(matrix);
    }
}