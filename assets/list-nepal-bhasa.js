
/*
 * Main
 */
const main = () => {
    const jsonUrl = 'https://asis2016.github.io/nepalbhasa.io/dictionary.nb.minified.json'
    fetch(jsonUrl)
        .then(response => {
            if (response.ok) {
                return response.json()
            } else {
                throw new Error('Network response was not ok.')
            }
        })
        .then(data => {
            accordionContainer(data)
        })
        .catch(error => {
            console.error('Error fetching JSON:', error)
        })
}

/*
 * Accordion container for displaying JSON data.
 *
 */
const accordionContainer = (data) => {
    const container = document.getElementById('accordionFlushMain');

    for (let i = 0; i < data.length; i++) {
        const item = data[i];
        const div = document.createElement('div');
        div.className = 'accordion-item'

        // inner HTML
        div.innerHTML = `
            <h1 class='accordion-header'>
                <button class='accordion-button collapsed' type='button' data-bs-toggle='collapse' 
                        data-bs-target='#flush-collapse${i}' aria-expanded='false' aria-controls='flush-collapse${i}'>
                    ${item['NepalBhasa']}
                </button>
            </h1>
            <div id='flush-collapse${i}' class='accordion-collapse collapse' data-bs-parent='#accordionFlushMain'>
                <div class='accordion-body'>
                    <!-- Nepal Bhasa -->
                    <div class='d-flex pt-2'>
                        <span class='me-3'>

                        </span>
                        <p>
                            ${capitalizeFirstLetter(item['English'])}
                        </p>
                    </div>
                    <!-- Nepali -->
                    <div class='d-flex pt-2'>
                        <span class='me-3'>
                            <img src='assets/images/np.png' alt='' width='25' height='25'>
                        </span>
                        <p>
                            ${item['Nepali']}
                        </p>
                    </div>
                    <!-- Deutsch -->
                    <div class='d-flex pt-2'>
                        <span class='me-3'>
                            <img src='assets/images/de.png' alt='' width='25' height='25'>
                        </span>
                        <p>
                            ${capitalizeFirstLetter(item['German'])}
                        </p>
                    </div>
                </div>
            </div>
        `
        // Append to the container
        container.appendChild(div);
    }
}

/*
 * Capitalize the first letter of the word
 */
function capitalizeFirstLetter(word) {
    if (word.length === 0) {
        return word;
    }
    return word.charAt(0).toUpperCase() + word.slice(1);
}

main()