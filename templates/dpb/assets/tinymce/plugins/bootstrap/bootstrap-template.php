<?php
$bootstrap_css_path = addslashes($_GET['bootstrap_css_path']);

/* language */

if (file_exists('langs/' . $_GET['language'] . '.php')) {
    require_once 'langs/' . $_GET['language'] . '.php';
} else { // default
    require_once 'langs/en_EN.php';
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
                <span><?php echo BREAKPOINT; ?></span>
            </div>
            <div class="col-md-12">
                <div class="text-center">
                <a href="#" class="breakpoint-tooltip" data-toggle="tooltip" data-placement="bottom" title="<?php echo BLOCKS_WILL_BE_STACKED_ON_XS_DEVICES; ?>"><div class="choice selector select-breakpoint" data-attr="col-xs"><span class="bootstrap-icon-phone prepend"></span>xs</div></a>
                <a href="#" class="breakpoint-tooltip" data-toggle="tooltip" data-placement="bottom" title="<?php echo BLOCKS_WILL_BE_STACKED_ON_XS_SMALL_DEVICES; ?>"><div class="choice selector select-breakpoint" data-attr="col-sm"><span class="bootstrap-icon-tablet prepend"></span>sm</div></a>
                <a href="#" class="breakpoint-tooltip" data-toggle="tooltip" data-placement="bottom" title="<?php echo BLOCKS_WILL_BE_STACKED_ON_XS_SMALL_MEDIUM_DEVICES; ?>"><div class="choice selector select-breakpoint" data-attr="col-md"><span class="bootstrap-icon-tablet-landscape prepend"></span>md</div></a>
                <a href="#" class="breakpoint-tooltip" data-toggle="tooltip" data-placement="bottom" title="<?php echo BLOCKS_WILL_NEVER_BE_STACKED; ?>"><div class="choice selector select-breakpoint" data-attr="col-lg"><span class="bootstrap-icon-screen prepend"></span>lg</div></a>
                </div>
            </div>
        </div>
        <div class="row margin-bottom-md" id="cols">
            <div class="choice-title">
                <span><?php echo COLS; ?></span>
            </div>
                <div class="row col-sm-12"><p class="alert alert-info text-center col-sm-6 col-sm-offset-3"><?php echo DRAG_DROP_ELEMENTS_TO_PREVIEW; ?></p></div>
            <div class="col-xs-1"><span>1/12<sup>e</sup></span></div>
            <div class="col-xs-2"><span>2/12<sup>e</sup></span></div>
            <div class="col-xs-3"><span>3/12<sup>e</sup></span></div>
            <div class="col-xs-4"><span>4/12<sup>e</sup></span></div>
            <div class="col-xs-5"><span>5/12<sup>e</sup></span></div>
            <div class="col-xs-6"><span>6/12<sup>e</sup></span></div>
            <div class="col-xs-7"><span>7/12<sup>e</sup></span></div>
            <div class="col-xs-8"><span>8/12<sup>e</sup></span></div>
            <div class="col-xs-9"><span>9/12<sup>e</sup></span></div>
            <div class="col-xs-10"><span>10/12<sup>e</sup></span></div>
            <div class="col-xs-11"><span>11/12<sup>e</sup></span></div>
            <div class="col-xs-12"><span>12/12<sup>e</sup></span></div>
        </div>
        <div class="row" id="preview">
            <div id="preview-title" class="margin-bottom-md">
                <span class="btn-primary"><?php echo PREVIEW; ?></span>
            </div>
            <div class="row margin-bottom-md dropzone" id="test-wrapper">
            <div class="row"><h2><?php echo DROP_ELEMENTS_HERE; ?></h2></div>
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
<script type="text/javascript" src="js/colorpicker.min.js"></script>
<script type="text/javascript" src="js/utils.min.js"></script>
<script type="text/javascript" src="js/jquery.htmlClean.min.js"></script>
<script type="text/javascript" src="js/iconset/iconset-glyphicon.min.js"></script>
<script type="text/javascript" src="js/bootstrap-iconpicker.min.js"></script>
<script type="text/javascript" src="google-code-prettify/prettify.js"></script>
<script type="text/javascript">
    var breakpoint = 'col-xs';
    var newBreakpoint = 'col-xs';
    /* add property for drop and data transfer */
    $.event.props.push('dataTransfer');
    $(document).ready(function () {

        makeResponsive();
        getBootstrapStyles();

        $('a[data-toggle="tooltip"]').tooltip();

        /* breakpoint */

        $('.selector.select-breakpoint').each(function (event, element) {

            /* set style on load */

            if ($(element).attr('data-attr') =="col-xs") {
                $(element).addClass('active');
            }

            $(element).on('click', function (event) {
                newBreakpoint = $(this).attr('data-attr');
                $('.selector.select-breakpoint').removeClass('active');
                $(this).addClass('active');
                updateClasses(breakpoint);
                updateCode();
            });
        });
        $('#cols div').attr('draggable','true').on({
            dragstart: function (e) {
                $(this).css('opacity', '0.5');

                /* store data to transfer */

                e.dataTransfer.setData('text', '.' + $(this).attr('class'));
            },
            dragenter: function (e) {
                e.preventDefault();
            },
            dragleave: function () {
            },
            dragover: function (e) {
                e.preventDefault();
            },
            dragend: function () {
                $(this).css('opacity', '1');
            }
        });
        makeDropable('#test-wrapper');

        function makeDropable(element)
        {
            $(element).on({
                dragenter: function (e) {
                    e.preventDefault();
                },
                dragover: function (e) {
                    e.preventDefault();
                    $('#test-wrapper div.row h2').animate({opacity: "-=2"}, 500,function () {
                        $(this).remove();
                    });

                    return false;
                },
                drop: function (e) {
                    e.preventDefault();
                    var data = e.dataTransfer.getData('text');
                    data = $('#cols').find(data).clone().css('opacity', '1').wrap('<div>').parent().html();
                    var newElement = $(this).find('div.row').append(data);
                    updateClasses('col-xs');
                    $(newElement).sortable({
                        callback: updateCode
                    });
                    updateCode();
                }
            });
        }

        function updateClasses(bpt)
        {
            $('#test-wrapper').find('div[class^="' + bpt + '"]').each(function () {
                var oldClass = $(this).attr('class');
                var newClass = oldClass.replace(bpt, newBreakpoint);
                $(this).removeClass(oldClass).addClass(newClass);
            });
            breakpoint = newBreakpoint;
        }
    });
</script>
</body>
</html>
