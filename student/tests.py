from django.test import TestCase, Client
from .models import Student


__doc__ = """
            运行测试用例的命令行如下：
                python manage.py test student.tests.StudentTest.test_post_student
          """


class StudentTest(TestCase):
    def setUp(self):
        Student.objects.create(
            name="jason",
            sex=1,
            profession="程序员",
            email="123@it.com",
            qq=12312312,
            phone=23424234
        )

    def test_create_and_show_sex(self):
        student = Student.objects.create(
            name="bluce",
            sex=1,
            profession="程序员",
            email="123@it.com",
            qq=12312312,
            phone=23424234
        )
        self.assertEqual(student.show_sex, "男", "性别字段内容跟展示不一致！")
        # self.assertEqual(student.get_sex_display(), "男", "性别字段内容跟展示不一致！")

    def test_filter(self):
        student = Student.objects.create(
            name="bluce",
            sex=1,
            profession="程序员",
            email="123@it.com",
            qq=12312312,
            phone=23424234
        )
        student_bluce = Student.objects.filter(name="bluce")
        self.assertEqual(student_bluce.count(), 1, "名字为{}的学生只能有一个".format(student.name))

    def test_get_index(self):
        # 测试首页的可用性
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200, "status code must be 200 !")

    def test_post_student(self):
        # 测试首页提交表单的可用性
        client = Client()
        data = {
            "name": "test_post_user",
            "sex": 1,
            "profession": "程序员",
            "email": "123@it.com",
            "qq": 12312312,
            "phone": 23424234
        }
        response = client.post("/", data)
        self.assertEqual(response.status_code, 302, "status code must be 302 !")
        response = client.get("/")
        self.assertTrue(b'test_post_user' in response.content, "response content must contain 'test_post_user'")

    def tearDown(self):
        super(StudentTest, self).tearDown()


