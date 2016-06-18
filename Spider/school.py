#!/usr/bin/env python
#coding=utf-8
#Author:Wanglj
#date:20150307

import urllib2
from lxml import etree
from lxml.html.clean import clean_html, Cleaner
import string
import sys
import os
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')


class School:
	def __init__(self, start_url):
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
		self.start_url = start_url
		self.url_list = []
		self.school_layer = {}
		self.school_layer[start_url] = {}
		self.fp = open("result", "a+")



	def get_second_layer(self, url):
		self.fp.write(url + "\n")
		print url


		req = urllib2.Request(url, headers=self.headers)
		response = urllib2.urlopen(req)
		page = response.read()
		page = etree.HTML(page)
		hrefs = page.xpath(u"//*/a")
		for href in hrefs:
			if href.attrib.has_key("href"):
				if href.attrib['href'].strip("\\").strip(" ") not in self.url_list:
					self.school_layer[self.start_url][url].append(href.attrib['href'].strip(" "))
					self.url_list.append(href.attrib['href'].strip("\\").strip(" "))
					self.fp.write("                         "+href.attrib['href'].strip("\\").strip(" ")+"\n")


	def get_url(self):
		self.url_list.append(self.start_url)
		second_url = []
		req = urllib2.Request(self.start_url, headers=self.headers)
		response = urllib2.urlopen(req)
		page = response.read()
		page = etree.HTML(page)
		hrefs = page.xpath(u"//*[@id='quick_link']/a")
		for href in hrefs:
			#self.url_list.append(href.attrib['href'])
			
			url = href.attrib['href'].strip(" ")
			if "http" not in url:
				if "ftp" in url:
					continue
				url = "http://www.hitwh.edu.cn/" + url
			second_url.append(url)
			self.school_layer[self.start_url][url] = []
			self.url_list.append(url.strip("\\"))

		hrefs = page.xpath(u"//*[@id='top_nav_right']/a")
		for href in hrefs:
			#if "http" in href.attrib['href']:
			url = href.attrib['href'].strip(" ")
			if "http" not in url:
				if "ftp" in url:
					continue
				url = "http://www.hitwh.edu.cn/" + url
			second_url.append(url)
			self.school_layer[self.start_url][url] = []
			self.url_list.append(url.strip("\\"))

		for url in second_url:
			self.get_second_layer(url)

		print self.school_layer
		#fp = open("result", "a+")
		
		#print self.school_layer
		# for result in self.url_list:
		# 	print result

def main():
	sc  = School("http://www.hitwh.edu.cn")
	sc.get_url()


if __name__ == '__main__':
	main()
