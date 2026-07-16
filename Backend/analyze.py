def analyze_company(metrics):
    pros = []
    cons = []

    # ROE analysis
    if metrics["roe"] >= 15:
        pros.append(f"Strong ROE of {metrics['roe']}%")
    else:
        cons.append(f"Low ROE of {metrics['roe']}%")

    # ROCE analysis
    if metrics["roce"] >= 20:
        pros.append(f"Healthy ROCE of {metrics['roce']}%")
    else:
        cons.append(f"Weak ROCE of {metrics['roce']}%")

    # Profitability
    if metrics["net_profit"] > 0:
        pros.append("Company is profitable")
    else:
        cons.append("Company is not profitable")

    return pros, cons
