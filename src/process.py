
def filter_records(records: list[dict], min_score: int) -> list[dict]:
    """Keep records whose score is greater than or equal to min_score."""
    return [r for r in records if r["score"] >= min_score]


def format_label(record: str) -> str:
    """Format a record as a readable label."""
    return record.strip().title()

def summarize(records: list[dict]) -> dict:
    """Return count, highest-scoring record, and average score."""
    if not records:
        return {
            "count": 0,
            "highest": None,
            "average": 0.0
        }

    return {
        "count": len(records),
        "highest": max(records, key=lambda r: r["score"]),
        "average": round(
            sum(r["score"] for r in records) / len(records), 1
        )
    }
