#!/usr/bin/python
# -*- coding: UTF-8 -*-

import jinja2
import json5
from collections import namedtuple
import sys
import getopt
import glob
import os
import errno
# import execjs
import utils


class OptArg:
    router_templ_file_path = './config/router.tmpl'
    view_templ_file_path = './config/view.tmpl'
    config_file_path = './config/config.json5'
    output_file_path = './src/'

    def __init__(self):
        pass


def underscore(s):
    return s.replace(" ", "_").replace("-", "_")


def get_opt_arg():
    optarg = OptArg()
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "hc:o:",
            ["config_file=", "output_file_path="]
        )
    except getopt.GetoptError:
        print('-c <code_file> -o <output_file_path>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('Usage: codegen -t <template_file> -c <config_file> -o <output_file_path>')
            sys.exit()
        elif opt in ("-c", "--config_file"):  # config file path
            optarg.config_file_path = arg
        elif opt in ("-o", "--output_file_path"):  # output file path
            optarg.output_file_path = arg
    return optarg


def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json5_to_obj(data): return json5.loads(data, object_hook=_json_object_hook)


def read_config(config_file_path):
    content = open(config_file_path, 'r').read()
    return json5_to_obj(content)


def write_to(file_path, content):
    # print(os.path.dirname(file_path))
    file_dir = os.path.dirname(file_path)
    if not os.path.exists(file_dir):
        try:
            os.makedirs(file_dir)
        except OSError as err:  # Guard against race condition
            if err.errno != errno.EEXIST:
                raise

    f = open(file_path, "w")
    try:
        f.write(content)
    finally:
        f.close()


if __name__ == '__main__':
    opt_arg = get_opt_arg()

    # init environment
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    env.filters['underscore'] = underscore
    env.filters['pascalcase'] = utils.pascalcase
    env.filters['camelcase'] = utils.camelcase

    # get template
    def get_file_templ(file_path):
        return env.get_template(file_path)
    
    
    def render_file(_template, _data, _path):
        output_file = _template.render(_data)
        output_file_path = env.from_string(_path).render(_data)
        if '' == output_file_path:
            raise ValueError('output path is empty')
        write_to(output_file_path, output_file)
    

    router_template = get_file_templ(opt_arg.router_templ_file_path)
    view_template = get_file_templ(opt_arg.view_templ_file_path)
        
    config = read_config(opt_arg.config_file_path)


    render_file(router_template, config._asdict(), opt_arg.output_file_path + 'router.js')

    for view in config.views:
        render_file (view_template, view._asdict(), opt_arg.output_file_path + view.name +'/index.vue')

        