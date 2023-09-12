let headerElement = document.querySelector('header'); // select the header element

toggle_header.addEventListener('click', () => {
    headerElement.classList.toggle('red');
    headerElement.classList.toggle('green');
}); // added event listener to the toggle_header element to toggle the header class
