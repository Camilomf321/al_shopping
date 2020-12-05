let addBtn = document.getElementsByClassName('add-cart')
let removeBtn = document.getElementsByClassName('remove-cart')


var proQty = $('.pro-qty');
proQty.prepend('<span class="dec qtybtn">-</span>');
proQty.append('<span class="inc qtybtn">+</span>');
var newVal;
proQty.on('click', '.qtybtn', function () {
    var $button = $(this);
    var oldValue = $button.parent().find('input').val();
    if ($button.hasClass('inc')) {
        newVal = parseFloat(oldValue) + 1;
    } else {
        // Don't allow decrementing below zero
        if (oldValue > 1) {
            newVal = parseFloat(oldValue) - 1;
        } else {
            newVal = 1;
        }
    }
    $button.parent().find('input').val(newVal);
});


/*ADD BUTTON*/
for (let i = 0; i < addBtn.length; i++) {
    addBtn[i].addEventListener('click', function () {
        let productId = this.dataset.product
        productId = parseInt(productId)
        addProduct(productId)
    })
}
/*ADD PRODUCT TO CART FUNCTION*/
function addProduct(productId) {
    let url = '/cart/add/'
   fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({'productId': productId})
        })
            .then((response) => {
                return response.json();
            })
            .then(() => {
                alert('El producto fue agregado')
            })
}

/*REMOVE BUTTON */
for (let i = 0; i < removeBtn.length; i++) {
    removeBtn[i].addEventListener('click', function () {
        //let action = this.dataset.action
        let productId = this.dataset.product
        productId = parseInt(productId)
        removeProduct(productId)
    })
}

/*REMOVE PRODUCT TO CART FUNCTION*/
function removeProduct(productId) {
    let url = '/cart/remove/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'productId': productId})
    })
        .then()
        .then(() => {
            location.reload()
        })
}



