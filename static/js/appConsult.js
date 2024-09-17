
function consult_user(){
    id = document.getElementById('ident').value
    fetch('/consult_user', {
        "method":"post",
        "headers":{"Content-Type":"application/json"},
        "body": JSON.stringify(id)
    })
}