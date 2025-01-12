document.getElementById('check-btn').addEventListener('click', function() {
    var password = document.getElementById('password').value;
    var special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~";
    var strength = { "Minimum_length": 0, "Upper": 0, "Lower": 0, "Special": 0, "Digit": 0 };
    var feedback = {
        "Minimum_length": "at least 8 characters",
        "Upper": "an uppercase letter",
        "Lower": "a lowercase letter",
        "Special": "a special character (e.g., !@#$%^&*)",
        "Digit": "a number"
    };

    // Check password strength
    if (password.length >= 8) strength["Minimum_length"] = 1;
    if (/[A-Z]/.test(password)) strength["Upper"] = 1;
    if (/[a-z]/.test(password)) strength["Lower"] = 1;
    if (/[!@#$%^&*(),.?":{}|<>]/.test(password)) strength["Special"] = 1;
    if (/[0-9]/.test(password)) strength["Digit"] = 1;

    var str = Object.values(strength).reduce((a, b) => a + b, 0);

    // Display password strength
    var result = document.getElementById('strength');
    if (str === 5) {
        result.innerHTML = 'Strong';
    } else if (str >= 3) {
        result.innerHTML = 'Moderate';
    } else {
        result.innerHTML = 'Weak';
    }

    // Display feedback if necessary
    var feedbackList = document.getElementById('feedback');
    feedbackList.innerHTML = '';
    if (str < 5) {
        for (var key in strength) {
            if (strength[key] === 0) {
                var li = document.createElement('li');
                li.textContent = feedback[key];
                feedbackList.appendChild(li);
            }
        }
    }
});
