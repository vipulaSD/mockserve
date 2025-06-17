import re

from faker import Faker
from jinja2 import Template


class ResponseGenerator:
    """Response generator"""

    def __init__(self):
        self.faker = Faker()

    def _render_string(self, s: str):
        pattern = r"{{\s*(\w+)\s*}}"
        matches = re.findall(pattern, s)
        context = {
            matcch: getattr(self.faker, matcch)()
            for matcch in matches
            if hasattr(self.faker, matcch)
        }
        return Template(s).render(context)

    def render_template(self, template_obj):
        if isinstance(template_obj, str):
            return self._render_string(template_obj)
        elif isinstance(template_obj, dict):
            return {k: self.render_template(v) for k, v in template_obj.items()}
        elif isinstance(template_obj, list):
            return [self.render_template(itm) for itm in template_obj]

        return template_obj
