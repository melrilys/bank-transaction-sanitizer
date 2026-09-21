import csv
from datetime import datetime

raw_data = [
    {"tx_id": "TX1001", "date": "2026-09-21", "user": "Lori James", "amount": "1500.50", "currency": "BRL"},
    {"tx_id": "TX1002", "date": "2026-09-21", "user": "John Doe", "amount": " -250.00 ", "currency": "USD"},
    {"tx_id": "TX1001", "date": "2026-09-21", "user": "Lori James", "amount": "1500.50", "currency": "BRL"},
    {"tx_id": "TX1003", "date": "ERROR", "user": "Alice Smith", "amount": "5000.00", "currency": "EUR"},
    {"tx_id": "TX1004", "date": "2026-09-20", "user": "Bob Johnson", "amount": "0.00", "currency": "BRL"},
    {"tx_id": "TX1008", "date": "2026-09-21", "user": "Candance Bennet", "amount": "1500.50", "currency": "BRL"},
    {"tx_id": "TX1009", "date": "2026-09-21", "user": "Stefan Smith", "amount": " -790.00 ", "currency": "USD"},
    {"tx_id": "TX1010", "date": "2026-09-21", "user": "Diana Z.s", "amount": "5500.50", "currency": "BRL"},
    {"tx_id": "TX1007", "date": "ERROR", "user": "Gregory Lewis", "amount": "9990.00", "currency": "EUR"},
    {"tx_id": "TX1005", "date": "2026-09-20", "user": "Marina Johnson", "amount": "9.00", "currency": "BRL"},
]

def clean_transactions(data):
    seen_ids = set()
    cleaned_list = []
    for tx in data:
        if tx["tx_id"] in seen_ids:
            continue
        try:
            tx_amount = float(tx["amount"].strip())
            if tx_amount <= 0:
                continue
        except ValueError:
            continue
        if tx["date"] == "ERROR":
            tx["date"] = datetime.now().strftime("%Y-%m-%d")
        tx["user"] = tx["user"].strip().title()
        tx["amount"] = tx_amount
        seen_ids.add(tx["tx_id"])
        cleaned_list.append(tx)
    return cleaned_list

if __name__ == "__main__":
    print(" Starting Intelligent Banking Sanitizer...")
    clean_data = clean_transactions(raw_data)
    for clean_tx in clean_data:
        print(f"✅ Approved Tx: {clean_tx['tx_id']} | User: {clean_tx['user']} | Total: {clean_tx['currency']} {clean_tx['amount']}")

