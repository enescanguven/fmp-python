"""Financial statements response models."""

from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class IncomeStatement(BaseModel):
    """Income statement model."""

    date: str
    symbol: str
    reported_currency: str = Field(alias="reportedCurrency")
    cik: str
    filling_date: Optional[str] = Field(None, alias="fillingDate")
    accepted_date: str = Field(alias="acceptedDate")
    calendar_year: Optional[str] = Field(None, alias="calendarYear")
    period: str
    revenue: Optional[float] = None
    cost_of_revenue: Optional[float] = Field(None, alias="costOfRevenue")
    gross_profit: Optional[float] = Field(None, alias="grossProfit")
    gross_profit_ratio: Optional[float] = Field(None, alias="grossProfitRatio")
    research_and_development_expenses: Optional[float] = Field(None, alias="researchAndDevelopmentExpenses")
    general_and_administrative_expenses: Optional[float] = Field(None, alias="generalAndAdministrativeExpenses")
    selling_and_marketing_expenses: Optional[float] = Field(None, alias="sellingAndMarketingExpenses")
    selling_general_and_administrative_expenses: Optional[float] = Field(None, alias="sellingGeneralAndAdministrativeExpenses")
    other_expenses: Optional[float] = Field(None, alias="otherExpenses")
    operating_expenses: Optional[float] = Field(None, alias="operatingExpenses")
    cost_and_expenses: Optional[float] = Field(None, alias="costAndExpenses")
    interest_income: Optional[float] = Field(None, alias="interestIncome")
    interest_expense: Optional[float] = Field(None, alias="interestExpense")
    depreciation_and_amortization: Optional[float] = Field(None, alias="depreciationAndAmortization")
    ebitda: Optional[float] = None
    ebitda_ratio: Optional[float] = Field(None, alias="ebitdaratio")
    operating_income: Optional[float] = Field(None, alias="operatingIncome")
    operating_income_ratio: Optional[float] = Field(None, alias="operatingIncomeRatio")
    total_other_income_expenses_net: Optional[float] = Field(None, alias="totalOtherIncomeExpensesNet")
    income_before_tax: Optional[float] = Field(None, alias="incomeBeforeTax")
    income_before_tax_ratio: Optional[float] = Field(None, alias="incomeBeforeTaxRatio")
    income_tax_expense: Optional[float] = Field(None, alias="incomeTaxExpense")
    net_income: Optional[float] = Field(None, alias="netIncome")
    net_income_ratio: Optional[float] = Field(None, alias="netIncomeRatio")
    eps: Optional[float] = None
    eps_diluted: Optional[float] = Field(None, alias="epsdiluted")
    weighted_average_shs_out: Optional[float] = Field(None, alias="weightedAverageShsOut")
    weighted_average_shs_out_dil: Optional[float] = Field(None, alias="weightedAverageShsOutDil")

    model_config = ConfigDict(populate_by_name=True)


