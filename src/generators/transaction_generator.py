from faker import Faker
import pandas as pd
import random


class TransactionGenerator:

    def __init__(self):
        self.fake = Faker()

        self.transaction_types = [
            "Deposit",
            "Withdrawal",
            "Transfer",
            "Purchase"
        ]

        self.payment_methods = [
            "ATM",
            "POS",
            "Online",
            "Mobile App"
        ]

        self.statuses = [
            "Completed",
            "Pending",
            "Failed"
        ]

    def generate_transaction(self, transaction_id, account_id):

        return {
            "transaction_id": transaction_id,
            "account_id": account_id,
            "transaction_type": random.choice(self.transaction_types),
            "amount": round(random.uniform(50, 50000), 2),
            "transaction_date": self.fake.date_time_between(
                start_date="-2y",
                end_date="now"
            ),
            "merchant": self.fake.company(),
            "payment_method": random.choice(self.payment_methods),
            "status": random.choice(self.statuses)
        }

    def generate_transactions(self, accounts_df):

        transactions = []

        transaction_id = 1

        for _, account in accounts_df.iterrows():

            number_of_transactions = random.randint(20, 100)

            for _ in range(number_of_transactions):

                transaction = self.generate_transaction(
                    transaction_id,
                    account["account_id"]
                )

                transactions.append(transaction)

                transaction_id += 1

        return transactions

    def generate_dataframe(self, accounts_df):

        return pd.DataFrame(
            self.generate_transactions(accounts_df)
        )