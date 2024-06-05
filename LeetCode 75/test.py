def test(s):
        
    clean_s = ' '.join(s.split())
        
    s_array = clean_s.split()
    result = ""

    for i in range(len(s_array) - 1, -1, -1):
        result = result + s_array[i]

    return result
    
    
s = "This                        is   an         example             string."
print(test(s))