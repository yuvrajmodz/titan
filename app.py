try:
    # Selenium aur WebDriver import kar rahe hain
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    # Chrome ke liye headless mode setup karte hain
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless mode mein run karne ke liye
    chrome_options.add_argument("--no-sandbox")  # No sandbox for VPS
    chrome_options.add_argument("--disable-dev-shm-usage")  # Shared memory issues ko fix karta hai

    # WebDriver ka instance create karte hain
    driver = webdriver.Chrome(options=chrome_options)

    # Website ko open karte hain to test
    driver.get("https://www.google.com")

    # Agar title successfully load hota hai to success message show karega
    if "Google" in driver.title:
        print("Selenium is installed and working correctly. Success!")
    else:
        print("Selenium installed but could not load page correctly.")
    
    # WebDriver ko band karte hain
    driver.quit()

except Exception as e:
    # Agar koi error ya exception aati hai to error message print karega
    print(f"Failed to run Selenium: {str(e)}")
