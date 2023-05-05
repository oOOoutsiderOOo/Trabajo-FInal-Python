profilePic = document.querySelector(".profile-picture");

popup = document.querySelector(".popup-wrapper");
changePicButton = document.querySelector("#change-pic-button");

modal = document.querySelector(".modal-wrapper");
cancelButton = document.querySelector(".cancel-button");

// Menú pop up

profilePic.addEventListener("click", () => {
    if (popup.style.visibility === "visible") {
        popup.style.visibility = "hidden";
    } else {
        popup.style.visibility = "visible";
    }
});

// Cerrar el menú pop up al hacer click fuera de él

document.addEventListener("click", e => {
    let target = e.target;
    if (!popup.contains(target)) {
        popup.style.visibility = "hidden";
    }
    if (target === profilePic.firstChild) {
        popup.style.visibility = "visible";
    }
});

popup.addEventListener("click", () => {
    if (popup.style.visibility === "visible") {
        popup.style.visibility = "hidden";
    }
});

// Modal para cambiar la foto de perfil

changePicButton.addEventListener("click", () => {
    modal.style.visibility = "visible";
});

cancelButton.addEventListener("click", () => {
    modal.style.visibility = "hidden";
});
