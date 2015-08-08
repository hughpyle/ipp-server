from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

def read_http(f):
	first_line = f.readline()
	if not first_line.startswith(b'POST / HTTP/'):
		raise ValueError('Invalid request')
	while True:
		line = f.readline()
		if line.rstrip(b'\r\n') == '':
			break

def write_http(f):
	f.write(b'\r\n'.join((
		b'HTTP/1.1 200 OK',
		b'Server: ipp-server',
		b'')))

def write_http_error(f):
	f.write(b'\r\n'.join((
		b'HTTP/1.1 500 Server Error',
		b'Server: ipp-server',
		b'',
		b'There was an error.',
		b'')))