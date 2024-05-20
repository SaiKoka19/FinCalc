#financial_Calculator 

#declare functions
def present_value(future_value, rate, periods):
    pv = future_value / (1 + rate) ** periods
    return pv

def future_value(present_value, rate, periods):
    fv = present_value * (1 + rate) ** periods
    return fv

def simple_interest(principal,rate,time):
    s_i = principal * (1 + rate*time)
    return s_i

def compound_interest(principal,rate,number_of_comp_periods,time):
    c_i = principal * (1 + (rate/number_of_comp_periods) ** number_of_comp_periods*time)
    return c_i

def annual_pecentage_rate(effective_annual_rate, time):
    apr = (((1 + effective_annual_rate) ** time)-1)/time
    return apr

def effective_annual_interest_rate(nominal_interest_rate, periods):
    eair = ((1 + (nominal_interest_rate/periods))** periods)-1
    return eair

def bond_value(coupon, rate, periods, par_value):
    bnd_val = (((coupon * (1/rate)(1-(1/(1+rate)** -periods)))/rate))+(par_value/((1 + rate)**periods))
    return bnd_val

def bond_current_yield(coupon_price, current_value_bnd):
    bnd_current_yield = (coupon_price/current_value_bnd)
    return bnd_current_yield

def stock_profit(price_sold,purchase_price,shares,buying_commission,selling_commission):
    s_profit = (((price_sold * shares)-selling_commission) - ((purchase_price * shares)+ buying_commission))
    return s_profit
    

#declare main function
def main():
    print("Financial Calculator")
    print("1. Present Value")
    print("2. Future Value")
    print("3. Simple Interest")
    print("4. Compound Interest")
    print("5. Annual Percentage Rate")
    print("6. Effective Annual Rate")
    print("7. Bond Value")
    print("8. Bond Current Yield")
    print("9. Stock Profit")
    choice = input("Select calculation: ")

    if choice == '1':
        fv = float(input("Enter future value: "))
        rate = float(input("Enter interest rate (as a decimal): "))
        periods = int(input("Enter number of periods: "))
        pv = present_value(fv, rate, periods)
        print(f"Present Value:${pv:.2f}")

    elif choice == '2':
        pv = float(input("Enter present value: "))
        rate = float(input("Enter interest rate (as a decimal): "))
        periods = int(input("Enter number of periods: "))
        fv = future_value(pv, rate, periods)
        print(f"Future Value:${fv:.2f}")

    elif choice == '3':
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter interest rate (as a decimal): "))
        time = int(input("Enter number of periods: "))
        s_i = principal * (1 + rate*time)
        print(f"Simple Interest:${s_i:.2f}")

    elif choice == '4':
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter interest rate (as a decimal): "))
        number_of_comp_periods = int(input("Enter number of compounding periods: "))
        time = int(input("Enter time in years: "))
        c_i = principal * (1 + (rate/number_of_comp_periods) ** number_of_comp_periods*time)
        print(f"Compound Interest:${c_i:.2f}")

    elif choice == '5':
        effective_annual_rate = float(input("Enter effective annual rate (as a decimal): "))
        time = int(input("Enter time period in years: "))
        apr = (((1 + effective_annual_rate) ** time)-1)*100/time
        print(f"Annual Percentage Rate: {apr:.2f}%")

    elif choice == '6':
        nominal_interest_rate = float(input("Enter interest rate (as a decimal): "))
        periods = int(input("Enter number of quarters: "))
        eair = (((1 + (nominal_interest_rate/periods))** periods)-1)*100
        print(f"Effective Annual Interest Rate: {eair:.2f}%")

    elif choice == '7':
        coupon = float(input("Enter Coupon Payment: "))
        rate = float(input("Enter interest rate (as a decimal): "))
        periods = int(input("Enter number of compounding periods: "))
        par_value = float(input("Enter Par value of bond: "))
        present_value_coupons = (coupon / rate) * (1 - (1 + rate)**-periods)
        present_value_par_value = par_value / (1 + rate)**periods
        bnd_val = present_value_coupons + present_value_par_value
        print(f"Bond Value:${bnd_val:.2f}")

    elif choice == '8':
        coupon_price = float(input("Enter Coupon Price: "))
        current_value_bnd = float(input("Enter Current Value of Bond: "))
        bnd_current_yield = (coupon_price/current_value_bnd)*(100)
        print(f"Bond Current Yield: {bnd_current_yield:.2f}%")
    
    elif choice == '9':
        price_sold = float(input("Enter price you sold the stock at: "))
        shares = float(input("Enter number of shares: "))
        selling_commission = float(input("Enter amount of selling commission fees paid: "))
        purchase_price = float(input("Enter price you bought the stock at: "))
        buying_commission = float(input("Enter amount of buying commission fees paid: "))
        s_profit = (((price_sold * shares)-selling_commission) - ((purchase_price * shares)+ buying_commission))
        print(f"Stock Profit:${s_profit:.2f}")
   
    else:
        print("Invalid choice. Please select from the following options.")
main()