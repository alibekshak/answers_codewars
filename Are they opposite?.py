def is_opposite(s1,s2):
    if s1 == '' or s2 == '':
        return False
    
    else:
        for i in range(len(s1)):
            for j in range(len(s2)):

                if s1[i] is not s2[j]:
                    return True
                else:
                    return False 