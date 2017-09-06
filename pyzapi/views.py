from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import (view_config)


class PyzapiViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return HTTPFound(location='/plain')

    @view_config(route_name='plain')
    def plain(self):
        name = self.request.params.get('name', 'No Name Provided')

        body = 'URL %s with name: %s' % (self.request.url, name)
        return Response(
            content_type='text/plain',
            body=body
        )

    @view_config(route_name='identities')
    def identities(self):
        identity = self.request.matchdict['identity']

        body = 'URL %s with id: %s' % (self.request.url, identity)

        return Response(
            content_type='text/plain',
            body=body,
        )
