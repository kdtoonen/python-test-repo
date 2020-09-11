message_account_was_already_created = "You already have an account, " \
                              "would you like to reset it and " \
                              "receive a change password link?"
message_account_is_created = "Your account has been created, " \
                             "please check you e-mail for further instructions"
message_error_creating_account = "Something went wrong creating your account, " \
                                 "please contact the site administrator"
message_cannot_set_password = "Unable to set password, please check password rules: " \
                              "<UL><LI>the password must contain an uppercase letter" \
                              "<LI>the password must contain a lowercase letter" \
                              "<LI>the password must contain a number" \
                              "<LI>both passwords must match" \
                              "<LI>passwords cannot be empty" \
                              "<LI>password length must be at least 11 characters</UL>"
email_message_confirmation = 'Subject: Confirm your e-mail and create login  \n\n' \
                   'Welcome to Reservatron. Please confirm that you have ' \
                   'created an account with us by following the link below. \n\n' \
                   '<a href="http://localhost:5000/resetpassword?reset_code=<reset_code>&email=' \
                   + '<email_address>">. ' \
                                      'CONFIRM ACCOUNT </a> \n\n' \
                                      'If the link does not work, please copy paste the following url in your browser: \n' \
                                     'http://localhost:5000/resetpassword?reset_code=<reset_code>&email=<email_address>\n\n' \
                                    'Thanks for using Reservatron.\n\n' \
                                    'Reservatron '