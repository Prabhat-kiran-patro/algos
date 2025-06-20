import wsgiref.simple_server
import urllib.parse

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def application(environ, start_response):
    # requested path
    path = environ["PATH_INFO"]
    # requested method
    method = environ["REQUEST_METHOD"]
    
    # content type of response
    content_type = "text/html"

    if path == "/":
        if method == "POST":
            # getting wsgi.input obj
            input_obj = environ["wsgi.input"]
            # length of body
            input_length = int(environ["CONTENT_LENGTH"])
            # getting body of wsgi.input obj
            # decoding to string
            body = input_obj.read(input_length).decode()

            # parsing body of form
            try:
                data = urllib.parse.parse_qs(body, keep_blank_values=True)
                # data of body in format
                input_str = data["list_of_ints"][0].strip()
                req = input_str.split()
                for i in range(len(req)):
                    # converting to int
                    req[i] = int(req[i])
                input_list = req.copy()  # keeping original list for display
                bubble_sort(req)  # sorting the list
                if req:
                    response = f"""
                        <html>
                            <body>
                                <h1>The given list has been sorted successfully!</h1>
                                <p>original list: {input_list}</p>
                                <p>sorted list: {req}</p>
                                <a href="/">Go Back</a>
                            </body>
                        </html>
                    """.encode()
                    status = "200 OK"
                else:
                    response = """
                        <html>
                            <body>
                                <h1>No input provided!</h1>
                                <p>Please enter a list of integers.</p>
                                <a href="/">Go Back</a>
                            </body>
                        </html>
                    """.encode()
                    status = "400 Bad Request"
            except ValueError:
                response = f"""
                    <html>
                        <body>
                            <h1>Invalid input!</h1>
                            <p>{input_str}</p>
                            <a href="/">Go Back</a>
                        </body>
                    </html>
                """.encode()
                status = "400 Bad Request"
        else:
            # reading html file
            with open("sortit.html","r") as f:
                response = f.read().encode()
            status = "200 OK"

    else:
        # 404 - path not found
        response = b"<h1>Not found</h1><p>Entered path not found</p>"
        status = "404 Not Found"

    # response headers
    headers = [
        ("Content-Type",content_type),
        ("Content-Length",str(len(response)))
    ]

    start_response(status, headers)
    return [response]
    

if __name__ == "__main__":
    w_s = wsgiref.simple_server.make_server(
        host="localhost",
        port=8021,
        app=application
    )
    w_s.serve_forever()