def find_pairs(arr,v):
    unique=[]
    for each in arr:                
        if(each not in unique):
            unique.append(each)
    
    count_pair=[]
    
    for each in unique:             
        count_pair.append(arr.count(each)) 
    print(count_pair) 
    
    final_count=0
    
    for each in count_pair:         
        final_count+=each//2
    return final_count        
            
n=10
sock_list=[10,20,20,10,10,30,50,10,20,20]       
print(find_pairs(sock_list, n)) 