# Chain-Matrix-Multiplication-with-DP
This is a project created for my Algorithms Course and tackles the problem of Chain-Matrix Multiplication, a classical optimization problem that requires determining the optimal order in which matrices must be multiplied to arrive at the product with the least amount of integer multiplications. The goal is to be as efficient as possible so as to reduce computational cost. 

## Naïve Algorithm
The most simple implementation would be plain recursion that would try all possible partitions and for each partition, it would recursively calculate the cost of the remaining brackets. But this means the same subproblem is called again and again resulting in a highly inefficient algorithm that runs in exponential time.  
We start with the first partition to get our first pair of subproblems. If our input matrices were ABCD then the first partition could be A(BCD) or (AB)(CD) or (ABC)D. In general, if we had n matrices, the first partition could be made in (n-1) ways. 

## DP Solution
Our approach works in a similar way by finding the optimal solution to the subproblems which decides the optimal solution of the whole problem. The difference is that intermediate costs of the subproblems are stored to avoid calculating the same thing again and again. This is the Top-Down approach with recursion and memoization.

First, let’s go through some of the basic properties of matrix multiplications (Note that A,B,C,D wherever used represent arbitrary matrices):
	Matrix multiplications are not commutative, meaning changing the sequence of the matrices will result in a completely different product. AB≠BA
	Matrix multiplications are associative, meaning changing the order of multiplication will result in the same product. A(BC)=(AB)C
	Two matrices can only be multiplied if the no. of columns of the preceding matrix is equal to the no. of rows of the succeeding matrix. So 〖(A〗_(a×b))(B_(b×c) ) would be valid but 〖(A〗_(a×b))(B_(c×d) ) would be invalid.
	The resulting product of two matrices will be of the order: no. of rows of the preceding matrix × no. of columns of the succeeding matrix. 〖(A〗_(a×b))(B_(b×c) )=C_(a×c)
In terms of time complexity, matrix multiplications takes roughly θ([rows of first matrix] × [columns of first matrix/rows of second matrix]×[columns of second matrix]) steps.
So 〖(A〗_(a×b))(B_(b×c) )=C_(a×c) would be θ(a×b×c) 
This is because the product will have a total of a×c entries where each entry takes b multiplications and (b-1) additions, the latter of which can be ignored. 
The main idea of the algorithm is calculating the cost of multiplying the matrices in different orders and then selecting the minimum cost.



The functioning of the algorithm can be better illustrated with a small example:
Say we want to multiply three matrices 〖(A〗_(4×1))(B_(1×2) ) and (C_(2×3)). We have two ways to go about this, either (AB)C or A(BC). 
Option 1: AB=D_(4×2)=4×1×2=8 & DC=4×2×3=24 i.e., 8+24=32 multiplications
Option 2: BC=D_(1×3)=1×2×3=6 & AD=4×1×3=12 i.e., 6+12=18 multiplications
The optimum order with a lower cost in terms of no. of multiplications is Option 2 with a total of 18 multiplications and the sequence of multiplications can be represented by (A(BC)).




## Pseudocode Analysis
The code itself is pretty simple. 
 
The input provided to the function is an array of integers of size, say, n. We extract from this array the orders of our matrices where, each set of arr[i]×arr[i+1] for all 0≤i<n gives us an order for a matrix. An array of length 2 makes one matrix. An array of length 3 makes 2 matrices…. An array of length n makes n-1 matrices.
Line 1 declares the start of our function which is supplied with the array of integers, starting & ending indices of the current chain of integers that constitute the current chain of matrices and the table of subproblems which is initially filled with all entries as -1.
Line 2 is our first base case where there are only two entries from the start index to the end index which would mean just one matrix and hence 0 multiplications.
Line 3 is our second base case where there are only three entries from our start index to our end index which would mean just two matrices. These can only be multiplied in one way that would take θ([rows of first matrix] × [columns of first matrix/rows of second matrix]×[columns of second matrix]) steps as mentioned before.
Line 4 checks our memoization table to see if the subproblem has already been calculated. This is the main reason our code is so efficient as it avoids re-computation of previously solved problems which would be result in an exponential running time.
Line 5 initializes our result infinity to make sure that when it is compared with the first intermediate cost, it will always be bigger. This allows us to calculate our first minimum.
Line 6 to 8 is our for loop that recursively calculates the cost of the left chain and the cost of the right chain and adds it to the no. of multiplications required to calculate the product of the matrices returned by the left chain and the right chain. The cost for every partition is stored in a temporary variable that is compared to the result after each partition calculations and is saved into result if the cost of the current split is less than the result. 
Line 9 stores the value of the minimum cost for the current chain from i to j in the memoization table so it is not calculated again when called another time.
Line 10 returns the minimum cost calculated for the current chain. 
The final solution is located at M[0][n-1] but to get there we need to obtain the value of every M[i][j] i.e., all subproblems meaning the n^2 values stored in the table. Each subproblem takes roughly n steps in the loop = θ(n) as each problem has n-2 partitions possible. This gives us a total time complexity of θ(n^3)
Extra space is required to store our 2D array of all the subproblems which gives us a space complexity of θ(n^2)

