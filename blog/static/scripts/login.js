const usernameInput = document.querySelector("#id_username");
const passwordInput = document.querySelector("#id_password");
const confirmPasswordInput = document.querySelector("#id_password2");

const submitButton = document.querySelector("#submit-button");

const errorMessage = document.querySelector(".error-message");

const url = new URL(window.location.href);
const searchParams = url.searchParams;
const credentialsError = searchParams.get("error") === "invalid_credentials" ? true : false;
const usernameTaken = searchParams.get("error") === "username_taken" ? true : false;
const passMismatch = searchParams.get("error") === "pass_mismatch" ? true : false;

//Chequea la url para ver si hay errores y los muestra

if (credentialsError || usernameTaken) {
    usernameInput.classList.add("is-invalid");
    passwordInput.classList.add("is-invalid");
    errorMessage.classList.remove("hide");
}

if (passMismatch) {
    errorMessage.textContent = "Las contraseñas no coinciden";
    passwordInput.classList.add("is-invalid");
    errorMessage.classList.remove("hide");
}

//Valida que las contraseñas imgresadas coincidan
//TODO Agregar validación de caracteres especiales
function validatePassword() {
    const pass1 = passwordInput.value;
    const pass2 = confirmPasswordInput.value;
    if (pass1 !== pass2) {
        submitButton.disabled = true;
        submitButton.style.cursor = "not-allowed";
        submitButton.style.backgroundColor = "#aaa";
        errorMessage.textContent = "Las contraseñas no coinciden";
        passwordInput.classList.add("is-invalid");
        confirmPasswordInput.classList.add("is-invalid");
        errorMessage.classList.remove("hide");
    } else {
        submitButton.disabled = false;
        submitButton.style.cursor = "pointer";
        submitButton.style.backgroundColor = "hsl(209, 100%, 60%)";
        passwordInput.classList.remove("is-invalid");
        confirmPasswordInput.classList.remove("is-invalid");
        errorMessage.classList.add("hide");
    }
}

usernameInput.addEventListener("input", () => {
    usernameInput.classList.remove("is-invalid");
    passwordInput.classList.remove("is-invalid");
    errorMessage.classList.add("hide");
});
passwordInput.addEventListener("input", () => {
    usernameInput.classList.remove("is-invalid");
    passwordInput.classList.remove("is-invalid");
    errorMessage.classList.add("hide");
});
