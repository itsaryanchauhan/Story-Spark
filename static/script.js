// script.js
const form = document.getElementById('story-form');
const generatedStoryDiv = document.getElementById('generated-story');
const noButton = document.getElementById('no-button');

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    submitStoryData();
});

async function submitStoryData(continueStory = false) {
    const genre = document.getElementById('genre').value;
    const character = document.getElementById('character').value;
    const setting = document.getElementById('setting').value;
    const conflict = document.getElementById('conflict').value;

    const data = { genre, character, setting, conflict, continue_story: continueStory };

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
}

noButton.addEventListener('click', function() {
    submitStoryData(true);
});
