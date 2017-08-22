schema = {'paths': {}}


class OpenApi(object):
    name = 'OpenApi'
    api = 2

    def __init__(self, file_output='schema.json'):
        print("init")

    def add_endpoint(self, method, url, summary=None, produces=None):
        if url not in schema['paths']:
            schema['paths'][url] = {}

        data = {'summary': summary,
                'produces': ['application/json'],
                'consumes': ['application/json']}

        schema['paths'][url][method] = data
        print('add :', method, url, summary, produces)

    def apply(self, callback, route):
        def get_produces():
            produces = {}
            for namespace in route.config:
                if 'produces' == namespace[:len('produces')]:
                    old = produces
                    final = namespace.split('.')[-1]
                    for key in namespace.split('.')[1:]:
                        if key not in old:
                            if final == key:
                                old[key] = route.config[namespace]
                                continue
                            old[key] = {}
                        old = old[key]

        self.add_endpoint(method=route.method, url=route.rule,
                          summary=route.config.get('summary'),
                          produces=get_produces())
        return callback
