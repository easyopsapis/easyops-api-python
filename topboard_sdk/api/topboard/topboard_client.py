# -*- coding: utf-8 -*-
import os
import sys


import topboard_sdk.model.topboard.comment_pb2

import topboard_sdk.model.topboard.issue_pb2

import topboard_sdk.model.topboard.product_pb2

import topboard_sdk.model.topboard.sprint_pb2

import topboard_sdk.api.topboard.delete_comment_pb2

import google.protobuf.empty_pb2

import topboard_sdk.api.topboard.delete_issue_pb2

import topboard_sdk.api.topboard.delete_product_pb2

import topboard_sdk.api.topboard.delete_sprint_pb2

import topboard_sdk.api.topboard.get_issue_pb2

import topboard_sdk.api.topboard.get_product_pb2

import topboard_sdk.api.topboard.get_sprint_pb2

import topboard_sdk.api.topboard.search_comment_pb2

import topboard_sdk.api.topboard.search_issue_pb2

import topboard_sdk.api.topboard.search_product_pb2

import topboard_sdk.api.topboard.search_sprint_pb2

import topboard_sdk.api.topboard.update_comment_pb2

import topboard_sdk.api.topboard.update_issue_pb2

import topboard_sdk.api.topboard.update_issue_step_pb2

import topboard_sdk.api.topboard.update_product_pb2

import topboard_sdk.api.topboard.update_sprint_pb2

import topboard_sdk.api.topboard.update_sprint_issue_pb2

import topboard_sdk.api.topboard.upload_temp_file_pb2

import topboard_sdk.utils.http_util
import google.protobuf.json_format


