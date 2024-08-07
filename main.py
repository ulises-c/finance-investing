import interest

a = interest.compound_interest(2809.13, 5, 365, 1/12)
print(f"${a:0.2f}")


# Example usage:
principal = 2809.13  # Initial principal amount
interest_rate = 5  # Annual interest rate (in percent)
compounds_per_year = 12  # Compounding frequency (monthly)
time_years = 1  # Time in years
deposit_amount = 200  # Deposit amount
deposit_interval_days = 14  # Deposit interval in days

final_amount = interest.compound_interest_deposits(principal, interest_rate, compounds_per_year,
                                         time_years, deposit_amount, deposit_interval_days)
print(f"Final amount after {time_years} years with deposits: ${final_amount:.2f}")

fv = interest.future_value(200, 5, 365, 1/12)
print(f"${fv:0.2f}")