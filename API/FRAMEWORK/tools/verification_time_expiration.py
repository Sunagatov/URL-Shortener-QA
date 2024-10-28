from datetime import datetime, timedelta
from dateutil import parser
from hamcrest import less_than_or_equal_to
from hamcrest.core import assert_that


def verify_expiration_date(url_info_from_mongodb, expected_days):
    """
    Verifies that the 'expirationDate' in the document is exactly 'expected_days' days from 'createdAt'.
    Handles date strings in ISO 8601 format with timezone information or datetime objects.

    Args:
        url_info_from_mongodb (dict): The MongoDB document containing 'createdAt' and 'expirationDate' fields.
        expected_days (int): The expected number of days between 'createdAt' and 'expirationDate'.

    Raises:
        AssertionError: If any of the assertions fail.
    """
    # Extract 'createdAt' and 'expirationDate' from the document
    created_at_value = url_info_from_mongodb.get('createdAt')
    expiration_date_value = url_info_from_mongodb.get('expirationDate')

    # Check if both dates are present
    if not created_at_value or not expiration_date_value:
        print("Document is missing 'createdAt' or 'expirationDate' fields.")
        return False

    # Parse or assign the date values
    try:
        # Handle 'createdAt'
        if isinstance(created_at_value, datetime):
            created_at = created_at_value
        elif isinstance(created_at_value, str):
            created_at = parser.isoparse(created_at_value)
        else:
            print(f"Unsupported type for 'createdAt': {type(created_at_value)}")
            return False

        # Handle 'expirationDate'
        if isinstance(expiration_date_value, datetime):
            expiration_date = expiration_date_value
        elif isinstance(expiration_date_value, str):
            expiration_date = parser.isoparse(expiration_date_value)
        else:
            print(f"Unsupported type for 'expirationDate': {type(expiration_date_value)}")
            return False

    except Exception as e:
        print(f"Error parsing date values: {e}")
        return False

    # Calculate the expected expiration date
    expected_expiration_date = created_at + timedelta(days=expected_days)

    # Calculate the difference in seconds between the actual and expected expiration dates
    time_difference = abs((expiration_date - expected_expiration_date).total_seconds())

    # Allow for a small margin of error (1 second)
    assert_that(
        time_difference,
        less_than_or_equal_to(1),
        f"Expiration date is not correctly set. Expected: {expected_expiration_date}, Actual: {expiration_date}"
    )
