import io

import jsonable

from mwtypes.util import none_or

from ..element_iterator import ElementIterator
from ..errors import MalformedXML
from .namespace import Namespace
from .page import Page


class SiteInfo(jsonable.Type):
    """
    """
    __slots__ = ('name', 'dbname', 'base', 'generator', 'case', 'namespaces')

    def initialize(self, name=None, dbname=None, base=None, generator=None,
                   case=None, namespaces=None):

        self.name = none_or(name, str)
        """
        The name of the site. : str | `None`
        """

        self.dbname = none_or(dbname, str)
        """
        The dbname of the site. : str | `None`
        """

        self.base = none_or(base, str)
        """
        TODO: ??? : str | `None`
        """

        self.generator = none_or(generator, str)
        """
        TODO: ??? : str | `None`
        """

        self.case = none_or(case, str)
        """
        TODO: ??? : str | `None`
        """

        self.namespaces = none_or(namespaces, list)
        """
        A list of :class:`mwtypes.Namespace` | `None`
        """

    @classmethod
    def load_namespaces(cls, element):
        namespaces = []
        for sub_element in element:
            tag = sub_element.tag

            if tag == "namespace":
                namespace = Namespace.from_element(sub_element)
                namespaces.append(namespace)
            else:
                assert False, "This should never happen"

        return namespaces

    @classmethod
    def from_element(cls, element):
        assert element.tag == "siteinfo", element.tag
        name = None
        dbname = None
        base = None
        generator = None
        case = None
        namespaces = None

        for sub_element in element:
            if sub_element.tag == 'sitename':
                name = sub_element.text
            elif sub_element.tag == 'dbname':
                dbname = sub_element.text
            elif sub_element.tag == 'base':
                base = sub_element.text
            elif sub_element.tag == 'base':
                base = sub_element.text
            elif sub_element.tag == 'generator':
                generator = sub_element.text
            elif sub_element.tag == 'case':
                case = sub_element.text
            elif sub_element.tag == 'namespaces':
                namespaces = cls.load_namespaces(sub_element)

        return cls(name=name, dbname=dbname, base=base, generator=generator,
                   case=case, namespaces=namespaces)
