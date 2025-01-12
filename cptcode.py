from flask import Flask, request, jsonify

# Load rockyou.txt passwords
rockyou_file = "rockyou.txt"
with open(rockyou_file, "r", encoding="latin-1") as file:
    rockyou_passwords = set(line.strip() for line in file)

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_password():
    data = request.get_json()  # Get JSON data from POST request
    password = data.get('password')
    
    if not password:
        return jsonify({"error": "Password is required"}), 400

    # Analyze password
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~"
    strength = {"Minimum_length": 0, "Upper": 0, "Lower": 0, "Special": 0, "Digit": 0}
    
    if len(password) >= 8:
        strength["Minimum_length"] = 1
    if any(char.isupper() for char in password):
        strength["Upper"] = 1
    if any(char.islower() for char in password):
        strength["Lower"] = 1
    if any(char in special_characters for char in password):
        strength["Special"] = 1
    if any(char.isdigit() for char in password):
        strength["Digit"] = 1
    
    total_strength = sum(strength.values())
    feedback = {
        "Minimum_length": "at least 8 characters",
        "Upper": "an uppercase letter",
        "Lower": "a lowercase letter",
        "Special": "a special character (e.g., !@#$%^&*)",
        "Digit": "a number",
    }
    missing_feedback = [feedback[key] for key, value in strength.items() if value == 0]
    
    response = {
        "strength": "Strong" if total_strength == 5 else "Moderate" if total_strength >= 3 else "Weak",
        "is_common": password in rockyou_passwords,
        "missing": missing_feedback,
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
