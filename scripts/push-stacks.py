# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import subprocess


# Get parameters
project = os.environ.get('PROJECT', '')
environment = os.environ.get('ENVIRONMENT', '')

# Set environment
if environment:
    for key, value in os.environ.items():
        suffix = '--' + environment
        if key.endswith(suffix):
            key = key.replace(suffix, '')
            os.environ[key] = value
    environment = environment.lower()

# Push stacks
for name in os.listdir('stacks'):
    try:
        name, ext = name.split('.')
        if project:
            cloud_name = '--'.join([project, name, environment])
    except Exception:
        continue
    if ext != 'yml':
        continue
    command = ''
    command += 'docker-cloud stack inspect {cloud_name} || '
    command += 'docker-cloud stack create --sync -f stacks/{name}.yml -n {cloud_name} && '
    command += 'docker-cloud stack update --sync -f stacks/{name}.yml {cloud_name}'
    command = command.format(name=name, cloud_name=cloud_name)
    subprocess.call(command, shell=True)
    print('Pushed stack: "%s" as "%s"' % (name, cloud_name))
