# 👇🏻 YOUR CODE 👇🏻:


def get_yearly_revenue(monthly_revenue):
  return monthly_revenue
  
def get_yearly_expenses(monthly_expenses):
  return monthly_expenses

def get_tax_amount(profit):
  if profit>100000:
    tax_amount = 0.25*profit
  else:
    tax_amount = 0.15*profit
  return tax_amount

def apply_tax_credits(tax_amount,tax_credits):
  return tax_amount*tax_credits

# /YOUR CODE
# BLUEPRINT | DONT EDIT
monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01

profit = get_yearly_revenue(monthly_revenue) - get_yearly_expenses(monthly_expenses)

print(profit)

tax_amount = get_tax_amount(profit)

print(tax_amount)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount,tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")


# /BLUEPRINT