## Implementation
The implementation seemed too simple so I added an extra bit of code to also print the order. This is done by labeling the matrices M0,M1,M2,M3… and employing the use of brackets to show the sequence of multiplications.
Matrices labeled Mi are of the order arr[i]×arr[i+1]
To achieve this, every cell in the memoization table contains a tuple to also track the order.
Our function returns two values namely the cost and the order. The latter is computed by adding brackets with the labeled matrices whenever a value is returned. 
At the end, the optimal cost, bracketed matrices and the memoization table is printed to easily visualize the algorithm. The addition of this feature did end in errors and a bit of debugging but makes the algorithm easier to comprehend and follow.

Working Example
Let’s take the same example as before of 〖(A〗_(4×1))(B_(1×2) ) and (C_(2×3)). 
This will be passed as an array of the form [4,1,2,3] into our function
arr=[4,1,2,3] 
n=len(arr)=len([4,1,2,3])=4 
Our memoization table will be a 4×4 table with all entries -1
	0	1	2	3
0	-1	-1	-1	-1
1	-1	-1	-1	-1
2	-1	-1	-1	-1
3	-1	-1	-1	-1

result = ∞
The first function called will be matrixMult(arr,0,3,M)
i=0 and j=3
It does not satisfy any of the if statements and will enter the for loop, recursively calling its left and right sub-chains.
First iteration:
k=i+1=1 
left = matrixMult(arr,0,1,M)
	This is base case 1 and it will return 0
	0	1	2	3
0	-1	0	-1	-1
1	-1	-1	-1	-1
2	-1	-1	-1	-1
3	-1	-1	-1	-1

right = matrixMult(arr,1,3,M)
	This is base case 2 and it will return arr[1]*arr[2]*arr[3]=1*2*3=6
	0	1	2	3
0	-1	0	-1	-1
1	-1	-1	-1	6
2	-1	-1	-1	-1
3	-1	-1	-1	-1

temp = left + right + (arr[0]*arr[3]*arr[1]) = 0+6+(4*3*1)=6+12=18
18<∞ and hence result = 18

Second iteration:
k=i+2=2 
left = matrixMult(arr,0,2,M)
	This is base case 2 and it will return arr[0]*arr[1]*arr[2]=4*1*2=8
	0	1	2	3
0	-1	0	8	-1
1	-1	-1	-1	6
2	-1	-1	-1	-1
3	-1	-1	-1	-1

right = matrixMult(arr,2,3,M)
	This is base case 1 and it will return 0
	0	1	2	3
0	-1	0	8	-1
1	-1	-1	-1	6
2	-1	-1	-1	0
3	-1	-1	-1	-1

temp = left + right + (arr[0]*arr[3]*arr[2]) = 8+0+(4*3*2)=8+24=32
32<18 is false and hence result remains 18
We exit the loop and save result to the table at M[0][n-1]
	0	1	2	3
0	-1	0	8	18
1	-1	-1	-1	6
2	-1	-1	-1	0
3	-1	-1	-1	-1

The result is returned = 18	

What passing this into our code will display:

## Installation & Configuration
1. Check version of Python or install Python 
`python --version or python3 --version` or `sudo apt install python3`
2. Clone the repository
```
git clone https://github.com/Zunairah-ikhan/Titanic-and-Ames-Housing-ML-Models.git 
```
5.  Navigate to directory containing Jupyter Notebook
```
cd Titanic-and-Ames-Housing-ML-Models
```
6. Open Jupyter notebook server & load the notebook (" " is used to escape the &)
```
jupyter notebook "Titanic&AmesHousingModels.ipynb"
```


1. Download: Save the file SP_Project.py to a directory of your choice.


3. Permissions (Linux/macOS): If you wish to run the script directly as an executable, you may need to grant execution permissions:
                                  `chmod +x SP_ Project.py`

- **Linux/macOS** -> `python3 SP_Project.py` or `./SP_Project.py`



##References
1. S. Dasgupta, C. H. Papadimitriou, & U. V. Vazirani. (July 18, 2006). Algorithms.
2. Geeks for Geeks. (23 July, 2025). *Matrix Chain Multiplication*. [https://www.geeksforgeeks.org/dsa/matrix-chain-multiplication-dp-8/](https://www.geeksforgeeks.org/dsa/matrix-chain-multiplication-dp-8/)
