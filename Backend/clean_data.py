def extract_metrics(raw_data):
    company = raw_data.get("company", {})
    data = raw_data.get("data", {})

    metrics = {}

    # Core metrics (already available)
    metrics["company_name"] = company.get("company_name", "Unknown")
    metrics["roe"] = float(company.get("roe_percentage", 0))
    metrics["roce"] = float(company.get("roce_percentage", 0))

    # Profit (latest year from P&L)
    profit_loss = data.get("profitloss", [])
    if profit_loss and isinstance(profit_loss, list):
        latest = profit_loss[0]
        metrics["net_profit"] = latest.get("net_profit", 0)
        metrics["sales"] = latest.get("sales", 0)
    else:
        metrics["net_profit"] = 0
        metrics["sales"] = 0

    return metrics
