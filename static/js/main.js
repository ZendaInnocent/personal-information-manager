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

// Delete Todo
const deleteBtns = document.querySelectorAll('.delete-btn');

deleteBtns.forEach(deleteTodo)

function deleteTodo(deleteBtn) {
    deleteBtn.addEventListener('click', () => {
        const swalWithBootstrapButtons = Swal.mixin({
            customClass: {
                confirmButton: 'btn btn-success me-2',
                cancelButton: 'btn btn-danger'
            },
            buttonsStyling: false
        })

        swalWithBootstrapButtons.fire({
            title: 'Are you sure you want to delete?',
            text: "You won't be able to revert this!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Yes, delete it!',
            cancelButtonText: 'No, cancel!',
            reverseButtons: false
        }).then((result) => {
            if (result.isConfirmed) {
                const url = deleteBtn.getAttribute('data-url')

                htmx.ajax('DELETE', url, { target: '#todos-list', swap: 'outerHTML' }).then(() => {
                    swalWithBootstrapButtons.fire(
                        'Deleted!',
                        'Your task has been deleted.',
                        'success'
                    )

                })

            } else if (
                result.dismiss === Swal.DismissReason.cancel
            ) {

            }
        })
    })
}


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
