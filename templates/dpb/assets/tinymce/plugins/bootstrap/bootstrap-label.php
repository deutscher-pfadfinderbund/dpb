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
    $newLabel = false;
    $labelStyle  = '';
    $labelText  = '';
    $labelCode  = '';
} else {
    $newLabel = true;
    $labelStyle  = 'label-primary';
    $labelText  = NEW_CONST;
    $labelCode  = '<span class="label label-primary">' . NEW_CONST . '</span>';
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
                <span><?php echo LABEL_STYLE; ?></span>
            </div>
            <div class="col-md-12">
                <div class="text-center">
                    <div class="choice selector select-label-style">
                        <span class="label label-default" data-attr="label-default">default</span>
                    </div>
                    <div class="choice selector select-label-style">
                        <span class="label label-primary" data-attr="label-primary">primary</span>
                    </div>
                    <div class="choice selector select-label-style">
                        <span class="label label-success" data-attr="label-success">success</span>
                    </div>
                    <div class="choice selector select-label-style">
                        <span class="label label-info" data-attr="label-info">info</span>
                    </div>
                    <div class="choice selector select-label-style">
                        <span class="label label-warning" data-attr="label-warning">warning</span>
                    </div>
                    <div class="choice selector select-label-style">
                        <span class="label label-danger" data-attr="label-danger">danger</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="row margin-bottom-md">
            <div class="choice-title">
                <span><?php echo LABEL_TEXT; ?></span>
            </div>
                <p></p>
                <div class="col-sm-6 col-sm-offset-3 form-inline">
                        <div class="form-group">
                        <label for="label-text"><?php echo YOUR_TEXT; ?> : </label>
                            <input name="label-text" class="form-control select-text" type="text" value="<?php echo NEW_CONST; ?>">
                        </div>
                </div>
        </div>
        <div class="row" id="preview">
            <div id="preview-title" class="margin-bottom-md">
                <span class="label-primary"><?php echo PREVIEW; ?></span>
            </div>
            <div class="col-sm-12 margin-bottom-md text-center" id="test-wrapper">
                <?php echo $labelCode ?>
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
    var newLabel  = '<?php echo $newLabel; ?>';
    var labelStyle  = '<?php echo $labelStyle; ?>';
    var labelText  = '<?php echo $labelText; ?>';
    var labelCode  = '<?php echo $labelCode; ?>';
    $(document).ready(function () {

        makeResponsive();
        getBootstrapStyles();

        /* if newLabel === false, we get code from tinymce */

        if (!newLabel) {
            labelCode = getCode('.label.active');
            var find = new Array(/\s?data-mce-[a-z]+="[^"]+"/g, / active/);
            var replace = new Array('', '');

            for (var i = find.length - 1; i >= 0; i--) {
                labelCode = labelCode.replace(find[i], replace[i]);
            }
            $('#test-wrapper').html(labelCode);
            labelText = $('#test-wrapper .label').html();

            /* get style from tinymce */

            $('.select-label-style span').each(function (index, el) {
                var dataAttr = $(this).attr('data-attr');
                if ($('#test-wrapper .label').hasClass(dataAttr)) {
                    labelStyle = dataAttr;
                }
            });

            /* input text value */

            $('.select-text').val(labelText);
        }

        /* label style */

        $('.selector.select-label-style').each(function (event, element) {

            /* set style on load */

            if ($(element).find('.label').attr('data-attr') == labelStyle) {
                $(element).addClass('active');
            }

            $(element).on('click', function (event) {
                $('.selector.select-label-style').removeClass('active');
                $(this).addClass('active');
                $('#test-wrapper').find('.label').removeClass(labelStyle);
                labelStyle = $(this).find('.label').attr('data-attr');
                $('#test-wrapper').find('.label').addClass(labelStyle);
                updateCode();
            });
        });

        updateCode();

        /* text input */

        $('input[name="label-text"]').on('click, focus', function () {
            $(this).on('keyup', function () {
                changeText(this);
            });
        });

        function changeText(input)
        {
            var value = $(input).prop('value');
            $('#test-wrapper').find('.label').html(value);
            updateCode();
        }
    });
</script>
</body>
</html>
