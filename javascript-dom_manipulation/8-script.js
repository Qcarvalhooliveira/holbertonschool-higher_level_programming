document.addEventListener("DOMContentLoaded", () => { // Define the event listener
    const helloElement = document.getElementById("hello"); // Select the element with the id 'hello'
  
    async function fetchAndDisplayTranslation() {  // Define the function
      try {
        const response = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr"); // Fetch the data
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`); // Check if the response is ok
        const translation = await response.text(); // Parse the data
        helloElement.textContent = translation; // Add the translation to the element
      } catch (error) { // Handle the error
        console.error("Fetch error:", error); // Log the error
      }
    }
  
    fetchAndDisplayTranslation(); // Call the function
  });
  
