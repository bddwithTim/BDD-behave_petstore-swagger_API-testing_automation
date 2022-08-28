import requests
import json

from behave import given, when, then
from petstore_swagger_bdd.context import PetStoreContext
from expects import equal, expect


@when("I make a {method} request to check the status of the {status} pets in the petstore site")
def step_impl_1(context: PetStoreContext, method: str, status: str):
    context.http_response = requests.request(
        method=method,
        url=context.base_url + f"/v2/pet/findByStatus?status={status}",
    )


@when('I make a {method} request to "{resource}" with this form data')
def step_impl_2(context: PetStoreContext, method: str, resource: str):
    content = json.loads(context.text.strip())
    context.http_response = requests.request(method=method, url=context.base_url + resource, json=content)


@then("the response status code is {code:d}")
def step_impl_3(context: PetStoreContext, code: int):
    if context.http_response is None:
        raise ValueError("No HTTP response has been recorded")
    expect(context.http_response.status_code).to(equal(code))


@when("I make a {method} request to the pet object")
def step_impl_4(context: PetStoreContext, method: str):
    if context.pet_store_object is None:
        raise ValueError("No value stored in context.pet_store_object.")
    requests.request(
        method=method,
        url=context.base_url + f'/v2/pet/{context.pet_store_object["id"]}',
    )


@given("a pet object is available in the petstore site")
def step_impl_5(context: PetStoreContext):
    context.execute_steps(
        """
        When I make a POST request to "/v2/pet" with this form data
        '''
          {
            "id": 0,
            "category": {
              "id": 0,
              "name": "string"
            },
            "name": "doggie",
            "photoUrls": [
              "string"
            ],
            "tags": [
              {
                "id": 0,
                "name": "string"
              }
            ],
            "status": "available"
          }
        '''
        """
    )
    if context.http_response is None:
        raise ValueError("No HTTP response has been recorded")
    context.pet_store_object = {
        "id": context.http_response.json()["id"],
        "name": context.http_response.json()["name"],
    }


@when("I make a {method} request to the store pet inventories")
def step_impl_6(context: PetStoreContext, method: str):
    """
    TO DO:
    :param context:
    :param method:
    :return:
    """
