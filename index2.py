

def max_salary(list):
    
    
    max=0
    dict={}
    
    for item in list:
        
        if (item["salary"]>max):
            
            max = item["salary"]
            dict = item
    
    
    return dict    