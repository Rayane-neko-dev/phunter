# PHunter

**PHunter** is a simple phishing tool project built with Django.  
⚠️ It is intended **for teaching purposes only** — I am **not responsible for any abuse**.

---

## Project Structure

The project consists of **three applications**:

1. **home**  
   → The local UI interface to launch and control the tool.

2. **instagram**  
   → A fake Instagram login page exposed **publicly**.

3. **victims**  
   → A local UI that displays the login data submitted by victims.

---

## Usage Instructions

To run this project correctly:

- You **must** use a **public tunnel** such as **ngrok**.
- Copy your public tunnel URL into the following places:
  - `views.py` in the `instagram` app
  - `CSRF_TRUSTED_ORIGINS` and `ALLOWED_HOSTS` in `settings.py`
  - The action link in the home page (`index.html`)

---

## Security & Limitations (To Be Fixed)

- The project is **not secure** (yet).
- Ngrok shows a warning asking the victim to trust the link.
- The fake Instagram page does **not redirect to Instagram** after login.

These issues will be addressed in future versions.


# coded by rayane-neko-dev

     /\_/\  
    ( o.o )    Meow~  
    /     \ 
   (       )  
  
   ( /   \ ) 
   
#


---

## Disclaimer XDDDDDDDDDDD 

This tool is **only for educational purposes**.  
Using it for malicious or illegal activity is **strictly prohibited**.

---
