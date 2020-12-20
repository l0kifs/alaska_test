Description
Basic test project based on the REST API of https://hub.docker.com/r/azshoo/alaska

In case of increasing number of tests they should be organized by features and prioritized.

Security and performance test not included.

Checklist
Basic check list for the API.

POST /bear - create
- send correct request (all parameters in place and correct)
- send request without one or more parameters. Check each parameter, some combinations and all parameters.
- send request with one or more parameters containing values of not expected type (int instead of str etc.) Check each parameter, some combinations and all parameters.
- send request with "bear_name" parameter containing empty string, or very long string
- send request with "bear_name" parameter containing unexpected characters (@+= etc.)
- send request with "bear_age" parameter containing negative, positive values, zero, very long value
- send request with "bear_age" parameter containing int, or double value
- send request with "bear_type" parameter containing every available type
- send request with "bear_type" parameter containing unexpected type (empty string, or some variation of characters)
- send request with all required and some unexpected parameters
- send request with list of bears

GET /bear - read all bears
- send request (precondition: no entries in DB)
- send request (precondition: one, or more then one entries in DB)

GET /bear/:id - read specific bear
- send request with existing id
- send request with nonexisting id of correct type
- send request with id containing unexpected characters

PUT /bear/:id - update specific bear
- same list of checks with "create"
- same list of checks with "read specific bear"

DELETE /bear - delete all bears
- same list of checks with "read all bears"

DELETE /bear/:id - delete specific bear
- same list of checks with "read specific bear"

General expected results.
- Depending on scenario expected response codes are 200/201, or 400. 500 is not acceptable.
- In case of an error response body contains consistent error description without sensitive information.
- In case of success response body contains nothing, or some operation result details (like id of created entity, entity itself etc.).
