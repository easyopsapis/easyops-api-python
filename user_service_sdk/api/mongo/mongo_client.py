# -*- coding: utf-8 -*-

import insert_pb2

import google.protobuf.empty_pb2

import remove_pb2

import remove_all_pb2

import search_pb2

import search_all_pb2

import search_one_pb2

import update_pb2

import update_all_pb2

import utils.http_util
import google.protobuf.json_format


class MongoClient(object):
    def __init__(self, server_ip="", server_port=0, service_name="", host=""):
        """
        初始化client
        :param server_ip: 指定sdk请求的server_ip，为空时走名字服务路由
        :param server_port: 指定sdk请求的server_port，与server_ip一起使用, 为空时走名字服务路由
        :param service_name: 指定sdk请求的service_name, 为空时按契约名称路由。如果server_ip和service_name同时设置，server_ip优先级更高
        :param host: 指定sdk请求服务的host名称, 如cmdb.easyops-only.com
        """
        if server_ip == "" and server_port != 0 or server_ip != "" and server_port == 0:
            raise Exception("server_ip和server_port必须同时指定")
        self._server_ip = server_ip
        self._server_port = server_port
        self._service_name = service_name
        self._host = host

    
    def insert(self, request, org, user, timeout=10):
        # type: (insert_pb2.InsertRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        mongodb搜索[内部]
        :param request: insert请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: google.protobuf.empty_pb2.Empty
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.mongo.Insert"
        uri = "/api/v1/mongo/{collection}/documents/insert".format(
            collection=request.collection,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def remove(self, request, org, user, timeout=10):
        # type: (remove_pb2.RemoveRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        mongodb删除记录[内部]
        :param request: remove请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: google.protobuf.empty_pb2.Empty
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.mongo.Remove"
        uri = "/api/v1/mongo/{collection}/documents/remove".format(
            collection=request.collection,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def remove_all(self, request, org, user, timeout=10):
        # type: (remove_all_pb2.RemoveAllRequest, int, str, int) -> remove_all_pb2.RemoveAllResponse
        """
        mongodb批量删除记录[内部]
        :param request: remove_all请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: remove_all_pb2.RemoveAllResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.mongo.RemoveAll"
        uri = "/api/v1/mongo/{collection}/documents/remove/all".format(
            collection=request.collection,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = remove_all_pb2.RemoveAllResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search(self, request, org, user, timeout=10):
        # type: (search_pb2.SearchRequest, int, str, int) -> search_pb2.SearchResponse
        """
        mongodb搜索[内部]
        :param request: search请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: search_pb2.SearchResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.mongo.Search"
        uri = "/api/v1/mongo/{collection}/documents/search".format(
            collection=request.collection,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = search_pb2.SearchResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_all(self, request, org, user, timeout=10):
        # type: (search_all_pb2.SearchAllRequest, int, str, int) -> search_all_pb2.SearchAllResponse
        """
        mongodb搜索[内部]
        :param request: search_all请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: search_all_pb2.SearchAllResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.mongo.SearchAll"
        uri = "/api/v1/mongo/{collection}/documents/search/all".format(
            collection=request.collection,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = search_all_pb2.SearchAllResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_one(self, request, org, user, timeout=10):
        # type: (search_one_pb2.SearchOneRequest, int, str, int) -> search_one_pb2.SearchOneResponse
        """
        mongodb搜索[内部]
        :param request: search_one请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: search_one_pb2.SearchOneResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.mongo.SearchOne"
        uri = "/api/v1/mongo/{collection}/documents/search/one".format(
            collection=request.collection,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = search_one_pb2.SearchOneResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update(self, request, org, user, timeout=10):
        # type: (update_pb2.UpdateRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        mongodb更新[内部]
        :param request: update请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: google.protobuf.empty_pb2.Empty
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.mongo.Update"
        uri = "/api/v1/mongo/{collection}/documents/update".format(
            collection=request.collection,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_all(self, request, org, user, timeout=10):
        # type: (update_all_pb2.UpdateAllRequest, int, str, int) -> update_all_pb2.UpdateAllResponse
        """
        mongodb批量更新[内部]
        :param request: update_all请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: update_all_pb2.UpdateAllResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.mongo.UpdateAll"
        uri = "/api/v1/mongo/{collection}/documents/update/all".format(
            collection=request.collection,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = update_all_pb2.UpdateAllResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
