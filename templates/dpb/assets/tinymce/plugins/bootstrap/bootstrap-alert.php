<?php
$bootstrap_css_path = addslashes($_GET['bootstrap_css_path']);
function siteURL()
{
    $protocol = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off' || $_SERVER['SERVER_PORT'] == 443) ? "https://" : "http://";
    $domainName = $_SERVER['HTTP_HOST'];

    return $protocol.$domainName;
}
define('SITE_URL', siteURL());

/* language */

if (file_exists('langs/' . $_GET['language'] . '.php')) {
    require_once 'langs/' . $_GET['language'] . '.php';
} else { // default
    require_once 'langs/en_EN.php';
}
if (isset($_GET['edit'])) {
    $newAlert         = false;
    $alertDismissable = '';
    $alertText        = '';
    $alertStyle       = '';
    $alertCode        = '';
} else {
    $newAlert         = true;
    $alertDismissable = true;
    $alertText        = 'Well done! You successfully read this <a href="#" class="alert-link">important alert message</a>.';
    $alertStyle       = 'alert-success';
    $alertCode        = '<div class="alert alert-success alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>Well done! You successfully read this <a href="#" class="alert-link">important alert message</a>.</div>';
}
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <link rel="stylesheet" href="<?php echo $bootstrap_css_path; ?>">
    <link rel="stylesheet" href="css/plugin.min.css">
    <link href="google-code-prettify/prettify.css" type="text/css" rel="stylesheet" />
    <link href='http://fonts.googleapis.com/css?family=Source+Code+Pro' rel='stylesheet' type='text/css'>
</head>
<body>
    <div class="container">
        <div class="row margin-bottom-md">
            <div class="choice-title">
                <span><?php echo DISMISSABLE; ?></span>
            </div>
            <div class="col-md-12">
                <div class="text-center">
                    <div class="btn-group btn-toggle-dismissable">
                        <button class="btn btn-sm btn-default" data-attr="false"><?php echo NO_CLOSE_BUTTON; ?></button>
                        <button class="btn btn-sm btn-success active" data-attr="true"><?php echo CLOSE_BUTTON; ?></button>
                    </div>
                </div>
            </div>
        </div>
        <div class="row margin-bottom-md">
            <div class="choice-title">
                <span><?php echo ALERT_STYLE; ?></span>
            </div>
            <div class="col-sm-2 col-sm-offset-2 col-xs-6 text-center">
                <div class="choice selector select-alert-style">
                    <div class="alert alert-success" data-attr="alert-success">success</div>
                </div>
            </div>
            <div class="col-sm-2 col-xs-6 text-center">
                <div class="choice selector select-alert-style">
                    <div class="alert alert-info" data-attr="alert-info">info</div>
                </div>
            </div>
            <div class="col-sm-2 col-xs-6 text-center">
                <div class="choice selector select-alert-style">
                    <div class="alert alert-warning" data-attr="alert-warning">warning</div>
                </div>
            </div>
            <div class="col-sm-2 col-xs-6 text-center">
                <div class="choice selector select-alert-style">
                    <div class="alert alert-danger" data-attr="alert-danger">danger</div>
                </div>
            </div>
        </div>
        <div class="row margin-bottom-md">
            <div class="choice-title">
                <span><?php echo ALERT_TEXT; ?></span>
            </div>
                <p></p>
                <div class="col-sm-8 col-sm-offset-2 form-inline margin-bottom-md">
                        <div class="form-group">
                        <label for="alert-text"><?php echo YOUR_TEXT; ?> : </label>
                            <input name="alert-text" class="form-control select-text" type="text" size="52" value="Well done! You successfully read this &lt;a href=&quot;#&quot; class=&quot;alert-link&quot;&gt;important alert message&lt;/a&gt;.">
                        </div>
                </div>
                <div class="col-sm-12">
                    <p class="text-success text-center"><?php echo HTML_AUTHORIZED; ?></p>
                </div>
        </div>
        <div class="row" id="preview">
            <div id="preview-title" class="margin-bottom-md">
                <span class="label-primary"><?php echo PREVIEW; ?></span>
            </div>
            <div class="col-sm-12 margin-bottom-md" id="test-wrapper">
                <?php echo $alertCode ?>
            </div>
        </div>
        <div class="row">
            <div id="code-title">
                <a href="#" id="code-slide-link"><?php echo CODE; ?> <i class="glyphicon glyphicon-arrow-up"></i></a>
            </div>
            <div class="col-sm-12" id="code-wrapper">
                <pre></pre>
            </div>
        </div>
    </div>
