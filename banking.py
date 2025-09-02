"""
Bank Account Simulation

Task:
- Manage simple bank accounts.
- Store accounts in dictionary { "account_number": {"name": str, "balance": float} }
- Deposit, withdraw, transfer between accounts.
- Use *args for batch deposits/withdrawals.
- Use **kwargs for flexible account creation (e.g., overdraft_limit).

// NOT FOR THIS TASK
Future OOP Extension:
- BankAccount class with methods deposit(), withdraw(), transfer().
- Bank class to manage all accounts.
"""

accounts = {}

def create_account(account_number, name, **kwargs):
    """Create an account with optional features like overdraft_limit."""
    pass

def deposit(account_number, amount):
    """Deposit money into account.
        return "Account not found!" (if account does not exists)
        return Deposited {amount} into {accounts name}'s account. if account exists
    """
    pass

def withdraw(account_number, amount):
    """Withdraw money if balance is sufficient. else: insufficient funds"""
    pass

def transfer(from_acc, to_acc, amount):
    """Transfer money between accounts. if funds is sufficient"""
    pass

accounts = {}

def create_account(account_number, name, **kwargs):
    """Create an account with optional features like overdraft_limit."""
    if account_number not in accounts:
        accounts[account_number] = {
            "name": name,
            "balance": 0.0
        }
        # Add optional fields (like overdraft_limit, account_type, etc.)
        accounts[account_number].update(kwargs)
        return f"Account {account_number} created for {name}."
    else:
        return f"Account {account_number} already exists!"


def deposit(account_number, *amounts):
    """Deposit one or more amounts into account."""
    if account_number not in accounts:
        return "Account not found!"

    total = sum(amounts)
    accounts[account_number]["balance"] += total
    return f"Deposited {total} into {accounts[account_number]['name']}'s account."


def withdraw(account_number, *amounts):
    """Withdraw money if balance (plus overdraft_limit if any) is sufficient."""
    if account_number not in accounts:
        return "Account not found!"

    total = sum(amounts)
    balance = accounts[account_number]["balance"]
    overdraft = accounts[account_number].get("overdraft_limit", 0)

    if balance + overdraft >= total:
        accounts[account_number]["balance"] -= total
        return f"Withdrew {total} from {accounts[account_number]['name']}'s account."
    else:
        return "Insufficient funds."


def transfer(from_acc, to_acc, amount):
    """Transfer money between accounts if funds are sufficient."""
    if from_acc not in accounts or to_acc not in accounts:
        return "One or both accounts not found!"

    balance = accounts[from_acc]["balance"]
    overdraft = accounts[from_acc].get("overdraft_limit", 0)

    if balance + overdraft >= amount:
        accounts[from_acc]["balance"] -= amount
        accounts[to_acc]["balance"] += amount
        return f"Transferred {amount} from {accounts[from_acc]['name']} to {accounts[to_acc]['name']}."
    else:
        return "Insufficient funds for transfer."



print(create_account("A001", "Alice", overdraft_limit=100))
print(create_account("A002", "Bob"))

print(deposit("A001", 200, 150))   # batch deposit
print(withdraw("A001", 50, 25))    # batch withdrawal
print(transfer("A001", "A002", 100)) # batch transfer
print(accounts)
