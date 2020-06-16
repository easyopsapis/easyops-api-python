# -*- coding: utf-8 -*-

import notify_sdk.api.msgpub.msgpub_client

import notify_sdk.api.oplog.oplog_client

import notify_sdk.api.org.org_client

import notify_sdk.api.subscriber.subscriber_client

import notify_sdk.api.subscriber_manager.subscriber_manager_client

import notify_sdk.api.topic.topic_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.msgpub = notify_sdk.api.msgpub.msgpub_client.MsgpubClient(server_ip, server_port, service_name)
        
        self.oplog = notify_sdk.api.oplog.oplog_client.OplogClient(server_ip, server_port, service_name)
        
        self.org = notify_sdk.api.org.org_client.OrgClient(server_ip, server_port, service_name)
        
        self.subscriber = notify_sdk.api.subscriber.subscriber_client.SubscriberClient(server_ip, server_port, service_name)
        
        self.subscriber_manager = notify_sdk.api.subscriber_manager.subscriber_manager_client.SubscriberManagerClient(server_ip, server_port, service_name)
        
        self.topic = notify_sdk.api.topic.topic_client.TopicClient(server_ip, server_port, service_name)
        
