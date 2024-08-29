$(document).ready(function() {
    console.log('Document is ready');

    // Inicializar DataTable
    const table = $('#scrapedData').DataTable();

    $('#uploadForm').on('submit', function(event) {
        event.preventDefault();
        console.log('Form submitted');

        const formData = new FormData();
        const fileField = document.querySelector('input[type="file"]');
        formData.append('pdfFile', fileField.files[0]);

        $('#loader').show();
        $.ajax({
            url: '/upload',
            type: 'POST',
            processData: false,
            contentType: false,
            data: formData,
            success: function(response) {
                console.log('Response:', response);
                $('#response').html('<div class="alert alert-success text-center">Archivo subido con éxito!</div>');
                populateTable(response.scraped_data);
                $('#tableContainer').removeClass('d-none'); // Mostrar la tabla
            },
            error: function(error) {
                console.log('Error:', error);
                $('#response').html('<div class="alert alert-danger">Error al subir el archivo: ' + error.responseJSON.error + '</div>');
            },
            complete: function() {
                $('#loader').hide();
            }
        });
    });

    function populateTable(data) {
        console.log('Populating table with data:', data);
        table.clear();
        data.forEach((item, index) => {
            table.row.add([
                index + 1,
                `<img src="${item.img_url}" alt="Image" style="max-width: 100px; height: auto;">`,
                `<a href="${item.href}" target="_blank">${item.title}</a>`,
                item.price,
                item.features,
                item.location
            ]).draw();
        });
    }
});