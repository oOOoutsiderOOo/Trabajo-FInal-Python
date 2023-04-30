profilePic = document.querySelector(".profile-picture");

popup = document.querySelector(".popup-wrapper");
changePicButton = document.querySelector("#change-pic-button");

modal = document.querySelector(".modal-wrapper");
cancelButton = document.querySelector(".cancel-button");

profilePic.addEventListener("click", () => {
    if (popup.style.visibility === "visible") {
        popup.style.visibility = "hidden";
    } else {
        popup.style.visibility = "visible";
    }
});

popup.addEventListener("click", () => {
    if (popup.style.visibility === "visible") {
        popup.style.visibility = "hidden";
    }
});

changePicButton.addEventListener("click", () => {
    modal.style.visibility = "visible";
});

cancelButton.addEventListener("click", () => {
    modal.style.visibility = "hidden";
});
