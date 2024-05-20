const form = document.getElementById('story-form');
const generatedStoryDiv = document.getElementById('generated-story');
const feedbackSection = document.getElementById('feedback-section');
const yesButton = document.getElementById('yes-button');
const noButton = document.getElementById('no-button');

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
        feedbackSection.style.display = 'block'; // Show feedback options
    } catch (error) {
        console.error('Error:', error);
        generatedStoryDiv.textContent = 'Error: Something went wrong.';
    }
});

yesButton.addEventListener('click', function() {
    alert('Thank you for your feedback!');
    feedbackSection.style.display = 'none'; // Hide feedback section
});

noButton.addEventListener('click', function() {
    alert('Please adjust your inputs and try again.');
    feedbackSection.style.display = 'none'; // Hide feedback section
});
