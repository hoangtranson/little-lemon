# HTTP Method

GET - Returns the requested resource. If not found, returns a 404 Not Found status code.

POST - Creates a record. The POST request always comes with an HTTP request body containing JSON or Form URL encoded data, which is also called a payload. If the data is valid, the API endpoint will create a new resource based on these data. Although you can create multiple resources with a single POST call, it is not considered a best practice to do so.

PUT - Instructs the API to replace a resource. Like a POST request, the PUT request also comes with data. A PUT request usually supplies all data for a particular resource so that the API developer can fully replace that resource with the provided data. A PUT request deals with a single resource.

PATCH - Tells the API to update a part of the resource. Note the difference between a PUT and a PATCH call. A PUT call replaces the complete resource, while the PATCH call only updates some parts. A PATCH request also deals with a single record.

DELETE - Instructs the API to delete a resource.

# HTTP Status

## 100-199

This range is mainly used to pass on some information. For example, sometimes an API needs time to process the request and it can’t instantly deliver the result. In such a case, the API developer can set it to keep returning 102 – Processing until the result is ready. This way, the client understands that the result isn’t ready and should be checked again.

## 200-299

These are the success codes. If the client requests something and the API acts successfully, it should deliver the output with one of these status codes.

For example, for a PUT, PATCH, or DELETE call, you can return 200 – Successful if the operation was successful. For a successful POST call, you can set it to return a 201 – Created status code when the resource has been created successfully.

## 300-399

These are the redirection codes. Suppose as an API developer, you changed the API endpoint from /api/items to api/menu-items. If the client makes an API call to /api/items, then you can redirect the client to this new endpoint /api/menu-items with a 301 – Permanently moved status code so that the client can make new calls to that endpoint next time.

## 400-499

4xx status codes are used in the following situation: if the client requests something that does not exist, sends an invalid payload with insufficient data, or wants to perform an action that the client is not authorized for.

For the above scenarios, the appropriate status codes will be:

- 404 - Not Found if the client requests something that doesn’t exist,
- 400 - Bad Request if a client sends an invalid payload with insufficient data,
- 401 - Unauthorized,
- 403 - Forbidden if the client tries to perform an action it's not authorized for.

## 500-599

These alarming status codes are usually automatically generated on the server side if something goes wrong in the code, and the API developer doesn't write code to deal with those errors. For example, a client requests a non-existing resource, and the API developer tries to display that resource without adequately checking if that resource exists in the database. Or if the API developer didn't validate the incoming data and attempted to create a new resource with invalid or insufficient data. You, as an API developer, should always avoid 5xx errors.

## Response types

HTML

- Accept: text/html

JSON and JSONP

- Accept: application/json

XML

- Accept: application/xml

- Accept: text/xml

YAML

- Accept: application/yaml

- Accept: application/x-yaml

- Accept: text/yaml
