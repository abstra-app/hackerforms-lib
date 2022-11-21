metadata = {
    "file-input": {
        "name": "FileInput",
        "libFunc": "read_file",
        "type": "file-input",
        "description": "Read a file value from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
            "multiple": {"type": "boolean"},
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "initialValue": {
                "type": ["string", "array"],
                "description": "The initial value of the input",
                "default": "",
            },
        },
    },
    "image-input": {
        "name": "ImageInput",
        "libFunc": "read_image",
        "type": "image-input",
        "description": "",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "initialValue": {
                "type": ["string", "array"],
                "description": "The initial value of the input",
                "items": {"type": "string"},
            },
            "multiple": {
                "type": "boolean",
                "description": "Whether the input accepts multiple values or not",
            },
        },
    },
    "video-input": {
        "name": "VideoInput",
        "libFunc": "read_video",
        "type": "video-input",
        "description": "",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "initialValue": {
                "type": ["string", "array"],
                "description": "The initial value of the input",
                "items": {"type": "string"},
            },
            "multiple": {
                "type": "boolean",
                "description": "Whether the input accepts multiple values or not",
            },
        },
    },
    "text-input": {
        "name": "TextInput",
        "libFunc": "read_text",
        "type": "text-input",
        "description": "Read a text value from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "initialValue": {
                "type": "string",
                "description": "The initial value of the input",
                "default": "",
            },
            "placeholder": {
                "type": "string",
                "description": "The placeholder text to display in the input",
                "default": "Your answer here",
            },
            "mask": {
                "type": "string",
                "description": "A mask to apply to the input",
                "default": None,
            },
        },
    },
    "textarea-input": {
        "name": "TextareaInput",
        "libFunc": "read_textarea",
        "type": "textarea-input",
        "description": "Read a textarea value from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "initialValue": {
                "type": "string",
                "description": "The initial value of the input",
                "default": "",
            },
            "placeholder": {
                "type": "string",
                "description": "The placeholder text to display in the input",
                "default": "Your answer here",
            },
        },
    },
    "tag-input": {
        "name": "TagInput",
        "libFunc": "read_tag",
        "type": "tag-input",
        "description": "Read a tag value from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "initialValue": {
                "type": ["array", "null"],
                "description": "The initial value of the input",
                "items": {"type": ["string", "number"]},
                "default": [""],
            },
            "placeholder": {
                "type": "string",
                "description": "The placeholder text to display in the input",
                "default": "Your answer here",
            },
        },
    },
    "number-input": {
        "name": "NumberInput",
        "libFunc": "read_number",
        "type": "number-input",
        "description": "Read a number value from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "initialValue": {
                "type": "number",
                "description": "The initial value of the input",
                "default": 0,
            },
            "min": {"type": "number", "description": "The minimum value of the input"},
            "max": {"type": "number", "description": "The maximun value of the input"},
            "step": {"type": "number", "description": "The step for the input"},
            "placeholder": {
                "type": "string",
                "description": "The placeholder text to display in the input",
                "default": "Your answer here",
            },
        },
    },
    "email-input": {
        "name": "EmailInput",
        "libFunc": "read_email",
        "type": "email-input",
        "description": "Read an email value from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "initialValue": {
                "type": "string",
                "description": "The initial value of the input",
                "default": "",
            },
            "placeholder": {
                "type": "string",
                "description": "The placeholder text to display in the input",
                "default": "Your email here",
            },
        },
    },
    "phone-input": {
        "name": "PhoneInput",
        "libFunc": "read_phone",
        "type": "phone-input",
        "description": "Read a phone value from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "initialValue": {
                "type": "object",
                "description": "The initial value of the input",
                "properties": {
                    "countryCode": {
                        "type": "string",
                        "description": "The phone number's country code",
                    },
                    "nationalNumber": {
                        "type": "string",
                        "description": "The phone number's national number",
                    },
                },
            },
            "placeholder": {
                "type": "string",
                "description": "The placeholder text to display in the input",
                "default": "",
            },
        },
    },
    "multiple-choice-input": {
        "name": "MultipleChoiceInput",
        "libFunc": "read_multiple_choice",
        "type": "multiple-choice-input",
        "description": "Read a multiple choice value from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
            "options": {
                "type": "array",
                "description": "The options that the user can select from",
                "items": {
                    "type": ["string", "object"],
                    "properties": {
                        "key": {
                            "type": "string",
                            "description": "The key of the option on the returning object",
                        },
                        "value": {
                            "type": "any",
                            "description": "The value of the option on the returning object",
                        },
                    },
                },
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "multiple": {
                "type": "boolean",
                "description": "Whether the input should accept multiple answers",
                "default": False,
            },
            "min": {
                "type": "number",
                "description": "The minimal amount of options that should be selected",
                "default": None,
            },
            "max": {
                "type": "number",
                "description": "The maximum amount of options that should be selected",
                "default": None,
            },
            "initialValue": {
                "type": "any",
                "description": "The initial value of the input",
                "items": {"type": ["string", "number"]},
                "default": None,
            },
        },
    },
    "date-input": {
        "name": "DateInput",
        "libFunc": "read_date",
        "type": "date-input",
        "description": "Read a date value from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "initialValue": {
                "type": "string",
                "description": "The initial value of the input",
                "default": None,
            },
        },
    },
    "dropdown-input": {
        "name": "DropdownInput",
        "libFunc": "read_dropdown",
        "type": "dropdown-input",
        "description": "Read a dropdown value from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
            "options": {
                "type": "array",
                "description": "The options that the user can select from",
                "items": {
                    "type": ["string", "object"],
                    "properties": {
                        "key": {
                            "type": "string",
                            "description": "The key of the option on the returning object",
                        },
                        "value": {
                            "type": "any",
                            "description": "The value of the option on the returning object",
                        },
                    },
                },
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "initialValue": {
                "type": "any",
                "description": "The initial value of the input",
                "items": {"type": ["string", "number"]},
            },
            "placeholder": {
                "type": "string",
                "description": "The placeholder text to display in the input",
                "default": "Choose your option",
            },
            "multiple": {
                "type": "boolean",
                "description": "Whether the input should accept multiple answers",
                "default": False,
            },
        },
    },
    "list-input": {
        "name": "ListInput",
        "libFunc": "read_list",
        "type": "list-input",
        "description": "Read a list value from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "itemSchema": {"type": "any"},
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "initialValue": {"type": "array", "default": [{}]},
            "min": {
                "type": "number",
                "description": "The minimum number of items to allow",
                "default": "",
            },
            "max": {
                "type": "number",
                "description": "The maximum number of items to allow",
                "default": "",
            },
            "addButtonText": {
                "type": "string",
                "description": "The text to display on the add button",
            },
            "overloadedItemSchemas": {"type": "any"},
        },
    },
    "cards-input": {
        "name": "CardsInput",
        "libFunc": "read_cards",
        "type": "cards-input",
        "description": "Read a text value from the user simple text input",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {"type": "string", "description": "The label of the input"},
            "options": {
                "type": "array",
                "description": "The options that the user can select from",
                "items": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "image": {"type": "string"},
                        "description": {"type": "string"},
                    },
                },
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "multiple": {
                "type": "boolean",
                "description": "Whether the input can have multiple values",
                "default": False,
            },
            "searchable": {"type": "boolean", "description": "Display a search input"},
            "initialValue": {
                "type": ["object", "array", "null"],
                "description": "The initial value of the input",
                "items": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "image": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "default": None,
                },
                "properties": {
                    "title": {"type": "string"},
                    "image": {"type": "string"},
                    "description": {"type": "string"},
                },
            },
            "direction": {
                "type": "string",
                "oneOf": ["horizontal", "vertical"],
                "description": "Whether the cards direction should be 'horizontal' or 'vertical'",
                "default": "vertical",
            },
        },
    },
    "pandas-row-selection-input": {
        "name": "PandasRowSelectionInput",
        "libFunc": "read_pandas_row_selection",
        "type": "pandas-row-selection-input",
        "description": "",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "table": {
                "type": "object",
                "properties": {
                    "data": {"type": "array"},
                    "schema": {
                        "type": "object",
                        "properties": {"fields": {"type": "array"}},
                    },
                },
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
        },
    },
    "html-list-input": {
        "name": "HtmlListInput",
        "libFunc": "read_html_list",
        "type": "html-list-input",
        "description": "Read a list of html values from the user ",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {"type": "string", "description": "The label of the input"},
            "options": {
                "type": "array",
                "description": "The options that the user can select from",
                "items": {
                    "type": "object",
                    "properties": {
                        "html": {"type": "string"},
                        "value": {"type": "string"},
                    },
                },
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "multiple": {
                "type": "boolean",
                "description": "Whether the input can have multiple values",
                "default": False,
            },
            "css": {"type": "string"},
            "initialValue": {
                "type": ["object", "array", "null"],
                "description": "The initial value of the input",
                "items": {
                    "type": "object",
                    "properties": {
                        "html": {"type": "string"},
                        "value": {"type": "string"},
                    },
                    "default": None,
                },
                "properties": {"html": {"type": "string"}, "value": {"type": "string"}},
            },
        },
    },
    "time-input": {
        "name": "TimeInput",
        "libFunc": "read_time",
        "type": "time-input",
        "description": "Read a time value from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "initialValue": {
                "type": "string",
                "description": "The initial value of the input",
                "default": None,
            },
            "format": {
                "type": "string",
                "description": "The format of time options. 24hs (0-23) or ampm (0-12)",
                "default": "24hs",
            },
        },
    },
    "password-input": {
        "name": "PasswordInput",
        "libFunc": "read_password",
        "type": "password-input",
        "description": "Read a password value from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "placeholder": {
                "type": "string",
                "description": "The placeholder text to display in the input",
                "default": "Your password here",
            },
            "lowercaseRequired": {
                "type": ["boolean", "string"],
                "description": "Whether the input must have at least one lowercase character",
                "default": True,
            },
            "uppercaseRequired": {
                "type": ["boolean", "string"],
                "description": "Whether the input must have at least one uppercase character",
                "default": True,
            },
            "specialRequired": {
                "type": ["boolean", "string"],
                "description": "Whether the input must have at least one special character",
                "default": True,
            },
            "digitRequired": {
                "type": ["boolean", "string"],
                "description": "Whether the input must have at least one digit",
                "default": True,
            },
            "minLength": {
                "type": "number",
                "description": "Minimum length of the password",
                "default": 8,
            },
            "maxLength": {
                "type": ["number", "null"],
                "description": "Maximum length of the password",
                "default": None,
            },
            "size": {
                "type": ["number", "null"],
                "description": "Size of the password",
                "default": None,
            },
            "pattern": {
                "type": ["string", "null"],
                "description": "A regex pattern for the accepted password",
                "default": None,
            },
            "autocomplete": {
                "type": "string",
                "description": "Allow the user's password manager to automatically enter the password",
                "default": "current-password",
            },
        },
    },
    "code-input": {
        "name": "CodeInput",
        "libFunc": "read_code",
        "type": "code-input",
        "description": "Read a piece of code from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {"type": "string", "description": "The label of the input"},
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "language": {
                "type": "string",
                "description": "Programming language for syntax highlighting",
            },
            "initialValue": {
                "type": "string",
                "description": "The initial value of the input",
                "default": "",
            },
        },
    },
    "nps-input": {
        "name": "NpsInput",
        "libFunc": "read_nps",
        "type": "nps-input",
        "description": "Gets NPS feedback from user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {"type": "string", "description": "The label of the input"},
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "min": {
                "type": "number",
                "description": "Minimum value of NPS",
                "default": 0,
            },
            "max": {
                "type": "number",
                "description": "Maximum value of NPS",
                "default": 10,
            },
            "minHint": {
                "type": "string",
                "description": "Hint of minimum option",
                "default": "Not at all likely",
            },
            "maxHint": {
                "type": "string",
                "description": "Hint of maximum option",
                "default": "Extremely likely",
            },
            "initialValue": {
                "type": "number",
                "description": "The initial value of the input",
            },
        },
    },
    "currency-input": {
        "name": "CurrencyInput",
        "libFunc": "read_currency",
        "type": "currency-input",
        "description": "Read currency value from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
            "currency": {"type": "string", "description": "The currency to use"},
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "initialValue": {
                "type": "number",
                "description": "The initial value of the input",
                "default": "",
            },
            "min": {"type": "number", "description": "The minimum value of the input"},
            "max": {"type": "number", "description": "The maximun value of the input"},
            "step": {"type": "number", "description": "The step for the input"},
            "placeholder": {
                "type": "string",
                "description": "The placeholder text to display in the input",
                "default": "",
            },
        },
    },
    "number-slider-input": {
        "name": "NumberSliderInput",
        "libFunc": "read_number_slider",
        "type": "number-slider-input",
        "description": "Read a number value from the user",
        "params": {
            "key": {
                "type": "string",
                "description": "The key of the input on the returning object",
            },
            "label": {
                "type": "string",
                "description": "The label to display above the input",
            },
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "hint": {
                "type": ["string", "null"],
                "description": "message describing the input",
                "default": None,
            },
            "required": {
                "type": ["boolean", "string"],
                "description": "Whether the input is required or not",
                "default": True,
            },
            "initialValue": {
                "type": "number",
                "description": "The initial value of the input",
                "default": 0,
            },
            "min": {
                "type": "number",
                "description": "The minimum value of the input",
                "default": 0,
            },
            "max": {
                "type": "number",
                "description": "The maximun value of the input",
                "default": 100,
            },
            "step": {
                "type": "number",
                "description": "The step for the input",
                "default": 1,
            },
        },
    },
    "text-output": {
        "name": "TextOutput",
        "libFunc": "display_text",
        "type": "text-output",
        "description": "Display a text to the user",
        "params": {"text": {"type": "string"}},
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
        },
    },
    "markdown-output": {
        "name": "MarkdownOutput",
        "libFunc": "display_markdown",
        "type": "markdown-output",
        "description": "Display a formatted text to the user",
        "params": {"text": {"type": "string"}},
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
        },
    },
    "image-output": {
        "name": "ImageOutput",
        "libFunc": "display_image",
        "type": "image-output",
        "description": "Display an image to the user",
        "params": {"imageUrl": {"type": "string"}},
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "subtitle": {"type": "string", "default": ""},
        },
    },
    "link-output": {
        "name": "LinkOutput",
        "libFunc": "display_link",
        "type": "link-output",
        "description": "Display a link to the user",
        "params": {"linkText": {"type": "string"}, "linkUrl": {"type": "string"}},
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "sameTab": {"type": "boolean", "default": False},
        },
    },
    "file-output": {
        "name": "FileOutput",
        "libFunc": "display_file",
        "type": "file-output",
        "description": "Display a button for the user to download a file",
        "params": {"fileUrl": {"type": "string"}},
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "downloadText": {"type": "string", "default": "Download here"},
        },
    },
    "html-output": {
        "name": "HtmlOutput",
        "libFunc": "display_html",
        "type": "html-output",
        "description": "Display a html snippet to the user",
        "params": {"html": {"type": "string"}},
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
        },
    },
    "pandas-output": {
        "name": "PandasOutput",
        "libFunc": "display_pandas",
        "type": "pandas-output",
        "description": "Display a pandas dataframe to the user",
        "params": {
            "table": {
                "type": "object",
                "properties": {
                    "data": {"type": "array"},
                    "schema": {
                        "type": "object",
                        "properties": {"fields": {"type": "array"}},
                    },
                },
            },
            "displayIndex": {"type": "boolean", "default": False},
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
        },
    },
    "plotly-output": {
        "name": "PlotlyOutput",
        "libFunc": "display_plotly",
        "type": "plotly-output",
        "description": "Display a plotly figure to the user",
        "params": {"figure": {"type": "any"}},
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
        },
    },
    "iframe-output": {
        "name": "IframeOutput",
        "libFunc": "display_iframe",
        "type": "iframe-output",
        "description": "Display an inline iframe to the user",
        "params": {"url": {"type": "string"}},
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "width": {"type": "string"},
            "height": {"type": "string"},
        },
    },
    "progress-output": {
        "name": "ProgressOutput",
        "libFunc": "display_progress",
        "type": "progress-output",
        "description": "Display a progress bar. This widget is shown on screen until the script shows a new widget",
        "params": {
            "current": {"type": "number", "default": 50},
            "total": {"type": "number", "default": 100},
        },
        "optionals": {
            "columns": {
                "type": "number",
                "description": "number of columns this input will take",
            },
            "fullWidth": {
                "type": "boolean",
                "description": "Whether the widget should take up the full width of the page",
            },
            "text": {"type": "string", "default": ""},
        },
    },
}
