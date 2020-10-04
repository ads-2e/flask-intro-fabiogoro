import os
from flask import template_rendered
from server import app


class AbstractViewCase(object):

    templates = []
    _defaultLinks = [
        '/',
        '/entrar/',
        '/static/',
        '/inscrever/'
    ]

    longMessage = False

    def _registrar_template(self, app, template, context):
        if len(self.templates) > 0:
            self.templates = []
        self.templates.append((template, context))

    def _links(self):
        return []

    def setUp(self):
        template_rendered.connect(self._registrar_template)
        self.template_str = open(
            os.path.join(
                os.path.dirname(__file__),
                'templates/'+self._template)
            ).read()
        self.client = app.test_client()
        self.response = self.client.get(self._url)
        self.conteudo = self.response.data.decode('UTF-8')

    def tearDown(self):
        template_rendered.disconnect(self._registrar_template)

    def test_ok(self):
        self.assertEqual(
            200,
            self.response.status_code,
            msg="Caminho {} não respondeu com 200".format(self._url)
        )

    def test_links_pagina(self):
        links = self._defaultLinks + self._links()
        for link in links:
            self.assertIn(
                link,
                self.conteudo,
                msg="Link de endereço {} não encontrado!".format(link)
            )

    def test_template_usado(self):
        templates = []
        for template, context in self.templates:
            templates.append(template)
            if getattr(template, 'name') == self._template:
                return True
        raise AssertionError(
            'Template {} não foi usado. Templates utilizados: {}'.format(
                self._template,
                templates
            )
        )
