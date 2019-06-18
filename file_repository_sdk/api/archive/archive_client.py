# -*- coding: utf-8 -*-

import create_pb2

import create_and_register_pb2

import delete_archive_pb2

import delete_archive_v2_pb2

import get_archive_diff_size_pb2

import get_archive_file_info_pb2

import get_archive_list_pb2

import get_archive_sign_info_pb2

import get_archive_size_pb2

import model.file_repository.diff_pb2

import utils.http_util
import google.protobuf.json_format


class ArchiveClient(object):
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

    
    def create(self, request, org, user, host="", timeout=10):
        """
        创建归档
        :param request: create请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: create_pb2.CreateResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.archive.Create"
        uri = "/archive"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.file_repository_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = create_pb2.CreateResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_and_register(self, request, org, user, host="", timeout=10):
        """
        创建归档并注册版本
        :param request: create_and_register请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: create_and_register_pb2.CreateAndRegisterResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.archive.CreateAndRegister"
        uri = "/v2/archive"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.file_repository_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = create_and_register_pb2.CreateAndRegisterResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_archive(self, request, org, user, host="", timeout=10):
        """
        删除归档版本
        :param request: delete_archive请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: delete_archive_pb2.DeleteArchiveResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.archive.DeleteArchive"
        uri = "/archive/:packageId/:versionId".format(
            packageId=request.packageId,
            versionId=request.versionId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.file_repository_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = delete_archive_pb2.DeleteArchiveResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_archive_v_2(self, request, org, user, host="", timeout=10):
        """
        删除归档版本，并且删除版本元数据
        :param request: delete_archive_v_2请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: delete_archive_v2_pb2.DeleteArchiveV2Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.archive.DeleteArchiveV2"
        uri = "/v2/archive/:packageId/:versionId".format(
            packageId=request.packageId,
            versionId=request.versionId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.file_repository_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = delete_archive_v2_pb2.DeleteArchiveV2Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_diff_size(self, request, org, user, host="", timeout=10):
        """
        获取版本差异大小
        :param request: get_diff_size请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_archive_diff_size_pb2.GetDiffSizeResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.archive.GetDiffSize"
        uri = "/archive/diff/size/@packageId"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.file_repository_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = get_archive_diff_size_pb2.GetDiffSizeResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_file_info(self, request, org, user, host="", timeout=10):
        """
        获取归档版本文件信息
        :param request: get_file_info请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_archive_file_info_pb2.GetFileInfoResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.archive.GetFileInfo"
        uri = "/archive/info/@packageId/@versionId"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.file_repository_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = get_archive_file_info_pb2.GetFileInfoResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def listdir(self, request, org, user, host="", timeout=10):
        """
        获取文件列表
        :param request: listdir请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_archive_list_pb2.ListdirResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.archive.Listdir"
        uri = "/archive/list/@packageId/@versionId"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.file_repository_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = get_archive_list_pb2.ListdirResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_sign(self, request, org, user, host="", timeout=10):
        """
        获取归档版本签名信息
        :param request: get_sign请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_archive_sign_info_pb2.GetSignResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.archive.GetSign"
        uri = "/archive/sign/@packageId/@versionId"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.file_repository_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = get_archive_sign_info_pb2.GetSignResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_size(self, request, org, user, host="", timeout=10):
        """
        获取版本大小
        :param request: get_size请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_archive_size_pb2.GetSizeResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.archive.GetSize"
        uri = "/archive/size/@packageId/@versionId"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.file_repository_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = get_archive_size_pb2.GetSizeResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_difference(self, request, org, user, host="", timeout=10):
        """
        获取版本差异列表
        :param request: get_difference请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.file_repository.diff_pb2.Diff
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.archive.GetDifference"
        uri = "/archive/difference/:packageId".format(
            packageId=request.packageId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.file_repository_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = model.file_repository.diff_pb2.Diff()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_package_difference(self, request, org, user, host="", timeout=10):
        """
        获取不同包的版本差异列表
        :param request: get_package_difference请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.file_repository.diff_pb2.Diff
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.archive.GetPackageDifference"
        uri = "/archive/difference"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.file_repository_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = model.file_repository.diff_pb2.Diff()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
