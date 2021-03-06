def barchart(hapi, x, y, w, h, params):
    options = {
        "ticks_y": 10,
        "tick_size": 5,
        "range_y": [0, 100],
        "data": {"a": 10, "b": 20},
        "bin_color": (255, 99, 97),
        "line_color": (200, 200, 200),
        "text_color": (100, 100, 100),
        "mouse_line": False,
    }
    options.update(params)
    hapi.stroke_size(2)
    hapi.stroke(options["line_color"])
    hapi.line(x, y, x, y + h)
    hapi.line(x, y + h, x + w, y + h)
    hapi.fill(options["text_color"])
    y_top_val = options["range_y"][1]
    for t in range(options["ticks_y"]):
        hapi.line(
            x,
            y + (t * (h // options["ticks_y"])),
            x - options["tick_size"],
            y + (t * (h // options["ticks_y"])),
        )
        hapi.text(y_top_val, x - 20, y + (t * (h // options["ticks_y"])) - 10)
        y_top_val -= (options["range_y"][1] - options["range_y"][0]) // options[
            "ticks_y"
        ]

    num_data = len(options["data"].keys())
    divs = 1 + 1 + (num_data * 2) + (num_data - 1)
    space_unit = w // divs
    current_x = x + space_unit
    for i, d in enumerate(options["data"]):
        hapi.fill(options["bin_color"])
        bin_height = hapi.constrain(
            options["data"][d], options["range_y"][0], options["range_y"][1], 0, h
        )
        hapi.rotate(0)
        hapi.rect(current_x, y + h - bin_height, 2 * space_unit, bin_height)
        hapi.fill(hapi.color["black"])
        hapi.push_matrix()
        hapi.rotate(270)
        hapi.text(d, current_x + space_unit, y + h + 5)
        hapi.pop_matrix()
        current_x += 3 * space_unit

    if options["mouse_line"]:
        hapi.stroke_size(2)
        hapi.stroke(hapi.color["red"])
        l_height = hapi.mouseY()
        if hapi.mouseY() < y:
            l_height = y
        elif hapi.mouseY() > y + h:
            l_height = y + h
        hapi.line(x, l_height, x + w, l_height)


def linechart(hapi, x, y, w, h, params):
    options = {
        "ticks_y": 10,
        "ticks_x": 10,
        "tick_size": 5,
        "range_y": [0, 100],
        "range_x": [0, 100],
        "data": [[10, 20], [10, 15], [80, 30], [90, 10]],
        "labels": ["apple", "", "", "tree"],
        "line_color": (200, 200, 200),
        "text_color": (100, 100, 100),
        "mouse_line": False,
    }
    options.update(params)
    hapi.stroke_size(2)
    hapi.stroke(options["line_color"])
    hapi.line(x, y, x, y + h)
    hapi.line(x, y + h, x + w, y + h)
    hapi.fill(options["text_color"])

    y_top_val = options["range_y"][1]
    for t in range(options["ticks_y"]):
        hapi.line(
            x,
            y + (t * (h // options["ticks_y"])),
            x - options["tick_size"],
            y + (t * (h // options["ticks_y"])),
        )
        hapi.text(y_top_val, x - 20, y + (t * (h // options["ticks_y"])) - 10)
        y_top_val -= (options["range_y"][1] - options["range_y"][0]) // options[
            "ticks_y"
        ]
    x_val = options["range_x"][0]
    for t in range(options["ticks_x"] + 1):
        hapi.line(
            x + (t * (w // options["ticks_x"])),
            y + h,
            x + (t * (w // options["ticks_x"])),
            y + h + options["tick_size"],
        )
        hapi.push_matrix()
        hapi.rotate(270)
        hapi.text(x_val, x + (t * (w // options["ticks_x"])), y + h + 5)
        hapi.pop_matrix()
        x_val += (options["range_x"][1] - options["range_x"][0]) // options["ticks_x"]

    for i, d in enumerate(options["data"]):
        hapi.stroke_size(2)
        hapi.stroke(options["line_color"])
        try:
            # x1 = hapi.constrain(d[0], options['range_x'][0], options['range_x'][1], 0, w)
            # y1 = hapi.constrain(d[1], options['range_y'][0], options['range_y'][1], 0, h)
            # x2 = hapi.constrain(options['data'][i+1][0], options['range_x'][0], options['range_x'][1], 0, w)
            # y2 = hapi.constrain(options['data'][i+1][1], options['range_y'][0], options['range_y'][1], 0, h)
            # hapi.line(x1, x2, y1, y2)
            x1 = hapi.constrain(
                d[0], options["range_x"][0], options["range_x"][1], x, x + w
            )
            y1 = (
                60
                + h
                - hapi.constrain(
                    d[1], options["range_y"][0], options["range_y"][1], y, y + h
                )
            )
            x2 = hapi.constrain(
                options["data"][i + 1][0],
                options["range_x"][0],
                options["range_x"][1],
                x,
                x + w,
            )
            y2 = (
                60
                + h
                - hapi.constrain(
                    options["data"][i + 1][1],
                    options["range_y"][0],
                    options["range_y"][1],
                    y,
                    y + h,
                )
            )
            # 60 is arbitrary value
            # hapi.fill(hapi.color['yellow'])
            # print(x1, y1)
            hapi.line(x1, y1, x2, y2)
            # hapi.line(x1, y1, x2, y2)
        except IndexError:
            pass

    if options["mouse_line"]:
        hapi.stroke_size(2)
        hapi.stroke(hapi.color["red"])
        limit_y = hapi.mouseY()
        limit_x = hapi.mouseX()
        if limit_y < y:
            limit_y = y
        elif limit_y > y + h:
            limit_y = y + h
        if limit_x < x:
            limit_x = x
        elif limit_x > x + w:
            limit_x = x + w

        hapi.line(x, limit_y, x + w, limit_y)
        hapi.line(limit_x, y, limit_x, y + h)
        tex = "{} {}".format(limit_x, limit_y)
        hapi.text(tex, 100, 100)
