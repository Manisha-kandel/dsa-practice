Array Problems Revision:



\## LC 0001 – Two Sum



--Current version:--

Hashmap storing number → index.

Check complement = target - nums\[i].

If seen → return indices.



--Preferred alternative:--

Same approach (this is optimal already).



Status: ✅ Solid.







\## LC 0014 – Longest Common Prefix



--Current version:--

Find min string length.

Column-wise comparison across all strings.

Stop on first mismatch.



--Preferred alternative:--

Sort array, compare first and last only.

Cleaner in interviews.



Status: ✅ Good. Alternative cleaner.







\## LC 0027 – Remove Element



--Current version:--

Delete while iterating. Adjust pointer.



⚠️ Delete = O(n) shift → inefficient.



--Preferred alternative:--

Overwrite using write pointer.

No deletion. O(n).



Must upgrade to overwrite method.







\## LC 0036 – Valid Sudoku



--Current version:--

Row\[9]\[9], Col\[9]\[9], Box\[3]\[3]\[9] boolean tracking.



Works.



--Preferred alternative:--

Single box index formula:

`box = (r // 3) - 3 + (c // 3)`

Cleaner structure.



Status: ✅ Both valid.

Keep current as acceptable alternative.







\## LC 0041 – First Missing Positive



--Current version:--

Index marking using +n.

Use modulo to recover original value.



Correct.



--Preferred alternative:--

Same. This is optimal O(n).



Status: ✅ Strong understanding.







\## LC 0049 – Group Anagrams



--Current version:--

Sorted(word) as hashmap key.



--Preferred alternative:--

26-count tuple as key (faster, no sorting).



Status: ✅ Yours fine.

Learn tuple-count version.







\## LC 0075 – Sort Colors



--Current version:--

Two-pass swap logic.



⚠️ Slight confusion in pointer rules.



--Preferred version:--

Dutch National Flag (3 pointers).

Exact rules must be memorized.



Needs reinforcement.







\## LC 0122 – Best Time to Buy and Sell II



--Current version:--

DP-style reasoning.



⚠️ Overcomplicated.



--Preferred version:--

Add all positive differences.

Simple greedy.



Upgrade mental model.







\## LC 0128 – Longest Consecutive Sequence



--Current version:--

Set-based logic.

You mentioned sorting — remove that.



--Preferred version:--

Only start streak if (x-1 not in set).

O(n).



Solid concept. Avoid sorting.







\## LC 0169 – Majority Element



--Current version:--

Likely hashmap.



--Preferred version:--

Boyer-Moore Voting.

O(1) space.



Must master this.







\## LC 0229 – Majority Element II



--Current version:--

Threshold check via hashmap.



--Preferred version:--

Extended Boyer-Moore (2 candidates).



Upgrade later.







\## LC 0217 – Contains Duplicate



--Current version:--

Hash set.



Optimal.







\## LC 0238 – Product of Array Except Self



--Current version:--

Prefix + suffix arrays.



Correct.



--Preferred version:--

Reuse output array to reduce space.



Good understanding.







\## LC 0242 – Valid Anagram



--Current version:--

Frequency diff array.



Optimal.







\## LC 0271 – Encode \& Decode Strings



--Current version:--

Length#string format.



Concept correct.



⚠️ Implementation precision needed.







\## LC 0304 – Range Sum Query 2D



--Current version:--

Extra row + column.

PIE logic: top + left - diag + value.



Excellent conceptual clarity.







\## LC 0347 – Top K Frequent



--Current version:--

Min-heap of size k.



Minor confusion about heap type.



Reminder: Python heapq = min heap.



Solid overall.







\## LC 0560 – Subarray Sum Equals K



--Current version:--

Prefix sum hashmap.

Initialize map\[0] = 1.



Strong understanding.







\## LC 0705 / 0706 – Design HashSet / HashMap



Basic wrapper logic.



Need more implementation comfort.







\## LC 0912 – Sort an Array



--Current version:--

Counting sort when range small.



Good reasoning.



Reminder: default to merge/quick unless constraints small.







\## LC 1929 – Concatenation of Array



Straightforward extend.









