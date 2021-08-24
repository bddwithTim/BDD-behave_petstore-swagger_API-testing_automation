@feature @pet_store_api
Feature: Pet store API

  @positive
  Scenario Outline: Find pets by status
    When I make a GET request to check the status of the <status> pets in the petstore site
    Then the response status code is 200

  Examples: Pets by status
    |  status    |
    |  available |
    |  pending   |
    |  sold      |


  @positive
  Scenario: Pet object that needs to be added to the store
    When I make a POST request to "/v2/pet" with this form data
    """
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
      """
    Then the response status code is 200


  @positive
  Scenario: Delete pet object
    Given a pet object is available in the petstore site
    When I make a DELETE request to the pet object
    Then the response status code is 200


  @wip @positive
  Scenario: Check Store inventory
    When I make a GET request to the store pet inventories
    Then the response status code is 200