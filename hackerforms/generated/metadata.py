metadata = {
    "textarea-input": {
        "type": "textarea-input",
        "description": "Read a textarea value from the user",
        "pythonAPI": {
            "name": "read_textarea",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": 'The initial value to display to the user. Defaults to "".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '""',
                },
                {
                    "argName": "placeholder",
                    "description": 'The placeholder text to display to the user. Defaults to "Your answer here".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '"Your answer here"',
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [
                {"typeName": "str", "typeDescription": "The value entered by the user"}
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label of the input",
                },
                {
                    "argName": "initialValue",
                    "typeName": "string",
                    "description": "The initial value of the input",
                    "default": "",
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
                {
                    "argName": "placeholder",
                    "typeName": "string",
                    "description": "The placeholder text to display in the input",
                    "default": "Your answer here",
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "label": "What kind of things are you building with Abstra Cloud?"
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_textarea",
                "key": "example1",
                "code": 'ans = read_textarea("What kind of things are you building with Abstra Cloud?")\n',
            }
        ],
    },
    "list-input": {
        "type": "list-input",
        "description": "Read a list value from the user",
        "pythonAPI": {
            "name": "read_list",
            "params": [
                {
                    "argName": "item_schema",
                    "description": "The schema for the items of the list",
                    "typeName": "ListItemSchema",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": "The initial value to display to the user. Defaults to [{}].",
                    "typeName": "any",
                    "isKwarg": True,
                    "default": "[{}]",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "min",
                    "description": "Min value accepted by the input. Defaults to None.",
                    "typeName": "float",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "max",
                    "description": "Max value accepted by the input. Defaults to None.",
                    "typeName": "float",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "add_button_text",
                    "description": 'Label to be displayed on the add button. Defaults to "+".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '"+"',
                },
            ],
            "returns": [
                {
                    "typeName": "list",
                    "typeDescription": "The values entered by the user",
                }
            ],
        },
        "brokerAPI": {
            "params": [
                {"argName": "itemSchema", "typeName": "any", "description": ""},
                {
                    "argName": "initialValue",
                    "typeName": "array",
                    "description": "",
                    "default": [{}],
                    "isOptional": True,
                },
                {
                    "argName": "min",
                    "typeName": "number",
                    "description": "The minimum number of items to allow",
                    "default": "",
                    "isOptional": True,
                },
                {
                    "argName": "max",
                    "typeName": "number",
                    "description": "The maximum number of items to allow",
                    "default": "",
                    "isOptional": True,
                },
                {
                    "argName": "addButtonText",
                    "typeName": "string",
                    "description": "The text to display on the add button",
                    "isOptional": True,
                },
                {
                    "argName": "overloadedItemSchemas",
                    "typeName": "any",
                    "description": "",
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "initialValue": [{}],
                    "min": 1,
                    "max": 3,
                    "itemSchema": [
                        {
                            "hint": None,
                            "initialValue": "",
                            "key": "Name",
                            "label": "Name",
                            "placeholder": "Your answer here",
                            "required": True,
                            "type": "text-input",
                        },
                        {
                            "hint": None,
                            "initialValue": "",
                            "key": "Email",
                            "label": "Email",
                            "placeholder": "Your answer here",
                            "required": True,
                            "type": "email-input",
                        },
                    ],
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_list",
                "key": "example1",
                "code": "item = ListItemSchema().read(\"Name\").read_email(\"Email\")\nans = read_list(item, min=1, max=3)\n# ans = [{'Name': '', 'Email': ''}]\n",
            }
        ],
    },
    "video-input": {
        "type": "video-input",
        "description": "Read a video file value from the user",
        "pythonAPI": {
            "name": "read_video",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": 'The initial value to display to the user. Defaults to "".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '""',
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "multiple",
                    "description": "Whether the user will be allowed to upload multiple files. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [
                {
                    "typeName": "FileResponse or FileResponse[]",
                    "typeDescription": 'A dict containing the video uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of videos in case of multiple flag set as True',
                }
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label of the input",
                },
                {
                    "argName": "initialValue",
                    "typeName": ["string", "array"],
                    "description": "The initial value of the input",
                    "items": {"typeName": "string"},
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
                {
                    "argName": "multiple",
                    "typeName": "boolean",
                    "description": "Whether the input accepts multiple values or not",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {"label": "Upload your video"},
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_video",
                "key": "example1",
                "code": 'fileResponse = read_video("Upload your video")\nfile = fileResponse.file  # File object\nurl = fileResponse.url  # Url to the file\ncontent = fileResponse.content  # Raw file content\n',
            }
        ],
    },
    "tag-input": {
        "type": "tag-input",
        "description": "Read a tag value from the user",
        "pythonAPI": {
            "name": "read_tag",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": "The initial value to display to the user. Defaults to [].",
                    "typeName": "list",
                    "isKwarg": True,
                    "default": "[]",
                },
                {
                    "argName": "placeholder",
                    "description": 'The placeholder text to display to the user. Defaults to "Your answer here".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '"Your answer here"',
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [
                {
                    "typeName": None,
                    "typeDescription": "list(str) or list(float): The value entered by the user",
                }
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label of the input",
                },
                {
                    "argName": "initialValue",
                    "typeName": ["array", "null"],
                    "description": "The initial value of the input",
                    "default": [""],
                    "items": {"typeName": ["string", "number"]},
                    "isOptional": True,
                },
                {
                    "argName": "placeholder",
                    "typeName": "string",
                    "description": "The placeholder text to display in the input",
                    "default": "Your answer here",
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "label": "Type and press enter to add a tag",
                    "initialValue": ["Red", "Green", "Blue"],
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_tag",
                "key": "example1",
                "code": 'ans = read_tag(\n    "Type and press enter to add a tag", initial_value=["Red", "Green", "Blue"]\n)\n# ans = ["Red", "Green" or "Blue"]`\n',
            }
        ],
    },
    "time-input": {
        "type": "time-input",
        "description": "Read a time value from the user",
        "pythonAPI": {
            "name": "read_time",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": 'The initial value to display to the user. Defaults to "".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '""',
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "format",
                    "description": 'Whether the input is in the format 24hs or AM/PM. Defaults to "24hs".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '"24hs"',
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [
                {
                    "typeName": "datetime.time",
                    "typeDescription": "A datetime.time object representing the value entered by the user",
                }
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label of the input",
                },
                {
                    "argName": "initialValue",
                    "typeName": "string",
                    "description": "The initial value of the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "format",
                    "typeName": "string",
                    "description": "The format of time options. 24hs (0-23) or ampm (0-12)",
                    "default": "24hs",
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {"label": "Select a time below"},
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_time",
                "key": "example1",
                "code": 'ans = read_time("Select a time below")\n# ans = 00:00:00\n',
            }
        ],
    },
    "number-slider-input": {
        "type": "number-slider-input",
        "description": "Read a number value from the user",
        "pythonAPI": {
            "name": "read_number_slider",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": "The initial value to display to the user. Defaults to 0.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "0",
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "min",
                    "description": "Min value accepted by the input. Defaults to None.",
                    "typeName": "float",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "max",
                    "description": "Max value accepted by the input. Defaults to None.",
                    "typeName": "float",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "step",
                    "description": "The value to be incremented or decremented while using the input button. Defaults to None.",
                    "typeName": "float",
                    "isKwarg": True,
                    "default": "None",
                },
            ],
            "returns": [
                {
                    "typeName": "float",
                    "typeDescription": "The value entered by the user",
                }
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "min",
                    "typeName": "number",
                    "description": "The minimum value of the input",
                    "isOptional": True,
                },
                {
                    "argName": "max",
                    "typeName": "number",
                    "description": "The maximun value of the input",
                    "isOptional": True,
                },
                {
                    "argName": "step",
                    "typeName": "number",
                    "description": "The step for the input",
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
                {
                    "argName": "placeholder",
                    "typeName": "string",
                    "description": "The placeholder text to display in the input",
                },
            ]
        },
        "examples": [
            {
                "props": {"label": "Set volume"},
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_number",
                "key": "example1",
                "code": 'age = read_number_slider("Set volume")\n',
            }
        ],
    },
    "text-input": {
        "type": "text-input",
        "description": "Read a text value from the user",
        "pythonAPI": {
            "name": "read",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": 'The initial value to display to the user. Defaults to "".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '""',
                },
                {
                    "argName": "placeholder",
                    "description": 'The placeholder text to display to the user. Defaults to "Your answer here".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '"Your answer here"',
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "mask",
                    "description": "A mask to apply to the input. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
            ],
            "returns": [
                {"typeName": "str", "typeDescription": "The value entered by the user"}
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label of the input",
                },
                {
                    "argName": "initialValue",
                    "typeName": "string",
                    "description": "The initial value of the input",
                    "default": "",
                    "isOptional": True,
                },
                {
                    "argName": "mask",
                    "typeName": "string",
                    "description": "A mask to apply to the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
                {
                    "argName": "placeholder",
                    "typeName": "string",
                    "description": "The placeholder text to display in the input",
                    "default": "Your answer here",
                },
            ]
        },
        "examples": [
            {
                "props": {"label": "What is your name?"},
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read",
                "key": "example1",
                "code": 'name = read("What is your name?")\n',
            },
            {
                "props": {
                    "label": "What is your credit card number?",
                    "mask": "0000 0000 0000 0000",
                },
                "name": "Mask Example",
                "description": "The following example shows the usage of the mask property for read widget. In the mask property, the '0' digit represents a numeric value, the 'a' digit represents an alphabetic value and other digits are recognized as part of the value",
                "key": "example2",
                "code": 'read("What is your credit card number?", mask="0000 0000 0000 0000")\n',
            },
        ],
    },
    "phone-input": {
        "type": "phone-input",
        "description": "Read a phone value from the user",
        "pythonAPI": {
            "name": "read_phone",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": "The initial value to display to the user. If dictionary, it contains two keys: 'country_code' (string with optional + sign or number) and 'national_number' (str or number). Ex: {'country_code': '+55', 'national_number': '21999990000'}. Defaults to \"\".",
                    "typeName": "str or dict",
                    "isKwarg": True,
                    "default": '""',
                },
                {
                    "argName": "placeholder",
                    "description": 'The placeholder text to display to the user. Defaults to "".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '""',
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [
                {
                    "typeName": "PhoneResponse",
                    "typeDescription": 'A dict containing the value entered by the user ({"raw": str, "masked": str})',
                }
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label of the input",
                },
                {
                    "argName": "initialValue",
                    "typeName": "object",
                    "description": "The initial value of the input",
                    "isOptional": True,
                    "properties": [
                        {
                            "argName": "countryCode",
                            "typeName": "string",
                            "description": "The phone number's country code",
                        },
                        {
                            "argName": "nationalNumber",
                            "typeName": "string",
                            "description": "The phone number's national number",
                        },
                    ],
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
                {
                    "argName": "placeholder",
                    "typeName": "string",
                    "description": "The placeholder text to display in the input",
                    "default": "",
                },
            ]
        },
        "examples": [
            {
                "props": {"label": "What is your phone number?"},
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_phone",
                "key": "example1",
                "code": 'phone = read_phone("What is your phone number?")\nnumber = phone.raw  # eg: 5521999999999\nmasked = phone.masked  # eg: +55 (21) 99999-9999\n',
            }
        ],
    },
    "image-input": {
        "type": "image-input",
        "description": "Read a image file value from the user ",
        "pythonAPI": {
            "name": "read_image",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": 'The initial value to display to the user. Defaults to "".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '""',
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "multiple",
                    "description": "Whether the user will be allowed to upload multiple files. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [
                {
                    "typeName": "FileResponse or FileResponse[]",
                    "typeDescription": 'A dict containing the image file uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of images in case of multiple flag set as True',
                }
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label to display above the input",
                },
                {
                    "argName": "initialValue",
                    "typeName": ["string", "array"],
                    "description": "The initial value of the input",
                    "default": "",
                    "isOptional": True,
                    "items": {"typeName": "string"},
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
                {
                    "argName": "multiple",
                    "typeName": "boolean",
                    "description": "Whether the input accepts multiple values or not",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {"label": "Upload your .png image"},
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_image",
                "key": "example1",
                "code": 'fileResponse = read_image("Upload your .png image")\nfile = fileResponse.file  # File object\nurl = fileResponse.url  # Url to the file\ncontent = fileResponse.content  # Raw file content\n',
            }
        ],
    },
    "email-input": {
        "type": "email-input",
        "description": "Read an email value from the user",
        "pythonAPI": {
            "name": "read_email",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": 'The initial value to display to the user. Defaults to "".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '""',
                },
                {
                    "argName": "placeholder",
                    "description": 'The placeholder text to display to the user. Defaults to "Your email here".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '"Your email here"',
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "invalid_email_message",
                    "typeName": "str",
                    "description": "Invalid e-mail message",
                    "isKwarg": True,
                    "default": "Hmm… doesn't look like an email",
                },
            ],
            "returns": [
                {"typeName": "str", "typeDescription": "The value entered by the user"}
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label to display above the input",
                },
                {
                    "argName": "invalidEmailMessage",
                    "typeName": "string",
                    "description": "Invalid e-mail message",
                    "default": "Hmm… doesn't look like an email",
                },
                {
                    "argName": "initialValue",
                    "typeName": "string",
                    "description": "The initial value of the input",
                    "default": "",
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
                {
                    "argName": "placeholder",
                    "typeName": "string",
                    "description": "The placeholder text to display in the input",
                },
            ]
        },
        "examples": [
            {
                "props": {"label": "What is your email?"},
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_email",
                "key": "example1",
                "code": 'email = read_email("What is your email?")\n',
            }
        ],
    },
    "multiple-choice-input": {
        "type": "multiple-choice-input",
        "description": "Read a multiple choice value from the user",
        "pythonAPI": {
            "name": "read_multiple_choice",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "options",
                    "description": "TN options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]",
                    "typeName": "list",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "multiple",
                    "description": "Whether the user can select multiple options. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "min",
                    "description": "The minimal amount of options that should be selected. Defaults to None.",
                    "typeName": "number",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "max",
                    "description": "The maximum amount of options that should be selected. Defaults to None.",
                    "typeName": "number",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "initial_value",
                    "description": "The initial value to display to the user. Defaults to None.",
                    "typeName": None,
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "required",
                    "description": 'WNther the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [
                {
                    "typeName": None,
                    "typeDescription": "list or any: The values/value selected by the user",
                }
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label to display above the input",
                },
                {
                    "argName": "multiple",
                    "typeName": "boolean",
                    "description": "Whether the input should accept multiple answers",
                    "default": False,
                    "isOptional": True,
                },
                {
                    "argName": "initialValue",
                    "typeName": "any",
                    "description": "The initial value of the input",
                    "items": {"typeName": ["string", "number"]},
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "min",
                    "typeName": "number",
                    "description": "The minimum number of items to allow",
                    "default": "",
                    "isOptional": True,
                },
                {
                    "argName": "max",
                    "typeName": "number",
                    "description": "The maximum number of items to allow",
                    "default": "",
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
                {
                    "argName": "options",
                    "typeName": "array",
                    "description": "The options that the user can select from",
                    "items": {
                        "typeName": ["string", "object"],
                        "properties": [
                            {
                                "argName": "key",
                                "typeName": "string",
                                "description": "The key of the option on the returning object",
                            },
                            {
                                "argName": "value",
                                "typeName": "any",
                                "description": "The value of the option on the returning object",
                            },
                        ],
                    },
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "label": "Which programming language do you prefer?",
                    "options": ["Python", "JavaScript"],
                },
                "name": "Basic Example",
                "description": "Basic use of read_multiple_choice",
                "key": "example1",
                "code": 'ans = read_multiple_choice(\n    "Which programming language do you prefer?",\n    ["Python", "JavaScript"],\n)\n# ans = "Python" or "JavaScript"\n',
            },
            {
                "props": {
                    "label": "Which programming language do you prefer?",
                    "options": ["Python", "JavaScript"],
                },
                "name": "Label and value dict",
                "description": "Use a dictionary to specify the label and value of each option. The label will be displayed to the user, and the value will be returned by the widget.",
                "key": "example2",
                "code": 'ans = read_multiple_choice(\n    "Which programming language do you prefer?",\n    [{"label": " Python", "value": "py"}, {"label": "JavaScript", "value": "js"}],\n)\n# ans = "py" or "js"\n',
            },
            {
                "props": {
                    "label": "What features do you love?",
                    "options": ["forms", "jobs", "hooks"],
                    "multiple": True,
                },
                "name": "Checkboxes",
                "description": "Use `multiple=true` when you want allow users to select more than one option. This will make it returns a list.",
                "key": "example3",
                "code": 'ans = read_multiple_choice(\n    "What features do you love?", ["forms", "jobs", "hooks"], multiple=True\n)\n# ans = ["forms", "jobs", "hooks"]\n',
            },
        ],
    },
    "code-input": {
        "type": "code-input",
        "description": "Read a piece of code from the user",
        "pythonAPI": {
            "name": "read_code",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": 'The initial value to display to the user. Defaults to "".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '""',
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "language",
                    "description": "The programming language. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [
                {"typeName": "str", "typeDescription": "The value entered by the user"}
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label of the input",
                },
                {
                    "argName": "language",
                    "typeName": "string",
                    "description": "Programming language for syntax highlighting",
                    "isOptional": True,
                },
                {
                    "argName": "initialValue",
                    "typeName": "string",
                    "description": "The initial value of the input",
                    "default": "",
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "label": "Show me the code!",
                    "language": "c",
                    "initialValue": '#include<stdio.h>\nint main(int argc, char** argv) {\nchar name[256];\nscanf("%s", name);\nprintf("%s, here is", name);\n}',
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_code",
                "key": "example1",
                "code": 'ans = read_code("Show me the code!", language="c")\n',
            }
        ],
    },
    "date-input": {
        "type": "date-input",
        "description": "Read a date value from the user",
        "pythonAPI": {
            "name": "read_date",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": "The initial value to display to the user. Defaults to None.",
                    "typeName": "datetime.date or time.struct_time or str (YYYY-MM-DD)",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [
                {
                    "typeName": "datetime.date",
                    "typeDescription": "The value entered by the user",
                }
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label to display above the input",
                },
                {
                    "argName": "initialValue",
                    "typeName": "string",
                    "description": "The initial value of the input",
                    "default": None,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {"label": "When were you born?"},
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_date",
                "key": "example1",
                "code": 'birthday = read_date("When were you born?")\nyear = birthday.year\nmonth = birthday.month\nday = birthday.day\n',
            }
        ],
    },
    "password-input": {
        "type": "password-input",
        "description": "Read a password value from the user",
        "pythonAPI": {
            "name": "read_password",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "placeholder",
                    "description": 'The placeholder text to display to the user. Defaults to "".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '""',
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "lowercase_required",
                    "description": "Whether the input must have at least one lowercase character. Defaults to True.",
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "uppercase_required",
                    "description": "Whether the input must have at least one uppercase character. Defaults to True.",
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "special_required",
                    "description": "Whether the input must have at least one special character. Defaults to True.",
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "digit_required",
                    "description": "Whether the input must have at least one digit. Defaults to True.",
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "min_length",
                    "description": "Minimum length of the password. Defaults to 8.",
                    "typeName": "int",
                    "isKwarg": True,
                    "default": "8",
                },
                {
                    "argName": "max_length",
                    "description": "Maximum length of the password. Defaults to None.",
                    "typeName": "int",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "size",
                    "description": "Size of the password. Defaults to None.",
                    "typeName": "int",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "pattern",
                    "description": "A regex pattern for the accepted password. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "autocomplete",
                    "description": 'The autocomplete HTML attribute. Defaults to "current-password".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '"current-password"',
                },
            ],
            "returns": [
                {"typeName": "str", "typeDescription": "The value entered by the user"}
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label of the input",
                },
                {
                    "argName": "lowercaseRequired",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input must have at least one lowercase character",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "uppercaseRequired",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input must have at least one uppercase character",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "specialRequired",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input must have at least one special character",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "digitRequired",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input must have at least one digit",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "minLength",
                    "typeName": "number",
                    "description": "Minimum length of the password",
                    "default": 8,
                    "isOptional": True,
                },
                {
                    "argName": "maxLength",
                    "typeName": ["number", "null"],
                    "description": "Maximum length of the password",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "size",
                    "typeName": ["number", "null"],
                    "description": "Size of the password",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "pattern",
                    "typeName": ["string", "null"],
                    "description": "A regex pattern for the accepted password",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "autocomplete",
                    "typeName": "string",
                    "description": "Allow the user's password manager to automatically enter the password",
                    "default": "current-password",
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
                {
                    "argName": "placeholder",
                    "typeName": "string",
                    "description": "The placeholder text to display in the input",
                },
            ]
        },
        "examples": [
            {
                "props": {"label": "Insert your password below"},
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_password",
                "key": "example1",
                "code": 'ans = read_password("Insert your password below")\n',
            }
        ],
    },
    "number-input": {
        "type": "number-input",
        "description": "Read a number value from the user",
        "pythonAPI": {
            "name": "read_number",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": "The initial value to display to the user. Defaults to 0.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "0",
                },
                {
                    "argName": "placeholder",
                    "description": 'The placeholder text to display to the user. Defaults to "Your answer here".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '"Your answer here"',
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "min",
                    "description": "Min value accepted by the input. Defaults to None.",
                    "typeName": "float",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "max",
                    "description": "Max value accepted by the input. Defaults to None.",
                    "typeName": "float",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "step",
                    "description": "The value to be incremented or decremented while using the input button. Defaults to None.",
                    "typeName": "float",
                    "isKwarg": True,
                    "default": "None",
                },
            ],
            "returns": [
                {
                    "typeName": "float",
                    "typeDescription": "The value entered by the user",
                }
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label to display above the input",
                },
                {
                    "argName": "initialValue",
                    "typeName": "number",
                    "description": "The initial value of the input",
                    "isOptional": True,
                },
                {
                    "argName": "min",
                    "typeName": "number",
                    "description": "The minimum value of the input",
                    "isOptional": True,
                },
                {
                    "argName": "max",
                    "typeName": "number",
                    "description": "The maximun value of the input",
                    "isOptional": True,
                },
                {
                    "argName": "step",
                    "typeName": "number",
                    "description": "The step for the input",
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
                {
                    "argName": "placeholder",
                    "typeName": "string",
                    "description": "The placeholder text to display in the input",
                    "default": "Your answer here",
                },
            ]
        },
        "examples": [
            {
                "props": {"label": "How old are you?"},
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_number",
                "key": "example1",
                "code": 'age = read_number("How old are you?")\n',
            }
        ],
    },
    "cards-input": {
        "type": "cards-input",
        "description": "Read a text value from the user simple text input",
        "pythonAPI": {
            "name": "read_cards",
            "params": [
                {
                    "argName": "label",
                    "description": "The text related to this field",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "options",
                    "description": "The options to display to the user, eg. [\n{'title': 'Option 1', 'image': 'https://image_1.png', 'description': 'option 1 description'},\n{'title': 'Option 2', 'image': 'https://image_2.png', 'description': 'option 2 description'}]",
                    "typeName": "list",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "multiple",
                    "description": "Whether the user can select multiple options. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "initial_value",
                    "description": "The initial value to display to the user. Defaults to None.",
                    "typeName": "list",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "searchable",
                    "description": "Whether to show a search bar. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "direction",
                    "description": "Whether the cards direction should be 'horizontal' or 'vertical'. Defaults to 'vertical'.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "'vertical'",
                },
            ],
            "returns": [
                {
                    "typeName": None,
                    "typeDescription": "list, any: The options/option selected by the user",
                }
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label of the input",
                },
                {
                    "argName": "options",
                    "typeName": "array",
                    "description": "The options that the user can select from",
                    "items": {
                        "typeName": "object",
                        "properties": [
                            {
                                "argName": "title",
                                "typeName": "string",
                                "description": "",
                            },
                            {
                                "argName": "image",
                                "typeName": "string",
                                "description": "",
                            },
                            {
                                "argName": "description",
                                "typeName": "string",
                                "description": "",
                            },
                        ],
                    },
                },
                {
                    "argName": "multiple",
                    "typeName": "boolean",
                    "description": "Whether the input can have multiple values",
                    "default": False,
                    "isOptional": True,
                },
                {
                    "argName": "searchable",
                    "typeName": "boolean",
                    "description": "Display a search input",
                    "isOptional": True,
                },
                {
                    "argName": "initialValue",
                    "typeName": ["object", "array", "null"],
                    "description": "The initial value of the input",
                    "isOptional": True,
                    "items": {
                        "typeName": "object",
                        "properties": [
                            {
                                "argName": "title",
                                "typeName": "string",
                                "description": "",
                            },
                            {
                                "argName": "image",
                                "typeName": "string",
                                "description": "",
                            },
                            {
                                "argName": "description",
                                "typeName": "string",
                                "description": "",
                            },
                        ],
                        "default": None,
                    },
                },
                {
                    "argName": "direction",
                    "typeName": "string",
                    "description": "Whether the cards direction should be 'horizontal' or 'vertical'",
                    "oneOf": ["horizontal", "vertical"],
                    "default": "vertical",
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "label": "Choose your character",
                    "options": [
                        {
                            "title": "Charmander",
                            "image": "https://img.pokemondb.net/sprites/sword-shield/icon/charmander.png",
                            "description": "Fire",
                        },
                        {
                            "title": "Bulbasaur",
                            "image": "https://img.pokemondb.net/sprites/sword-shield/icon/bulbasaur.png",
                            "description": "Grass",
                        },
                        {
                            "title": "Squirtle",
                            "image": "https://img.pokemondb.net/sprites/sword-shield/icon/squirtle.png",
                            "description": "Water",
                        },
                    ],
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_cards",
                "key": "example1",
                "code": 'card = read_cards(\n    "Choose your character",\n    [\n        {\n            "title": "Charmander",\n            "image": "https://img.pokemondb.net/sprites/sword-shield/icon/charmander.png",\n            "description": "Fire",\n        },\n        {\n            "title": "Bulbasaur",\n            "image": "https://img.pokemondb.net/sprites/sword-shield/icon/bulbasaur.png",\n            "description": "Grass",\n        },\n        {\n            "title": "Squirtle",\n            "image": "https://img.pokemondb.net/sprites/sword-shield/icon/squirtle.png",\n            "description": "Water",\n        },\n    ],\n)\n# card = { \'title\': ..., \'image\': ..., \'description\': ... }\n',
            }
        ],
    },
    "nps-input": {
        "type": "nps-input",
        "description": "Gets NPS feedback from user",
        "pythonAPI": {
            "name": "read_nps",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "min",
                    "description": "Min value accepted by the input. Defaults to 0.",
                    "typeName": "int",
                    "isKwarg": True,
                    "default": "0",
                },
                {
                    "argName": "max",
                    "description": "Max value accepted by the input. Defaults to 10.",
                    "typeName": "int",
                    "isKwarg": True,
                    "default": "10",
                },
                {
                    "argName": "min_hint",
                    "description": 'Text to display next to the min value. Defaults to "Not at all likely".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '"Not at all likely"',
                },
                {
                    "argName": "max_hint",
                    "description": 'Text to display next to the max value. Defaults to "Extremely likely".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '"Extremely likely"',
                },
                {
                    "argName": "initial_value",
                    "description": "The initial value to display to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [
                {"typeName": "int", "typeDescription": "The value entered by the user"}
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "min",
                    "typeName": "number",
                    "description": "Minimum value of NPS",
                    "default": 0,
                    "isOptional": True,
                },
                {
                    "argName": "max",
                    "typeName": "number",
                    "description": "Maximum value of NPS",
                    "default": 10,
                    "isOptional": True,
                },
                {
                    "argName": "minHint",
                    "typeName": "string",
                    "description": "Hint of minimum option",
                    "default": "Not at all likely",
                    "isOptional": True,
                },
                {
                    "argName": "maxHint",
                    "typeName": "string",
                    "description": "Hint of maximum option",
                    "default": "Extremely likely",
                    "isOptional": True,
                },
                {
                    "argName": "initialValue",
                    "typeName": "number",
                    "description": "The initial value of the input",
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "label": "How likely are you to recommend Abstra Cloud?",
                    "minHint": "No way!",
                    "maxHint": "Hell yeah!",
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_nps",
                "key": "example1",
                "code": 'ans = read_nps(\n    "How likely are you to recommend Abstra Cloud?",\n    min_hint="No way!",\n    max_hint="Hell yeah!",\n)\n',
            }
        ],
    },
    "currency-input": {
        "type": "currency-input",
        "description": "Read currency value from the user",
        "pythonAPI": {
            "name": "read_currency",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": "The initial value to display to the user. Defaults to 0.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "0",
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not, eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "placeholder",
                    "description": 'The placeholder text to display to the user. Defaults to "Your answer here".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '"Your answer here"',
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "min",
                    "description": 'The minimum value allowed, eg. "0". Defaults to None.',
                    "typeName": "float",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "max",
                    "description": 'The maximum value allowed, eg. "100". Defaults to None.',
                    "typeName": "float",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "step",
                    "description": "The value to be incremented or decremented while using the input button. Defaults to None.",
                    "typeName": "float",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "currency",
                    "description": 'The currency to display to the user, eg. "USD", "BRL, "EUR", "GBP". Defaults to "USD".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '"USD"',
                },
            ],
            "returns": [
                {
                    "typeName": "float",
                    "typeDescription": "The value entered by the user",
                }
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label to display above the input",
                },
                {
                    "argName": "currency",
                    "typeName": "string",
                    "description": "The currency to use",
                },
                {
                    "argName": "initialValue",
                    "typeName": "number",
                    "description": "The initial value of the input",
                    "default": "",
                    "isOptional": True,
                },
                {
                    "argName": "min",
                    "typeName": "number",
                    "description": "The minimum value of the input",
                    "isOptional": True,
                },
                {
                    "argName": "max",
                    "typeName": "number",
                    "description": "The maximun value of the input",
                    "isOptional": True,
                },
                {
                    "argName": "step",
                    "typeName": "number",
                    "description": "The step for the input",
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
                {
                    "argName": "placeholder",
                    "typeName": "string",
                    "description": "The placeholder text to display in the input",
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "label": "How many credits do you want?",
                    "initialValue": 10,
                    "min": 10,
                    "currency": "USD",
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_currency",
                "key": "example1",
                "code": 'read_currency(\n    f"How many credits do you want?", currency="USD", initial_value=10, min=10\n)\n',
            }
        ],
    },
    "file-input": {
        "type": "file-input",
        "description": "Read a file value from the user",
        "pythonAPI": {
            "name": "read_file",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": 'The initial value to display to the user. Defaults to "".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '""',
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "multiple",
                    "description": "Whether the user will be allowed to upload multiple files. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [
                {
                    "typeName": "FileResponse or FileResponse[]",
                    "typeDescription": 'A dict containing the file uploaded by the user ({"file": file, "url": str, "content": bytes}) or a list of files in case of multiple flag set as True',
                }
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label to display above the input",
                },
                {
                    "argName": "initialValue",
                    "typeName": ["string", "array"],
                    "description": "The initial value of the input",
                    "default": "",
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {"label": "Upload your .xlsx file"},
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_file",
                "key": "example1",
                "code": 'fileResponse = read_file("Upload your .xlsx file")\nfile = fileResponse.file  # File object\nurl = fileResponse.url  # Url to the file\ncontent = fileResponse.content  # Raw file content\n',
            }
        ],
    },
    "rating-input": {
        "type": "rating-input",
        "description": "Read a rating value from the user",
        "pythonAPI": {
            "name": "read_rating",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "initial_value",
                    "description": "The initial value to display to the user. Defaults to 0.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "0",
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "max",
                    "description": "Max value accepted by the input. Defaults to None.",
                    "typeName": "float",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "char",
                    "description": "Which char should be displayed as icon?",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": None,
                },
            ],
            "returns": [
                {
                    "typeName": "float",
                    "typeDescription": "The value entered by the user",
                }
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label of the input",
                },
                {
                    "argName": "initialValue",
                    "typeName": "number",
                    "description": "The initial value of the input",
                    "default": 0,
                    "isOptional": True,
                },
                {
                    "argName": "max",
                    "typeName": "number",
                    "description": "The maximum value of the input",
                    "default": 5,
                    "isOptional": True,
                },
                {
                    "argName": "char",
                    "typeName": "string",
                    "description": "Which char should be displayed as icon?",
                    "default": "⭐",
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {"label": "How much do you rate this movie?"},
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_rating",
                "key": "example1",
                "code": 'read_rating("How do you rate this movie?")\n',
            },
            {
                "props": {
                    "label": "How do you evaluate your Python skills?",
                    "char": "🐍",
                    "max": 3,
                },
                "name": "Custom chars and number of points",
                "description": "The following example demonstrate some of the available functionality for read_rating",
                "key": "example2",
                "code": 'read_rating("How much do you rate this movie?", char="🐍", max=3)\n',
            },
        ],
    },
    "dropdown-input": {
        "type": "dropdown-input",
        "description": "Read a dropdown value from the user",
        "pythonAPI": {
            "name": "read_dropdown",
            "params": [
                {
                    "argName": "label",
                    "description": "The label to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "options",
                    "description": "The options to display to the user, eg. ['Option 1', 'Option 2'] or [{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}]",
                    "typeName": "list",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "multiple",
                    "description": "Whether the user can select multiple options. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "initial_value",
                    "description": "The initial value to display to the user. Defaults to None.",
                    "typeName": None,
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "placeholder",
                    "description": 'The placeholder text to display to the user. Defaults to "Choose an option".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '"Choose an option"',
                },
                {
                    "argName": "required",
                    "description": 'Whether the input is required or not eg. "this field is required". Defaults to True.',
                    "typeName": "bool or str",
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [
                {"typeName": "str", "typeDescription": "The value selected by the user"}
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "label",
                    "typeName": "string",
                    "description": "The label to display above the input",
                },
                {
                    "argName": "initialValue",
                    "typeName": "any",
                    "description": "The initial value of the input",
                    "items": {"typeName": ["string", "number"]},
                    "isOptional": True,
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
                {
                    "argName": "options",
                    "typeName": "array",
                    "description": "The options that the user can select from",
                    "items": {
                        "typeName": ["string", "object"],
                        "properties": [
                            {
                                "argName": "key",
                                "typeName": "string",
                                "description": "The key of the option on the returning object",
                            },
                            {
                                "argName": "value",
                                "typeName": "any",
                                "description": "The value of the option on the returning object",
                            },
                        ],
                    },
                },
                {
                    "argName": "placeholder",
                    "typeName": "string",
                    "description": "The placeholder text to display in the input",
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "label": "Choose a color",
                    "options": ["Red", "Green", "Blue"],
                },
                "name": "Basic Example",
                "description": "Basic use of read_dropdown",
                "key": "example1",
                "code": 'ans = read_dropdown(\n    "Choose a color",\n    ["Red", "Green", "Blue"],\n)\n# ans = "Red", "Green" or "Blue"\n',
            },
            {
                "props": {
                    "label": "Choose a color",
                    "options": ["Red", "Green", "Blue"],
                },
                "name": "Label and value dict",
                "description": "Use a dictionary to specify the label and value of each option. The label will be displayed to the user, and the value will be returned by the widget.",
                "key": "example2",
                "code": 'ans = read_dropdown(\n    "Choose a color",\n    [\n        {"label": "Red", "value": "R"},\n        {"label": "Green", "value": "G"},\n        {"label": "Blue", "value": "B"},\n    ],\n)\n# ans = "R", "G" or "B"\n',
            },
        ],
    },
    "pandas-row-selection-input": {
        "type": "pandas-row-selection-input",
        "description": "Display a pandas dataframe as a table and allow the user to select rows",
        "pythonAPI": {
            "name": "read_pandas_row_selection",
            "params": [
                {
                    "argName": "df",
                    "description": "The pandas dataframe to be displayed",
                    "typeName": "pandas.DataFrame",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "required",
                    "description": "Whether the input is required or not. Defaults to True.",
                    "typeName": None,
                    "isKwarg": True,
                    "default": "True",
                },
                {
                    "argName": "hint",
                    "description": "A tooltip displayed to the user. Defaults to None.",
                    "typeName": "str",
                    "isKwarg": True,
                    "default": "None",
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [
                {"typeName": "list", "typeDescription": "The list of selected rows"}
            ],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "table",
                    "typeName": "object",
                    "description": "",
                    "properties": [
                        {"argName": "data", "typeName": "array", "description": ""},
                        {
                            "argName": "schema",
                            "typeName": "object",
                            "description": "",
                            "properties": [
                                {
                                    "argName": "fields",
                                    "typeName": "array",
                                    "description": "",
                                }
                            ],
                        },
                    ],
                },
                {
                    "argName": "key",
                    "typeName": "string",
                    "description": "The key of the input on the returning object",
                },
                {
                    "argName": "hint",
                    "typeName": ["string", "null"],
                    "description": "message describing the input",
                    "default": None,
                    "isOptional": True,
                },
                {
                    "argName": "required",
                    "typeName": ["boolean", "string"],
                    "description": "Whether the input is required or not",
                    "default": True,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "table": {
                        "schema": {
                            "fields": [
                                {"name": "Country", "type": "string"},
                                {"name": "Population", "type": "number"},
                            ],
                            "primaryKey": ["Country"],
                        },
                        "data": [
                            {"Country": "USA", "Population": "32,700,000"},
                            {"Country": "China", "Population": "1,300,000,000"},
                            {"Country": "Japan", "Population": "126,000,000"},
                        ],
                    }
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_pandas",
                "key": "example1",
                "code": 'data = [\n    {"Country": "USA", "Population": "32,700,000"},\n    {"Country": "China", "Population": "1,300,000,000"},\n    {"Country": "Japan", "Population": "126,000,000"},\n]\ndf = pd.DataFrame(data)\nread_pandas_row_selection(df)\n',
            }
        ],
    },
    "pandas-output": {
        "type": "pandas-output",
        "description": "Display a pandas dataframe to the user",
        "pythonAPI": {
            "name": "display_pandas",
            "params": [
                {
                    "argName": "df",
                    "description": "The dataframe to display to the user",
                    "typeName": "pandas.DataFrame",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "display_index",
                    "description": "Whether to show a index column. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "table",
                    "typeName": "object",
                    "description": "",
                    "properties": [
                        {"argName": "data", "typeName": "array", "description": ""},
                        {
                            "argName": "schema",
                            "typeName": "object",
                            "description": "",
                            "properties": [
                                {
                                    "argName": "fields",
                                    "typeName": "array",
                                    "description": "",
                                }
                            ],
                        },
                    ],
                },
                {
                    "argName": "displayIndex",
                    "typeName": "boolean",
                    "description": "",
                    "default": False,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "table": {
                        "schema": {
                            "fields": [
                                {"name": "Country", "type": "string"},
                                {"name": "Population", "type": "number"},
                            ],
                            "primaryKey": ["Country"],
                        },
                        "data": [
                            {"Country": "USA", "Population": "32,700,000"},
                            {"Country": "China", "Population": "1,300,000,000"},
                            {"Country": "Japan", "Population": "126,000,000"},
                        ],
                    }
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for display_pandas",
                "key": "example1",
                "code": "display_pandas(df)\n",
            }
        ],
    },
    "progress-output": {
        "type": "progress-output",
        "description": "Display a progress bar. This widget is shown on screen until the script shows a new widget",
        "pythonAPI": {
            "name": "display_progress",
            "params": [
                {
                    "argName": "current",
                    "description": "The progress being made. Defaults to 50.",
                    "typeName": "float",
                    "isKwarg": False,
                    "default": "50",
                },
                {
                    "argName": "total",
                    "description": "Total progress. Defaults to 100.",
                    "typeName": "float",
                    "isKwarg": False,
                    "default": "100",
                },
                {
                    "argName": "text",
                    "description": 'The text displayed with this progress step. Defaults to "".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '""',
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [],
        },
        "brokerAPI": {
            "params": [
                {
                    "argName": "current",
                    "typeName": "number",
                    "description": "",
                    "default": 50,
                },
                {
                    "argName": "total",
                    "typeName": "number",
                    "description": "",
                    "default": 100,
                },
                {
                    "argName": "text",
                    "typeName": "string",
                    "description": "",
                    "default": "",
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {"current": 50, "total": 100},
                "name": "Default behavior",
                "description": "This is what happens when there is no parameter passed",
                "key": "example1",
                "code": "display_progress()\n",
            },
            {
                "props": {"current": 8, "total": 10, "text": "Almost there!"},
                "name": "Custom fields",
                "description": "You can customize the current and total number of steps. Also the message of each step",
                "key": "example2",
                "code": 'from time import sleep\n\ndisplay_progress(0, 10, "Computing values")\n\n# Do some computation\nsleep(1)\n\ndisplay_progress(8, 10, "Almost there!")\n\n# Do some other computation\nsleep(1)\n\ndisplay("Done")\n',
            },
        ],
    },
    "link-output": {
        "type": "link-output",
        "description": "Display a link to the user",
        "pythonAPI": {
            "name": "display_link",
            "params": [
                {
                    "argName": "link_url",
                    "description": "The url of the link to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "link_text",
                    "description": 'The text to display on the link. Defaults to "Click here".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '"Click here"',
                },
                {
                    "argName": "same_tab",
                    "description": "Whether to open the link in the same tab or not. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [],
        },
        "brokerAPI": {
            "params": [
                {"argName": "linkText", "typeName": "string", "description": ""},
                {"argName": "linkUrl", "typeName": "string", "description": ""},
                {
                    "argName": "sameTab",
                    "typeName": "boolean",
                    "description": "",
                    "default": False,
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "linkUrl": "https://console.abstracloud.com",
                    "linkText": "Abstra Cloud Homepage",
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for display_link",
                "key": "example1",
                "code": 'display_link("https://console.abstracloud.com", link_text="Abstra Cloud Homepage")\n',
            }
        ],
    },
    "image-output": {
        "type": "image-output",
        "description": "Display an image to the user",
        "pythonAPI": {
            "name": "display_image",
            "params": [
                {
                    "argName": "image",
                    "description": "The image to display to the user",
                    "typeName": "Union[str, io.IOBase]",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
                {
                    "argName": "subtitle",
                    "description": 'The subtitle of the image. Defaults to "".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '""',
                },
            ],
            "returns": [],
        },
        "brokerAPI": {
            "params": [
                {"argName": "imageUrl", "typeName": "string", "description": ""},
                {
                    "argName": "subtitle",
                    "typeName": "string",
                    "default": "",
                    "description": "",
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "imageUrl": "https://placekitten.com/200/200",
                    "subtitle": "Meooow",
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for display_image",
                "key": "example1",
                "code": 'display_image("https://placekitten.com/200/200", subtitle="Meooow")\n',
            }
        ],
    },
    "html-output": {
        "type": "html-output",
        "description": "Display a html snippet to the user",
        "pythonAPI": {
            "name": "display_html",
            "params": [
                {
                    "argName": "html",
                    "description": "The html snippet to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [],
        },
        "brokerAPI": {
            "params": [
                {"argName": "html", "typeName": "string", "description": ""},
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "html": '<svg width="100" height="100"><circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" /></svg>'
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for display_html",
                "key": "example1",
                "code": 'display_html(\n    \'<svg width="100" height="100"><circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" /></svg>\'\n)\n',
            }
        ],
    },
    "file-output": {
        "type": "file-output",
        "description": "Display a button for the user to download a file",
        "pythonAPI": {
            "name": "display_file",
            "params": [
                {
                    "argName": "file",
                    "description": "The file to download",
                    "typeName": "Union[str, io.IOBase]",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "download_text",
                    "description": 'The text to display on the button that will download the file. Defaults to "Download here".',
                    "typeName": "str",
                    "isKwarg": True,
                    "default": '"Download here"',
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [],
        },
        "brokerAPI": {
            "params": [
                {"argName": "fileUrl", "typeName": "string", "description": ""},
                {
                    "argName": "downloadText",
                    "typeName": "string",
                    "default": "Download here",
                    "description": "",
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "fileUrl": "https://placekitten.com/200/300",
                    "downloadText": "Click here to reveal the secret",
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for display_file",
                "key": "example1",
                "code": 'display_file(\n    "https://placekitten.com/200/300", download_text="Click here to reveal the secret"\n)\n',
            }
        ],
    },
    "markdown-output": {
        "type": "markdown-output",
        "description": "Display a formatted text to the user",
        "pythonAPI": {
            "name": "display_markdown",
            "params": [
                {
                    "argName": "text",
                    "description": "The formatted text to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [],
        },
        "brokerAPI": {
            "params": [
                {"argName": "text", "typeName": "string", "description": ""},
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "text": "\n## Let's see some examples 8-)\n\n* 1^th^ H~2~0 \n\n- [ ] Task\n\n* ==Mark==\n\n* [Link](https://www.abstracloud.com/)"
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for display_markdown",
                "key": "example1",
                "code": 'display_markdown(\n    """\n## Let\'s see some examples 8-)\n\n* 1^th^ H~2~0\n\n\n\n- [ ] Task\n\n* ==Mark==\n\n* [Link](https://www.abstracloud.com/)"""\n)\n',
            }
        ],
    },
    "plotly-output": {
        "type": "plotly-output",
        "description": "Display a plotly figure to the user",
        "pythonAPI": {
            "name": "display_plotly",
            "params": [
                {
                    "argName": "fig",
                    "description": "The figure to display to the user",
                    "typeName": "Any",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [],
        },
        "brokerAPI": {
            "params": [
                {"argName": "figure", "typeName": "any", "description": ""},
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "figure": "iris",
                    "layout": {"width": "400", "height": "230"},
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for display_plotly",
                "key": "example1",
                "code": "display_plotly(figure)\n",
            }
        ],
    },
    "iframe-output": {
        "type": "iframe-output",
        "description": "Display an inline iframe to the user",
        "pythonAPI": {
            "name": "display_iframe",
            "params": [
                {
                    "argName": "url_or_html",
                    "description": "The link to the document or the own document to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "width",
                    "description": 'The width of the iframe. Defaults to "800".',
                    "typeName": "int",
                    "isKwarg": True,
                    "default": '"800"',
                },
                {
                    "argName": "height",
                    "description": 'The height of the iframe. Defaults to "600".',
                    "typeName": "int",
                    "isKwarg": True,
                    "default": '"600"',
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [],
        },
        "brokerAPI": {
            "params": [
                {"argName": "url", "typeName": "string", "description": ""},
                {
                    "argName": "width",
                    "typeName": "string",
                    "description": "",
                    "isOptional": True,
                },
                {
                    "argName": "height",
                    "typeName": "string",
                    "description": "",
                    "isOptional": True,
                },
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {
                    "url": "https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d2965.0824050173574!2d-93.63905729999999!3d41.998507000000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1sWebFilings%2C+University+Boulevard%2C+Ames%2C+IA!5e0!3m2!1sen!2sus!4v1390839289319",
                    "width": "300",
                    "height": "250",
                },
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for display_iframe",
                "key": "example1",
                "code": 'display_iframe(\n    "https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d2965.0824050173574!2d-93.63905729999999!3d41.998507000000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1sWebFilings%2C+University+Boulevard%2C+Ames%2C+IA!5e0!3m2!1sen!2sus!4v1390839289319",\n    width="300",\n    height="250",\n)\n',
            }
        ],
    },
    "text-output": {
        "type": "text-output",
        "description": "Display a text to the user",
        "pythonAPI": {
            "name": "display",
            "params": [
                {
                    "argName": "text",
                    "description": "The text to display to the user",
                    "typeName": "str",
                    "isKwarg": False,
                    "default": None,
                },
                {
                    "argName": "full_width",
                    "description": "Whether the input should use full screen width. Defaults to False.",
                    "typeName": "bool",
                    "isKwarg": True,
                    "default": "False",
                },
            ],
            "returns": [],
        },
        "brokerAPI": {
            "params": [
                {"argName": "text", "description": "", "typeName": "string"},
                {
                    "argName": "columns",
                    "typeName": "number",
                    "description": "number of columns this input will take",
                    "isOptional": True,
                },
                {
                    "argName": "fullWidth",
                    "typeName": "boolean",
                    "description": "Whether the widget should take up the full width of the page",
                    "isOptional": True,
                },
            ]
        },
        "examples": [
            {
                "props": {"text": "Hello world!"},
                "name": "Basic Example",
                "description": "The following example demonstrate some of the available functionality for read_display",
                "key": "example1",
                "code": 'display("Hello world!")\n',
            }
        ],
    },
}
