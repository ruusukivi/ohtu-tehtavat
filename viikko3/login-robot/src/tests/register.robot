*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallee  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k234  kalle123
    Output Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  kallee  k
    Output Should Contain  Password must be at least 8 characters long and contain also numbers

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kallee  kallekalle
    Output Should Contain  Password must be at least 8 characters long and contain also numbers

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123