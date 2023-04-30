post = document.querySelectorAll(".post-body");

post.forEach(element => {
    console.log(element.innerHTML);
    element.innerHTML = element.innerHTML.replaceAll(".\n", ". <br>");
});
