'''
Created on Feb 24, 2017

@author: BhavinSoni
'''
'''
def fastED(S1, S2):
    '''''' Returns the edit distance between the strings first and second.''''''
    def fastEDhelper(S1, S2, memo):
        if (S1, S2) in memo:
            return memo [(S1, S2)]
        if S1 == '':
            result = len(S2)
        elif S2 == '':
            result = len(S1)
        elif S1[0] == S2[0]:
            result = fastEDhelper(S1[1:], S2[1:], memo)
        else:
            substitution = 1 + fastEDhelper(S1[1:], S2[1:],memo)
            deletion = 1 + fastEDhelper(S1[1:], S2, memo)
            insertion = 1 + fastEDhelper(S1, S2[1:],memo)
            result = min(substitution, deletion, insertion)
        
        memo[(S1,S2)] = result
        return result
    
    return fastEDhelper(S1, S2, {})

print (fastED("xylophone", "yellow"))
'''
student_scores = {} 
student_scores['Brian'] = 76 
student_scores['Brian'] = 56 
student_scores['brian'] = student_scores['Brian'] 
class_scores = [ 96, 76, 56 ] 

print(student_scores['brian'])

