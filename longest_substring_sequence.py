# Online Python compil

def check_substring(mystr,jump):
    
    start = i = int(0)
    end = jump
    substr = mystr[start:end]
    flag = int(0)
    
    while i < len(mystr):
        
        if mystr[start:end] != '':
            if substr != mystr[start:end]:
                flag = -1
                break
            else:
                print(f"substr {substr}  mystr {mystr[start:end]} flag {flag}")
        
        start = end
        end = end + jump
        i = i + 1
        
        
    return flag

def longest_substring(mystr):
    flag = jump = i = int(0)
    threshold = int(4)
    
    while True:
        if i  >= threshold:
            return -1
            
        if check_substring(mystr,jump + 1) == 0:
            return 1
        
        else:
            i = i + 1
            jump = jump + 1    
            




mystr = "aaaaaabaaaa"

print(longest_substring(mystr))
    
