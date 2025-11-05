# ISS Overhead Notifier 🌌

This Python script notifies you via email when the **International Space Station (ISS)** is passing near your location **at night**.  
It uses public APIs to track the ISS position and local sunrise/sunset times.

---

## Tech Stack

- **Language:** Python 3.x  
- **Libraries:** `requests`, `datetime`, `smtplib`, `time`  
- **APIs:**  
  - [Open Notify ISS API](http://api.open-notify.org) (for ISS position)  
  - [Sunrise-Sunset API](https://sunrise-sunset.org/api) (for light conditions)  

---

## Features

- Tracks the ISS’s real-time location.  
- Checks if the ISS is overhead within ±5° latitude/longitude of your coordinates.  
- Determines if it’s currently nighttime.  
- Sends an email alert when both conditions are true.  

---

## Setup

1. Update your location coordinates in the script:  
   ```python
   LAT = your_latitude
   LONG = your_longitude

2. Configure your email credentials:
   
  EMAIL = "your_email@example.com"
  PASSWORD = "your_app_password"

Ensure you enable **"App Passwords"** or allow less secure apps if using Gmail.

Install dependencies:

`pip install requests`

* * * * *

How It Works
------------

-   **ISS Tracking:** Fetches ISS coordinates from the Open Notify API.

-   **Day/Night Detection:** Gets local sunrise and sunset times using the Sunrise-Sunset API.

-   **Condition Check:**

    -   If the ISS is nearby **and** it's dark, sends an email notification.

-   **Loop:** Runs continuously, checking every 60 seconds.

* * * * *

Example Usage
-------------

Run the script:

`python iss_notifier.py`

* * * * *

Outcome
-------

When the ISS is overhead and it's dark outside, you'll receive an email alert:

**Subject:** Look up\
**Body:** Notification

* * * * *

Notes
-----

-   Keep your email credentials secure (use **environment variables** in production).

-   Ensure your system clock is accurate.

-   The frequency of checks can be adjusted via:

    `time.sleep(60)`
