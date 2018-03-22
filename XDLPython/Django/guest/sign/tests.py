from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class IndexPageTest(TestCase):

    def test_index_page1(self):
        respons = self.client.get(reverse('index')) # 使用url的别名来指定地址.
        self.assertEqual(respons.status_code,200)
        self.assertTemplateUsed(respons,'index.html') # 断言是否为给定模板

    def test_index_page2(self):
        respons = self.client.get(reverse('index'))
        self.assertEqual(respons.status_code, 200)
        self.assertIn(b'<html', respons.content)  # 断言response内容中是否包含某字符



