Feature: Páros szám ellenőrzése

  Scenario: Páros szám ellenőrzése
    Given the number is 4
    When I check the number
    Then the result should be "even"

  Scenario: Páratlan szám ellenőrzése
    Given the number is 5
    When I check the number
    Then the result should be "odd"

  Scenario: Nulla ellenőrzése
    Given the number is 0
    When I check the number
    Then the result should be "even"

  # Kiegészítő feladat: Negatív számok
  Scenario: Negatív páros szám ellenőrzése
    Given the number is -4
    When I check the number
    Then the result should be "even"

  Scenario: Negatív páratlan szám ellenőrzése
    Given the number is -5
    When I check the number
    Then the result should be "odd"