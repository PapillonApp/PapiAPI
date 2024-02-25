document.addEventListener('DOMContentLoaded', function() {
    async function fetchAPI(endpoint, elementId) {
        try {
            const response = await fetch(endpoint);
            const data = await response.json();
            const apiResponseCodeElement = document.getElementById(elementId);
            apiResponseCodeElement.textContent = JSON.stringify(data, null, 2);
        } catch (error) {
            console.error('Une erreur s\'est produite :', error);
        }
    }


    fetchAPI('http://127.0.0.1:5000/staff', 'apiResponse');
    fetchAPI('http://127.0.0.1:5000/warning', 'apiResponse2'); 
    fetchAPI('http://127.0.0.1:5000/disclaimerIE', 'apiResponse3'); 
});
