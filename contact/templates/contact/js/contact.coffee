check_form_input = (id, title) ->
  if $(id).val() == ""
    $(id + "-div").addClass "has-warning"
    #$(id + "-div").tooltip({placement: 'bottom',trigger: 'manual',title: title}).tooltip('show')
    return false
  else
    $(id + "-div").removeClass "has-warning"
    $(id + "-div").tooltip().tooltip('hide')
    return true

check_form_botcheck = (id, title, value) ->
  if $(id).val() != value
    $(id + "-div").addClass "has-warning"
    $(id + "-div").tooltip({placement: 'bottom',trigger: 'manual',title: title}).tooltip('show')
    return false
  else
    $(id + "-div").removeClass "has-warning"
    $(id + "-div").tooltip().tooltip('hide')
    return true

$ ->
  $("#submit").click ->
    $('[data-toggle="tooltip"]').tooltip()

    title = "Bitte fülle dieses Feld aus"

    valid0 = check_form_input("#firstname", title)
    valid1 = check_form_input("#lastname", title)
    valid2 = check_form_input("#email", title)
    valid3 = check_form_input("#subject", title)
    valid4 = check_form_botcheck("#botcheck", "Bitte beantworte die Frage mit ja", "ja")
    valid5 = check_form_input("#message", title)

    if valid0 and valid1 and valid2 and valid3 and valid4 and valid5
      $("#contact-form").hide()
      $("#proceeding").show()
      $("#contact-form").submit()