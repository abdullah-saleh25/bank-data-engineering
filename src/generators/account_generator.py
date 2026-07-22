from faker import Faker
import pandas as pd
import random


class AccountGenerator:
    def __init__(self):
        self.fake = Faker()

        self.account_types = [
            "Savings",
            "Current",
            "Salary"
        ]

        self.account_status = [
            "Active",
            "Dormant",
            "Closed"
        ]

        self.currency = "EGP"

    def generate_account(self, account_id: int, customer_id: int) -> dict:
        return {
            "account_id": account_id,
            "customer_id": customer_id,
            "account_number": str(random.randint(100000000000, 999999999999)),
            "account_type": random.choice(self.account_types),
            "balance": round(random.uniform(1000, 500000), 2),
            "currency": self.currency,
            "status": random.choice(self.account_status),
            "branch_id": random.randint(1, 20),
            "opened_date": self.fake.date_between(
                start_date="-10y",
                end_date="today"
            )
        }

    def generate_accounts(self, customers_df: pd.DataFrame) -> list:
        accounts = []
        account_id = 1

        for _, customer in customers_df.iterrows():

            number_of_accounts = random.randint(1, 3)

            for _ in range(number_of_accounts):
                account = self.generate_account(
                    account_id=account_id,
                    customer_id=customer["customer_id"]
                )

                accounts.append(account)
                account_id += 1

        return accounts

    def generate_dataframe(self, customers_df: pd.DataFrame) -> pd.DataFrame:
        accounts = self.generate_accounts(customers_df)
        return pd.DataFrame(accounts)