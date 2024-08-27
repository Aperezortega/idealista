$(document).ready(function() {
    console.log('Document is ready');

    // Inicializar DataTable
    const table = $('#scrapedData').DataTable();

    $('#scrapForm').on('submit', function(event) {
        event.preventDefault();
        console.log('Form submitted');

        const url = $('#url').val();
        console.log('URL:', url);

        $.ajax({
            url: '/scrap',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ url: url }),
            success: function(response) {
                console.log('Response:', response);
                $('#response').html('<div class="alert alert-success">Scraping successful!</div>');
                populateTable(response);
            },
            error: function(error) {
                console.log('Error:', error);
                $('#response').html('<div class="alert alert-danger">Error: ' + error.responseJSON.error + '</div>');
            }
        });
    });

    function populateTable(data) {
        console.log('Populating table with data:', data);
        table.clear();
        data.forEach(item => {
            table.row.add([
                item.title,
                `<a href="${item.href}" target="_blank">${item.href}</a>`,
                item.price,
                item.img_url,
                item.features,
                item.location
            ]).draw();
        });
    }
});