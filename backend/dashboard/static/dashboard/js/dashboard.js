$('#id_product').on('change', (e) => {
    let gtin = $('#id_product').find(":selected").val();
    $.ajax({
        url: fetch_companies_url,
        data: { 'gtin': gtin },
        async: true,
        dataType: 'json',
        success: function (data) {
            $('#id_start_date').val(data.start_date);
            $('#id_end_date').val(data.end_date);
            $('#id_companies').empty();
            for (let i = 0; i < data.companies.length; i++) {
                let name = data.companies[i].commercial_name || data.companies[i].name;
                if (data.companies[i].selected) {
                    $('#id_companies').append('<option selected value="' + data.companies[i].cnpj + '"> ' + name + "</option>");
                } else {
                    $('#id_companies').append('<option value="' + data.companies[i].cnpj + '"> ' + name + "</option>");
                }

            }
        }
    });
});