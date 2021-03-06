from __future__ import unicode_literals

from ..models import WebLink

from .literals import (
    TEST_WEB_LINK_LABEL, TEST_WEB_LINK_LABEL_EDITED, TEST_WEB_LINK_TEMPLATE
)


class WebLinkTestMixin(object):
    def _create_test_web_link(self):
        self.test_web_link = WebLink.objects.create(
            label=TEST_WEB_LINK_LABEL, template=TEST_WEB_LINK_TEMPLATE,
        )


class WebLinkViewTestMixin(object):
    def _request_test_document_web_link_instance_view(self):
        return self.post(
            viewname='web_links:web_link_instance_view', kwargs={
                'document_pk': self.test_document.pk,
                'web_link_pk': self.test_web_link.pk
            }
        )

    def _request_test_document_web_link_list_view(self):
        return self.get(
            viewname='web_links:document_web_link_list', kwargs={
                'pk': self.test_document.pk
            }
        )

    def _request_test_web_link_create_view(self):
        return self.post(
            viewname='web_links:web_link_create', data={
                'label': TEST_WEB_LINK_LABEL,
                'template_template': TEST_WEB_LINK_TEMPLATE,
            }
        )

    def _request_test_web_link_delete_view(self):
        return self.post(
            viewname='web_links:web_link_delete', kwargs={
                'pk': self.test_web_link.pk
            }
        )

    def _request_test_web_link_edit_view(self):
        return self.post(
            viewname='web_links:web_link_edit', kwargs={
                'pk': self.test_web_link.pk
            }, data={
                'label': TEST_WEB_LINK_LABEL_EDITED,
                'template_template': TEST_WEB_LINK_TEMPLATE
            }
        )

    def _request_test_web_link_list_view(self):
        return self.get(viewname='web_links:web_link_list')
