document.querySelector("#btn-register").addEventListener('click', register_view)
document.querySelector("#btn-consult").addEventListener('click', consult_view)

function register_view () {
    window.location = "/register_page"
}

function consult_view () {
    window.location = "/consult_page"
}