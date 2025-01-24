def solar_investment_calculator():
    print("🌞 Solar Investment Calculator ☀️💰")
    print("Estimate your savings and break-even period by switching to solar energy.\n")

    # User Inputs
    monthly_bill = float(input("Enter your average monthly electricity bill ($): "))
    system_cost = float(input("Enter the total cost of installing solar panels ($): "))
    system_lifespan = int(input("Enter the expected lifespan of the solar system (years): "))
    tax_credit = float(input("Enter the government incentive or tax credit amount ($): "))
    solar_coverage = float(input("Enter the percentage of your electricity usage covered by solar (0-100%): ")) / 100
    energy_buyback_rate = float(input("Enter the energy buyback rate per kWh ($): "))

    # Calculations
    annual_savings = (monthly_bill * 12) * solar_coverage
    net_cost = system_cost - tax_credit
    break_even_years = net_cost / annual_savings
    total_savings = annual_savings * system_lifespan

    # Display Results
    print("\n🔹 Solar Investment Summary 🔹")
    print(f"✅ Estimated Annual Savings: ${annual_savings:,.2f}")
    print(f"✅ Break-even Period: {break_even_years:.1f} years")
    print(f"✅ Total Savings Over {system_lifespan} Years: ${total_savings:,.2f}")

if __name__ == "__main__":
    solar_investment_calculator()

