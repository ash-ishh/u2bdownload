from fasthtml import common as fh

from pytube_wrapper import get_video_information, get_stream_attributes

css = fh.Style(
    ":root { --pico-font-size: 100%; --pico-font-family-monospace: ui-monospace;}",
)
app, rt = fh.fast_app(live=True, hdrs=(fh.picolink, css))


def make_streams_table(streams):
    stream_rows = []
    columns = get_stream_attributes()
    table_head = fh.Thead(
        fh.Tr(*[fh.Th(value["display_name"]) for key, value in columns.items()])
    )
    for stream in streams:
        stream_data_for_row = []
        for key, value in columns.items():
            if value["type"] == "url":
                cell = fh.Td(fh.A("Link", href=stream[key], target="_blank"))
            else:
                cell = fh.Td(stream[key])
            stream_data_for_row.append(cell)
        stream_row = fh.Tr(*stream_data_for_row)
        stream_rows.append(stream_row)
    table_body = fh.Tbody(*stream_rows)
    table = fh.Table(table_head, table_body)
    return table


@rt("/")
def get():
    url_input = fh.Input(id="url", placeholder="URL")
    submit_button = fh.Button("Submit")
    url_group = fh.Group(url_input, submit_button)
    input_form = fh.Form(
        url_group, hx_post="/", target_id="result", hx_swap="innerHTML"
    )
    input_card = fh.Card(input_form)
    result_div = fh.Div(id="result")
    app_name = "u2bdownload"
    title = fh.Title(app_name)
    heading = fh.H1(app_name, style="text-align: center;")
    main = fh.Main(
        heading,
        input_card,
        result_div,
        cls="container",
    )
    return title, main


@rt("/")
def post(url: str):
    video_information = get_video_information(url)
    error = video_information["error"]
    if not error:
        title = video_information["title"]
        streams = video_information["streams"]
        streams_table = make_streams_table(streams)
        heading_css = "text-align: center; padding: 2rem;"
        heading = fh.H2(title, style=heading_css)
        return heading, streams_table
    else:
        error_css = "background-color: #ffebee; border: 1px solid #f44336; color: #b71c1c; padding: 10px; border-radius: 4px; margin:10px;"
        error_div = fh.Div(
            error,
            style=error_css,
        )
        return error_div


if __name__ == "__main__":
    fh.serve(port=8080)
