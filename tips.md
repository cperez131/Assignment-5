```python
shortestListLength = 9
mostConstrainedXPos = 0
mostConstrainedYPos = 0

for each row:
	for each column:
		if this cell is a list
			if the length of that cell is shorter than shortestListLength
			 	shortestListLength = length of that cell
				save the position in the other variables (mostConstrained...)

return (mostConstrainedXPos, mostConstrainedYPos)
```