class BalanceSheet(BaseModel):
    """Balance sheet statement model."""

    date: str
    symbol: str
    reported_currency: str = Field(alias="reportedCurrency")
    cik: str
    filling_date: Optional[str] = Field(None, alias="fillingDate")
    accepted_date: str = Field(alias="acceptedDate")
    calendar_year: Optional[str] = Field(None, alias="calendarYear")
    period: str
    cash_and_cash_equivalents: Optional[float] = Field(None, alias="cashAndCashEquivalents")
    short_term_investments: Optional[float] = Field(None, alias="shortTermInvestments")
    cash_and_short_term_investments: Optional[float] = Field(None, alias="cashAndShortTermInvestments")
    net_receivables: Optional[float] = Field(None, alias="netReceivables")
    inventory: Optional[float] = None
    other_current_assets: Optional[float] = Field(None, alias="otherCurrentAssets")
    total_current_assets: Optional[float] = Field(None, alias="totalCurrentAssets")
    property_plant_equipment_net: Optional[float] = Field(None, alias="propertyPlantEquipmentNet")
    goodwill: Optional[float] = None
    intangible_assets: Optional[float] = Field(None, alias="intangibleAssets")
    goodwill_and_intangible_assets: Optional[float] = Field(None, alias="goodwillAndIntangibleAssets")
    long_term_investments: Optional[float] = Field(None, alias="longTermInvestments")
    tax_assets: Optional[float] = Field(None, alias="taxAssets")
    other_non_current_assets: Optional[float] = Field(None, alias="otherNonCurrentAssets")
    total_non_current_assets: Optional[float] = Field(None, alias="totalNonCurrentAssets")
    other_assets: Optional[float] = Field(None, alias="otherAssets")
    total_assets: Optional[float] = Field(None, alias="totalAssets")
    account_payables: Optional[float] = Field(None, alias="accountPayables")
    short_term_debt: Optional[float] = Field(None, alias="shortTermDebt")
    tax_payables: Optional[float] = Field(None, alias="taxPayables")
    deferred_revenue: Optional[float] = Field(None, alias="deferredRevenue")
    other_current_liabilities: Optional[float] = Field(None, alias="otherCurrentLiabilities")
    total_current_liabilities: Optional[float] = Field(None, alias="totalCurrentLiabilities")
    long_term_debt: Optional[float] = Field(None, alias="longTermDebt")
    deferred_revenue_non_current: Optional[float] = Field(None, alias="deferredRevenueNonCurrent")
    deferred_tax_liabilities_non_current: Optional[float] = Field(None, alias="deferredTaxLiabilitiesNonCurrent")
    other_non_current_liabilities: Optional[float] = Field(None, alias="otherNonCurrentLiabilities")
    total_non_current_liabilities: Optional[float] = Field(None, alias="totalNonCurrentLiabilities")
    other_liabilities: Optional[float] = Field(None, alias="otherLiabilities")
    capital_lease_obligations: Optional[float] = Field(None, alias="capitalLeaseObligations")
    total_liabilities: Optional[float] = Field(None, alias="totalLiabilities")
    preferred_stock: Optional[float] = Field(None, alias="preferredStock")
    common_stock: Optional[float] = Field(None, alias="commonStock")
    retained_earnings: Optional[float] = Field(None, alias="retainedEarnings")
    accumulated_other_comprehensive_income_loss: Optional[float] = Field(None, alias="accumulatedOtherComprehensiveIncomeLoss")
    othertotal_stockholders_equity: Optional[float] = Field(None, alias="othertotalStockholdersEquity")
    total_stockholders_equity: Optional[float] = Field(None, alias="totalStockholdersEquity")
    total_equity: Optional[float] = Field(None, alias="totalEquity")
    total_liabilities_and_stockholders_equity: Optional[float] = Field(None, alias="totalLiabilitiesAndStockholdersEquity")
    minority_interest: Optional[float] = Field(None, alias="minorityInterest")
    total_liabilities_and_total_equity: Optional[float] = Field(None, alias="totalLiabilitiesAndTotalEquity")
    total_investments: Optional[float] = Field(None, alias="totalInvestments")
    total_debt: Optional[float] = Field(None, alias="totalDebt")
    net_debt: Optional[float] = Field(None, alias="netDebt")

    model_config = ConfigDict(populate_by_name=True)


