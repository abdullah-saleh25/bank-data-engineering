from faker import Faker
import pandas as pd
import random


class LoanGenerator:

    def __init__(self):
        self.fake = Faker()

        self.loan_types = [
            "Personal",
            "Car",
            "Mortgage"
        ]

        self.statuses = [
            "Active",
            "Closed",
            "Rejected"
        ]

    def generate_loan(self, loan_id, customer_id):

        return {

            "loan_id": loan_id,

            "customer_id": customer_id,

            "loan_type": random.choice(self.loan_types),

            "loan_amount": round(
                random.uniform(10000, 1000000),
                2
            ),

            "interest_rate": round(
                random.uniform(8, 20),
                2
            ),

            "status": random.choice(
                self.statuses
            ),

            "start_date": self.fake.date_between(
                start_date="-10y",
                end_date="today"
            )

        }

    def generate_loans(self, customers_df):

        loans = []

        loan_id = 1

        for _, customer in customers_df.iterrows():

            if random.random() < 0.40:

                loans.append(

                    self.generate_loan(
                        loan_id,
                        customer["customer_id"]
                    )

                )

                loan_id += 1

        return loans

    def generate_dataframe(self, customers_df):

        return pd.DataFrame(
            self.generate_loans(customers_df)
        )