import json
from fetch_details import fetch_company_data
from clean_data import extract_metrics
from analyze import analyze_company
from db_config import get_connection
from colorama import Fore, Style, init
import logging

# Initialize colorama
init(autoreset=True)

# Logging configuration
logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_company_analysis(company_id):
    """
    Core function used by API / frontend.
    Fetches, cleans, analyzes and stores company data.
    Returns structured JSON-safe dictionary.
    """

    # ===== FETCH DATA =====
    raw_text = fetch_company_data(company_id)
    raw_data = json.loads(raw_text)

    # ===== HANDLE API ERROR =====
    if "error" in raw_data:
        raise Exception(f"No data found for company: {company_id}")

    # ===== CLEAN DATA =====
    metrics = extract_metrics(raw_data)

    # ===== ANALYSIS =====
    pros, cons = analyze_company(metrics)

    # ===== STORE IN DATABASE =====
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO ml (
        company_id, company_name, roe, roce, net_profit, pros, cons
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        company_name = VALUES(company_name),
        roe = VALUES(roe),
        roce = VALUES(roce),
        net_profit = VALUES(net_profit),
        pros = VALUES(pros),
        cons = VALUES(cons),
        updated_at = CURRENT_TIMESTAMP;
    """

    cursor.execute(query, (
        company_id,
        metrics["company_name"],
        metrics["roe"],
        metrics["roce"],
        metrics["net_profit"],
        ", ".join(pros),
        ", ".join(cons)
    ))

    conn.commit()
    cursor.close()
    conn.close()

    # ===== RETURN STRUCTURED DATA =====
    return {
        "id": company_id,
        "name": metrics["company_name"],
        "roe": metrics["roe"],
        "roce": metrics["roce"],
        "net_profit": metrics["net_profit"],
        "pros": pros,
        "cons": cons
    }


def display_result(company_name, company_id, result, current, total):
    print("\n" + "=" * 60)
    print(f"Processing [{current}/{total}] - {company_name} ({company_id})")
    print("=" * 60)

    logging.info(f"Processing {company_name} ({company_id})")

    print(Fore.GREEN + "\nTop Pros:")
    for pro in result.get("pros", []):
        print(Fore.GREEN + f"✔ {pro}")
        logging.info(f"PRO: {pro}")

    print(Fore.RED + "\nTop Cons:")
    for con in result.get("cons", []):
        print(Fore.RED + f"✘ {con}")
        logging.info(f"CON: {con}")

    print(Fore.CYAN + "\nCompleted Successfully\n")
    logging.info("Completed Successfully\n")


# =========================
# CLI ENTRY POINT
# =========================
if __name__ == "__main__":

    print(Fore.CYAN + "\nBluestocks Financial Analysis CLI\n")

    company_id = input("Enter Company ID (example: TCS, INFY, BAJAJ-AUTO): ").strip().upper()

    try:
        print(Fore.YELLOW + "\nFetching and analyzing...\n")

        result = get_company_analysis(company_id)

        # Single company progress (1/1)
        display_result(
            result["name"],
            result["id"],
            result,
            current=1,
            total=1
        )

        print(Fore.GREEN + "Analysis Completed Successfully ✔")
        logging.info("Final Success")

    except Exception as e:
        print(Fore.RED + f"\nError: {str(e)}")
        logging.error(f"Error occurred: {str(e)}")
