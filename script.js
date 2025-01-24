function calculateSolarInvestment() {
    // Get user inputs
    let monthlyBill = parseFloat(document.getElementById("monthlyBill").value);
    let systemCost = parseFloat(document.getElementById("systemCost").value);
    let systemLifespan = parseInt(document.getElementById("systemLifespan").value);
    let taxCredit = parseFloat(document.getElementById("taxCredit").value);
    let solarCoverage = parseFloat(document.getElementById("solarCoverage").value) / 100;
    let energyBuybackRate = parseFloat(document.getElementById("energyBuybackRate").value);

    // Calculate savings
    let annualSavings = (monthlyBill * 12) * solarCoverage;
    let netCost = systemCost - taxCredit;
    let breakEvenYears = netCost / annualSavings;
    let totalSavings = annualSavings * systemLifespan;

    // Display results
    document.getElementById("annualSavings").innerText = `✅ Estimated Annual Savings: $${annualSavings.toFixed(2)}`;
    document.getElementById("breakEven").innerText = `✅ Break-even Period: ${breakEvenYears.toFixed(1)} years`;
    document.getElementById("totalSavings").innerText = `✅ Total Savings Over ${systemLifespan} Years: $${totalSavings.toFixed(2)}`;
}
