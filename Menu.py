from Regex_To_Dfa import *

#inp = "(01*1)*1"
print("\nProject 5 : Construction of an Dfa equivalent to a Regular Expression\nBy Patrick Lenis & Paul Cvasa")
print("Regular expression examples : xy, x+y, x*, (xy*y)*y\n")
inp = input("Your regular expression : ")

nfaObj = NFAfromRegex(inp)
nfa = nfaObj.getNFA()

print ("\nNFA: ")
nfaObj.displayNFA()

# dfaObj = DFAfromNFA(nfa)
# dfa = dfaObj.getDFA()

#print ("\nDFA: ")
#dfaObj.displayDFA()

