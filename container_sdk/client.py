# -*- coding: utf-8 -*-

import container_sdk.api.cluster.cluster_client

import container_sdk.api.configmap.configmap_client

import container_sdk.api.event.event_client

import container_sdk.api.hpa.hpa_client

import container_sdk.api.image.image_client

import container_sdk.api.ingress.ingress_client

import container_sdk.api.member.member_client

import container_sdk.api.namespace.namespace_client

import container_sdk.api.node.node_client

import container_sdk.api.org.org_client

import container_sdk.api.persistentvolumeclaim.persistentvolumeclaim_client

import container_sdk.api.proxy.proxy_client

import container_sdk.api.resourcegroup.resourcegroup_client

import container_sdk.api.secret.secret_client

import container_sdk.api.service.service_client

import container_sdk.api.storageclass.storageclass_client

import container_sdk.api.task.task_client

import container_sdk.api.workload.workload_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.cluster = container_sdk.api.cluster.cluster_client.ClusterClient(server_ip, server_port, service_name)
        
        self.configmap = container_sdk.api.configmap.configmap_client.ConfigmapClient(server_ip, server_port, service_name)
        
        self.event = container_sdk.api.event.event_client.EventClient(server_ip, server_port, service_name)
        
        self.hpa = container_sdk.api.hpa.hpa_client.HpaClient(server_ip, server_port, service_name)
        
        self.image = container_sdk.api.image.image_client.ImageClient(server_ip, server_port, service_name)
        
        self.ingress = container_sdk.api.ingress.ingress_client.IngressClient(server_ip, server_port, service_name)
        
        self.member = container_sdk.api.member.member_client.MemberClient(server_ip, server_port, service_name)
        
        self.namespace = container_sdk.api.namespace.namespace_client.NamespaceClient(server_ip, server_port, service_name)
        
        self.node = container_sdk.api.node.node_client.NodeClient(server_ip, server_port, service_name)
        
        self.org = container_sdk.api.org.org_client.OrgClient(server_ip, server_port, service_name)
        
        self.persistentvolumeclaim = container_sdk.api.persistentvolumeclaim.persistentvolumeclaim_client.PersistentvolumeclaimClient(server_ip, server_port, service_name)
        
        self.proxy = container_sdk.api.proxy.proxy_client.ProxyClient(server_ip, server_port, service_name)
        
        self.resourcegroup = container_sdk.api.resourcegroup.resourcegroup_client.ResourcegroupClient(server_ip, server_port, service_name)
        
        self.secret = container_sdk.api.secret.secret_client.SecretClient(server_ip, server_port, service_name)
        
        self.service = container_sdk.api.service.service_client.ServiceClient(server_ip, server_port, service_name)
        
        self.storageclass = container_sdk.api.storageclass.storageclass_client.StorageclassClient(server_ip, server_port, service_name)
        
        self.task = container_sdk.api.task.task_client.TaskClient(server_ip, server_port, service_name)
        
        self.workload = container_sdk.api.workload.workload_client.WorkloadClient(server_ip, server_port, service_name)
        
