'''
-----------------------------------------------------
Dynamic Connectivity : Union-find Algoritham
-----------------------------------------------------
Author:  Ketulkumar Suthar
Email:   k2lsuthar@gmail.com
__updated__ = "2020-04-23"
-----------------------------------------------------
-----------------------------------------------------
'''

class UnionFind:

    _nums = []
    def __init__(self, N):
        """
        Initialize List and its ID

        :param N: Number of interger
        :rtype: object
        """
        self._nums = [i for i in range(N)]

    def is_connected(self,x,y):
        """
        This method check X and Y connected or not.
        :param x: cordinate X
        :param y: cordinate Y
        :return: boolean true /false
        """
        return self._nums[x] == self._nums[y]


    def union(self, x,y):
        """

        :param x: int
        :param y: int
        :return: None
        """
        _xid = self._nums[x]
        _yid = self._nums[y]
        if _xid == _yid: return
        i = 0
        while i < len(self._nums):
            if self._nums[i] == _xid:
                self._nums[i] = _yid
            i+=1




u = UnionFind(10)
u.union(4,3)
print(u._nums)
u.union(3,8)
print(u._nums)
u.union(6,5)
print(u._nums)
u.union(9,4)
print(u._nums)
u.union(2,1)
print(u._nums)
print(u.is_connected(8,9))
print(u.is_connected(5,0))



