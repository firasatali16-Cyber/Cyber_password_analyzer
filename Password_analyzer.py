import re
import os

def check_password_strength(password):
    score = 0
    suggestions = []

    # 1. Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password is too short (Minimum 8 characters required).")

    # 2. Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    # 3. Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    # 4. Number Check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number (0-9).")

    # 5. Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character (e.g., @, #, $, %).")

    return score, suggestions

def check_rockyou_leak(password):
    # Kali Linux default rockyou path
    rockyou_path = "/usr/share/wordlists/rockyou.txt"
    
    if not os.path.exists(rockyou_path):
        return "Wordlist status: rockyou.txt not found in default path. Skipping database check."
        
    try:
        # Reading file safely line by line to handle large data
        with open(rockyou_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                if line.strip() == password:
                    return True
        return False
    except Exception as e:
        return f"Error reading database: {str(e)}"

# --- MAIN PROGRAM ---
print("=========================================")
print("=== CYBER SECURITY PASSWORD ANALYZER ===")
print("=========================================\n")

user_pass = input("Enter a password to test its strength: ")

# Running Leak Check first
print("\nChecking hacker databases (rockyou.txt)...")
is_leaked = check_rockyou_leak(user_pass)

if is_leaked is True:
    print("🚨 WARNING: This password was found in previous DATA BREACHES! Hackers can crack it instantly.")
elif is_leaked is False:
    print("✅ Safe from common data breaches (Not found in RockYou list).")
else:
    print(f"ℹ️ {is_leaked}")
    
# Running Complexity Check
score, suggestions = check_password_strength(user_pass)

print(f"\nPassword Score: {score}/6")
if score == 6:
    print("Strength: 🔥 Extremely Strong! Excellent security.")
elif score >= 4:
    print("Strength: ⚠️ Moderate. Could be improved.")
else:
    print("Strength: 🔴 Weak Credential! Vulnerable to cyber attacks.")

if suggestions:
    print("\nSuggestions for improvement:")
    for suggestion in suggestions:
        print(f" - {suggestion}")
