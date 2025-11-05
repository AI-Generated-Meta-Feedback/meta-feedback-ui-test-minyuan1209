Algorithm choice: insertion sort
It is stable, performs well on a small dataset, and understands.
The stability matters because for the books on the same shelf, the order in which they were returned must be preserved.

sorting strategy:
if A.shelfNumber < B. shelfNumber,A comes first
if both have the same sheld number, maintain their existing on (By returnOrder).
Example: Compare(shelf5,order2) vs(shelf5,order3)- keep 2 before 3. 

time complexity: 
O(n²) for random input (insertion sort or bubble sort).
Best case: O(n) if nearly sorted.
For 25 books, this is efficient and simple to code.


