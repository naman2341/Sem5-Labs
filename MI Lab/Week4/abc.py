def k_neighbours(self, x):
        """
        Find K nearest neighbours of each point in train dataset x
        Note that the point itself is not to be included in the set of k Nearest Neighbours
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            k nearest neighbours as a list of (neigh_dists, idx_of_neigh)
            neigh_dists -> N x k Matrix(float) - Dist of all input points to its k closest neighbours.
            idx_of_neigh -> N x k Matrix(int) - The (row index in the dataset) of the k closest neighbours of each input

            Note that each row of both neigh_dists and idx_of_neigh must be SORTED in increasing order of distance
        """
        #The k nearest neihbours are
        #1. Find the distance between the point and all the other points
        lst=find_distance(self,x)
        #2. Sort the distances in ascending order
        lst.sort()
        #3. Find the indices of the k nearest neighbours
        #4. Return the indices of the k nearest neighbours
        return lst
        