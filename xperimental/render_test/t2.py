from jinja2 import Template

# Input data
aixp_auto_warmup_models = [
    "lowres_general_detector",
]

# Jinja2 template
template_str = """
"AUTO_WARMUPS" : {
{% for model in aixp_auto_warmup_models %}
  "{{ model }}" : {}{% if not loop.last %},{% endif %}
{% endfor %}
}
"""

# Compile the template
template = Template(template_str)

# Render the template with input data
rendered_output = template.render(aixp_auto_warmup_models=aixp_auto_warmup_models)

print(rendered_output.strip())
