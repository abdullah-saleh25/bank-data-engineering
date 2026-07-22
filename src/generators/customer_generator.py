from faker import Faker
import pandas as pd
import random


class CustomerGenerator:
    """
    Generate fake customer data for the banking project.
    """

    def __init__(self):
        self.fake = Faker()

        self.min_credit_score = 300
        self.max_credit_score = 850

        self.min_income = 30000
        self.max_income = 500000

    def generate_customer(self, customer_id: int) -> dict:
        """
        Generate a single fake customer.

        Args:
            customer_id (int): Customer unique ID.

        Returns:
            dict: Customer record.
        """
        return {
            "customer_id": customer_id,
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "gender": random.choice(["Male", "Female"]),
            "date_of_birth": self.fake.date_of_birth(
                minimum_age=18,
                maximum_age=75,
            ),
            "national_id": str(
                random.randint(10000000000000, 99999999999999)
            ),
            "email": self.fake.email(),
            "phone": self.fake.phone_number(),
            "address": self.fake.street_address(),
            "city": self.fake.city(),
            "country": "Egypt",
            "occupation": self.fake.job(),
            "annual_income": random.randint(
                self.min_income,
                self.max_income,
            ),
            "credit_score": random.randint(
                self.min_credit_score,
                self.max_credit_score,
            ),
            "customer_since": self.fake.date_between(
                start_date="-15y",
                end_date="today",
            ),
        }

    def generate_customers(self, count: int) -> list:
        """
        Generate multiple customer records.

        Args:
            count (int): Number of customers.

        Returns:
            list: List of customer dictionaries.
        """
        customers = []

        for customer_id in range(1, count + 1):
            customer = self.generate_customer(customer_id)
            customers.append(customer)

        return customers

    def generate_dataframe(self, count: int) -> pd.DataFrame:
        """
        Generate customer data as a pandas DataFrame.

        Args:
            count (int): Number of customers.

        Returns:
            pd.DataFrame: Customer dataset.
        """
        customers = self.generate_customers(count)
        return pd.DataFrame(customers)