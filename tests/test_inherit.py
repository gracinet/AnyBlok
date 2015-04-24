# This file is a part of the AnyBlok project
#
#    Copyright (C) 2014 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok.tests.testcase import DBTestCase
from anyblok import Declarations
register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin
Core = Declarations.Core


def simple_subclass_model():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @register(Model)
    class Test:
        id = Integer(primary_key=True)
        name = String()

    @register(Model)  # noqa
    class Test:
        other = String()


def simple_subclass_Core_Base():

    @register(Core)
    class Base:

        def mymethod(self):
            return 1

    @register(Core)  # noqa
    class Base:

        def mymethod(self):
            return 10 * super(Base, self).mymethod()

    @register(Model)
    class Test:
        pass


def simple_subclass_Core_SqlBase():
    Integer = Declarations.Column.Integer

    @register(Core)
    class SqlBase:

        def mymethod(self):
            return 1

    @register(Core)  # noqa
    class SqlBase:

        def mymethod(self):
            return 10 * super(SqlBase, self).mymethod()

    @register(Model)
    class Test:
        id = Integer(primary_key=True)


def simple_subclass_model_change_type():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @register(Model)
    class Test:
        id = Integer(primary_key=True)
        name = String()

    @register(Model)  # noqa
    class Test:
        name = Integer()


def simple_subclass_model_change_type_and_subclass_add_field():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @register(Model)
    class Test:
        id = Integer(primary_key=True)
        name = String()

    @register(Model)  # noqa
    class Test:
        name = Integer()

    @register(Model)  # noqa
    class Test:
        other = String()


def mixin_one_model():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @register(Mixin)
    class MixinName:

        name = String()

    @register(Model)
    class Test(Mixin.MixinName):

        id = Integer(primary_key=True)
        other = String()


def mixin_two_model():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @register(Mixin)
    class MixinName:

        name = String()

    @register(Model)
    class Test(Mixin.MixinName):

        id = Integer(primary_key=True)
        other = String()

    @register(Model)
    class Test2(Mixin.MixinName):

        id = Integer(primary_key=True)
        other = String()


def mixin_one_model_with_subclass():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @register(Mixin)
    class MixinName:

        name = String()

    @register(Model)
    class Test(Mixin.MixinName):

        id = Integer(primary_key=True)

    @register(Model)  # noqa
    class Test:

        other = String()


def mixin_one_model_by_subclass():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @register(Mixin)
    class MixinName:

        name = String()

    @register(Model)
    class Test:

        id = Integer(primary_key=True)

    @register(Model)  # noqa
    class Test(Mixin.MixinName):

        other = String()


def mixin_with_foreign_key_one_model():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @register(Model)
    class TestFk:

        name = String(primary_key=True)

    @register(Mixin)
    class MixinName:

        name = String(foreign_key=(Model.TestFk, 'name'))

    @register(Model)
    class Test(Mixin.MixinName):

        id = Integer(primary_key=True)


def mixin_with_foreign_key_two_model():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @register(Model)
    class TestFk:

        name = String(primary_key=True)

    @register(Mixin)
    class MixinName:

        name = String(foreign_key=(Model.TestFk, 'name'))

    @register(Model)
    class Test(Mixin.MixinName):

        id = Integer(primary_key=True)

    @register(Model)
    class Test2(Mixin.MixinName):

        id = Integer(primary_key=True)


def mixin_one_model_by_subclass_and_with():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @register(Mixin)
    class MixinName:

        name = String()

    @register(Model)
    class Test:

        id = Integer(primary_key=True)

    @register(Model)  # noqa
    class Test(Mixin.MixinName):
        pass

    @register(Model)  # noqa
    class Test:

        other = String()


def mixin_one_model_with_subclass_and_subclass_mixin():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @register(Mixin)
    class MixinName:

        name = String()

    @register(Model)
    class Test:

        id = Integer(primary_key=True)

    @register(Model)  # noqa
    class Test(Mixin.MixinName):
        pass

    @register(Mixin)  # noqa
    class MixinName:

        other = String()


def inherit_by_another_model():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @register(Model)
    class MainModel:

        id = Integer(primary_key=True)
        name = String()

    @register(Model)
    class Test(Model.MainModel):

        id = Integer(primary_key=True)
        mainmodel = Integer(foreign_key=(Model.MainModel, 'id'))
        other = String()


