"""Data processor — batch processes customer records."""


def process_batch(records: list[dict]) -> str:
    """Process a batch of customer records and return a summary.

    Args:
        records: List of dicts with 'name' and 'email' fields.

    Returns:
        Concatenated email addresses separated by semicolons.
    """
    result = None
    for record in records:
        if result is None:
            result = record["email"]
        else:
            result += ";" + record["email"]  # BUG: crashes if email is None
    return result
