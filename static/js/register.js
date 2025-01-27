document.getElementById('registerForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const national_id = document.getElementById('national_id').value;
    const phone_number = document.getElementById('phone_number').value;
    const address = document.getElementById('address').value;
    const password = document.getElementById('password').value;

    const response = await fetch('/api/users/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, national_id, phone_number, address, password }),
    });

    if (response.ok) {
        alert('Registration successful. Please login.');
        window.location.href = '/login';
    } else {
        alert('Registration failed. Please try again.');
    }
});