# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import io
import os
import json
import subprocess


# Push stacks
for filename in os.listdir('stacks'):
    try:
        name, ext = filename.split('.')
    except Exception:
        continue
    if ext != 'yml':
        continue
    meta = io.open('stacks/%s' % filename, encoding='utf-8').readline()
    meta = json.loads(meta.replace('#', '', 1).strip())
    for environment in meta['environments']:
        for key, value in list(os.environ.items()):
            suffix = '__' + environment.upper()
            if key.endswith(suffix):
                key = key.replace(suffix, '')
                os.environ[key] = value
        cloud_name = '--'.join([meta['namespace'].upper(), name, environment.upper()])
        command = ''
        command += 'docker-cloud stack inspect {cloud_name} || '
        command += 'docker-cloud stack create --sync -f stacks/{name}.yml -n {cloud_name} && '
        command += 'docker-cloud stack update --sync -f stacks/{name}.yml {cloud_name}'
        command = command.format(name=name, cloud_name=cloud_name)
        code = subprocess.call(command, shell=True)
        if code:
            exit(code)
        print('Pushed stack: "%s" as "%s"' % (name, cloud_name))
