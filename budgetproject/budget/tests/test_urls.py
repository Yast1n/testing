from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import project_list,ProjectCreateView, project_detail

class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse('list')
        print(resolve(url))
        self.assertEqual(resolve(url).func, project_list)


    def test_add_url_resolves(self):
        url = reverse('add')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, ProjectCreateView)

    def test_detail_url_resolves(self):
        url = reverse('detail',args=['some-slug'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, project_detail)