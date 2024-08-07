def compound_interest(P:float, r:float, n:float, t:float) -> float:
    """
    Simple compounding interest formula without deposits
    Formula: A = P * (1+(r/n))^(n*t)
    A = amount in dollars
    P = principal
    r = interest rate
    n = times compounded per year
    t = time in years
    """
    r = r / 100 # convert to percent
    return P * (1+(r/n))**(n*t)

def compound_interest_deposits(P:float, r:float, n:float, t:float, da:float, dt:float) -> float:
    """
    Compounding interest formula with deposits at a set interval
    Call `compound_interest()` (recursively?)
    dt = time delta in between deposits in days
    da = deposit amount in dollars
    """
    # BUG & TODO: Compounds too much, fix to compound correctly
    dt = dt / 365 # convert to years
    total_interest = 0
    # Calculate interest for each deposit interval
    for _ in range(int(t / dt)):
        # Calculate interest for the current interval
        interest = compound_interest(P, r, n, dt)
        # Add the deposit amount & interest to the principal for the next interval
        P += (da + interest)
    return P

def future_value(da:float, r:float, n:float, t:float):
    """
    Formula: FV = da * ((((1+(r/n))^nt) - 1) / (r/n))
    """
    r = r / 100
    numerator = ((1 + (r/n))**(n*t) )- 1
    return da * numerator / (r/n)