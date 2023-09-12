document.getElementById('add_item').addEventListener('click', () => {
    let newItem = document.createElement('li');
    newItem.textContent = 'Item';
    // Create a new <li> element and add it to the <ul> element

    let myList = document.querySelector('.my_list');
    myList.appendChild(newItem);
}); // Select the <ul> element with class 'my_list' and append a new <li> element
