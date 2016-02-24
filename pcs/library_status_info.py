from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from lxml import etree
import settings

from errors import ReportItem
import error_codes
from errors import LibraryError

'''
The intention is put there knowledge about cluster state structure.
Hide information about underlaying xml is desired too.
'''

class _Attrs(object):
    def __init__(self, owner_name, attrib, required_attrs):
        '''
        attrib lxml.etree._Attrib - wrapped attribute collection
        required_attrs dict of required atribute names object_name:xml_attribute
        '''
        self.owner_name = owner_name
        self.attrib = attrib
        self.required_attrs = required_attrs

    def __getattr__(self, name):
        if name in self.required_attrs.keys():
            try:
                attr_specification = self.required_attrs[name]
                if isinstance(attr_specification, basestring):
                    return self.attrib[attr_specification]
                else:
                    attr_name, attr_transform = attr_specification
                    return attr_transform(self.attrib[attr_name])
            except KeyError:
                raise AttributeError(
                    "Missing attribute '{0}' ('{1}' in source) in '{2}'"
                    .format(name, self.required_attrs[name], self.owner_name)
                )

        raise AttributeError(
            "'{0}' does not declare attribute '{1}'"
            .format(self.owner_name, name)
        )

class _Children(object):
    def __init__(self, owner_name, dom_part, children, sections):
        self.owner_name = owner_name
        self.dom_part = dom_part
        self.children = children
        self.sections = sections

    def __getattr__(self, name):
        if name in self.children.keys():
            element_name, wrapper = self.children[name]
            return [
                wrapper(element)
                for element in self.dom_part.findall('.//' + element_name)
            ]

        if name in self.sections.keys():
            element_name, wrapper = self.sections[name]
            return wrapper(self.dom_part.findall('.//' + element_name)[0])

        raise AttributeError(
            "'{0}' does not declare child or section '{1}'"
            .format(self.owner_name, name)
        )

class _Element(object):
    required_attrs = {}
    children = {}
    sections = {}

    def __init__(self, dom_part):
        self.dom_part = dom_part
        self.attrs = _Attrs(
            self.__class__.__name__,
            self.dom_part.attrib,
            self.required_attrs
        )
        self.children_access = _Children(
            self.__class__.__name__,
            self.dom_part,
            self.children,
            self.sections,
        )

    def __getattr__(self, name):
        return getattr(self.children_access, name)

class _SummaryNodes(_Element):
    required_attrs = {
        'count': ('number', lambda x: int(x)),
    }

class _SummaryResources(_Element):
    required_attrs = {
        'count': ('number', lambda x: int(x)),
    }

class _SummarySection(_Element):
    sections = {
        'nodes': ('nodes_configured', _SummaryNodes),
        'resources': ('resources_configured', _SummaryResources),
    }

class _Node(_Element):
    required_attrs = {
        'name': 'name',
        'type': 'type',
    }

class _NodeSection(_Element):
    children = {
        'nodes': ('node', _Node),
    }

def _get_valid_cluster_state_dom(xml):
    try:
        dom = etree.fromstring(xml)
        etree.RelaxNG(file=settings.crm_mon_schema).assertValid(dom)
        return dom
    except (etree.XMLSyntaxError, etree.DocumentInvalid):
        raise LibraryError(ReportItem.error(
            error_codes.BAD_CLUSTER_STATE_FORMAT,
            'pacemaker produced state information in invalid format',
        ))

class ClusterState(_Element):
    sections = {
        'summary': ('summary', _SummarySection),
        'node_section': ('nodes', _NodeSection),
    }

    def __init__(self, xml):
        self.dom = _get_valid_cluster_state_dom(xml)
        super(ClusterState, self).__init__(self.dom)
