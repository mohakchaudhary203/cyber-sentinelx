function validateForm(formType) {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const error = document.getElementById("error");

    error.innerText = "";

    if (username.length < 3) {
        error.innerText = "Username too short";
        return false;
    }

    if (password.length < 4) {
        error.innerText = "Password must be at least 4 characters";
        return false;
    }

    return true;
}