# simplex.py
# Created by Gen Blaine. Oct. 27, 2024
# This python program performs the Simplex Algorithm for Maximum Tableaus
import numpy as np

# change this to match the problem
array = np.array([
    [-1, 0, 0, 0, -300],
    [-1, -1, 0, 0, -500],
    [-1, -1, -1, -1, -900],
    [0, 1, 0, 1, 300],
    [0, 0, 1, 0, 200],
    [-1, -0.4, -0.4, -0.25, 0]
]).astype(np.float64)

rows, cols = array.shape

def pivot(pivot_row, pivot_column, pivot_element):
    # update the rest of the tableau first so that the older values are used
    for i in range(rows):
        for j in range(cols):
            if i != pivot_row and j != pivot_column:
                # Calculate the updated value of s as (p * s - q * r) / p
                row_entry = array[pivot_row, j]    # q in the same row as p
                col_entry = array[i, pivot_column] # r in the same column as p
                array[i, j] = (pivot_element * array[i, j] - row_entry * col_entry) / pivot_element
    # update the rows
    array[pivot_row, :] = array[pivot_row, :] / pivot_element
    # updates the columns
    array[:, pivot_column] = -1 * array[:, pivot_column] / pivot_element
    # update the pivot element
    array[pivot_row, pivot_column] = 1 / pivot_element

def simplexAlgorithm():
    last_column_all_non_neg = False
    last_column = array[:, -1]
    while (last_column_all_non_neg == False):
        leaving_row_index = None
        # subtract two to avoid the last row which is the objective function
        for i in range(len(last_column) - 2, -1, -1):
            if last_column[i] < 0:
                leaving_row_index = i
                break

        # Step 2: Calculate the ratios and find the entering column
        if leaving_row_index is not None:
            ratios = []
            for j in range(array.shape[1] - 1):  # Exclude last column (RHS)
                if array[leaving_row_index, j] < 0:
                    ratio = array[-1, j] / array[leaving_row_index, j]
                    ratios.append((ratio, j))
            
            # Find the smallest positive ratio
            if ratios:
                pivot_column_index = min(ratios)[1]
                pivot_element = array[leaving_row_index, pivot_column_index]
                
                print("Pivot row:", leaving_row_index)
                print("Pivot column:", pivot_column_index)
                print("Pivot element:", pivot_element)
                pivot(leaving_row_index, pivot_column_index, pivot_element)
                print(array)
            else:
                print("Tableau is infeasible")
                return
        else: # all values in last column are non negative
            last_column_all_non_neg = True
            return

def stepTwo():
    last_row_all_non_pos = False
    last_row = array[-1, :]
    while (last_row_all_non_pos == False):
        column_index = None
        # subtract one so the loop doesn't reach the last column
        for i in range(len(last_row) - 1):
            if last_row[i] > 0:
                column_index = i

        if column_index is not None:
            ratios = []
            for i in range(rows):
                if array[i][column_index] > 0:
                    ratio = array[i, -1] / array[i, column_index]
                    ratios.append((ratio, i))

            if ratios:
                pivot_row_index = min(ratios)[1]
                pivot_element = array[pivot_row_index, column_index]

                print("Pivot row:", pivot_row_index)
                print("Pivot column:", column_index)
                print("Pivot elment:", pivot_element)
                pivot(pivot_row_index, column_index, pivot_element)
                print(array)

            else:
                print("Tableau is unbounded")
                return
        else:
            last_row_all_non_pos = True
            return

def main():
    simplexAlgorithm()
    stepTwo()

main()