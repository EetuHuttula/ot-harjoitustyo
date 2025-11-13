import json
from pathlib import Path

from entities.user import User

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
DATA_FILE = DATA_DIR / "users.json"

if not DATA_FILE.exists():
	DATA_FILE.write_text("[]")


def _load_raw():
	"""Load raw JSON list of user records (dicts)."""
	try:
		with DATA_FILE.open("r", encoding="utf-8") as f:
			data = json.load(f)
	except Exception:
		data = []
	if not isinstance(data, list):
		data = []
	return data


def _save_raw(records):
	with DATA_FILE.open("w", encoding="utf-8") as f:
		json.dump(records, f, ensure_ascii=False, indent=2)


def add_user(username: str, password: str):
	"""Add a new user and persist to JSON file (plain text passwords).

	Raises Exception if username already exists or inputs invalid.
	"""
	if not username or not password:
		raise Exception("Username and password are required")

	records = _load_raw()
	if any(rec.get("username") == username for rec in records):
		raise Exception("Username already exists")

	record = {
		"username": username,
		"password": password, 
	}
	records.append(record)
	_save_raw(records)


def get_user_record(username: str):
	"""Return the raw stored record (dict) for username, or None."""
	records = _load_raw()
	for rec in records:
		if rec.get("username") == username:
			return rec
	return None


def get_user_by_username(username: str):
	"""Return a User instance for the username or None."""
	rec = get_user_record(username)
	if not rec:
		return None
	return User(rec.get("username"), rec.get("password"))


def verify_password(username: str, password: str):
	"""Verify given password against stored credentials. Returns True/False."""
	rec = get_user_record(username)
	if not rec:
		return False
	return rec.get("password") == password
