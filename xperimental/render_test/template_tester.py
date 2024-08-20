import os
import yaml
import jinja2
import json

def print_with_color(text, color="default"):
  """
  Prints the text in the specified color.

  Parameters
  ----------
  text : str
      The text to be printed.
  color : str, optional
      The color name as a string. Supported colors are:
      "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
      "default". The default is "default".

  Returns
  -------
  None
  """
  colors = {
    "default": "\033[39m",
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m"
  }

  # Get the escape code for the selected color, defaulting to "default"
  color_code = colors.get(color.lower(), colors["default"])

  # Print the text with the selected color
  print(f"{color_code}{text}\033[0m", flush=True)
  return



def validate_json(rendered_output):
  """
  Validates if the rendered output is valid JSON.

  Parameters
  ----------
  rendered_output : str
      The rendered template output as a string.

  Returns
  -------
  bool
      True if the rendered output is valid JSON, False otherwise.
  """
  try:
    json.loads(rendered_output)
    return True
  except json.JSONDecodeError as e:
    print(f"JSON validation error: {e}")
    return False


def load_inventory_vars(inventory_file):
  """
  Loads variables from the 'all:vars' section of an Ansible inventory file.

  Parameters
  ----------
  inventory_file : str
      Path to the Ansible inventory file.

  Returns
  -------
  dict
      A dictionary of variables found under 'all:vars'.
  """
  with open(inventory_file, 'r') as file:
    inventory = yaml.safe_load(file)

  # Extract variables from the 'all:vars' section
  vars_dict = inventory.get('all', {}).get('vars', {})
  return vars_dict


def render_template(template_name, variables):
  """
  Renders a Jinja2 template with the provided variables.

  Parameters
  ----------
  template_name : str
      The name of the template file.
  variables : dict
      A dictionary containing the variables to feed into the template.

  Returns
  -------
  str
      The rendered template as a string.
  """
  # Set up the Jinja2 environment to load templates from the current directory
  template_dir = os.path.dirname(os.path.abspath(template_name))
  env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

  # Load the template file
  template = env.get_template(os.path.basename(template_name))

  # Render the template with the provided variables
  return template.render(variables)


if __name__ == "__main__":
  # print CWD
  print_with_color(os.getcwd())
  FN_TEMPLATE = './aixp_factory/roles/aixp04_deploy/templates/admin_pipeline.json.j2'
  FN_INVENTORY = './aixp_factory/other/.hosts.yml'
  
  vars_dict = load_inventory_vars(FN_INVENTORY)
  # Example template file

  # Render the template and print the result
  rendered_output = render_template(FN_TEMPLATE, vars_dict)
  print_with_color(rendered_output)
  
  
  # Validate the rendered output as JSON
  if validate_json(rendered_output):
    print_with_color("Rendered output is valid JSON.", color='green')
  else:
    print_with_color("Rendered output is not valid JSON.", color='red')