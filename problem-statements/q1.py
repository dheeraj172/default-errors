#team name : default errors

def calculate_total_bill(amount: float, tip_percent: int )->float:
  amount = float(amount)
  tip_percent = float(tip_percent)
  
  if not (0 <=amount<=10000):
   raise ValueError("amount must be b/w 0 and 10000")
  if not (0<=tip_percent<=100):
   raise ValueError("amount must be b/w 0 and 100")  
    
  total_bill = amount + (amount * tip_percent)/100
  return round(total_bill,2)
