from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # our routes
    config.add_route('home', '/')
    config.add_route('plain', '/plain')
    config.add_route('identities', '/identities/{identity}')

    config.scan('.views')
    return config.make_wsgi_app()