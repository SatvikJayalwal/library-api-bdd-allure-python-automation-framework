from utilities.configurations import getQuery  # Assuming this returns a tuple from SQL

# Function to build payload manually
def addBookPayload(isbn, aisle):
    return {
        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John foe"
    }

# Function to build payload dynamically from a SQL DB query result
def buildPayLoadFromDB(query):
    addBody = {}
    result = getQuery(query)

    if result and len(result) >= 4:
        addBody['name'] = result[0]
        addBody['isbn'] = result[1]
        addBody['aisle'] = result[2]
        addBody['author'] = result[3]
    else:
        raise ValueError("Query did not return expected 4 fields")

    return addBody
