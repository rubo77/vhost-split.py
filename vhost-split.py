#!/usr/bin/env python
#
# @file   vhost-split.py
# @author Aleix Conchillo Flaque <aconchillo@gmail.com>
# @date   Wed Feb 14, 2007 12:50
# @brief  Splits <VirtualHost> entries into multiple files.
#

import re
import sys

if len(sys.argv) == 1:
  print "Usage: vhost-split.py <config_file>"
  sys.exit(1)

input = open(sys.argv[1], "rb")

p_comment = re.compile(r"[\s\t]*#.*")
p_begin = re.compile(r"<VirtualHost[^>]+>")
p_end = re.compile(r"</VirtualHost>")
p_server = re.compile(r"ServerName[\s\t]*(.*)")
file_name = "default"
found = False
commented = False
servers = {}
new_lines = []
n_total = 0
n_commented = 0
for line in input:
  if not found:
    m = p_begin.search(line)
    if m:
      found = True
      file_name = "default"
      new_lines.append(line)
      m = p_comment.search(line)
      commented = False
      if m:
        commented = True
  else:
    new_lines.append(line)
    m = p_server.search(line)
    if m:
      file_name = m.group(1).strip()
    m = p_end.search(line)
    if m:
      found = False
      if file_name in servers:
        servers[file_name] += 1
        file_name += "-%d" % servers[file_name]
      else:
        servers[file_name] = 0
      print "Creating virtual host file... %s" % file_name,
      if commented:
        n_commented += 1
        print " (commented)"
      else:
        print
      output = open(file_name, "wb")
      output.writelines(new_lines)
      output.close()
      new_lines = []
      n_total += 1

input.close()

print "\n%d virtual hosts created. %d commented.\n" % (n_total, n_commented)
