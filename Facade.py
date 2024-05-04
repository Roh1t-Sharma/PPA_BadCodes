class CustomerDataSystem:
    @staticmethod
    def add_customer(customer_details):
        print(f"Adding new customer: {customer_details['name']}")
        return customer_details  # Assume it returns customer info including an ID


class MarketingAutomationSystem:
    @staticmethod
    def send_welcome_email(email):
        print(f"We've sent a Welcome mail to you on {email}")


class SalesReportingSystem:
    def __init__(self):  # Sample data, it could be more complex database interaction in a real use case
        self.sales_data = {
            'FCD3489': {'description': 'MacBook Pro', 'potential_revenue': 20000},
            'FCD6723': {'description': 'Sony Alpha 9 III ', 'potential_revenue': 60000}
        }

    def generate_initial_sales_report(self, customer_id):
        print(f"Generating initial sales report for customer ID {customer_id}")
        # Simulating fetching customer interests based on initial data collection
        customer_interests = ['FCD3489', 'FCD6723']  # This would be dynamic in a real scenario
        report = {}
        for sku in customer_interests:
            item = self.sales_data.get(sku, {})
            report[sku] = {
                'product': item.get('description', 'N/A'),
                'potential_revenue': item.get('potential_revenue', 0)
            }
        return report


# Example of integrating the enhanced SalesReportingSystem into the CRMFacade
class CRMFacade:
    def __init__(self):
        self.customer_data = CustomerDataSystem()
        self.marketing = MarketingAutomationSystem()
        self.sales_reporting = SalesReportingSystem()

    def onboard_new_customer(self, name, email):
        customer_details = {'name': name, 'email': email}
        customer_info = self.customer_data.add_customer(customer_details)
        self.marketing.send_welcome_email(email)
        report = self.sales_reporting.generate_initial_sales_report(customer_info['name'])
        print("Sales Report Generated:")
        for sku, details in report.items():
            print(f"Product: {details['product']}, Potential Revenue: Rub.{details['potential_revenue']}")


# Main function remains the same
def main():
    customer_name = input("Enter customer name: ")
    customer_email = input("Enter customer email: ")

    crm_facade = CRMFacade()
    crm_facade.onboard_new_customer(customer_name, customer_email)


if __name__ == "__main__":
    main()
