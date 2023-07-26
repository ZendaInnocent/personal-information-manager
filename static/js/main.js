// Reset the form input after submission
document.body.addEventListener('htmx:afterSwap', function (evt) {
    const form = document.querySelector("form");
    form.reset();
});


htmx.on('messages', function (evt) {
    evt.detail.value.forEach(createToast);
})

function createToast(message) {
    // Clone the template
    const element = htmx.find("[data-toast-template]").cloneNode(true)

    // Remove the data-toast-template attribute
    delete element.dataset.toastTemplate

    // Set the CSS class
    element.className += " " + message.tags

    // Set the text
    htmx.find(element, "[data-toast-body]").innerText = message.message

    // Add the new element to the container
    htmx.find("[data-toast-container]").appendChild(element)

    // Show the toast using Bootstrap's API
    const toast = new bootstrap.Toast(element, { delay: 2000 })
    toast.show()
}
