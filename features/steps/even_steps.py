from behave import given, when, then
# Importáljuk a logikát a src mappából
from src.number_checker import check_number

@given('the number is {number}')
def step_given_number(context, number):
    # A kapott értéket egésszé (int) alakítjuk és elmentjük a context-be
    context.number = int(number)

@when('I check the number')
def step_when_check_number(context):
    # Meghívjuk a függvényt az elmentett számmal, és az eredményt is elmentjük
    context.result = check_number(context.number)

@then('the result should be "{expected}"')
def step_then_result(context, expected):
    # Ellenőrizzük, hogy a kapott eredmény megegyezik-e az elvárttal
    # Ha nem egyezik, hibaüzenetet dobunk
    assert context.result == expected, f"Hiba! Kapott: {context.result}, Elvárt: {expected}"