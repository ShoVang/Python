def pascal_triangle(numRows):
  if numRows == 0:
    return []

  elif numRows == 1:
    return [[1]]

  else:
    triangle = pascal_triangle(numRows - 1)  #building the traingle
    last_row = triangle[-1]
    current_row = [1]

    for i in range(len(last_row) - 1):
      current_row.append(
        last_row[i] + last_row[i + 1]
      )  # this is where it takes the 2 digits to get the sum to add into the current row

    current_row.append(1)
    triangle.append(current_row)
    return triangle


def print_pascal_triangle(rows):
  triangle = pascal_triangle(rows)

  for row in triangle:
    print(' '.join(map(str, row)))


num_rows = int(input("Enter the number of rows for Pascal's triangle: "))
print_pascal_triangle(num_rows)