<script type="text/javascript" src="js/jquery-2.1.1.min.js"></script>
<script type="text/javascript" src="js/bootstrap.min.js"></script>
<script type="text/javascript" src="js/utils.min.js"></script>
<script type="text/javascript" src="js/jquery.htmlClean.min.js"></script>
<script type="text/javascript" src="google-code-prettify/prettify.js"></script>
<script type="text/javascript">
    var newAlert         = '<?php echo $newAlert; ?>';
    var alertDismissable = '<?php echo $alertDismissable; ?>';
    var alertText        = '<?php echo $alertText; ?>';
    var alertStyle       = '<?php echo $alertStyle; ?>';
    var alertCode        = '<?php echo $alertCode; ?>';
    $(document).ready(function () {

        makeResponsive();
        getBootstrapStyles();

        /* if newAlert === false, we get code from tinymce */

        if (!newAlert) {
            alertCode = getCode(".alert.active");
            var find = new Array(/\s?data-mce-[a-z]+="[^"]+"/g, / active/);
            var replace = new Array('', '');

            for (var i = find.length - 1; i >= 0; i--) {
                alertCode = alertCode.replace(find[i], replace[i]);
            }
            $('#test-wrapper').html(alertCode);
            alertText = $('#test-wrapper .alert').html();

            /* get style from tinymce */

            $('.select-alert-style div').each(function (index, el) {
                var dataAttr = $(this).attr('data-attr');
                if ($('#test-wrapper div').hasClass(dataAttr)) {
                    alertStyle = dataAttr;
                }
            });

            /* get dismissable from tinymce */

            if ($('#test-wrapper button.close').length > 0) {
                alertDismissable = true;
            } else {
                alertDismissable = false;
                var btnGroup = $('.btn-toggle-dismissable')[0];
                toggleBtn(btnGroup);
            }

            /* input text value */

            $('.select-text').val(alertText);
        }

        updateCode();

        /* button style */

        $('.selector.select-alert-style').each(function (event, element) {

            /* set style on load */

            if ($(element).find('div').hasClass(alertStyle)) {
                $(element).addClass('active');
            }

            $(element).on('click', function (event) {
                $('.selector.select-alert-style').removeClass('active');
                $(this).addClass('active');
                $('#test-wrapper div').removeClass(alertStyle);
                alertStyle = $(this).find('div').attr('data-attr');
                $('#test-wrapper div').addClass(alertStyle);
                updateCode();
            });
        });

        /* text input */

        $('input[name="alert-text"]').on('click, focus', function () {
            $(this).on('keyup', function () {
                changeText(this);
            });
        });

        /* toggle dismissable */

        activateToggleDismissable();

        function changeText(input)
        {
            var value = $(input).prop('value');
            $('#test-wrapper').find('.alert').html(value);
            updateCode();
        }

        function activateToggleDismissable()
        {
            $('.btn-toggle-dismissable').on('click', function () {
                toggleDismissable(this);
            });
        }

        function toggleDismissable(btnGroup)
        {
            alertDismissable = toggleBtn(btnGroup);
            var alertDiv = $('#test-wrapper').find('div.alert');
            if (alertDismissable) {
                if ($('#test-wrapper button.close').length < 1) {
                    $('<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>').prependTo(alertDiv);
                    alertDiv.addClass('alert-dismissable');
                }
            } else {
                alertDiv.removeClass('alert-dismissable');
                alertDiv.find('button.close').remove();
            }
            updateCode();
        }
    });
</script>
</body>
</html>
