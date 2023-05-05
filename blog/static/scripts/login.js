const usernameInput = document.querySelector("#id_username");
const passwordInput = document.querySelector("#id_password");
const errorMessage = document.querySelector(".error-message");

const url = new URL(window.location.href);
const searchParams = url.searchParams;
const credentialsError = searchParams.get("error") === "invalid_credentials" ? true : false;
const usernameTaken = searchParams.get("error") === "username_taken" ? true : false;

//Chequea la url para ver si hay errores y los muestra

if (credentialsError || usernameTaken) {
    usernameInput.classList.add("is-invalid");
    passwordInput.classList.add("is-invalid");
    errorMessage.classList.remove("hide");
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
