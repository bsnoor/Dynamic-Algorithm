class Node:
    '''
    * class Node:
    * x,y - the price for get down (y) or left (x)
    * price - the best price from (0,0) to this node
    * price2 - the second best price from (0,0) to this node
    * priceFromTheEnd - the best price from (m,n) to this node
    '''
    x, y, price = 0, 0, 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.price = 0
        self.priceFromTheEnd = 0

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ") "
        # return "x=" + str(self.x) + ", y=" + str(self.y) + ", price=" + str(price)  + "; "


class AeroplaneProblem:
    '''
    /**
    * class AeroplaneProblem presents
    * how find one best/cheapest path, all best/cheapest paths
    * and more creative questions
    */
    '''
    cheapestPrice = 0
    mat = []

    def __init__(self, nodes):
        self.cheapestPrice = 0
        self.mat = nodes

    def getBestPrice(self):
        '''
        * Build a matrix that contains the price to get each point (from (0,0))
        * and the number of shortest path until each point
        * Complexity: O(n*m)
        :return:
        '''
        # n rows, m columns
        n = len(self.mat)
        m = len(self.mat[0])
        self.mat[0][0].price = 0
        # first column:
        for i in range(1, n):
            self.mat[i][0].price = int(self.mat[i - 1][0].y) + int(self.mat[i - 1][0].price)
        # first row:
        for j in range(1, m):
            self.mat[0][j].price = int(self.mat[0][j - 1].price) + int(self.mat[0][j - 1].x)
        # other cells
        for i in range(1, n):
            for j in range(1, m):
                a = int(self.mat[i - 1][j].price) + int(self.mat[i - 1][j].y)
                b = int(self.mat[i][j - 1].price) + int(self.mat[i][j - 1].x)
                # choose the best path to this cell
                if a < b:
                    self.mat[i][j].price = a
                elif a > b:
                         self.mat[i][j].price = b
                else:  # x==y
                    self.mat[i][j].price = a

        self.cheapestPrice = self.mat[n - 1][m - 1].price

    def getCheapestPrice(self):
        return self.cheapestPrice

    def printNodes(self):
        '''
        Print matrix of nodes
        :return:
        '''
        print("Matrix of nodes:")
        n = len(self.mat)
        m = len(self.mat[0])
        for i in range(n):
            for j in range(m):
                print(self.mat[i][j], end="")
            print()

    def printPrices(self):
        '''
        Print matrix of prices
        :return:
        '''
        print("Matrix of prices:")
        n = len(self.mat)
        m = len(self.mat[0])
        for i in range(n):
            for j in range(m):
                print(self.mat[i][j].price, "\t", end="")
            print()

    def getOneCheapestPath(self):
        '''
        Calculate One Best Path by Induction
        Complexity: O(n+m) - but first need to build the matrix - O(n*m)
        :return: one of shortest path - induction
        '''
        ans = ""
        i = len(self.mat) - 1
        j = len(self.mat[0]) - 1
        while i > 0 and j > 0:
            a = int(self.mat[i - 1][j].price) + int(self.mat[i - 1][j].y)
            b = int(self.mat[i][j - 1].price) + int(self.mat[i][j - 1].x)
            if a < b:
                ans = "1" + ans
                i -= 1
            else:
                ans = "0" + ans
                j -= 1
        if i == 0:
            while j > 0:
                ans = "0" + ans
                j -= 1
        else:  # j==0
            while i > 0:
                ans = "1" + ans
                i -= 1
        return ans

