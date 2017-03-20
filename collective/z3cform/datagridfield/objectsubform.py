# -*- coding: utf-8 -*-
from plone.app.z3cform.interfaces import IPloneFormLayer
from z3c.form.field import Fields
from z3c.form.form import BaseForm
from z3c.form.interfaces import IDataConverter
from z3c.form.interfaces import IErrorViewSnippet
from z3c.form.interfaces import IFormAware
from z3c.form.interfaces import IObjectWidget
from z3c.form.interfaces import ISubForm
from z3c.form.interfaces import ISubformFactory
from z3c.form.interfaces import IValidator
from zope.component import adapter
from zope.component import getMultiAdapter
from zope.interface import implementer
from zope.interface import Interface

import zope.schema


@implementer(ISubForm)
class ObjectSubForm(BaseForm):

    def __init__(self, context, request, parentWidget):
        self.context = context
        self.request = request
        self.__parent__ = parentWidget
        self.parentForm = parentWidget.form
        self.ignoreContext = self.__parent__.ignoreContext
        self.ignoreRequest = self.__parent__.ignoreRequest
        if IFormAware.providedBy(self.__parent__):
            self.ignoreReadonly = self.parentForm.ignoreReadonly
        self.prefix = self.__parent__.name

    def _validate(self):
        for widget in self.widgets.values():
            try:
                # convert widget value to field value
                converter = IDataConverter(widget)
                value = converter.toFieldValue(widget.value)
                # validate field value
                getMultiAdapter(
                    (
                        self.context,
                        self.request,
                        self.parentForm,
                        getattr(widget, 'field', None),
                        widget
                    ),
                    IValidator
                ).validate(value, force=True)
            except (zope.schema.ValidationError, ValueError) as error:
                # on exception, setup the widget error message
                view = getMultiAdapter(
                    (
                        error,
                        self.request,
                        widget,
                        widget.field,
                        self.parentForm,
                        self.context
                    ),
                    IErrorViewSnippet
                )
                view.update()
                widget.error = view

    def setupFields(self):
        self.fields = Fields(self.__parent__.field.schema)

    def update(self):
        if self.__parent__.field is None:
            raise ValueError(
                '{0:r}.field is None, that\'s a blocking point'.format(
                    self.__parent__
                )
            )
        # update stuff from parent to be sure
        self.mode = self.__parent__.mode
        self.setupFields()
        super(ObjectSubForm, self).update()

    def getContent(self):
        return self.__parent__._value


@adapter(
    Interface,        # widget value
    IPloneFormLayer,  # request
    Interface,        # widget context
    Interface,        # form
    IObjectWidget,    # widget
    Interface,        # field
    Interface         # field.schema
)
@implementer(ISubformFactory)
class SubformAdapter(object):
    """Most basic-default subform factory adapter"""

    factory = ObjectSubForm

    def __init__(self, context, request, widgetContext, form,
                 widget, field, schema):
        self.context = context
        self.request = request
        self.widgetContext = widgetContext
        self.form = form
        self.widget = widget
        self.field = field
        self.schema = schema

    def __call__(self):
        return self.factory(self.context, self.request, self.widget)
