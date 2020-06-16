from typing import List

class UpOrDownCounter(object):

    def __init__(self,start,end):
        self.start = start
        self.end = end

    def count(self):
        mycountlist: List[int] = []
        if self.start < self.end:
            for number in range(self.start,self.end):
                 mycountlist.append(number)
            return mycountlist
        else:
            for number in range(self.end,self.start):
                mycountlist.append(number)
            mycountlist.reverse()
            return mycountlist



if __name__ == "__main__":
    start = int(input("Please put in start value: "))
    end = int(input("Please, put in end value: "))
    up_or_down_func = UpOrDownCounter(start,end).count()
    print(up_or_down_func)


    

    

