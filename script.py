import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Initialize WebDriver
driver = webdriver.Chrome()

# Create an Excel workbook and sheet to store results
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Exchange Prices"

# Add headers to the sheet
ws.append(["Product Name", "Exchange Value"])

# Open Flipkart's website
driver.get("https://www.flipkart.com")

# Close the login pop-up if it appears
try:
    close_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '✕')]"))
    )
    close_button.click()
except TimeoutException:
    print("Login pop-up not present, continuing...")

# Search for the product (e.g., 'smartphone with exchange offer')
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("smartphone with exchange offer")
search_box.send_keys(Keys.RETURN)

# Wait for search results to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "MoPwtI")))

# Extract information from the first few products (e.g., top 5)
product_data = []
for i in range(1, 6):
    try:
        # Click the product link
        first_product = driver.find_element(By.XPATH, f"(//div[@class='_75nlfW'])[{i}]")
        first_product.click()

        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[1])

        # Handle pincode input
        try:
            pincode_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='pincodeInputId']"))
            )
            pincode_input.send_keys("382028")  # Example pincode
            pincode_input.send_keys(Keys.RETURN)
        except (TimeoutException, NoSuchElementException):
            print(f"Error handling pincode or exchange selection for product {i}")

        # Wait and click on "Buy with Exchange" (if available)
        try:
            buy_with_exchange = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Buy with Exchange')]"))
            )
            buy_with_exchange.click()
            print(f"Clicked 'Buy with Exchange' for Product {i}")
        except (TimeoutException, NoSuchElementException):
            print(f"Exchange option not found for product {i}.")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            continue

        # Enter "Poco X3" as the exchange device
        try:
            brand_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search your brand']"))
            )
            brand_input.send_keys("Poco")
            brand_input.send_keys(Keys.RETURN)

            # Select "Poco X3" from the drop-down
            model_option = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Poco X3')]"))
            )
            model_option.click()

            # Extract the exchange value
            exchange_value = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_1dMlfM"))
            )
            print(f"Exchange Value for Product {i}: {exchange_value.text}")
            product_data.append([first_product.text, exchange_value.text])

        except Exception as e:
            print(f"An error occurred during exchange selection for product {i}: {str(e)}")

        # Close the current tab and switch back to the main window
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    except Exception as e:
        print(f"An error occurred with product {i}: {str(e)}")

# Write all the collected data to the Excel sheet at once
for product in product_data:
    ws.append(product)

# Save the results to an Excel file
wb.save("exchange_prices.xlsx")

# Close the browser
driver.quit()

print("Exchange values have been saved to exchange_prices.xlsx.")
