import numpy as np 
import matplotlib.pyplot as plt 

def d(u, v):
	diff = u - v
	return diff.dot(diff)

def plot_kmeans(X, K, max_iters = 20, beta = 1.0):
	N, D = X.shape
	means = np.zeros((K, D))
	# responsibilities
	R = np.zeros((N, K))

	for k in range(K):
		# randomly selecting data points as means
		means[k] = X[np.random.choice(N)]

	grid_width = 5
	grid_height = max_iters // grid_width
	random_colors = np.random.random((K, 3))
	plt.figure()

	costs = np.zeros(max_iters)
	for i in range(max_iters):

		colors = R.dot(random_colors)
		plt.subplot(grid_width, grid_height, i + 1)
		plt.scatter(X[:, 0], X[:, 1], c=colors)
		plt.title("Iteration {}".format(i + 1))

		for k in range(K):
			for n in range(N):
				R[n, k] = np.exp(-beta * d(means[k], X[n])) / sum( np.exp(-beta * d(means[j], X[n])) for j in range(K) )
		
		for k in range(K):
			# taking the weighted average
			means[k] = R[:, k].dot(X) / R[:, k].sum()

		costs[i] = cost(X, R, means)
		if i > 0:
			if np.abs(costs[i] - costs[i - 1]) < 0.1:
				break

	plt.show()

	plt.plot(costs)
	plt.title("Costs")
	plt.show()

def cost(X, R, means):
	cost = 0
	for k in range(len(means)):
		for n in range(len(X)):
			cost += R[n, k] * d(means[k], X[n])

	return cost				

def main():
	s = 4
	D = 2

	mu1 = np.array([0, 0])
	mu2 = np.array([s, s])
	mu3 = np.array([-s, s])
	
	N = 900
	X = np.zeros((N, D))
	X[:300, :] = np.random.randn(300, D) + mu1
	X[300:600, :] = np.random.randn(300, D) + mu2
	X[600:, :] = np.random.randn(300, D) + mu2
	
	plt.scatter(X[:, 0], X[:, 1])
	plt.show()

	K = 3
	plot_kmeans(X, K)

	K = 5
	plot_kmeans(X, K, max_iters = 30)

	K = 5
	plot_kmeans(X, K, max_iters = 30, beta = 0.3)

if __name__ == '__main__':
	main()













