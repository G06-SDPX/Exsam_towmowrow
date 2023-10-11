*** Settings ***
Library           RequestsLibrary

*** Test Cases ***
True When X Is 17
    [Documentation]  Test the API with x=17, expecting a "True" response
    Create Session    api_session    http://localhost:5000  # Provide the correct base URL
    ${response}       GET On Session     api_session    /is_prime/17
    Should Be Equal As Strings    ${response.text}    True


False When X Is 36
    [Documentation]  Test the API with x=36, expecting a "False" response
    Create Session    api_session    http://localhost:5000  # Provide the correct base URL
    ${response}       GET On Session    api_session    /is_prime/36
    Should Be Equal As Strings    ${response.text}    False


True When X Is 13219
    [Documentation]  Test the API with x=13219, expecting a "True" response
    Create Session    api_session    http://localhost:5000  # Provide the correct base URL
    ${response}       GET On Session     api_session    /is_prime/13219
    Should Be Equal As Strings    ${response.text}    True
