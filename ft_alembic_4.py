import alchemy

print("=== Alembic 4 ===")
print("Accessing alchemy/elements.py using 'from ... import ...' structure")
print("Testing create_air:", alchemy.create_air())

print("Trying hidden function...")
print(alchemy.create_earth())