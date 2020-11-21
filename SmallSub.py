
max_char = 256 

def smallSub(str): 
	n = len(str)	
	mx_dist = count_distinct(str, n) 
	minl = n
	for i in range(n): 
		for j in range(n): 
			k = str[i:j] 
			kl = len(k) 
			sub_distinct_char = count_distinct(k, kl) 
	
			if (kl < minl and mx_dist == sub_distinct_char): 
				minl = kl 

	return minl 

def count_distinct(str, n): 

	count = [0] * max_char 
	for i in range(n): 
		count[ord(str[i])] += 1
	
	max_distinct = 0
	for i in range(max_char): 
		if (count[i] != 0): 
			max_distinct += 1	
	
	return max_distinct

if __name__ == "__main__": 
	
	str = "ABCDA" #to check with every string change this to input()
	l = smallSub(str); 
	print(l,end='')