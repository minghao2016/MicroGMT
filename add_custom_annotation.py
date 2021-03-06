#!/usr/bin/python

import time
import os
import sys
import subprocess
import argparse
from functions import *

def main():
	parser = argparse.ArgumentParser(description='Add custom annotation', \
		formatter_class=argparse.RawTextHelpFormatter)
	group1 = parser.add_argument_group('Mandatory inputs')
	group1.add_argument('-i', type=str, dest='in_table', \
		required=True, \
		help='Input summary table (Only ".all.form2.txt" tables)')
	group1.add_argument('-a', type=str, dest='custom_annot', \
		required=True, \
		help='Input custom annotation table')
	group1.add_argument('-d', type=str, dest='out_dir', \
		required=True, \
		help='Output directory')

	group2 = parser.add_argument_group('Optional arguments')
	group2.add_argument('-p', type=str, dest='out_pref', \
		default='annotated', \
		help='Prefix of the output annotated summary tables. Do not include path, except for folder name(s) inside output directory!')
	group2.add_argument('-l', type=str, dest='log', default="Add_custom_annotation.log", \
		help='Name of the log file [Add_custom_annotation.log]')

	args = parser.parse_args()

	param = {}
	param['out_dir'] = os.path.join(os.getcwd(),args.out_dir)
	param['out_pref'] = args.out_pref
	param['in_table'] = os.path.join(os.getcwd(),args.in_table)
	param['custom_annot'] = os.path.join(os.getcwd(),args.custom_annot)
	param['out_log']=os.path.join(param['out_dir'],args.log)

	with open(param['out_log'],'w') as f:
		f.write('[MicroGMT ' + \
			time.asctime( time.localtime(time.time()) ) + \
			'] Add custom annotation started.\n')

	f.close()

	log_print(param['out_log'],'==================== MicroGMT ====================')
	log_print(param['out_log'],'              Add_custom_annotation')
	log_print(param['out_log'],'              Version 1.3  (June 2020)')
	log_print(param['out_log'],'   Bug report: Yue Xing <yue.july.xing@gmail.com>')
	log_print(param['out_log'],'======================================================')

	custom_annotation(param['in_table'],param['custom_annot'],param['out_dir'],param['out_pref'])
	log_print(param['out_log'],"Successfully completed!")

if __name__ == '__main__':
	main()
