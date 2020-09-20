let addBtn = document.getElementsByClassName('add-cart')
let removeBtn = document.getElementsByClassName('remove-cart')
let inputQuantity = document.getElementById('quantity-input')


for (let i = 0; i < addBtn.length; i++) {
    addBtn[i].addEventListener('click', function (e){
        let action = this.dataset.action
        let productId = this.dataset.product
        productId = parseInt(productId)
        inputQuantity = parseInt(inputQuantity)
        addProduct(productId, action, inputQuantity)
    })
}
function addProduct(productId, action, quantity){
    let url = '/cart/add/'
    fetch(url, {
        method: 'POST',
        headers: {'Content-Type': 'application/json',
                  'X-CSRFToken': csrftoken},
        body:JSON.stringify({'productId': productId, 'action':action, 'quantity': quantity})
    })
        .then((response)=>{
            return response.json();
        })
        .then((data)=>{
            console.log((data));
        })
}


for (let i = 0; i < removeBtn.length; i++) {
    removeBtn[i].addEventListener('click', function (e){
        //let action = this.dataset.action
        let productId = this.dataset.product
        productId = parseInt(productId)
        console.log(productId)
        removeProduct(productId)
    })
}

function removeProduct(productId){
    let url = `/cart/remove/${productId}`
    fetch(url, {
        method: 'DELETE',
        headers: {'Content-Type': 'application/json',
                  'X-CSRFToken': csrftoken}
    })
        .then((response)=>{
            return response.json();
        })
        .then((data)=>{
            console.log((data));
        })
}

