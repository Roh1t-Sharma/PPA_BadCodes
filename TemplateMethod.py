import logging

# Configure logging
logging.basicConfig(level=logging.INFO)


class UserDataMigrator:
    def __init__(self, old_data_source, new_data_source):
        # Set up with old and new data sources
        self.old_data_source = old_data_source
        self.new_data_source = new_data_source

    def migrate(self):
        # Move data from old to new
        for old_data in self.old_data_source:
            # Change the old data to the new format
            new_data = self.transform_data(old_data)
            # Check if the new data matches the old data
            if not self.validate_data(old_data, new_data):
                logging.warning(f"Data integrity issue with user ID {old_data['userId']}")
                continue
            # Save the new data
            self.save_new_data(new_data)

    def transform_data(self, old_data):
        # Convert the old data to the new format
        new_data = {
            "id": old_data["userId"],
            "full_name": f"{old_data['firstName']} {old_data['lastName']}",
            "email": old_data["emailAddress"],
            "address": {
                "street": old_data["streetAddress"],
                "city": old_data["city"],
                "zipcode": old_data["postalCode"]
            }
        }
        return new_data

    def save_new_data(self, new_data):
        # Add the new data to the new data source
        self.new_data_source.append(new_data)

    # Temporary method for checking data integrity
    def validate_data(self, old_data, new_data):
        # Make sure the new data is correct
        if old_data["userId"] != new_data["id"]:
            return False
        if old_data["firstName"] not in new_data["full_name"] or old_data["lastName"] not in new_data["full_name"]:
            return False
        if old_data["emailAddress"] != new_data["email"]:
            return False
        if old_data["streetAddress"] != new_data["address"]["street"]:
            return False
        if old_data["city"] != new_data["address"]["city"]:
            return False
        if old_data["postalCode"] != new_data["address"]["zipcode"]:
            return False
        return True


def get_user_input():
    # Gather user input for the old data source
    old_data_source = []
    while True:
        try:
            user_data = {}
            user_data["userId"] = int(input("Enter user ID: "))
            user_data["firstName"] = input("Enter first name: ")
            user_data["lastName"] = input("Enter last name: ")
            user_data["emailAddress"] = input("Enter email address: ")
            user_data["streetAddress"] = input("Enter street address: ")
            user_data["city"] = input("Enter city: ")
            user_data["postalCode"] = input("Enter postal code: ")

            old_data_source.append(user_data)

            more = input("Want to add another user? (yes/no): ")
            if more.lower() != 'yes':
                break
        except ValueError as e:
            logging.error(f"Invalid input: {e}")
            continue
    return old_data_source


# Example usage
old_data_source = get_user_input()  # Get user input for old data
new_data_source = []

migrator = UserDataMigrator(old_data_source, new_data_source)
migrator.migrate()  # Do the data migration

# Show the new data to check the results
logging.info(f"New data source: {new_data_source}")
