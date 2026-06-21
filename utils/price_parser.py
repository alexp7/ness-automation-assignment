import re


def parse_price(price_text: str) -> float:
    match = re.search(r"\d+(?:,\d{3})*(?:\.\d{2})?", price_text)

    if not match:
        raise ValueError(f"Could not parse price from text: {price_text}")

    return float(match.group().replace(",", ""))