/**
 * Created with PyCharm.
 * User: Manuel
 * Date: 31/07/12
 * Time: 04:57 AM
 * To change this template use File | Settings | File Templates.
 */
$('#account_content').ready(function () {
    $('#form-change-password').submit(function () {
        $.ajax({
            url:'/change_password/',
            type:'POST',
            data:$(this).serialize(),
            success:function (data) {
                $('#error_account').html("");
                $('#error_account').html(data.error);
                $('#div_error_account').show();
            }
        });
        return false;
    });
});