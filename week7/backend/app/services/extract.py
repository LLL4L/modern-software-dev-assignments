import re

ACTION_PREFIXES = ("todo:", "action:", "fixme:", "hack:", "bug:", "note:")


def extract_action_items(text: str) -> list[str]:
    results: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        cleaned = re.sub(r"^[-*]\s+", "", stripped)
        normalized = cleaned.lower()

        if any(normalized.startswith(prefix) for prefix in ACTION_PREFIXES):
            results.append(cleaned)
        elif re.search(r"\[[ x]]", stripped):
            results.append(cleaned)
        elif stripped.endswith("!"):
            results.append(stripped)
    return results
