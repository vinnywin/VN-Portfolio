salary = 30000
numDependents = 6

stateTaxRate = 0.065
stateTax = salary * stateTaxRate

federalTaxRate = 0.28
federalTax = salary * federalTaxRate

dependentDeductionRate = 0.025
dependentDeduction = salary * dependentDeductionRate * numDependents

totalWithholding = stateTax + federalTax + dependentDeduction

takeHomePay = salary - totalWithholding

print("State Tax: $", stateTax)
print("Federal Tax: $", federalTax)
print("Dependents: $", dependentDeduction)
print("salary: $", salary)
print("Total Withholding: $", totalWithholding)
print("Take-Home Pay: $", takeHomePay)
print("20250227_NguyenViet_2-4")
