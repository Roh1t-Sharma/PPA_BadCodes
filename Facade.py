class CustomerDataSystem:
    def add_customer(self, customer_details):
        print(f"Adding new customer: {customer_details['name']}")
        # More complex logic to add customer to the database.

class MarketingAutomationSystem:
    def send_welcome_email(self, email):
        print(f"We've sent a Welcome mail to you on {email}")
        # Code to integrate with email service providers.

class SalesReportingSystem:
    def generate_initial_sales_report(self, customer_id):
        print(f"Generating initial sales report for customer ID {customer_id}")
        # Code to generate and return sales report.

# Client code
def main():
    customer_name = input("Enter customer name: ")
    customer_email = input("Enter customer email: ")

    customer_data = CustomerDataSystem()
    marketing = MarketingAutomationSystem()
    sales_reporting = SalesReportingSystem()

    # Direct interaction with multiple subsystems
    customer_details = {'name': customer_name, 'email': customer_email}
    customer_data.add_customer(customer_details)
    marketing.send_welcome_email(customer_email)
    sales_reporting.generate_initial_sales_report(customer_details['name'])  # Simplified customer ID usage

if __name__ == "__main__":
    main()

