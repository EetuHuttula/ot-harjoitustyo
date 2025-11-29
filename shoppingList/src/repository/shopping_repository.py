"""Shopping repository for persisting shopping items to JSON."""
import json
from pathlib import Path
from entities.shopping import Shopping

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
DATA_FILE = DATA_DIR / "shopping.json"

if not DATA_FILE.exists():
    DATA_FILE.write_text("[]")


def _load_raw():
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        data = []

    if not isinstance(data, list):
        data = []
    return data


def _save_raw(records):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def _next_id(records):
    if not records:
        return 1
    ids = [rec.get("id", 0) for rec in records if isinstance(rec.get("id", 0), int)]
    return max(ids, default=0) + 1

# AI GENERATED STARTS
def add_item(name: str, amount: str, owner: str):
    """Add a shopping item. Returns Shopping instance."""
    if not name:
        raise ValueError("Item name is required")
    records = _load_raw()
    # If an item with the same name and owner exists, try to aggregate amounts
    for rec in records:
        if rec.get("owner") == owner and rec.get("name") == name:
            # try to parse numeric amounts and add them
            try:
                existing = rec.get("amount")
                # attempt integer addition first
                existing_num = None
                new_num = None
                try:
                    existing_num = int(existing)
                except Exception:
                    try:
                        existing_num = float(existing)
                    except Exception:
                        existing_num = None
                try:
                    new_num = int(amount)
                except Exception:
                    try:
                        new_num = float(amount)
                    except Exception:
                        new_num = None

                if existing_num is not None and new_num is not None:
                    summed = existing_num + new_num
                    # use int when possible
                    if int(summed) == summed:
                        rec["amount"] = int(summed)
                    else:
                        rec["amount"] = summed
                else:
                    # fallback: overwrite with the provided amount string
                    rec["amount"] = amount

            except Exception:
                # if anything goes wrong, just overwrite
                rec["amount"] = amount

            _save_raw(records)
            return Shopping.from_dict(rec)

    # otherwise create a new record
    new_id = _next_id(records)
    rec = {"id": new_id, "name": name, "amount": amount, "owner": owner}
    records.append(rec)
    _save_raw(records)
    return Shopping.from_dict(rec)
# AI GENERATED ENDS

def list_items_by_owner(owner: str):
    """Return list of Shopping instances belonging to owner."""
    records = _load_raw()
    items = [Shopping.from_dict(rec) for rec in records if rec.get("owner") == owner]
    return items


def remove_item(item_id: int, owner: str):
    """Remove item by id if it belongs to owner. Returns True if removed."""
    records = _load_raw()
    new_records = [rec for rec in records if not (rec.get("id") == item_id and rec.get("owner") == owner)]
    if len(new_records) == len(records):
        return False
    _save_raw(new_records)
    return True


def delete_all_items():
    _save_raw([])
