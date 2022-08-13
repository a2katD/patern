class Parser:
    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            params = data.split('&')
            for param in params:
                key, value = param.split('=')
                result[key] = value
        return result


class GetRequests(Parser):
    @staticmethod
    def get_request_params(environ):
        query_string = environ['QUERY_STRING']
        request_params = GetRequests.parse_input_data(query_string)
        return request_params


class PostRequests(Parser):
    @staticmethod
    def get_wsgi_input_data(environ) -> bytes:
        content_length_data = environ.get('CONTENT_LENGTH')
        if content_length_data:
            content_length = int(content_length_data)
            data = environ['wsgi.input'].read(content_length)
        else:
            data = b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data
