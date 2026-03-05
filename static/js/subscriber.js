let subscribeForm = document.getElementById('subscribeForm')
let errors = document.getElementById('errors')

subscribeForm.addEventListener('submit', function(e){
    e.preventDefault()
    let email = document.getElementById('email').value
    console.log('test')
    fetch('http://127.0.0.1:8000/api/subscriber/', {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : subscribeForm.csrfmiddlewaretoken.value
        },
        body: JSON.stringify({'email' : email}) 
    }).then(
        response => {
            if(response.ok){
                subscribeForm.innerHTML = `<h2 style="color: rgb(255, 139, 90)"> Thanks for subscription! </h2>`
            }
            else{
                errors.innerText = 'Already subscribed!'
            }
        }
    )

})