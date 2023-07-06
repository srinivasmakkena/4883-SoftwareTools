from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# from pytubeex import get_ytstreams
import youtube_dl
import requests
import os
from urllib.parse import urlparse
import time,re,json


def get_size_in_human_readable(size_in_bytes):
    # Helper function to convert size in bytes to human-readable format
    if size_in_bytes == 0:
        return "0 B"
    size_units = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_in_bytes >= 1024 and i < len(size_units) - 1:
        size_in_bytes /= 1024
        i += 1
    return "{:.2f} {}".format(size_in_bytes, size_units[i])

def get_ytstreams(video_url):
    ydl = youtube_dl.YoutubeDL()
    # video_url = 'https://www.youtube.com/watch?v=k4rLJD7E0D0'
    info_dict = ydl.extract_info(video_url, download=False)
    streams=[]
    if 'formats' in info_dict:
        for stream in info_dict['formats']:
            stream['title'] = info_dict.get('title')
            stream['title'] = info_dict.get('title')
            size_in_bytes = stream.get('filesize')
            stream['size'] = get_size_in_human_readable(size_in_bytes) if size_in_bytes is not None else None
            streams.append(stream)
    return streams


def index(request):
    return render(request, "index.html")

def getstreams(request):
    url=request.GET.get('url')
    video_id = re.findall(r"watch\?v=([A-Za-z0-9_-]+)", url)[0]
    vurl='https://www.youtube.com/embed/'+video_id
    context={'videoSrc':vurl,'dropdown1Options':[],'dropdown2Options':[]}
    try:
        streams=get_ytstreams(url)
        acodec_not_none = []
        vcodec_not_none = []
        acodec_vcodec_combinations=[]
        for item in streams:
            if item['acodec'] != 'none':
                acodec_not_none.append(item)
            if item['vcodec'] != 'none':
                vcodec_not_none.append(item)
            if item['vcodec'] != 'none' and item['acodec'] != 'none':
                 context['dropdown1Options'].append(item)
        # acodec_vcodec_combinations =  [(a['acodec']," ", v['vcodec']) for a in acodec_not_none for v in vcodec_not_none]
        acodec_vcodec_combinations =  [(i['format_id']+' '+ i['format_note'],  i['acodec'], i['vcodec']) for i in streams]
        
        for i in streams:
            # print(i['acodec'],i['vcodec'])
            context['dropdown1Options'].append(i)
        print(streams[0])
    except Exception as e:
        # Print the exception
        print(f"An exception occurred: {e}")
    print(url)
    return JsonResponse(context)

def start_download(request):
    if 'dropdownValue' in request.GET:
        dropdown_value = request.GET['dropdownValue']
        selected_option = request.GET.get('dropdownValue')
        #   option_object = json.loads(selected_option)
        print(selected_option)
    context={}
    return JsonResponse(context)