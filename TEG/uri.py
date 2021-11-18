import sys

def min(a,b):
    if a < b:
        return a
    else:
        return b

if __name__ == '__main__':

	dist = []
	n = int(input())
	m = int(input())
	l=[]

	for i in range(0,n):
    		dist.append([])	
    		for j in range(0,n):
    			dist[i].append(sys.maxsize)
    


	for i in range(0,n):
		dist[i][i] = 0;

	for i in range(0,m):
		j = int(input())
		k = int(input())
		w = int(input())
		
		dist[j][k] = dist[k][j]
		w= dist[j][k]


	for i in range(0,n):
		for j in range(0,n):
			for k in range(0,n):
				dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

	maior = -1;
	menor = sys.maxsize;

	for i in range(0,n):
		maior = -1;
		for j in range(0,n):
			if (dist[i][j] > maior and dist[i][j] !=sys.maxsize):
				maior = dist[i][j]

		if (menor > maior and maior > 0):
			menor = maior



	print(menor);

