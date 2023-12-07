# The_Highest_Profit_Wins

[![License: AGPL](https://img.shields.io/badge/License-AGPL-blue.svg)](https://github.com/gotreasa/the_highest_profit_wins/blob/main/LICENSE)
[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_the_highest_profit_wins&metric=alert_status)](https://sonarcloud.io/dashboard?id=gotreasa_the_highest_profit_wins)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_the_highest_profit_wins&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=gotreasa_the_highest_profit_wins)
[![Build Status](https://github.com/gotreasa/the_highest_profit_wins/actions/workflows/cicd.yml/badge.svg)](https://github.com/gotreasa/the_highest_profit_wins/actions/workflows/cicd.yml)
[![Can I Deploy main to test](https://gotreasa.pactflow.io/pacticipants/the_highest_profit_wins_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)](https://gotreasa.pactflow.io/hal-browser/browser.html#https://gotreasa.pactflow.io/pacticipants/the_highest_profit_wins_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)

Welcome to the Python Template created via a cookiecutter recipe. The project template is designed for a development via a `Double Loop approach` (BDD-TDD) using pytest and several other pytest libs.

## Description

Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.

### Task

Write a function that returns both the minimum and maximum number of the given list/array.

Examples (Input --> Output)

```
[1,2,3,4,5] --> [1,5]
[2334454,5] --> [5,2334454]
[1]         --> [1,1]
```

### Remarks

All arrays or lists will always have at least one element, so you don't need to check the length. Also, your function will always get an array or a list, you don't have to check for null, undefined or similar.
