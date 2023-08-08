def seats_in_theater(tot_cols, tot_rows, col, row):
    left_of_us = tot_cols - col + 1 
    behind_us = tot_rows - row
    return left_of_us * behind_us 