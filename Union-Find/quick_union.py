'''
-----------------------------------------------------
Dynamic Connectivity : Union-find Algoritham
-----------------------------------------------------
Author:  Ketulkumar Suthar
Email:   k2lsuthar@gmail.com
__updated__ = "2020-04-23"
-----------------------------------------------------
THis is quick union algoritham. This is more faster than
quick union.
-----------------------------------------------------
'''

class QuickUnion:
    _nums = []
    def __init__(self, N):
        """
        THis method initialise _nums list. which contains id of parent node

        :param N: int
        """
        self._nums = [i for i in range(N)]

    def connected(self, x , y):
        """
        This method check two points are connected or not.

        :param x: int
        :param y: int
        :return: true/false
        """
        return self.root(x)== self.root(y)

    def root(self, x):
        """
        This function return index of root node.

        :param x:
        :return: int
        """
        while self._nums[x] != x:
            x = self._nums[x]
        return x

    def union(self, x, y):
        """
        This function joint two points x ,y and update _nums list for root node.

        :param x:
        :param y:
        :return:
        """
        _xid = self.root(x)
        _yid = self.root(y)

        self._nums[_xid] = _yid



u = QuickUnion(10)
u.union(4, 3)
print(u._nums)
u.union(3, 8)
print(u._nums)
u.union(6, 5)
print(u._nums)
u.union(9, 4)
print(u._nums)
u.union(2, 1)
print(u._nums)
u.union(5,0)
print(u._nums)
u.union(7,2)
print(u._nums)
u.union(6,1)
print(u._nums)
u.union(7,3)
print(u._nums)
print(u.connected(8, 9))
print(u.connected(5, 0))


