from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:
    flow.response.content = flow.response.content.decode().replace("Helloooo! I'm an honest website!", "You've been PWN'D! I'm an evil website").encode()
