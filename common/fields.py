from django.db import models


class OrdinalField(models.FloatField):

    def __init__(self, *args, **kwargs):
        kwargs['null'] = kwargs.get('null', False)
        kwargs['default'] = kwargs.get('default', 0)
        super(OrdinalField, self).__init__(*args, **kwargs)


class IntegerRangeField(models.IntegerField):

    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)
