from .anybloktestcase import AnyBlokTestCase
from anyblok.environment import EnvironmentManager, EnvironmentException
from anyblok.environment import ThreadEnvironment


class MockEnvironment:

    values = {}

    @classmethod
    def scoped_function_for_session(cls):
        return cls.__name__

    @classmethod
    def setter(cls, key, value):
        cls.values[key] = value

    @classmethod
    def getter(cls, key, default):
        return cls.values.get(key, default)


class TestEnvironment(AnyBlokTestCase):

    def setUp(self):
        super(TestEnvironment, self).setUp()
        EnvironmentManager.define_environment_cls(MockEnvironment)

    def tearDown(self):
        super(TestEnvironment, self).tearDown()
        EnvironmentManager.define_environment_cls(ThreadEnvironment)

    def test_set_and_get_variable(self):
        dbname = 'test db name'
        EnvironmentManager.set('dbname', dbname)
        self.assertEqual(EnvironmentManager.get('dbname'), dbname)

    def test_without_environment_for_set(self):
        # don't use define_environment_cls, because she must be verify
        EnvironmentManager.environment = None
        try:
            EnvironmentManager.set('dbname', 'test')
            self.fail('No watchdog for None environment')
        except EnvironmentException:
            pass

    def test_without_environment_for_get(self):
        # don't use define_environment_cls, because she must be verify
        EnvironmentManager.environment = None
        try:
            EnvironmentManager.get('dbname')
            self.fail('No watchdog for None environment')
        except EnvironmentException:
            pass

    def test_scoped_function_session(self):
        self.assertEqual(EnvironmentManager.scoped_function_for_session(),
                         MockEnvironment.scoped_function_for_session)

    def check_bad_define_environment(self, env):
        try:
            EnvironmentManager.define_environment_cls(env)
            self.fail("Bad environment class")
        except EnvironmentException as e:
            print(e)
            pass

    def test_bad_define_environment_scoped_function_session(self):

        class Env:

            @classmethod
            def setter(cls, key, value):
                pass

            @classmethod
            def getter(cls, key, default):
                pass

        self.check_bad_define_environment(Env)

        class Env(MockEnvironment):

            scoped_function_for_session = 'other'

        self.check_bad_define_environment(Env)

        class Env(MockEnvironment):

            def scoped_function_for_session(self):
                pass

        self.check_bad_define_environment(Env)

    def test_bad_define_environment_setter(self):

        class Env:

            @classmethod
            def scoped_function_for_session(cls):
                pass

            @classmethod
            def getter(cls, key, default):
                pass

        self.check_bad_define_environment(Env)

        class Env(MockEnvironment):

            setter = None

        self.check_bad_define_environment(Env)

        class Env(MockEnvironment):

            def setter(self, key, value):
                pass

        self.check_bad_define_environment(Env)

    def test_bad_define_environment_getter(self):

        class Env:

            @classmethod
            def scoped_function_for_session(cls):
                pass

            @classmethod
            def setter(cls, key, value):
                pass

        self.check_bad_define_environment(Env)

        class Env(MockEnvironment):

            getter = None

        self.check_bad_define_environment(Env)

        class Env(MockEnvironment):

            def getter(self, key, default):
                pass

        self.check_bad_define_environment(Env)


class TestThreadEnvironment(AnyBlokTestCase):

    def test_set_and_get_variable(self):
        dbname = 'test db name'
        EnvironmentManager.set('dbname', dbname)
        self.assertEqual(EnvironmentManager.get('dbname'), dbname)

    def test_scoped_function_session(self):
        self.assertEqual(EnvironmentManager.scoped_function_for_session(),
                         None)