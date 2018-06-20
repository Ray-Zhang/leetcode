class Node(object):
    def __init__(self, val):
        self.parent = None
        self.first_child = None
        self.next_sibling = None
        self.val = val

    def getNextCousin(self):
        if self.parent:
            uncle = self.parent.next_sibling
            while uncle:
                if uncle.first_child:
                    return uncle.first_child
                else:
                    uncle = uncle.next_sibling
        return None

    def getFirstNextLevel(self):
        if self.first_child:
            return self.first_child
        elif self.next_sibling:
            return self.next_sibling.getFirstNextLevel()
        else:
            return None

    def sumPerLevel(self):
        sums = []
        firstInLevel = self
        while firstInLevel:
            s = 0
            nd = firstInLevel
            while nd:
                s += nd.val
                if nd.next_sibling:
                    nd = nd.next_sibling
                else:
                    nd = nd.getNextCousin()
            sums.append(s)
            firstInLevel = firstInLevel.getFirstNextLevel()
        return sums

if __name__ == '__main__':
    n1 = Node(1)

    n211 = Node(2)
    n211.parent = n1
    n1.first_child = n211

    n212 = Node(3)
    n212.parent = n1
    n211.next_sibling = n212

    n213 = Node(4)
    n213.parent = n1
    n212.next_sibling = n213

    n311 = Node(5)
    n311.parent = n211
    n211.first_child = n311

    n312 = Node(6)
    n312.parent = n211
    n311.next_sibling = n312

    print(n1.sumPerLevel())
