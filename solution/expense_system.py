class ExpenseSystem:
    def __init__(self):
        self.expenses = []
        self.user_expense_summary = {}

    def add_expense(self, main_user, total_amount, other_users, share_type):
        """
        Assuming for now that amount get distributed equally
        """
        each_share = float(total_amount / (len(other_users) + 1))
        expense = {
            "metadata": {"main_user": main_user, "total_amount": total_amount},
            "other_users": [{user: each_share} for user in other_users],
        }

        self.expenses.append(expense)

        if main_user not in self.user_expense_summary:
            self.user_expense_summary[main_user] = {}

        # Adding all the user amount that main_user will recieve
        for user in other_users:
            if user not in self.user_expense_summary[main_user]:
                self.user_expense_summary[main_user][user] = 0
            self.user_expense_summary[main_user][user] += each_share

        # Adding amount that each other user will pay to main user
        for user in other_users:
            if user not in self.user_expense_summary:
                self.user_expense_summary[user] = {}

            if main_user not in self.user_expense_summary[user]:
                self.user_expense_summary[user][main_user] = 0

            self.user_expense_summary[user][main_user] -= each_share

    def list_user_expenses(self, user):
        pass

    def settle_funds(self, userA, userB):
        pass

    def generate_user_summary(self, user):
        if not len(self.expenses):
            raise Exception("Not added any expenses yet")

        user_expense_summary = self.user_expense_summary[user]
        for key, val in user_expense_summary.items():
            if val > 0:
                print(
                    "{key} owes {val} to user {user}".format(
                        key=key, val=val, user=user
                    )
                )

            elif val < 0:
                print(
                    "{user} owes {val} to user {key}".format(
                        key=key, val=-val, user=user
                    )
                )


expense_system = ExpenseSystem()
expense_system.add_expense("A", 1000, ["B", "C", "D"], "equal")
expense_system.add_expense("B", 1500, ["A", "C"], "equal")
print(expense_system.generate_user_summary("A"))
