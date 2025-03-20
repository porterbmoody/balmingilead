---
title: "pytube"
featured_image: "/images/python.jpeg"
date: 2025-03-19T10:58:08-04:00
tags: ["pytube", 'python']
---

# pytube

I tried this and this is the error I got

```{python}
pytube https://www.youtube.com/watch?v=PsVgYHSmDu0

```

Loading video...
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Scripts\pytube.exe\__main__.py", line 7, in <module>
    sys.exit(main())
             ~~~~^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\cli.py", line 53, in main
    _perform_args_on_youtube(youtube, args)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\cli.py", line 60, in _perform_args_on_youtube
    download_highest_resolution_progressive(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        youtube=youtube, resolution="highest", target=args.target
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\cli.py", line 474, in download_highest_resolution_progressive
    stream = youtube.streams.get_highest_resolution()
             ^^^^^^^^^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\__main__.py", line 296, in streams
    return StreamQuery(self.fmt_streams)
                       ^^^^^^^^^^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\__main__.py", line 176, in fmt_streams
    stream_manifest = extract.apply_descrambler(self.streaming_data)
                                                ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\__main__.py", line 157, in streaming_data
    if 'streamingData' in self.vid_info:
                          ^^^^^^^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\__main__.py", line 246, in vid_info
    innertube_response = innertube.player(self.video_id)
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\innertube.py", line 448, in player
    return self._call_api(endpoint, query, self.base_data)
           ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\innertube.py", line 390, in _call_api
    response = request._execute_request(
        endpoint_url,
        data=data
    )
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\request.py", line 37, in _execute_request
    return urlopen(request, timeout=timeout)  # nosec
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\urllib\request.py", line 189, in urlopen
    return opener.open(url, data, timeout)
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\urllib\request.py", line 495, in open
    response = meth(req, response)
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\urllib\request.py", line 604, in http_response
    response = self.parent.error(
        'http', request, response, code, msg, hdrs)
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\urllib\request.py", line 533, in error
    return self._call_chain(*args)
           ~~~~~~~~~~~~~~~~^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\urllib\request.py", line 466, in _call_chain
    result = func(*args)
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\urllib\request.py", line 613, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 400: Bad Request
PS C:\Users\porte\Documents\balmingilead> pytube https://www.youtube.com/watch?v=PsVgYHSmDu0
Loading video...
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Scripts\pytube.exe\__main__.py", line 7, in <module>
    sys.exit(main())
             ~~~~^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\cli.py", line 53, in main
    _perform_args_on_youtube(youtube, args)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\cli.py", line 60, in _perform_args_on_youtube
    download_highest_resolution_progressive(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        youtube=youtube, resolution="highest", target=args.target
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\cli.py", line 474, in download_highest_resolution_progressive
    stream = youtube.streams.get_highest_resolution()
             ^^^^^^^^^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\__main__.py", line 296, in streams
    return StreamQuery(self.fmt_streams)
                       ^^^^^^^^^^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\__main__.py", line 176, in fmt_streams
    stream_manifest = extract.apply_descrambler(self.streaming_data)
                                                ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\__main__.py", line 157, in streaming_data
    if 'streamingData' in self.vid_info:
                          ^^^^^^^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\__main__.py", line 246, in vid_info
    innertube_response = innertube.player(self.video_id)
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\innertube.py", line 448, in player
    return self._call_api(endpoint, query, self.base_data)
           ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\innertube.py", line 390, in _call_api
    response = request._execute_request(
        endpoint_url,
    ...<2 lines>...
        data=data
    )
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\site-packages\pytube\request.py", line 37, in _execute_request
    return urlopen(request, timeout=timeout)  # nosec
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\urllib\request.py", line 189, in urlopen
    return opener.open(url, data, timeout)
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\urllib\request.py", line 495, in open
    response = meth(req, response)
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\urllib\request.py", line 604, in http_response
    response = self.parent.error(
        'http', request, response, code, msg, hdrs)
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\urllib\request.py", line 533, in error
    return self._call_chain(*args)
           ~~~~~~~~~~~~~~~~^^^^^^^
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\urllib\request.py", line 466, in _call_chain
    result = func(*args)
  File "C:\Users\porte\AppData\Local\Programs\Python\Python313\Lib\urllib\request.py", line 613, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 400: Bad Request

