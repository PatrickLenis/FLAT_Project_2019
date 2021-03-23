#Generates NFA links out of an AbstractSyntax

#Node component data type
class Node(object):
    def __init__(self, type, data, next_r = None, next_l = None):
        self.type = type
        self.data = data
        self.next_r = next_r
        self.next_l = next_l

    #Link to option a.
    def get_next_r(self):
        return  self.next_r

    def set_next_r(self, next_r):
        self.next_r = next_r

    # Link to option b.
    def get_next_l(self):
        return self.next_l

    def set_next_l(self, next_l):
        self.next_l = next_l

    # Link to node data
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    # Link to node type
    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

#NFA data type
class NFA_List(object):
    def __init__(self, start = None, end = None):
        self.start = start
        self.end = end
