
function lib_ajax(button_id, element_id_1, element_id_2, url) {
    $(document).ready(function () {
        $("#" + button_id).click(function () {
            var element_val_1 = $("#" + element_id_1).val();
            var element_val_2 = $("#" + element_id_2).val();
            $.ajaxSetup(url,);
            $.ajax({
                url: url,
                type: 'POST',
                datatype: 'text',
                data: {
                    'csrfmiddlewaretoken':$('[name="csrfmiddlewaretoken"]').val(),
                    'os_name': element_val_1,
                    'os_version': element_val_2,
                },
                success: function(result){
                    $('#info').text(result);
                },
                error: function (xhr, ajaxOptions, thrownError) {
                    alert("thrwnErroe: " + thrownError);
                },
            });
        });
    });
}

function lib_select2() {
    $(document).ready(function() {
        $('.js-example-basic-single').select2();
    });
}

