import undetected_chromedriver as uc
import time

origin = "DEN"
destination = "ANU"
url = f"https://booking.flyfrontier.com/Flight/RetrieveSchedule?calendarSelectableDays.Origin={origin}&calendarSelectableDays.Destination={destination}"

# Launch patched Chrome
options = uc.ChromeOptions()
# Comment this out if you want to see the window
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = uc.Chrome(options=options)

print(f"Opening {url}")
driver.get(url)

# Wait for JS and CAPTCHA (if needed)
time.sleep(5)

with open("frontier_debug.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

driver.quit()
print("✅ Done. HTML saved to frontier_debug.html")


