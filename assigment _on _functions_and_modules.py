def transaction_summary (transactions):
    income = 0
    expenses = 0
    for amount in transactions:
        if amount>0:
            income+= amount 
        else:
         expenses += abs(amount)
    balance = income - expenses
    return{"income" : income,
           "expenses" : expenses,
           "balance" : balance}
transactions = ( 5000, -2000 ,1500 ,-800,3000)
print(transaction_summary(transactions))

def restock_items(inventory , threshold):
   needs_restock = []
   for item,quantity in inventory.itms ():
      if quantity< threshold:
         needs_restock.append(item)
         return needs_restock
      # test case;
      inventory = { "rice" : 10,
                   "beans" : 4,
                   "sugar" : 20}
      print(restock_items(inventory , 5))

def find_duplicates(items):
   seen = set()
   duplicates = []
   for item in items:
      if item in seen:
         if item not in duplicates:
            duplicates.append(item)  
         else:
            seen.add(item)
      return duplicates   
   print(find_duplicates([2,5,7,2,8,5,1]))

def count_logs(logs):
      log_counts ={}
      for log in logs:
         if log in log_counts:
            log_counts[log]+=1
         else:
            log_counts[log] = 1
      return log_counts
         #test case
logs = [ "info login successful", 
                 "error database failed" 
                 "info logout",  
                 "warning disk low" 
                 "error timeout" ]
print(count_logs(logs)) 
                 

                              
                

      


    
