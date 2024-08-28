$(document).ready(function() {
    console.log('Document is ready');

    // Inicializar DataTable
    const table = $('#scrapedData').DataTable();

    $('#scrapForm').on('submit', function(event) {
        event.preventDefault();
        console.log('Form submitted');

        const url = $('#url').val();
        console.log('URL:', url);
        $('#loader').show();
        $.ajax({
            url: '/scrap',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ url: url }),
            success: function(response) {
                console.log('Response:', response);
                $('#response').html('<div class="alert alert-success text-center">Scraping successful!</div>');
                populateTable(response);
                $('#tableContainer').removeClass('d-none'); // Mostrar la tabla
            },
            error: function(error) {
                console.log('Error:', error);
                $('#response').html('<div class="alert alert-danger">Error: ' + error.responseJSON.error + '</div>');
            },
            complete: function() {
                $('#loader').hide();
            }
        });
    });

    function populateTable(data) {
        console.log('Populating table with data:', data);
        table.clear();
        data.forEach(item => {
            table.row.add([
                `<img src="${item.img_url}" alt="Image" style="max-width: 100%; height: auto; display: block;">`,
                `<a href="${item.href}" target="_blank">${item.title}</a>`,
                item.price,
                item.features,
                item.location
            ]).draw();
        });
    }
});