def inherit_by_two_another_model():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @register(Model)
    class MainModel:

        id = Integer(primary_key=True)
        name = String()

    @register(Model)
    class Test(Model.MainModel):

        id = Integer(primary_key=True)
        mainmodel = Integer(foreign_key=(Model.MainModel, 'id'))
        other = String()

    @register(Model)
    class Test2(Model.MainModel):

        id = Integer(primary_key=True)
        mainmodel = Integer(foreign_key=(Model.MainModel, 'id'))
        other = String()


def inherit_by_another_model_and_subclass_mainmodel():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @register(Model)
    class MainModel:

        id = Integer(primary_key=True)
        name = String()

    @register(Model)
    class Test(Model.MainModel):

        id = Integer(primary_key=True)
        mainmodel = Integer(foreign_key=(Model.MainModel, 'id'))

    @register(Model)  # noqa
    class MainModel:

        other = String()


def inherit_base_and_add_method():

    @register(Core)
    class Base:

        def method_from_base(self, x):
            return x * 2

    @register(Model)
    class Test:
        pass


def inherit_base_and_add_method_after_create_model():

    @register(Model)
    class Test:
        pass

    @register(Core)
    class Base:

        def method_from_base(self, x):
            return x * 2


def inherit_base_and_add_method_sub_classes():

    @register(Core)
    class Base:

        def method_from_base(self, x):
            return x * 2

    @register(Model)
    class Test:

        def method_from_base(self, x):
            return super(Test, self).method_from_base(x) + 3


def inherit_base_and_add_method_sub_classes_by_mixin():

    @register(Core)
    class Base:

        def method_from_base(self, x):
            return x * 2

    @register(Mixin)
    class TestMixin:

        def method_from_base(self, x):
            return super(TestMixin, self).method_from_base(x) + 3

    @register(Model)
    class Test(Mixin.TestMixin):
        pass


def inherit_sql_base_on_simple_model():

    @register(Core)
    class Base:

        def is_sql_base(self):
            return False

    @register(Core)
    class SqlBase:

        def is_sql_base(self):
            return True

    @register(Model)
    class Test:
        pass


def inherit_sql_base_on_sql_model():
    Integer = Declarations.Column.Integer

    @register(Core)
    class Base:

        def is_sql_base(self):
            return False

    @register(Core)
    class SqlBase:

        def is_sql_base(self):
            return True

    @register(Model)
    class Test:

        id = Integer(primary_key=True)


