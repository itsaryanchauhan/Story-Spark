// script.js
const form = document.getElementById('story-form');
const generatedStoryDiv = document.getElementById('generated-story');

form.addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent default form submission behavior

    const genre = document.getElementById('genre').value;
    const character = document.getElementById('character').value;
    const setting = document.getElementById('setting').value;
    const conflict = document.getElementById('conflict').value;

    const data = { genre, character, setting, conflict };

    try {
        const response = await fetch('/generate_story', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        generatedStoryDiv.textContent = result.generated_story;
    } catch (error) {
        console.error('Error:', error);
        generatedStoryDiv.textContent = 'Error: Something went wrong.';
    }
});
