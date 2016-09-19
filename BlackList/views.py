# coding=utf-8
from __future__ import unicode_literals

from django.shortcuts import render
import os
import pandas as pd
import shelve
# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import Shop
from django.template import loader
from django.http import Http404



class IndexView(generic.ListView):
	template_name = 'BlackList/index.html'
	context_object_name = 'latest_shop_list'

	def get_queryset(self):

		"""Return the last five published questions."""
		return Shop.objects.order_by('-update_date')[:5]
#
# def index(request):
#     # # latest_shop_list = Shop.objects.order_by('-update_date')[:5]
#     # # output = ', '.join([s.shop_name for s in latest_shop_list])
#     # # return HttpResponse(output)
#     # latest_shop_list = Shop.objects.order_by('-update_date')[:5]
#     # template = loader.get_template('BlackList/index.html')
#     # context = {
#     #     'latest_shop_list': latest_shop_list,
#     # }
#     s = '<p><a href = "/blacklist/commentdisp">Comment Restructured By Keywords(Draft)</a></p>\n<p><a href = "/blacklist/crawler">Log of Crawler</a></p>'
#     return HttpResponse(s)





def detail(request, shop_id):
    try:
        shop = Shop.objects.get(pk=shop_id)
    except Shop.DoesNotExist:
        raise Http404("Shop does not exist")
    return render(request, 'BlackList/detail.html', {'shop': shop})


def crawlerStatus(request):
	f = open("/mnt/WhiteMouseLab/Crawler/logging.record");
	L = f.read();
	f.close();
	return HttpResponse(L);


def commentsNLPResult(request):
	"""
	<table border="1">
	<tr>
	<td>Row 1, cell 1</td>
	<td>Row 1, cell 2</td>
	</tr>
	</table>
	<tr>
	<th>Heading</th>
	<th>Another Heading</th>
	</tr>
	"""

	s = '<table border="1">\n<tr>\nComments On Shops Related To Stomache Illness\n</tr>\n'
	
	s += "<tr><td>Shop_ID</td><td>Author</td><td>Keywords</td><td>Comments</td></tr>"

	data_path = "/Users/admin/Code/ProjectCode/UndecidedProject/CrawlerAboutDianping/";
	csv_path = os.path.join(data_path, "shop.csv");
	comment_path = os.path.join(data_path, "comments");
	csvdata = pd.read_csv(csv_path);
	vocabulary = ["拉肚子", "腹泄", "闹肚子","胃疼","肚子疼","肚子痛",
	"不新鲜","臭","原料","发霉","异味",'变质','变味','剩下','坏','馊','酸','腥',	'吐','拉','疼','发烧','不适','不舒服',
	'脏','乱','不卫生','不干净','老鼠','蟑螂',
	'苍蝇','蚊子','头发','夹子','玻璃','钢丝球','沙子','石头'];

	for ind in csvdata.index:
		url_id = csvdata["shop_id"][ind];
		filepath =  os.path.join(comment_path, str(url_id) + ".dat.db");
		shevepath = os.path.join(comment_path, str(url_id) + ".dat");
		if os.path.exists(filepath):
			rec = shelve.open(shevepath);
			lastauthor = None;
			for key in rec.keys():
				comments = rec[key];
				for author in comments:
					comm = comments[author];
					comm = comm.decode('utf-8')
					for word in vocabulary:
						if word in comm:
							if lastauthor!= None and int(author)== int(lastauthor):
								lastauthor = author;
							else:
								lastauthor = author;
								# print "%s : %s" % (author, comm);
								shop_id = '<a href="http://www.dianping.com/shop/%s">%s</a>' % (url_id, csvdata["shop_name"][ind].decode('utf-8'))
								s += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n' % (shop_id, author, word, comm);
	return HttpResponse(s);


