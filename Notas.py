











# Wait for the title of the most recent card to become equal to title_before
WebDriverWait(...).until(...)




# Check that there is one less card now
cards_after = len(...)
assert ...

# Comprobar que ahora hay una tarjeta menos
cards_after = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))
assert cards_before - cards_after == 1

