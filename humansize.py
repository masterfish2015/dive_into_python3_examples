#!/usr/bin/python3
# -*- coding: utf-8 -*-
SUFFIXES = {
	1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
	1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilo_is_1024 = True):
	''' Convert a file size to human-readable form

	keyword arguments:
	size--------------file size in bytes
	a_kilo_is_1024----if True(default), use multiples of 1024, or 1000

	returns: string
	'''
	if size < 0 :
		raise ValueError('number must be non-negative')

	multiple = 1024 if a_kilo_is_1024 else 1000
	for suffix in SUFFIXES[multiple]:
		size /= multiple
		if size < multiple:
			return '{0:.1f} {1}'.format(size, suffix)

	raise ValueError('number too large')


if __name__ == '__main__' :
	print(approximate_size(100000000000, False))
	print(approximate_size(100000000000))
