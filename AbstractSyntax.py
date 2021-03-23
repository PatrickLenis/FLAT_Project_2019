# Makes an abstract syntaxt (tree) outh of checked list


def Make_Tree(Input_List):
    # recursive adding subtrees
    def Recursive_Subtree(index):

        Result = []  # for printing final result
        item = Input_List[index]  # takes one item at a time

        while item != ")":  # checks for an ent to subtree/tree

            if item == "(":  # checks for start of the subtree
                Subtree, index = Recursive_Subtree(index + 1)  # recursivity
                Result.append(Subtree)
            else:  # appends single atoms
                Result.append(item)

            index += 1  # step
            item = Input_List[index]

        return Result, index

    return Recursive_Subtree(1)[0]

def Flatten_List(Abstract_Syntax):

    Output_List = []

    if len(Abstract_Syntax) > 1:
        if len(Abstract_Syntax) == 2:
            if '*' in Abstract_Syntax:
                Output_List.append(Abstract_Syntax[1])
                Output_List.append(Abstract_Syntax[0])
            else:
                Output_List.append('_')
                Output_List.append(Abstract_Syntax[0])
                Output_List.append(Abstract_Syntax[1])

        if len(Abstract_Syntax) == 3:
            Output_List.append(Abstract_Syntax[1])
            Output_List.append(Abstract_Syntax[0])
            Output_List.append('0')
            Output_List.append(Abstract_Syntax[2])

    return Output_List

def Flatten_Abstract_List(Abstract_Syntax):
    Abstract_Syntax = Flatten_List(Abstract_Syntax)

    Output_List = []

    for element in Abstract_Syntax:
        if len(element) == 1:
            Output_List.append(element)
        else:
            Aux_List = Flatten_Abstract_List(element)
            for aux_element in Aux_List:
                Output_List.append(aux_element)

    return Output_List

