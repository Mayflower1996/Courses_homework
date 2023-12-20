*** Settings ***
Library    PythonLibrary    pass.py

*** Test Cases ***
Positive Test
    ${password}    Set Variable    Password123
    ${expected_result}    Set Variable    True

Negative Test - Length
    ${password}    Set Variable    abc123
    ${expected_result}    Set Variable    False

Negative Test - No uppercase letter
    ${password}    Set Variable    password123
    ${expected_result}    Set Variable    False

Negative Test - No lowercase letter
    ${password}    Set Variable    PASSWORD123
    ${expected_result}    Set Variable    False

Negative Test - No digit
    ${password}    Set Variable    Password
    ${expected_result}    Set Variable    False

*** Keywords ***
Check Password
    [Arguments]    ${password}    ${expected_result}
    ${result}    Check Password    ${password}  ${expected_result}
    Should Be Equal As Strings    ${result}    ${expected_result}
