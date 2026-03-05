// let updateBtns = document.getElementsByClassName('update-item')


// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// const csrftoken = getCookie('csrftoken');


// for (let i = 0; i < updateBtns.length; i++) {
//     updateBtns[i].addEventListener('click', function (event) {
//         event.preventDefault()
//         productId = this.dataset.product
//         action = this.dataset.action

//         console.log('Items added!', productId, action)

//         let url = 'update-item/'
//         fetch(url, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'X-CSRFToken': csrftoken
//             },
//             body: JSON.stringify({
//                 'productId': productId,
//                 'action': action
//             })
//         }).then((response) => {
//             return response.json()
//         }).then((data) => {
//             console.log(data)
//             location.reload()
//         })

//     })
// }


let updateBtns = document.getElementsByClassName('update-item')

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

for (let btn of updateBtns) {
    btn.addEventListener('click', function (e) {
        e.preventDefault()

        let productId = this.dataset.product
        let action = this.dataset.action

        fetch('/shop/update-item/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                productId: productId,
                action: action
            })
        })
        .then(res => res.json())
        .then(data => {
            console.log('Cart updated')
            location.reload()
        })
    })
}