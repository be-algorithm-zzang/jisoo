def solution(brown, yellow):
    answer = []
    
    total=brown+yellow
    
    a=2
    b=4-brown
    c=2*yellow
    
    
    x1= (-b + (b**2-4*a*c)**0.5)//(2*a)
    x2 = (-b - (b**2-4*a*c)**0.5)//(2*a)
    
    row=2
    
    if x1>=x2:
        row+=x1
    
    answer.append(row)
    answer.append(total//row)   
    
    answer.sort(reverse=True)
    
    return answer