"""Shopping repository for persisting shopping items to JSON."""
from pathlib import Path
from entities.shopping import Shopping
from repository.json_utils import load_raw, save_raw

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
DATA_FILE = DATA_DIR / "shopping.json"

if not DATA_FILE.exists():
    DATA_FILE.write_text("[]")


def _load_raw():
    """Load raw JSON list of shopping records."""
    return load_raw(DATA_FILE)


def _save_raw(records):
    """Save shopping records to JSON file."""
    save_raw(DATA_FILE, records)


def _next_id(records):
    """Calculate the next available ID for a shopping item."""
    if not records:
        return 1
    ids = [rec.get("id", 0) for rec in records
           if isinstance(rec.get("id", 0), int)]
    return max(ids, default=0) + 1


def _parse_numeric_value(value):
    """Parse a string value to int or float, or return None."""
    try:
        return int(value)
    except (ValueError, TypeError):
        pass
    try:
        return float(value)
    except (ValueError, TypeError):
        pass
    return None


def _update_existing_item(rec, amount):
    """Update an existing item's amount by aggregating if possible."""
    existing = rec.get("amount")
    existing_num = _parse_numeric_value(existing)
    new_num = _parse_numeric_value(amount)

    if existing_num is not None and new_num is not None:
        summed = existing_num + new_num
        if int(summed) == summed:
            rec["amount"] = int(summed)
        else:
            rec["amount"] = summed
    else:
        rec["amount"] = amount

#Ai GENERATED START
def add_item(name: str, amount: str, owner: str):
    """Add a shopping item. Returns Shopping instance."""
    if not name:
        raise ValueError("Item name is required")
    records = _load_raw()

    for rec in records:
        if rec.get("owner") == owner and rec.get("name") == name:
            _update_existing_item(rec, amount)
            _save_raw(records)
            return Shopping.from_dict(rec)

    new_id = _next_id(records)
    rec = {"id": new_id, "name": name, "amount": amount, "owner": owner}
    records.append(rec)
    _save_raw(records)
    return Shopping.from_dict(rec)
# Ai GENERATED ENDS

def list_items_by_owner(owner: str):
    """Return list of Shopping instances belonging to owner."""
    records = _load_raw()
    items = [Shopping.from_dict(rec) for rec in records if rec.get("owner") == owner]
    return items


def remove_item(item_id: int, owner: str):
    """Remove item by id if it belongs to owner. Returns True if removed."""
    records = _load_raw()
    new_records = [rec for rec in records
                   if not (rec.get("id") == item_id
                           and rec.get("owner") == owner)]
    if len(new_records) == len(records):
        return False
    _save_raw(new_records)
    return True


def delete_all_items():
    """Delete all items from the shopping repository."""
    _save_raw([])


def load_all_items():
    """Load all items from the shopping repository."""
    return _load_raw()


def save_all_items(items):
    """Save all items to the shopping repository."""
    _save_raw(items)
