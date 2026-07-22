from generators.customer_generator import CustomerGenerator
from generators.account_generator import AccountGenerator
from generators.transaction_generator import TransactionGenerator
from generators.branch_generator import BranchGenerator
from generators.loan_generator import LoanGenerator
from utils.file_manager import FileManager

NUMBER_OF_CUSTOMERS = 100
NUMBER_OF_BRANCHES = 20


def main():

    # Generate Customers
    customer_generator = CustomerGenerator()
    customers_df = customer_generator.generate_dataframe(NUMBER_OF_CUSTOMERS)

    # Generate Accounts
    account_generator = AccountGenerator()
    accounts_df = account_generator.generate_dataframe(customers_df)

    # Generate Transactions
    transaction_generator = TransactionGenerator()
    transactions_df = transaction_generator.generate_dataframe(accounts_df)

    # Generate Branches
    branch_generator = BranchGenerator()
    branches_df = branch_generator.generate_dataframe(NUMBER_OF_BRANCHES)

    # Generate Loans
    loan_generator = LoanGenerator()
    loans_df = loan_generator.generate_dataframe(customers_df)

    file_manager = FileManager()

    file_manager.save_csv(customers_df, "customers")
    file_manager.save_csv(accounts_df, "accounts")
    file_manager.save_csv(transactions_df, "transactions")
    file_manager.save_csv(branches_df, "branches")
    file_manager.save_csv(loans_df, "loans")

    print("=" * 60)
    print("Data Generation Summary")
    print("=" * 60)

    print(f"Customers    : {len(customers_df)}")
    print(f"Accounts     : {len(accounts_df)}")
    print(f"Transactions : {len(transactions_df)}")
    print(f"Branches     : {len(branches_df)}")
    print(f"Loans        : {len(loans_df)}")

    print("\nCustomers Sample")
    print(customers_df.head())

    print("\nAccounts Sample")
    print(accounts_df.head())

    print("\nTransactions Sample")
    print(transactions_df.head())

    print("\nBranches Sample")
    print(branches_df.head())

    print("\nLoans Sample")
    print(loans_df.head())


if __name__ == "__main__":
    main()