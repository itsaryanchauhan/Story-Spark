const form = document.getElementById('story-form');
const generatedStoryDiv = document.getElementById('generated-story');

form.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission behavior

  // Capture user input from the form
  const genre = document.getElementById('genre').value;
  const character = document.getElementById('character').value;
  const setting = document.getElementById('setting').value;
  const conflict = document.getElementById('conflict').value;

  // Prepare data to send to the backend
  const data = { genre, character, setting, conflict };

  // Send AJAX request to the backend
  fetch('/generate_story', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  .then(response => response.json())  // Parse JSON response
  .then(data => {
    // Display the generated story
    generatedStoryDiv.textContent = data.generated_story;
  })
  .catch(error => {
    console.error('Error:', error);
    // Handle errors appropriately (e.g., display an error message to the user)
  });
});
