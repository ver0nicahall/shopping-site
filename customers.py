"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return (
            f"<Customer: {self.first_name}, {self.last_name}, {self.email}, {self.password}>"
        )
def read_customers_from_file(filepath):

    """Read customer data and populate dictionary of customers."""

    customers = {}

    with open(filepath) as file:
        for line in file:
            (
                first_name,
                last_name,
                email,
                password
            ) = line.rstrip().split('|')
            customers[email] = Customer(first_name, last_name, email, password)
            
    return customers

def get_by_email(email):
    """Takes in a customer's email address and returns Customer object."""

    if email not in all_customers:
        return None
    else:
        return all_customers[email]
    # return all_customers.get(all_customers[email], None)


all_customers = read_customers_from_file('customers.txt')