class TestInherit(DBTestCase):

    def check_registry(self, Model):
        t = Model.insert(name="test", other="other")
        t2 = Model.query().first()
        self.assertEqual(t2, t)

    def test_simple_subclass_model(self):
        registry = self.init_registry(simple_subclass_model)
        self.check_registry(registry.Test)

    def test_inherit_multi_mixins(self):
        def add_in_registry():
            Integer = Declarations.Column.Integer
            String = Declarations.Column.String

            @register(Mixin)
            class MixinName:

                name = String()

            @register(Mixin)
            class MixinOther:

                other = String()

            @register(Model)
            class Test(Mixin.MixinName, Mixin.MixinOther):

                id = Integer(primary_key=True)

        registry = self.init_registry(simple_subclass_model)
        self.check_registry(registry.Test)

    def test_inherit_cascade_mixins(self):
        def add_in_registry():
            Integer = Declarations.Column.Integer
            String = Declarations.Column.String

            @register(Mixin)
            class MixinName:

                name = String()

            @register(Mixin)
            class MixinOther:

                other = String()

            @register(Mixin)
            class MTest(Mixin.MixinName, Mixin.MixinOther):
                pass

            @register(Model)
            class Test(Mixin.MTest):

                id = Integer(primary_key=True)

        registry = self.init_registry(simple_subclass_model)
        self.check_registry(registry.Test)

    def test_simple_subclass_Core_Base(self):
        registry = self.init_registry(simple_subclass_Core_Base)
        m = registry.Test()
        self.assertEqual(m.mymethod(), 10)

    def test_simple_subclass_Core_SqlBase(self):
        registry = self.init_registry(simple_subclass_Core_SqlBase)
        m = registry.Test()
        self.assertEqual(m.mymethod(), 10)

    def test_simple_subclass_model_change_type(self):
        registry = self.init_registry(simple_subclass_model_change_type)

        t = registry.Test.insert(name=1)
        t2 = registry.Test.query().first()
        self.assertEqual(t2, t)
        self.assertEqual(t.name, 1)

    def test_simple_subclass_model_change_type_and_subclass_add_field(self):
        registry = self.init_registry(
            simple_subclass_model_change_type_and_subclass_add_field)

        t = registry.Test.insert(name=1, other='other')
        t2 = registry.Test.query().first()
        self.assertEqual(t2, t)
        self.assertEqual(t.name, 1)

    def test_mixin_one_model(self):
        registry = self.init_registry(mixin_one_model)
        self.check_registry(registry.Test)

    def test_mixin_two_model(self):
        registry = self.init_registry(mixin_two_model)
        self.check_registry(registry.Test)
        self.check_registry(registry.Test2)

    def test_mixin_one_model_with_subclass(self):
        registry = self.init_registry(mixin_one_model_with_subclass)
        self.check_registry(registry.Test)

    def test_mixin_one_model_by_subclass(self):
        registry = self.init_registry(mixin_one_model_by_subclass)
        self.check_registry(registry.Test)

    def test_mixin_with_foreign_key_one_model(self):
        registry = self.init_registry(mixin_with_foreign_key_one_model)

        val = 'test'
        registry.TestFk.insert(name=val)
        t = registry.Test.insert(name=val)
        t2 = registry.Test.query().first()
        self.assertEqual(t2, t)

    def test_mixin_with_foreign_key_two_model(self):
        registry = self.init_registry(mixin_with_foreign_key_two_model)

        for val in ('test', 'test2'):
            registry.TestFk.insert(name=val)

        t = registry.Test.insert(name='test')
        t2 = registry.Test.query().first()
        self.assertEqual(t2, t)

        t3 = registry.Test2.insert(name='test2')
        t4 = registry.Test2.query().first()
        self.assertEqual(t3, t4)

    def test_mixin_one_model_by_subclass_and_with(self):
        registry = self.init_registry(mixin_one_model_by_subclass_and_with)
        self.check_registry(registry.Test)

    def test_mixin_one_model_with_subclass_and_subclass_mixin(self):
        registry = self.init_registry(
            mixin_one_model_with_subclass_and_subclass_mixin)
        self.check_registry(registry.Test)

    def test_inherit_by_another_model(self):
        registry = self.init_registry(inherit_by_another_model)
        self.check_registry(registry.Test)

    def test_inherit_by_two_another_model(self):
        registry = self.init_registry(inherit_by_two_another_model)
        self.check_registry(registry.Test)
        self.check_registry(registry.Test2)

    def test_inherit_by_another_model_and_subclass_mainmodel(self):
        registry = self.init_registry(
            inherit_by_another_model_and_subclass_mainmodel)
        self.check_registry(registry.Test)

    def check_inherit_base(self, function, value):
        registry = self.init_registry(function)
        test = registry.Test()
        self.assertEqual(test.method_from_base(2), value)

    def test_inherit_base_and_add_method(self):
        self.check_inherit_base(inherit_base_and_add_method, 4)

    def test_inherit_base_and_add_method_after_create_model(self):
        self.check_inherit_base(inherit_base_and_add_method_after_create_model,
                                4)

    def test_inherit_base_and_add_method_sub_classes(self):
        self.check_inherit_base(inherit_base_and_add_method_sub_classes, 7)

    def test_inherit_base_and_add_method_sub_classes_by_mixin(self):
        self.check_inherit_base(
            inherit_base_and_add_method_sub_classes_by_mixin, 7)

    def check_inherit_sql_base(self, function, value):
        registry = self.init_registry(function)
        test = registry.Test()
        self.assertEqual(test.is_sql_base(), value)

    def test_inherit_sql_base_on_simple_model(self):
        self.check_inherit_sql_base(inherit_sql_base_on_simple_model, False)

    def test_inherit_sql_base_on_sql_model(self):
        self.check_inherit_sql_base(inherit_sql_base_on_sql_model, True)