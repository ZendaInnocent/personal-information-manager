// Reset the form input after submission
document.body.addEventListener('htmx:afterSwap', function (evt) {
    const form = document.querySelector("form");
    form.reset();
});

htmx.onLoad(() => {
    htmx.findAll('.toast').forEach((element) => {
        let toast = bootstrap.Toast.getInstance(element)

        if (!toast) {
            const toast = new bootstrap.Toast(element)
            toast.show()
        }
        // } else if (!toast.isShown()) {
        //     toast.dispose()
        //     element.remove()
        // }
    })
})

htmx.onLoad(function (content) {
    var sortables = content.querySelectorAll(".sortable");
    for (var i = 0; i < sortables.length; i++) {
        var sortable = sortables[i];
        new Sortable(sortable, {
            animation: 150,
            ghostClass: 'blue-background-class'
        });
    }
})



// const Toast = Swal.mixin({
//     toast: true,
//     position: 'top-end',
//     showConfirmButton: false,
//     timer: 3000,
//     timerProgressBar: true,
//     didOpen: (toast) => {
//         toast.addEventListener('mouseenter', Swal.stopTimer)
//         toast.addEventListener('mouseleave', Swal.resumeTimer)
//     }
// })

// Toast.fire({
//     icon: 'success',
//     title: 'Signed in successfully'
// })
