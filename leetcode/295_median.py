class MedianFinder(object):

    def __init__(self):
        self.arr = [None]


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.arr[0] is None:
            self.arr[0] = num
        else:
            index = self._find_place(num)
            self._insert(index=index, num=num)

    def _find_place(self, num):
        i = 0
        j = len(self.arr)-1

        # Граничные случаи
        if num <= self.arr[i]:
            return -1 # Сигнал на вставку слева
        elif num >= self.arr[j]:
            return j

        # Внутри массива
        while (j-i > 1):
            k = i+(j-i)//2
            if self.arr[k] < num:
                i = k
            elif self.arr[k] > num:
                j = k
            else:
                i = k
                j = k
        return i


    def _insert(self, index, num):
        new_arr = [None for i in range(len(self.arr)+1)]
        if index == -1:
            new_arr[0] = num
            for i in range(1, len(new_arr)):
                new_arr[i] = self.arr[i-1]
        else:
            i = 0 
            while i <= index:
                new_arr[i] = self.arr[i]
                i+=1
            
            new_arr[index+1] = num

            i = index+2
            while i < len(new_arr):
                new_arr[i] = self.arr[i-1]
                i+=1

        self.arr = new_arr


    def _resize(self, left):
        """
        :type left: bool
        :rtype: None
        """
        pass
        

    def findMedian(self):
        """
        :rtype: float
        """
        N = len(self.arr)
        if N%2 == 0:
            id1 = int(N/2)
            id2 = id1-1
            res = float(self.arr[id1]+self.arr[id2])/2
        else:
            res = float(self.arr[int(N//2)])

        return res
        
if __name__ == '__main__':
    mf = MedianFinder()
    mf.arr = [1,2,3,4]
    mf._insert(index=2, num=3)
    print(mf.arr)
    
    mf.addNum(num=6)
    print(mf.arr)

    mf.addNum(num=5)
    print(mf.arr)

    mf.addNum(num=0)
    print(mf.arr)

    res = mf.findMedian()
    print(res)


    mf = MedianFinder()
    mf.addNum(1)




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()