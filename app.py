from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    suggestions = []
    
    # Logic for password strength
    if len(password) >= 12: 
        score += 2
    elif len(password) >= 8: 
        score += 1
    else:   
        suggestions.append("Password is too short (min 8 characters).")

    if re.search(r"[A-Z]", password): 
        score += 1
    else: 
        suggestions.append("Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password): 
        score += 1
    else: 
        suggestions.append("Add at least one lowercase letter (a-z).")

    if re.search(r"[0-9]", password): 
        score += 1
    else: 
        suggestions.append("Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): 
        score += 1
    else: 
        suggestions.append("Add at least one special character.")      
    
    return score, suggestions

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        password = request.form.get('password')
        score, suggestions = check_password_strength(password)
        result = {
            'score': score,
            'suggestions': suggestions,
            'password': password
        }
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)