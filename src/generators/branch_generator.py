from faker import Faker
import pandas as pd


class BranchGenerator:

    def __init__(self):
        self.fake = Faker("en_US")

    def generate_branch(self, branch_id):

        return {
            "branch_id": branch_id,
            "branch_name": f"Branch {branch_id}",
            "city": self.fake.city(),
            "address": self.fake.street_address(),
            "manager_name": self.fake.name(),
            "phone": self.fake.phone_number()
        }

    def generate_branches(self, count):

        branches = []

        for branch_id in range(1, count + 1):
            branches.append(
                self.generate_branch(branch_id)
            )

        return branches

    def generate_dataframe(self, count):

        return pd.DataFrame(
            self.generate_branches(count)
        )