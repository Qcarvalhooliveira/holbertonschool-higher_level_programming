let redClass = document.querySelector('#red_header'); // select the id red_header element

redClass.addEventListener('click', () => {
    redClass.classList.add('red');
}); // added event listener to the red_header id to add red class to the header element on click
