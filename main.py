
def main(): 
    principal = float(input("Purchase price > ")); 
    balance = principal - (principal * 0.1); 
    interest_rate = 0.12;
    payment = balance * 0.05; 
    i = 1
    line_new = '{:>2}  {:>12}  {:>8} {:>8} {:>12}'.format("Month", "Current balance", "  Interest","Payment","  New balance"); 
    print(); 
    print(line_new); 
    print("--------------------------------------------------------")

    while i <= 12: 
        interest = balance * (interest_rate/12); 
        old_balance = balance; 
        balance = balance - interest - payment; 
    
        print('%2d' '%15.2f' '%15.2f' '%10.2f' '%12.2f'% (i,old_balance,interest,payment,balance))
        print("________________________________________________________")
        i += 1; 
    
main();    
    
