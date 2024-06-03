document.addEventListener('DOMContentLoaded', function() {
    console.log("hello")
    const loginForm = document.querySelector('.loginForm');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Prepare the data to be sent in the request body
        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);

        // Send a POST request to the login API endpoint
        fetch('http://127.0.0.1:8000/dashboard/login/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Check if login was successful
            if (data && data.user && data.token) {
                // Store user data and token in local storage
                localStorage.setItem('user_data', JSON.stringify(data.user));
                localStorage.setItem('token', data.token);

                // Redirect the user to the dashboard or any other desired page
                window.location.href = 'http://127.0.0.1:8000/frontend/dashboard/'; // Change '/dashboard' to the actual dashboard URL
            } else {
                // Display an error message to the user
                const errorMessage = document.querySelector('.error-message');
                errorMessage.textContent = 'Invalid username or password';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
