let apiUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json"; // Define the API URL
let characterElement = document.getElementById("character"); // Select the element with the id 'character'

async function fetchCharacterName() { // Define the function
  try {
    let response = await fetch(apiUrl); // Fetch the data
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`); // Check if the response is ok
    let data = await response.json(); // Parse the data
    characterElement.textContent = data.name; // Update the text content
  } catch (error) {
    console.error("Fetch error:", error); // Log the error
  }
}

fetchCharacterName(); // Call the function
