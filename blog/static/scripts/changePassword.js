const oldPassword = document.querySelector("#id_old_password");
const newPassword = document.querySelector("#id_new_password");
const newPassword2 = document.querySelector("#id_new_password2");
const changeButton = document.querySelector("#change-button");
const errorMessage = document.querySelector(".mismatch");
const changePasswordModal = document.querySelector(".change-password-modal-wrapper");

const url = new URL(window.location.href);
const searchParams = url.searchParams;

const wrongPassword = searchParams.get("error") === "wrong_password" ? true : false;
const passMismatch = searchParams.get("error") === "pass_mismatch" ? true : false;

if (wrongPassword) {
    openModal();
    errorMessage.style.visibility = "visible";
    errorMessage.textContent = "Password incorrecto";
    oldPassword.style.border = "1px solid hsl(0, 100%, 74%)";

    oldPassword.addEventListener("click", () => {
        oldPassword.style.border = "1px solid hsl(0, 0%, 75%)";
        errorMessage.style.visibility = "hidden";
    });
}

if (passMismatch) {
    openModal();
    errorMessage.style.visibility = "visible";
    errorMessage.textContent = "Las contraseñas no coinciden";
    newPassword.style.border = "1px solid hsl(0, 100%, 74%)";
    newPassword2.style.border = "1px solid hsl(0, 100%, 74%)";

    newPassword.addEventListener("click", () => {
        newPassword.style.border = "1px solid hsl(0, 0%, 75%)";
        newPassword2.style.border = "1px solid hsl(0, 0%, 75%)";
        errorMessage.style.visibility = "hidden";
    });
}

function validateNewPassword() {
    const pass1 = newPassword.value;
    const pass2 = newPassword2.value;
    if (pass1 !== pass2) {
        errorMessage.style.visibility = "visible";
        changeButton.disabled = true;
        changeButton.style.cursor = "not-allowed";
        changeButton.style.backgroundColor = "#aaa";
        newPassword.classList.add("is-invalid");
        newPassword2.classList.add("is-invalid");
    } else {
        errorMessage.style.visibility = "hidden";
        changeButton.disabled = false;
        changeButton.style.cursor = "pointer";
        changeButton.style.backgroundColor = "hsl(350, 100%, 60%)";
        changeButton.style.color = "hsl(0, 0%, 95%)";
        newPassword.classList.remove("is-invalid");
        newPassword2.classList.remove("is-invalid");
    }
}

function closeModal() {
    changePasswordModal.style.visibility = "hidden";
}
function openModal() {
    changePasswordModal.style.visibility = "visible";
}
