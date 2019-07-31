#!/usr/bin/env python
# -*- coding: utf-8 -*-
# stdlib
import base64
import urllib
import urllib2
import json
import logging


class EasyException(Exception):
    def __init__(self, code, code_explain, error, data):
        """
        easyops的错误异常
        :param code: 返回码
        :param code_explain: 详细定位问题用的错误字符串解释
        :param error: 给用户看的美观的字符串解释
        :param data: 额外的返回数据
        """
        self.code = code
        self.code_explain = code_explain
        self.error = error
        self.data = data


class UnknownException(EasyException):
    def __init__(self, error):
        self.code = 100010
        self.code_explain = "ERR_UNKNOWN"
        self.error = error
        self.data = {}


class NameServiceException(EasyException):
    def __init__(self, session_id):
        self.code = 100013
        self.code_explain = "ERR_UNAVAILABLE"
        self.error = "name service error, session_id={}".format(session_id)
        self.data = {}


def do_http(method, url, params={}, headers={}, timeout=10):
    """
    do http request
    """
    method = method.upper()
    if not isinstance(params, dict) or not isinstance(headers, dict):
        raise Exception('params and headers must be dict')
    if len(params) > 0:
        if method == 'GET':
            data = urllib.urlencode(params)
            request = urllib2.Request('%s?%s' % (url, data))
        else:
            if headers.get('Content-Type', '').lower() == 'application/json':
                data = json.dumps(params)
            else:
                data = urllib.urlencode(params)
            request = urllib2.Request(url, data=data)
    else:
        request = urllib2.Request(url)
    for key, val in headers.items():
        request.add_header(key, val)
    request.get_method = lambda: method
    response = urllib2.urlopen(request, timeout=timeout)
    data = response.read()
    response.close()
    return data


def do_api_request(
        method, src_name, dst_name, host, uri, params={}, headers={}, timeout=10, auth_user="", auth_password="", server_ip="", server_port=0
):
    headers['Content-Type'] = 'application/json'
    if host:
        headers['Host'] = host
    if auth_user:
        base64string = base64.b64encode('%s:%s' % (auth_user, auth_password))
        headers["Authorization"] = "Basic %s" % base64string

    if server_ip != "" and server_port != 0:
        ip = server_ip
        port = server_port
    else:
        import ens_api
        session_id, ip, port = ens_api.get_service_by_name(src_name, dst_name)
        if session_id <= 0:
            raise NameServiceException(session_id)

    url = "http://{ip}:{port}{uri}".format(ip=ip, port=port, uri=uri)
    data = None
    try:
        data = do_http(method, url, params, headers, timeout)
        data_obj = json.loads(data)
        logging.debug(
            "method: {method}, url: {url}, params: {params}, headers: {headers}, timeout: {timeout}, data: {data}".
                format(method=method, url=url, params=params, headers=headers, timeout=timeout, data=data_obj)
        )
    except ValueError as e:
        logging.error(
            "json decode error, method={0} url={1}, "
            "params={2}, headers={3}, timeout={4}, data={5}".format(method, url, params, headers, timeout, data)
        )
        raise UnknownException(e)
    except urllib2.HTTPError as e:
        data = e.read()
        logging.error(
            "json decode error, method={0} url={1}, "
            "params={2}, headers={3}, timeout={4}, data={5}".format(method, url, params, headers, timeout, data)
        )
        try:
            data_obj = json.loads(data)
        except Exception, e:
            raise UnknownException(e)
        raise EasyException(data_obj["code"], data_obj.get("codeExplain"), data_obj.get("error"), data_obj.get("data"))
    else:
        return data_obj