class CashFlowStatement(BaseModel):
    """Cash flow statement model."""

    date: str
    symbol: str
    reported_currency: str = Field(alias="reportedCurrency")
    cik: str
    filling_date: Optional[str] = Field(None, alias="fillingDate")
    accepted_date: str = Field(alias="acceptedDate")
    calendar_year: Optional[str] = Field(None, alias="calendarYear")
    period: str
    net_income: Optional[float] = Field(None, alias="netIncome")
    depreciation_and_amortization: Optional[float] = Field(None, alias="depreciationAndAmortization")
    deferred_income_tax: Optional[float] = Field(None, alias="deferredIncomeTax")
    stock_based_compensation: Optional[float] = Field(None, alias="stockBasedCompensation")
    change_in_working_capital: Optional[float] = Field(None, alias="changeInWorkingCapital")
    accounts_receivables: Optional[float] = Field(None, alias="accountsReceivables")
    inventory: Optional[float] = None
    accounts_payables: Optional[float] = Field(None, alias="accountsPayables")
    other_working_capital: Optional[float] = Field(None, alias="otherWorkingCapital")
    other_non_cash_items: Optional[float] = Field(None, alias="otherNonCashItems")
    net_cash_provided_by_operating_activities: Optional[float] = Field(None, alias="netCashProvidedByOperatingActivities")
    investments_in_property_plant_and_equipment: Optional[float] = Field(None, alias="investmentsInPropertyPlantAndEquipment")
    acquisitions_net: Optional[float] = Field(None, alias="acquisitionsNet")
    purchases_of_investments: Optional[float] = Field(None, alias="purchasesOfInvestments")
    sales_maturities_of_investments: Optional[float] = Field(None, alias="salesMaturitiesOfInvestments")
    other_investing_activites: Optional[float] = Field(None, alias="otherInvestingActivites")
    net_cash_used_for_investing_activites: Optional[float] = Field(None, alias="netCashUsedForInvestingActivites")
    debt_repayment: Optional[float] = Field(None, alias="debtRepayment")
    common_stock_issued: Optional[float] = Field(None, alias="commonStockIssued")
    common_stock_repurchased: Optional[float] = Field(None, alias="commonStockRepurchased")
    dividends_paid: Optional[float] = Field(None, alias="dividendsPaid")
    other_financing_activites: Optional[float] = Field(None, alias="otherFinancingActivites")
    net_cash_used_provided_by_financing_activities: Optional[float] = Field(None, alias="netCashUsedProvidedByFinancingActivities")
    effect_of_forex_changes_on_cash: Optional[float] = Field(None, alias="effectOfForexChangesOnCash")
    net_change_in_cash: Optional[float] = Field(None, alias="netChangeInCash")
    cash_at_end_of_period: Optional[float] = Field(None, alias="cashAtEndOfPeriod")
    cash_at_beginning_of_period: Optional[float] = Field(None, alias="cashAtBeginningOfPeriod")
    operating_cash_flow: Optional[float] = Field(None, alias="operatingCashFlow")
    capital_expenditure: Optional[float] = Field(None, alias="capitalExpenditure")
    free_cash_flow: Optional[float] = Field(None, alias="freeCashFlow")

    model_config = ConfigDict(populate_by_name=True)


class FinancialGrowth(BaseModel):
    """Financial growth metrics model."""

    symbol: str
    date: str
    period: str
    revenue_growth: Optional[float] = Field(None, alias="revenueGrowth")
    gross_profit_growth: Optional[float] = Field(None, alias="grossProfitGrowth")
    ebit_growth: Optional[float] = Field(None, alias="ebitgrowth")
    operating_income_growth: Optional[float] = Field(None, alias="operatingIncomeGrowth")
    net_income_growth: Optional[float] = Field(None, alias="netIncomeGrowth")
    eps_growth: Optional[float] = Field(None, alias="epsgrowth")
    eps_diluted_growth: Optional[float] = Field(None, alias="epsdilutedGrowth")
    operating_cash_flow_growth: Optional[float] = Field(None, alias="operatingCashFlowGrowth")
    free_cash_flow_growth: Optional[float] = Field(None, alias="freeCashFlowGrowth")
    asset_growth: Optional[float] = Field(None, alias="assetGrowth")
    book_value_per_share_growth: Optional[float] = Field(None, alias="bookValueperShareGrowth")
    debt_growth: Optional[float] = Field(None, alias="debtGrowth")
    receivables_growth: Optional[float] = Field(None, alias="receivablesGrowth")
    inventory_growth: Optional[float] = Field(None, alias="inventoryGrowth")
    rd_expense_growth: Optional[float] = Field(None, alias="rdexpenseGrowth")
    sga_expenses_growth: Optional[float] = Field(None, alias="sgaexpensesGrowth")

    model_config = ConfigDict(populate_by_name=True)
