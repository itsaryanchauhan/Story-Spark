const form = document.getElementById('story-form');
const generatedStoryDiv = document.getElementById('generated-story');

form.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission behavior

  const genre = document.getElementById('genre').value;
  const character = document.getElementById('character').value;
  const setting = document.getElementById('setting').value;
  const conflict = document.getElementById('conflict').value;

  const data = { genre, character, setting, conflict };

  fetch('/generate_story', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  .then(response => response.json()) // Parse JSON response
  .then(data => {
    generatedStoryDiv.textContent = data.generated_story;
    const isStoryLongEnough = confirm("Is the story length sufficient?");
    if (!isStoryLongEnough) {
      fetchStory(); // Simulate form submission for continuation (optional)
    }
  })
  .catch(error => {
    console.error('Error:', error);
    generatedStoryDiv.textContent = 'Error: Something went wrong.';
  });
});

// Optional function for continuing the story (if implemented in python)
function fetchStory() {
  // Simulate form submission to fetch story again
  const form = document.getElementById('story-form');
  form.submit();
}
