post = document.querySelectorAll(".post-body");

// Renderiza correctamente los saltos de línea en los párrafos
post.forEach(element => {
    element.innerHTML = element.innerHTML.replaceAll(".\n", ". <br>");
});