class TopboardClient(object):
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

    
    def create_comment(self, request, org, user, timeout=10):
        # type: (topboard_sdk.model.topboard.comment_pb2.Comment, int, str, int) -> topboard_sdk.model.topboard.comment_pb2.Comment
        """
        创建评论
        :param request: create_comment请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.model.topboard.comment_pb2.Comment
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.CreateComment"
        uri = "/api/v1/comments"
        
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.model.topboard.comment_pb2.Comment()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_issue(self, request, org, user, timeout=10):
        # type: (topboard_sdk.model.topboard.issue_pb2.Issue, int, str, int) -> topboard_sdk.model.topboard.issue_pb2.Issue
        """
        创建问题
        :param request: create_issue请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.model.topboard.issue_pb2.Issue
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.CreateIssue"
        uri = "/api/v1/issues"
        
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.model.topboard.issue_pb2.Issue()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_product(self, request, org, user, timeout=10):
        # type: (topboard_sdk.model.topboard.product_pb2.Product, int, str, int) -> topboard_sdk.model.topboard.product_pb2.Product
        """
        创建产品
        :param request: create_product请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.model.topboard.product_pb2.Product
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.CreateProduct"
        uri = "/api/v1/products"
        
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.model.topboard.product_pb2.Product()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_sprint(self, request, org, user, timeout=10):
        # type: (topboard_sdk.model.topboard.sprint_pb2.Sprint, int, str, int) -> topboard_sdk.model.topboard.sprint_pb2.Sprint
        """
        创建迭代
        :param request: create_sprint请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.model.topboard.sprint_pb2.Sprint
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.CreateSprint"
        uri = "/api/v1/sprints"
        
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.model.topboard.sprint_pb2.Sprint()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_comment(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.delete_comment_pb2.DeleteCommentRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除评论
        :param request: delete_comment请求
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
            route_name = "easyops.api.topboard.topboard.DeleteComment"
        uri = "/api/v1/comments/{commentID}".format(
            commentID=request.commentID,
        )
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.topboard_sdk",
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
    
    def delete_issue(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.delete_issue_pb2.DeleteIssueRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除问题
        :param request: delete_issue请求
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
            route_name = "easyops.api.topboard.topboard.DeleteIssue"
        uri = "/api/v1/issues/{issueID}".format(
            issueID=request.issueID,
        )
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.topboard_sdk",
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
    
    def delete_product(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.delete_product_pb2.DeleteProductRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除产品
        :param request: delete_product请求
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
            route_name = "easyops.api.topboard.topboard.DeleteProduct"
        uri = "/api/v1/products/{productID}".format(
            productID=request.productID,
        )
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.topboard_sdk",
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
    
    def delete_sprint(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.delete_sprint_pb2.DeleteSprintRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除迭代
        :param request: delete_sprint请求
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
            route_name = "easyops.api.topboard.topboard.DeleteSprint"
        uri = "/api/v1/sprints/{sprintID}".format(
            sprintID=request.sprintID,
        )
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.topboard_sdk",
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
    
    def get_issue(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.get_issue_pb2.GetIssueRequest, int, str, int) -> topboard_sdk.model.topboard.issue_pb2.Issue
        """
        获取问题详情
        :param request: get_issue请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.model.topboard.issue_pb2.Issue
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.GetIssue"
        uri = "/api/v1/issues/{issueID}".format(
            issueID=request.issueID,
        )
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.model.topboard.issue_pb2.Issue()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_product(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.get_product_pb2.GetProductRequest, int, str, int) -> topboard_sdk.model.topboard.product_pb2.Product
        """
        获取产品详情
        :param request: get_product请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.model.topboard.product_pb2.Product
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.GetProduct"
        uri = "/api/v1/products/{productID}".format(
            productID=request.productID,
        )
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.model.topboard.product_pb2.Product()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_sprint(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.get_sprint_pb2.GetSprintRequest, int, str, int) -> topboard_sdk.model.topboard.sprint_pb2.Sprint
        """
        获取迭代详情
        :param request: get_sprint请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.model.topboard.sprint_pb2.Sprint
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.GetSprint"
        uri = "/api/v1/sprints/{sprintID}".format(
            sprintID=request.sprintID,
        )
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.model.topboard.sprint_pb2.Sprint()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_comment(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.search_comment_pb2.SearchCommentRequest, int, str, int) -> topboard_sdk.api.topboard.search_comment_pb2.SearchCommentResponse
        """
        搜索评论
        :param request: search_comment请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.api.topboard.search_comment_pb2.SearchCommentResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.SearchComment"
        uri = "/api/v1/comments/search"
        
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.api.topboard.search_comment_pb2.SearchCommentResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_issue(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.search_issue_pb2.SearchIssueRequest, int, str, int) -> topboard_sdk.api.topboard.search_issue_pb2.SearchIssueResponse
        """
        搜索问题
        :param request: search_issue请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.api.topboard.search_issue_pb2.SearchIssueResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.SearchIssue"
        uri = "/api/v1/issues/search"
        
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.api.topboard.search_issue_pb2.SearchIssueResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_product(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.search_product_pb2.SearchProductRequest, int, str, int) -> topboard_sdk.api.topboard.search_product_pb2.SearchProductResponse
        """
        搜索产品
        :param request: search_product请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.api.topboard.search_product_pb2.SearchProductResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.SearchProduct"
        uri = "/api/v1/products/search"
        
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.api.topboard.search_product_pb2.SearchProductResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_sprint(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.search_sprint_pb2.SearchSprintRequest, int, str, int) -> topboard_sdk.api.topboard.search_sprint_pb2.SearchSprintResponse
        """
        搜索迭代
        :param request: search_sprint请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.api.topboard.search_sprint_pb2.SearchSprintResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.SearchSprint"
        uri = "/api/v1/sprints/search"
        
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.api.topboard.search_sprint_pb2.SearchSprintResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_comment(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.update_comment_pb2.UpdateCommentRequest, int, str, int) -> topboard_sdk.model.topboard.comment_pb2.Comment
        """
        更新评论
        :param request: update_comment请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.model.topboard.comment_pb2.Comment
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.UpdateComment"
        uri = "/api/v1/comments/{commentID}".format(
            commentID=request.commentID,
        )
        requestParam = request.comment
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.model.topboard.comment_pb2.Comment()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_issue(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.update_issue_pb2.UpdateIssueRequest, int, str, int) -> topboard_sdk.model.topboard.issue_pb2.Issue
        """
        更新问题
        :param request: update_issue请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.model.topboard.issue_pb2.Issue
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.UpdateIssue"
        uri = "/api/v1/issues/{issueID}".format(
            issueID=request.issueID,
        )
        requestParam = request.issue
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.model.topboard.issue_pb2.Issue()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_issue_step(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.update_issue_step_pb2.UpdateIssueStepRequest, int, str, int) -> topboard_sdk.model.topboard.issue_pb2.Issue
        """
        更新问题步骤
        :param request: update_issue_step请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.model.topboard.issue_pb2.Issue
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.UpdateIssueStep"
        uri = "/api/v1/issues/{issueID}/step".format(
            issueID=request.issueID,
        )
        requestParam = request.step
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.model.topboard.issue_pb2.Issue()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_product(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.update_product_pb2.UpdateProductRequest, int, str, int) -> topboard_sdk.model.topboard.product_pb2.Product
        """
        更新产品
        :param request: update_product请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.model.topboard.product_pb2.Product
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.UpdateProduct"
        uri = "/api/v1/products/{productID}".format(
            productID=request.productID,
        )
        requestParam = request.product
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.model.topboard.product_pb2.Product()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_sprint(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.update_sprint_pb2.UpdateSprintRequest, int, str, int) -> topboard_sdk.model.topboard.sprint_pb2.Sprint
        """
        更新迭代
        :param request: update_sprint请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.model.topboard.sprint_pb2.Sprint
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.UpdateSprint"
        uri = "/api/v1/sprints/{sprintID}".format(
            sprintID=request.sprintID,
        )
        requestParam = request.sprint
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.model.topboard.sprint_pb2.Sprint()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_sprint_issue(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.update_sprint_issue_pb2.UpdateSprintIssueRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        更新问题所属迭代
        :param request: update_sprint_issue请求
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
            route_name = "easyops.api.topboard.topboard.UpdateSprintIssue"
        uri = "/api/v1/sprints/issues"
        
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.topboard_sdk",
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
    
    def upload_temp_file(self, request, org, user, timeout=10):
        # type: (topboard_sdk.api.topboard.upload_temp_file_pb2.UploadTempFileRequest, int, str, int) -> topboard_sdk.api.topboard.upload_temp_file_pb2.UploadTempFileResponse
        """
        上传临时文件
        :param request: upload_temp_file请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: topboard_sdk.api.topboard.upload_temp_file_pb2.UploadTempFileResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.topboard.topboard.UploadTempFile"
        uri = "/api/v1/uploadtempfile"
        
        requestParam = request
        
        rsp_obj = topboard_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.topboard_sdk",
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
        rsp = topboard_sdk.api.topboard.upload_temp_file_pb2.UploadTempFileResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
