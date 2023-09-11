def calculate_court_fee(case_type, claim_amount):
    fee_multipliers = {
        'civil': 0.02,      
        'criminal': 100,    
        'family': 0.015,    
        'property': 0.03,    
        'probate': 0.01,    
        'tax': 0.04,     
        'labor': 0.02,     
        'contract': 0.025, 
    }
    if case_type not in fee_multipliers:
        return "Invalid case type"
    fee = fee_multipliers[case_type] * claim_amount
    return fee
case_type = input("Enter the case type (e.g., civil, criminal, family, property, probate, tax, labor, contract, etc.): ")
claim_amount = float(input("Enter the claim amount: "))
court_fee = calculate_court_fee(case_type, claim_amount)
if court_fee == "Invalid case type":
    print("Invalid case type. Please enter a valid case type.")
else:
    print(f"The court fee for the {case_type} case with a claim amount of {claim_amount} is {court_fee}")
