// Reset the form input after submission
document.body.addEventListener('htmx:afterSwap', function (evt) {
    const form = document.querySelector("form");
    form.reset();
});
